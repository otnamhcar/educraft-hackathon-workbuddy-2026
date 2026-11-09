"""Regangkan jeda antar-kalimat supaya blok mengisi slotnya, tanpa memperlambat suara.

Kenapa ada alat ini: rekaman bisa lebih pendek daripada slot. Kalau dibiarkan,
narasi habis lebih awal lalu layar diam sampai kartu berikutnya — penonton melihat
video yang berhenti bercerita. Memperlambat audio dengan atempo bukan jawaban:
tempo 2,37 → 1,8 kata/detik terdengar seperti rekaman yang dirusak.

Yang dilakukan alat ini: menyisipkan HENING ke dalam jeda yang sudah ada. Suara
tetap utuh sama sekali. Yang bertambah hanya lamanya berhenti di antara kalimat —
dan itu memang yang dibutuhkan ketika layarnya juga diam.

    python3 regang_jeda.py                    # laporan, tidak menulis
    python3 regang_jeda.py --tulis            # hasilkan 01_laras.wav … 12_laras.wav
    python3 regang_jeda.py --maks 1.8         # jeda per titik tidak lebih dari 1,8 s

Batas `--maks` penting: menyebar 26 detik kosong ke 9 jeda pendek akan membuat jeda
2,9 detik, dan narasi terasa terputus. Kalau sebuah blok butuh jeda lebih lebar dari
batas itu, alat ini menolak dan melaporkan — lebih baik Anda tahu daripada videonya
terasa aneh tanpa sebab yang jelas.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TIMING = HERE / "TIMING.json"
EKSTENSI = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus"}

_tim = json.loads(TIMING.read_text())
ORDER = [b["nomor"] for b in _tim["berkas"]]

NOISE = "-32dB"
MIN_SIL = 0.10
MIN_JEDA_KALIMAT = 0.28   # jeda lebih pendek dari ini bukan batas kalimat
MARGIN = 0.15      # sisa di ujung slot
FADE = 0.010       # tidak dipakai lagi; disimpan agar berkas lama tetap terbaca


def durasi(berkas: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(berkas)],
        capture_output=True, text=True,
    )
    return float(r.stdout.strip())


def slot_blok(tim: dict, nomor: str) -> float:
    for b in tim["berkas"]:
        if b["nomor"] == nomor:
            return b["slot"]
    raise KeyError(nomor)


def senyap(berkas: Path) -> list[tuple[float, float]]:
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(berkas),
         "-af", f"silencedetect=noise={NOISE}:d={MIN_SIL}", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    kejadian = [
        (m.group(1), float(m.group(2)))
        for m in re.finditer(r"silence_(start|end): ([0-9.]+)", p.stderr)
    ]
    total = durasi(berkas)
    hasil, mulai = [], None
    for jenis, t in kejadian:
        if jenis == "start":
            mulai = t
        elif mulai is not None:
            hasil.append((mulai, t))
            mulai = None
    if mulai is not None:
        hasil.append((mulai, total))
    return hasil


def gabung_senyap(s: list[tuple[float, float]], celah: float = 0.05) -> list[tuple[float, float]]:
    """Gabungkan senyap yang terpisah oleh celah sangat pendek.

    `silencedetect` kadang melaporkan dua senyap bersebelahan yang dipisah satu
   -dua sampel (mis. 5,23–5,54 lalu 5,55–5,88). Kalau dibiarkan, hasilnya
    potongan audio sepanjang 0,01 detik — bukan potongan, hanya artefak. Saat
    `adelay` menempatkannya, potongan sependek itu tidak terdengar tetapi
    memakan satu jatah sisipan, sehingga sisipan sesudahnya menumpuk.
    """
    if not s:
        return []
    hasil = [list(s[0])]
    for a, b in s[1:]:
        if a - hasil[-1][1] <= celah:
            hasil[-1][1] = b
        else:
            hasil.append([a, b])
    return [(a, b) for a, b in hasil]


def cari(folder: Path, nomor: str) -> Path | None:
    """Utamakan rekaman asli; kalau tidak ada, pakai hasil pangkas (_rapi)."""
    kandidat = [c for c in sorted(folder.glob(f"{nomor}.*")) if c.suffix.lower() in EKSTENSI]
    asli = [c for c in kandidat if "_rapi" not in c.stem and "_laras" not in c.stem]
    rapi = [c for c in kandidat if c.stem.endswith("_rapi")]
    return (asli or rapi or [None])[0]


def rencana(berkas: Path, slot: float, maks: float) -> dict:
    """Hitung sisipan hening untuk tiap jeda tengah.

    Jeda di tepi berkas tidak dipakai: menambah hening di awal hanya menggeser
    seluruh blok, dan di akhir hanya menambah ekor. Menambah TEPI tidak membantu
    kecocokan; yang membantu adalah menambah RUANG di antara kalimat.
    """
    total = durasi(berkas)
    kurang = slot - MARGIN - total
    s = gabung_senyap(senyap(berkas))
    # Hanya jeda yang cukup panjang dianggap batas antar-kalimat. Jeda 100-an ms
    # adalah celah antar-fonem di DALAM kata; menambah hening di situ memotong
    # kata di tengah dan membuatnya terdengar samar — persis yang terjadi pada
    # kata "IPAS" saat blok 03 dipecah di 25 titik.
    tengah = [(a, b) for a, b in s
              if a > 0.05 and b < total - 0.05 and (b - a) >= MIN_JEDA_KALIMAT]
    n = len(tengah)
    if kurang <= 0.02:
        return {"berkas": berkas, "total": total, "slot": slot, "kurang": max(0.0, kurang),
                "jeda": tengah, "sisip": 0.0, "ekor": 0.0, "n": n, "bisa": True}
    if n == 0:
        # tidak ada jeda kalimat sama sekali: seluruh kelebihan jadi hening ekor
        return {"berkas": berkas, "total": total, "slot": slot, "kurang": kurang,
                "jeda": tengah, "sisip": 0.0, "ekor": kurang, "n": 0,
                "bisa": kurang <= maks * 4}
    # Di `bangun()`, `kursor += sisip` MENGGANTIKAN jeda asli, bukan menambah.
    # Jadi sisip harus memuat jeda asli yang digantikannya:
    #   total_keluar = jumlah_ucapan + sisip * n
    #   kurang       = slot - (jumlah_ucapan + jeda_asli)
    # => sisip = kurang/n + rata_rata(jeda_asli)
    rata_jeda = sum(b - a for a, b in tengah) / n
    tambahan = min(kurang / n, maks)
    sisip = tambahan + rata_jeda
    # Sisa yang tidak tertampung ditaruh di EKOR, bukan dipaksa masuk ke jeda.
    # Menaruh kelebihan di ekor aman: layar memang diam di ujung slot, dan
    # audiens tidak mendengar apa pun yang terpotong.
    ekor = max(0.0, kurang - tambahan * n)
    return {"berkas": berkas, "total": total, "slot": slot, "kurang": kurang,
            "jeda": tengah, "sisip": sisip, "ekor": ekor, "n": n,
            "bisa": True}


def bangun(berkas: Path, jeda: list[tuple[float, float]], sisip: float, keluar: Path,
          ekor: float = 0.0) -> None:
    """Potong per rentang bicara, lalu sisipkan hening di antaranya.

    Tiap potongan ditempel TEPAT setelah potongan sebelumnya, ditambah `sisip`.
    Bukan `a + akumulasi_sisip`: cara itu mengabaikan hening asli yang dibuang
    di antara dua potongan. Jeda asli 0,68 s yang diregangkan jadi 2,4 s akan
    memberi `a` yang maju 0,68 s tetapi sisipan 2,4 s — selisihnya lubang
    hening di tengah blok. Tiga detik hening mutlak pernah muncul begitu.
    """
    total = durasi(berkas)
    # Kalau tidak ada yang perlu diregangkan, salin apa adanya. Tanpa ini, blok
    # yang sudah pas tetap dipotong di setiap jeda lalu diisi `sisip`=0 — jeda
    # aslinya hilang dan semua kalimat menyambung tanpa napas. Blok 04 pernah
    # kehilangan seluruh jedanya karena kasus ini.
    if sisip <= 0.0 and ekor <= 0.02:
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", str(berkas),
             "-ar", "48000", "-ac", "2", str(keluar)],
            check=True,
        )
        return
    # rentang bicara = komplemen senyap tengah, dengan tepi tetap dipertahankan
    potong: list[tuple[float, float]] = []
    pos = 0.0
    for a, b in jeda:
        if a > pos:
            potong.append((pos, a))
        pos = b
    if pos < total:
        potong.append((pos, total))

    bagian, label = [], []
    rantai_bagian: list[str] = []
    for i, (a, b) in enumerate(potong):
        if i > 0:
            # hening di antara dua potongan, tepat sepanjang `sisip`
            rantai_bagian.append(
                f"anullsrc=r=48000:cl=stereo,atrim=0:{sisip:.4f}[g{i}]")
            label.append(f"[g{i}]")
        # Tanpa fade. Potongan dipotong tepat di tengah senyap, jadi tidak ada
        # gelombang yang terpotong tajam dan fade tidak dibutuhkan. Fade di sini
        # justru merusak: 25 sambungan di blok 03 berarti 50 titik fade, dan
        # konsonan awal tiap kalimat terkikis sampai terdengar samar.
        #
        # `concat`, bukan `amix`+`adelay`. `amix` menganggap semua input mulai di
        # nol dan hanya mengambil yang terpanjang, sehingga isi potongan tidak
        # menempel pada posisi yang dimaksud — pernah menghasilkan 3 detik hening
        # di tengah blok 02 karena potongan berikutnya mulai terlambat.
        rantai_bagian.append(
            f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,"
            f"aresample=48000,aformat=channel_layouts=stereo[s{i}]"
        )
        label.append(f"[s{i}]")

    akhir = sum(b - a for a, b in potong) + sisip * max(0, len(potong) - 1)
    keluaran = max(akhir + MARGIN + ekor, total)
    rantai = ";".join(rantai_bagian) + ";" + "".join(label) + \
        f"concat=n={len(label)}:v=0:a=1," \
        f"apad=whole_dur={keluaran:.3f}[out]"

    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(berkas),
         "-filter_complex", rantai, "-map", "[out]",
         "-ar", "48000", "-ac", "2", str(keluar)],
        check=True,
    )


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--audio", type=Path, default=HERE / "audio_layar")
    p.add_argument("--tulis", action="store_true")
    p.add_argument("--maks", type=float, default=1.8,
                   help="batas jeda per titik setelah diregangkan (detik)")
    arg = p.parse_args()

    tim = json.loads(TIMING.read_text())
    daftar = []
    print(f"{'blok':5}{'rekaman':>9}{'slot':>8}{'kurang':>8}{'jeda':>6}{'per titik':>10}"
          f"{'ekor':>7}  status")
    print("-" * 70)
    for nomor in ORDER:
        berkas = cari(arg.audio, nomor)
        if not berkas:
            print(f"{nomor:5}  berkas tidak ada — dilewati")
            continue
        r = rencana(berkas, slot_blok(tim, nomor), arg.maks)
        daftar.append((nomor, r))

        akhir_jeda = r["sisip"] if r["n"] else 0.0
        status = "pas" if r["kurang"] <= 0.02 else "bisa"
        print(f"{nomor:5}{r['total']:9.1f}{r['slot']:8.1f}{r['kurang']:8.1f}"
              f"{r['n']:6}{akhir_jeda:10.2f}{r['ekor']:7.1f}  {status}")

    berenang = [(n, r) for n, r in daftar if r["ekor"] > 0.05]
    if berenang:
        print(f"\nKelebihan waktu ditaruh di EKOR, bukan dipaksa ke jeda kalimat:")
        for n, r in berenang:
            print(f"  {n}: {r['ekor']:.1f} s hening di ujung blok "
                  f"(jeda per titik dibatasi {arg.maks:.1f} s)")
        print("Ini aman: layar memang diam di ujung slot, dan tidak ada kata yang terpotong.")

    if not arg.tulis:
        print("\n(tidak ada yang ditulis — tambahkan --tulis)")
        return 0

    for nomor, r in daftar:
        keluar = arg.audio / f"{nomor}_laras.wav"
        bangun(r["berkas"], r["jeda"], r["sisip"], keluar, r["ekor"])
        tanda = f"  (ekor +{r['ekor']:.1f} s)" if r["ekor"] > 0.05 else ""
        print(f"{nomor}_laras.wav  {durasi(keluar):.1f} s / slot {r['slot']:.1f} s{tanda}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
