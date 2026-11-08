"""Ukur tempo dan perilaku jeda mesin TTS dari berkas yang sudah jadi.

Skrip TTS bukan sumber kebenaran soal durasi. Yang benar adalah berkas audionya.
Alat ini membongkar satu berkas jadi tiga angka:

    tempo murni      kata/detik saat benar-benar bersuara, tanpa jeda apa pun
    napas tambahan   jeda yang muncul sendiri, bukan dari ((⏱️=…)) — mesin menambah
                     jeda di dalam kalimat (setelah koma, setelah titik dua)
    rasio jeda       berapa kali lebih panjang jeda yang diminta ((⏱️=…)) dibanding
                     yang tertulis

Dipakai untuk menjawab satu pertanyaan saja: kalau angka jeda diturunkan, apakah
blok ini muat di slotnya, atau kalimatnya memang kelebihan kata.

    python3 ukur_tempo.py                 # laporan semua blok yang ada berkasnya
    python3 ukur_tempo.py --audio audio   # berkasnya di folder lain
    python3 ukur_tempo.py --json          # untuk dibaca setel_jeda.py
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKRIP = HERE / "SKRIP_TTS_LAYAR.md"
TIMING = HERE / "TIMING.json"
EKSTENSI = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".opus"}

# Dibaca dari TIMING.json supaya jumlah segmen tidak perlu disalin ke tiap skrip.
_tim = json.loads(TIMING.read_text())
ORDER = [b["nomor"] for b in _tim["berkas"]]
NAMES = [b["segmen"] for b in _tim["berkas"]]

# Ambang pemisah dua jenis senyap. Di bawah ini napas di dalam kalimat; di atasnya
# jeda yang memang diminta. Dari pengukuran: napas 0,39–0,58 s, jeda terpendek
# yang diminta 0,95 s. Batas 0,75 s jatuh di tengah ruang kosong itu.
NAPAS_MAKS = 0.75
NAPAS_MIN = 0.12

POLA_JEDA = re.compile(r"\(\(⏱️=(\d+)\)\)")


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
    """Kembalikan (mulai, selesai) tiap rentang senyap, termasuk yang di ujung berkas."""
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", str(berkas),
         "-af", "silencedetect=noise=-30dB:d=0.12", "-f", "null", "-"],
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


def blok_skrip(teks: str) -> dict[str, str]:
    return {
        m.group(1): m.group(2)
        for m in re.finditer(r"^## `(\d{2})`.*?```\n(.*?)```", teks, re.M | re.S)
    }


def cari(folder: Path, nomor: str) -> Path | None:
    for c in sorted(folder.glob(f"{nomor}.*")):
        if c.suffix.lower() in EKSTENSI:
            return c
    return None


def ukur(nomor: str, berkas: Path, isi_skrip: str, slot: float) -> dict:
    jeda = [int(x) for x in POLA_JEDA.findall(isi_skrip)]
    teks = POLA_JEDA.sub(" ", isi_skrip)
    kata = len(re.findall(r"[A-Za-zÀ-ÿ0-9]+", teks))

    rentang = senyap(berkas)
    panjang = [b - a for a, b in rentang]
    napas = [x for x in panjang if NAPAS_MIN <= x <= NAPAS_MAKS]
    jeda_audio = [x for x in panjang if x > NAPAS_MAKS]

    total = durasi(berkas)
    ucapan = total - sum(napas) - sum(jeda_audio)
    tempo = kata / ucapan if ucapan > 0 else 0.0

    # Rasio hanya bisa dihitung kalau jumlah titiknya masuk akal. Kalau tidak,
    # pencocokan posisi berisiko salah pasang dan rasionya jadi sampah.
    rasio = None
    if jeda and len(jeda_audio) >= max(3, len(jeda) // 2):
        # Buang titik ujung blok dari kedua sisi: yang di skrip mengisi sisa slot,
        # yang di audio ikut terpotong di ujung rekaman. Membandingkannya menyesatkan.
        a, b = jeda[:-1], jeda_audio[:-1]
        if a and b:
            pasangan = list(zip(a, b))[: min(len(a), len(b))]
            if pasangan:
                rasio = sum(y * 1000 for _, y in pasangan) / sum(x for x, _ in pasangan)

    return {
        "nomor": nomor,
        "berkas": berkas.name,
        "kata": kata,
        "durasi": total,
        "slot": slot,
        "tempo": tempo,
        "napas_ms": sum(napas) * 1000,
        "jumlah_napas": len(napas),
        "jeda_skrip_ms": sum(jeda),
        "jeda_audio_ms": sum(jeda_audio) * 1000,
        "jumlah_jeda_skrip": len(jeda),
        "rasio_jeda": rasio,
        "ucapan": ucapan,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--audio", type=Path, default=HERE)
    p.add_argument("--skrip", type=Path, default=SKRIP)
    p.add_argument("--json", action="store_true")
    arg = p.parse_args()

    tim = json.loads(TIMING.read_text())
    skrip = blok_skrip(arg.skrip.read_text())

    hasil = []
    for nomor, nama in zip(ORDER, NAMES):
        berkas = cari(arg.audio, nomor)
        if not berkas or nomor not in skrip:
            continue
        slot = slot_blok(tim, nomor)
        hasil.append(ukur(nomor, berkas, skrip[nomor], slot))

    if not hasil:
        print("tidak ada berkas audio yang cocok.", file=sys.stderr)
        return 1

    if arg.json:
        print(json.dumps(hasil, indent=2, ensure_ascii=False))
        return 0

    print(f"{'blok':5}{'kata':>5}{'slot':>7}{'durasi':>8}{'tempo':>7}"
          f"{'napas':>8}{'jeda':>7}{'rasio':>7}{'muat?':>8}")
    print("-" * 66)
    for h in hasil:
        rasio = f"{h['rasio_jeda']:.2f}" if h["rasio_jeda"] else "  —"
        muat = "ya" if h["durasi"] <= h["slot"] else f"+{h['durasi'] - h['slot']:.1f}s"
        print(f"{h['nomor']:5}{h['kata']:5}{h['slot']:7.0f}{h['durasi']:8.2f}"
              f"{h['tempo']:7.2f}{h['napas_ms'] / 1000:8.1f}{h['jeda_audio_ms'] / 1000:7.1f}"
              f"{rasio:>7}{muat:>8}")

    tempo = sum(h["kata"] for h in hasil) / sum(h["ucapan"] for h in hasil)
    napas = sum(h["napas_ms"] for h in hasil) / 1000 / len(hasil)
    rasio = [h["rasio_jeda"] for h in hasil if h["rasio_jeda"]]

    # Sebaran tempo antar blok. Ini yang menentukan apakah satu angka tempo cukup:
    # kalau rentangnya lebar, memakai rata-rata membuat perkiraan meleset beberapa
    # detik di blok yang paling jauh dari rata-rata. Terukur pada mesin ini: 2,56
    # sampai 3,03 — selisih 0,47 kata/detik, cukup untuk menggeser blok 02 sekitar
    # 7 detik. Karena itu penghitungan ulang dilakukan per blok.
    kps = [h["tempo"] for h in hasil]
    print(f"\ntempo murni mesin   : {tempo:.2f} kata/detik (rata-rata berbobot)")
    print(f"  sebaran antar blok: {min(kps):.2f} – {max(kps):.2f} "
          f"(selisih {max(kps) - min(kps):.2f})")
    print(f"napas tambahan      : {napas * 1000:.0f} ms per blok, di luar kendali skrip")
    if rasio:
        print(f"rasio jeda diminta  : {sum(rasio) / len(rasio):.2f}× lebih panjang dari angka skrip")
        print(f"  artinya ((⏱️=1000)) keluar sebagai ±{1000 * sum(rasio) / len(rasio):.0f} ms")
    return 0


if __name__ == "__main__":
    sys.exit(main())
