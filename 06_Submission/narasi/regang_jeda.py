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
MARGIN = 0.15      # sisa di ujung slot
FADE = 0.010       # fade di tepi sisipan, mencegah bunyi "tik"


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
    s = senyap(berkas)
    tengah = [(a, b) for a, b in s if a > 0.05 and b < total - 0.05]
    n = len(tengah)
    if kurang <= 0.02 or n == 0:
        return {"berkas": berkas, "total": total, "slot": slot, "kurang": max(0.0, kurang),
                "jeda": tengah, "sisip": 0.0, "n": n, "bisa": True}
    sisip = kurang / n
    return {"berkas": berkas, "total": total, "slot": slot, "kurang": kurang,
            "jeda": tengah, "sisip": sisip, "n": n, "bisa": sisip <= maks}


def bangun(berkas: Path, jeda: list[tuple[float, float]], sisip: float, keluar: Path) -> None:
    """Potong per rentang bicara, lalu sisipkan hening di antaranya.

    Kunci kebenarannya: tiap potongan dipertahankan pada POSISI ASALNYA (`a`)
    ditambah total sisipan untuk jeda yang sudah dilewati. Bukan akumulasi dari
    nol — akumulasi dari nol membuat potongan saling menimpa, dan karena `amix`
    menjumlahkan gelombang, bagian yang menimpa ikut hilang.
    """
    total = durasi(berkas)
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
    sisipan_sebelum = 0.0
    akhir = 0.0
    for i, (a, b) in enumerate(potong):
        if i > 0:
            # jeda antara potongan sebelumnya dan ini sudah dilewati
            sisipan_sebelum += sisip
        tunda = a + sisipan_sebelum          # posisi absolut asal + sisipan
        panjang = b - a
        bagian.append(
            f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,"
            f"afade=t=in:st=0:d={FADE},"
            f"afade=t=out:st={max(0.0, panjang - FADE):.3f}:d={FADE},"
            f"adelay={int(round(tunda * 1000))}:all=1[s{i}]"
        )
        label.append(f"[s{i}]")
        akhir = max(akhir, tunda + panjang)

    keluaran = max(akhir + MARGIN, total)
    rantai = ";".join(bagian) + ";" + "".join(label) + \
        f"amix=inputs={len(potong)}:normalize=0:duration=longest," \
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
    print(f"{'blok':5}{'rekaman':>9}{'slot':>8}{'kurang':>8}{'jeda':>6}{'per titik':>10}  status")
    print("-" * 62)
    for nomor in ORDER:
        berkas = cari(arg.audio, nomor)
        if not berkas:
            print(f"{nomor:5}  berkas tidak ada — dilewati")
            continue
        r = rencana(berkas, slot_blok(tim, nomor), arg.maks)
        daftar.append((nomor, r))
        status = "pas" if r["kurang"] <= 0.02 else ("bisa" if r["bisa"] else "TIDAK BISA")
        print(f"{nomor:5}{r['total']:9.1f}{r['slot']:8.1f}{r['kurang']:8.1f}"
              f"{r['n']:6}{r['sisip']:10.2f}  {status}")

    gagal = [(n, r) for n, r in daftar if r["kurang"] > 0.02 and not r["bisa"]]
    if gagal:
        print(f"\n{len(gagal)} blok butuh jeda lebih lebar dari {arg.maks:.1f} s per titik:")
        for n, r in gagal:
            print(f"  {n}: kurang {r['kurang']:.1f} s dibagi {r['n']} jeda "
                  f"= {r['sisip']:.2f} s. Batas {arg.maks:.1f} s.")
        print("Blok itu tetap ditulis apa adanya, tapi narasinya akan terdengar banyak berhenti.")

    if not arg.tulis:
        print("\n(tidak ada yang ditulis — tambahkan --tulis)")
        return 0

    for nomor, r in daftar:
        keluar = arg.audio / f"{nomor}_laras.wav"
        if r["kurang"] <= 0.02:
            keluar = arg.audio / f"{nomor}_laras.wav"
            bangun(r["berkas"], r["jeda"], 0.0, keluar)
        else:
            bangun(r["berkas"], r["jeda"], r["sisip"], keluar)
        print(f"{nomor}_laras.wav  {durasi(keluar):.1f} s / slot {r['slot']:.1f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
