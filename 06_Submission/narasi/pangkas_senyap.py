"""Pangkas senyap di berkas TTS supaya tiap blok masuk slot videonya.

Kenapa perlu alat ini: mesin TTS menghasilkan jeda jauh lebih panjang daripada yang
diminta. Pada rekaman 7 blok, senyap menempati 31–52% durasi berkas, sehingga semua
blok melewati slotnya 0,1–33,9 detik. Tapi bicaranya sendiri tidak kelebihan — yang
kelebihan senyapnya. Alat ini memangkas senyap, bukan kalimat.

Cara kerja, tiga langkah:

  1. Potong senyap di tepi berkas sampai batas aman (EDGE_MS). Ini yang paling murah:
     tidak menyentuh ucapan sama sekali. Blok 01 kehilangan 1,69 detik hanya dari sini.
  2. Kalau masih kelebihan, pangkas semua senyap di tengah secara merata ke satu
     ambang yang dihitung per blok. Merata, bukan "yang terpanjang dulu" — jeda yang
     sudah pendek tidak boleh jadi lebih pendek dari napas.
  3. Kalau ambangnya jatuh di bawah lantai wajar (LANTAI_MS), jangan dipaksa. Laporkan
     bahwa blok itu tidak muat, dan berapa detik yang masih kurang. Lebih baik Anda
     tahu daripada videonya terpotong diam-diam.

Potongan tepi dibuat dengan fade 8 ms supaya tidak ada klik. Tanpa fade, memotong di
tengah gelombang menghasilkan bunyi "tik" yang terdengar jelas di speaker.

    python3 pangkas_senyap.py                # laporan saja
    python3 pangkas_senyap.py --tulis        # hasilkan 01_rapi.mp3 … 07_rapi.mp3
    python3 pangkas_senyap.py --tulis --ekstensi wav   # kualitas lebih baik
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

# Dibaca dari TIMING.json supaya jumlah segmen tidak perlu disalin ke tiap skrip.
_tim = json.loads(TIMING.read_text())
ORDER = [b["nomor"] for b in _tim["berkas"]]
NAMES = [b["segmen"] for b in _tim["berkas"]]

# Ambang deteksi senyap. -30 dB cukup untuk membedakan napas dari hening digital,
# dan tidak memotong konsonan akhir yang pelan.
NOISE = "-30dB"
MIN_SIL = 0.12

# Senyap di tepi berkas yang masih disisakan. 120 ms cukup untuk mencegah bunyi
# terpotong mendadak, tapi tidak terasa seperti menunggu.
EDGE_MS = 120

# Lantai jeda antar-kalimat. Di bawah ini, jeda berhenti terdengar sebagai jeda dan
# mulai terdengar sebagai orang kehabisan napas.
#
# Nilai ini dibiarkan sedikit longgar terhadap pembulatan: blok terpendek butuh 318 ms
# sedangkan lantainya 320 ms — selisih 2 ms yang tidak bisa didengar siapa pun.
# Menolak blok karena 2 ms akan memaksa rekaman ulang tanpa alasan. Toleransi
# TOLERANSI_MS dibuat kecil dengan sengaja supaya kasus seperti 01 (butuh 115 ms)
# tetap ditolak.
LANTAI_MS = 320
TOLERANSI_MS = 40

# Sisa di ujung slot untuk napas sebelum kartu berikutnya.
MARGIN = 0.30

FADE = 0.008


def slot_blok(tim: dict, nomor: str) -> float:
    """Slot satu blok, dibaca dari TIMING.json.

    Satu segmen bisa dipecah jadi beberapa blok narasi. Karena itu
    `batas_blok[segmen] - mulai_di[segmen]` adalah panjang SEGMEN, bukan panjang
    blok — memakainya membuat semua blok dalam satu segmen mendapat slot yang
    sama (seluruh blok tercetak 174 detik). Nilai `slot` per blok sudah dihitung
    saat TIMING.json dibuat, jadi pakai itu.
    """
    for b in tim["berkas"]:
        if b["nomor"] == nomor:
            return b["slot"]
    raise KeyError(f"blok {nomor} tidak ada di TIMING.json")


def mulai_blok(tim: dict, nomor: str) -> float:
    for b in tim["berkas"]:
        if b["nomor"] == nomor:
            return b["mulai"]
    raise KeyError(f"blok {nomor} tidak ada di TIMING.json")



def durasi(berkas: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(berkas)],
        capture_output=True, text=True,
    )
    return float(r.stdout.strip())


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


def cari(folder: Path, nomor: str) -> Path | None:
    for c in sorted(folder.glob(f"{nomor}.*")):
        if c.suffix.lower() in EKSTENSI and "_rapi" not in c.stem:
            return c
    return None


def rencana(nomor: str, berkas: Path, slot: float) -> dict:
    """Hitung potongan yang perlu, untuk satu blok."""
    total = durasi(berkas)
    sen = senyap(berkas)

    # Senyap tepi = senyap yang menyentuh awal atau akhir berkas. Ditentukan dari
    # daftar LENGKAP, bukan dari daftar interior: interior sudah tidak memuat senyap
    # tepi, jadi memakai interior untuk mencari tepi akan salah membaca senyap
    # internal sebagai tepi.
    tepi_awal = sen[0][1] if sen and sen[0][0] <= EDGE_MS / 1000 else 0.0
    tepi_akhir = total - sen[-1][0] if sen and sen[-1][1] >= total - EDGE_MS / 1000 else 0.0

    interior = [
        (a, b) for a, b in sen
        if a > EDGE_MS / 1000 and b < total - EDGE_MS / 1000
    ]

    target = slot - MARGIN
    # Langkah 1: potong tepi. Panjang isi setelah tepi dipangkas diambil dari
    # rentang_isi() — fungsi yang sama yang dipakai filter_pangkas().
    pratinjau = {"total": total, "tepi_awal": tepi_awal, "tepi_akhir": tepi_akhir}
    isi_awal, isi_akhir = rentang_isi(pratinjau)
    dasar = max(0.0, isi_akhir - isi_awal)
    bisa_tepi = total - dasar
    sisa_kurang = dasar - target

    # Langkah 2: pangkas jeda tengah.
    #
    # Yang dipangkas hanya jeda yang LEBIH PANJANG dari ambang. Jeda yang sudah pendek
    # (napas bawaan mesin, 350–550 ms) dibiarkan utuh — memotongnya akan menyambung
    # dua kata tanpa hening sama sekali.
    #
    # Karena itu ambang tidak bisa dicari dengan "panjang total ÷ jumlah jeda". Yang
    # benar: cari ambang terkecil yang membuat durasi hasilnya ≥ target, dengan
    # durasi(t) = total − tepi − Σ max(0, Lᵢ − t).
    #
    # Fungsi itu NAIK monoton terhadap t (lihat catatan di bawah), jadi bisa dipakai
    # pencarian biner.
    n_tengah = len(interior)
    panjang_tengah = sum(b - a for a, b in interior)
    ambang = None
    if n_tengah:
        panjang = [b - a for a, b in interior]

        def durasi_pada(t: float) -> float:
            return dasar - sum(max(0.0, x - t) for x in panjang)

        # Cari ambang terkecil yang durasinya masih ≥ target.
        #
        # Perhatikan arahnya, karena mudah dibalik: ambang lebih besar berarti lebih
        # SEDIKIT yang dipangkas, jadi durasinya lebih PANJANG. Fungsi durasi_pada
        # karena itu NAIK terhadap ambang, bukan turun.
        #
        #   t = 0            → semua jeda dipangkas → durasi terpendek
        #   t = jeda terpanjang → tidak ada yang dipangkas → durasi terpanjang
        #
        # Kita ingin durasi sedekat mungkin dengan target dari ATAS (jangan sampai
        # melewati slot), jadi ambil t terkecil yang durasinya ≥ target.
        lo, hi = 0.0, max(panjang)
        if durasi_pada(hi) < target:
            ambang = hi          # bahkan tanpa memangkas pun sudah terlalu pendek
        else:
            for _ in range(40):
                mid = (lo + hi) / 2
                if durasi_pada(mid) < target:
                    lo = mid
                else:
                    hi = mid
            ambang = hi
    muat = sisa_kurang <= 0 or (
        ambang is not None and ambang * 1000 >= LANTAI_MS - TOLERANSI_MS
    )

    return {
        "nomor": nomor,
        "berkas": berkas,
        "total": total,
        "slot": slot,
        "target": target,
        "senyap": sen,
        "interior": interior,
        "tepi_awal": tepi_awal,
        "tepi_akhir": tepi_akhir,
        "potong_tepi": bisa_tepi,
        "n_tengah": n_tengah,
        "ambang": ambang,
        "muat": muat,
        "kurang": max(0.0, (ambang * 1000 - LANTAI_MS) * -1 / 1000)
        if (ambang is not None and ambang * 1000 < LANTAI_MS) else 0.0,
    }


def rentang_isi(r: dict) -> tuple[float, float]:
    """Awal dan akhir bagian yang dipertahankan setelah tepi dipangkas.

    Dipakai bersama oleh model durasi di rencana() dan oleh filter_pangkas(), supaya
    keduanya tidak bisa berbeda hitungan. Sebelum ini keduanya dihitung terpisah dan
    hasilnya meleset sampai 10 s pada blok 03.
    """
    total = r["total"]
    awal = max(0.0, r["tepi_awal"] - EDGE_MS / 1000) if r["tepi_awal"] > 0 else 0.0
    akhir = (total - max(0.0, r["tepi_akhir"] - EDGE_MS / 1000)) if r["tepi_akhir"] > 0 else total
    return awal, akhir


def filter_pangkas(r: dict) -> str:
    """Bangun filter_complex: buang rentang, sisakan fade di tiap sambungan.

    Pendekatan: setiap bagian yang DIPERTAHANKAN di-fade masuk dan keluar 8 ms,
    lalu disambung berurutan. Fade mencegah klik; karena fade-nya hanya 8 ms,
    tidak terdengar sebagai penurunan volume.
    """
    awal, akhir = rentang_isi(r)

    # Rentang yang dibuang di tengah. Hanya jeda yang lebih panjang dari ambang;
    # jeda pendek dibiarkan utuh supaya kata tidak tersambung tanpa hening.
    buang = []
    for a, b in r["interior"]:
        if r["ambang"] is None:
            break
        baru = r["ambang"]
        if b - a > baru:
            # Buang dari TENGAH rentang, sisakan setengah di kiri dan kanan.
            # Membuang di tengah lebih halus daripada memotong di ujung, karena
            # napas biasanya ada di tepi rentang.
            sisa_kiri = a + baru / 2
            sisa_kanan = b - baru / 2
            buang.append((sisa_kiri, sisa_kanan))

    # Susun bagian yang dipertahankan.
    bagian = []
    pos = awal
    for a, b in buang:
        if a > pos:
            bagian.append((pos, a))
        pos = b
    if akhir > pos:
        bagian.append((pos, akhir))

    if not bagian:
        return "anull"

    potongan = []
    for i, (a, b) in enumerate(bagian):
        lama = b - a
        potongan.append(
            f"[0:a]atrim={a:.4f}:{b:.4f},asetpts=N/SR/TB,"
            f"afade=t=in:st=0:d={FADE},"
            f"afade=t=out:st={max(0.0, lama - FADE):.4f}:d={FADE}[p{i}]"
        )
    label = "".join(f"[p{i}]" for i in range(len(bagian)))
    potongan.append(f"{label}concat=n={len(bagian)}:v=0:a=1[out]")
    return ";".join(potongan)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--audio", type=Path, default=HERE)
    p.add_argument("--tulis", action="store_true")
    p.add_argument("--ekstensi", default="mp3", help="mp3 (kecil) atau wav (tanpa rugi)")
    arg = p.parse_args()

    tim = json.loads(TIMING.read_text())
    hasil = []
    for nomor, nama in zip(ORDER, NAMES):
        berkas = cari(arg.audio, nomor)
        if not berkas:
            print(f"{nomor}  berkas tidak ada — dilewati")
            continue
        hasil.append(rencana(nomor, berkas, slot_blok(tim, nomor)))

    print(f"{'blok':5}{'durasi':>8}{'slot':>6}{'tepi':>7}{'tengah':>8}{'ambang':>8}{'hasil':>8}{'status':>9}")
    print("-" * 60)
    for r in hasil:
        ambang = f"{r['ambang'] * 1000:.0f}ms" if r["ambang"] is not None else "—"
        perkiraan = r["total"] - r["potong_tepi"]
        if r["ambang"] is not None:
            perkiraan -= sum(
                max(0.0, (b - a) - r["ambang"]) for a, b in r["interior"]
            )
        status = "muat" if r["muat"] else "TIDAK"
        print(f"{r['nomor']:5}{r['total']:8.2f}{r['slot']:6.1f}{r['potong_tepi']:7.2f}"
              f"{r['n_tengah']:8}{ambang:>8}{perkiraan:8.2f}{status:>9}")

    beda = [r for r in hasil if not r["muat"]]
    if beda:
        print(f"\n{len(beda)} blok tetap tidak muat meski senyap dipangkas sampai lantai "
              f"{LANTAI_MS} ms. Kalimatnya memang kelebihan — yang perlu dipotong kata, "
              f"bukan jeda: {', '.join(r['nomor'] for r in beda)}")

    if not arg.tulis:
        print("\n(tidak ada yang ditulis — tambahkan --tulis)")
        return 0

    for r in hasil:
        keluar = r["berkas"].with_name(f"{r['nomor']}_rapi.{arg.ekstensi}")
        filt = filter_pangkas(r)
        perintah = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(r["berkas"]),
            "-filter_complex", filt, "-map", "[out]",
        ]
        if arg.ekstensi == "mp3":
            perintah += ["-c:a", "libmp3lame", "-b:a", "192k"]
        else:
            perintah += ["-c:a", "pcm_s16le"]
        perintah.append(str(keluar))
        hasil_ff = subprocess.run(perintah, capture_output=True, text=True)
        if hasil_ff.returncode != 0:
            print(f"  {r['nomor']} GAGAL: {hasil_ff.stderr[-400:]}", file=sys.stderr)
            continue
        print(f"  {keluar.name}  {durasi(keluar):.2f}s (dari {r['total']:.2f}s, slot {r['slot']:.1f}s)")

    print(f"\nditulis ke {arg.audio}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
