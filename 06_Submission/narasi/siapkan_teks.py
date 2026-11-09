"""Turunkan audio_layar/01.txt … 07.txt dari SKRIP_TTS_LAYAR.md.

Berkas .txt hanyalah salinan tempel: tanda jeda dibuang supaya bersih saat
ditempel ke editor TTS. Sumber kebenarannya tetap SKRIP_TTS_LAYAR.md — begitu
angka di sana berubah, jalankan berkas ini.

    python3 siapkan_teks.py          # tulis ulang yang berbeda
    python3 siapkan_teks.py --cek    # hanya laporkan, tidak menulis

Berkas yatim (nomor yang sudah tidak ada di skrip) dihapus, supaya sisa blok
dari struktur lama tidak ikut terbaca sebagai blok aktif.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKRIP = HERE / "SKRIP_TTS_LAYAR.md"
TUJUAN = HERE / "audio_layar"
POLA_JEDA = re.compile(r"\(\(⏱️=\d+\)\)")

# Judul blok memakai heading tepat setelah baris pemisah, jadi pola ini tidak
# boleh menelan tanda baca di judul. Blok diambil dari ``` … ``` pertama sesudah
# heading nomornya.
#
# Sufiks huruf diizinkan (`09b`) karena satu segmen bisa punya dua blok narasi.
# Tanpa `b?`, blok `09b` tidak terbaca sama sekali — lalu `09b.txt` dianggap
# yatim dan dihapus oleh pembersihan di bawah, tepat setelah dibuat.
POLA_BLOK = re.compile(r"^## `(\d{2}b?)`[^\n]*\n(?:(?!^## `).)*?```\n(.*?)\n```", re.M | re.S)


def blok_skrip(teks: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in POLA_BLOK.finditer(teks)}


def bersihkan(isi: str) -> str:
    """Buang tanda jeda dan rapikan spasi yang tertinggal.

    Tanda jeda sering berada di ujung baris di dalam skrip, jadi setelah dibuang
    tersisa baris yang diawali spasi. Tanpa langkah kedua, salinan .txt terlihat
    menggantung dan kelihatan seperti salah tulis.
    """
    teks = POLA_JEDA.sub(" ", isi)
    baris = [re.sub(r"\s+", " ", b).strip() for b in teks.split("\n")]
    teks = "\n".join(baris)
    return re.sub(r"\n{3,}", "\n\n", teks).strip()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--skrip", type=Path, default=SKRIP)
    p.add_argument("--cek", action="store_true")
    arg = p.parse_args()

    blok = blok_skrip(arg.skrip.read_text())
    if not blok:
        print(f"Tidak ada blok terbaca di {arg.skrip}", file=sys.stderr)
        return 1

    TUJUAN.mkdir(exist_ok=True)
    beda = 0
    for nomor in sorted(blok):
        baru = bersihkan(blok[nomor])
        berkas = TUJUAN / f"{nomor}.txt"
        lama = berkas.read_text().strip() if berkas.exists() else ""
        if baru == lama:
            print(f"{nomor}.txt  sama")
            continue
        beda += 1
        print(f"{nomor}.txt  {'BEDA' if lama else 'BARU'} — {len(lama)} → {len(baru)} karakter")
        if not arg.cek:
            berkas.write_text(baru + "\n")

    # buang berkas yatim: nomor yang tidak ada lagi di skrip
    for sisa in sorted(TUJUAN.glob("*.txt")):
        if sisa.stem not in blok:
            print(f"{sisa.name}  YATIM — nomor tidak ada di skrip")
            if not arg.cek:
                sisa.unlink()

    if arg.cek:
        print(f"\n{beda} berkas perlu diperbarui (--cek: tidak ditulis)")
    else:
        print(f"\n{beda} berkas diperbarui · {len(blok)} blok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
