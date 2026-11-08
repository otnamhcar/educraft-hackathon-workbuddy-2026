"""Buat subtitle dari skrip berjeda + audio hasil TTS.

Prinsipnya: subtitle mengikuti ucapan, bukan sebaliknya.

1. Skrip dipecah jadi kalimat di setiap jeda `((⏱️=ms))`. Jeda milik kalimat sebelumnya.
2. Panjang ucapan tiap kalimat dihitung dari jumlah kata dibagi tempo.
3. Waktu tiap kalimat = (waktu mulai blok) + (durasi ucapan sebelumnya) + (jeda sebelumnya).
4. Kalimat yang terlalu panjang dipecah lagi di koma, dan waktunya dibagi menurut jumlah kata.

Kalau audio TTS-nya sudah ada, setiap titik potong diverifikasi dengan mendeteksi keheningan
nyata. Kalau mesin mengabaikan jeda, angkanya akan ketahuan sebelum video dirender.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKRIP = HERE / "SKRIP_TTS_JEDA.md"
TIMING = HERE / "TIMING.json"

POLA_JEDA = re.compile(r"\(\(⏱️=(\d+)\)\)")

MAKS_BARIS = 42          # karakter per baris. Di atas ini mata harus melompat balik.
BARIS_PER_CUE = 2        # dua baris per cue. Tiga baris menutupi terlalu banyak gambar.
MAKS_CUE = 7.0           # detik. Lebih lama, penonton membaca ulang cue yang sama.
MIN_CUE = 1.2            # detik. Lebih pendek, cue berkedip.
MIN_KATA_CUE = 3         # di bawah ini, lebih baik digabung dengan cue sebelumnya.
KATA_DIPERTAHANKAN = {"Persetujuan", "Baik,", "Satu.", "Ditolak."}  # sengaja sendirian
NAPAS = 0.06             # celah antar cue supaya tidak menyambung jadi satu balok.


@dataclass
class Kalimat:
    teks: str
    jeda_ms: int          # hanya untuk pemetaan waktu; tidak ditulis ke SRT
    kata: int


# Jeda di skrip adalah perintah untuk mesin TTS, bukan tanda baca. Karena itu jeda
# TIDAK ditampilkan ke penonton sebagai celah gambar-kosong-tanpa-teks: subtitle tetap
# menyala selama jeda, dengan kata terakhir kalimat masih terbaca. Alasannya, penonton
# yang membaca lebih lambat butuh waktu itu; menghapus teksnya saat suara berhenti
# justru membuat mereka kehilangan tempat. Celah hanya dibuat di batas blok.


def baca_blok(teks: str) -> dict[str, str]:
    return {m.group(1): m.group(2) for m in re.finditer(r"## `(\d{2})`.*?```\n(.*?)```", teks, re.S)}


def pecah(isi: str) -> list[Kalimat]:
    hasil: list[Kalimat] = []
    buf, pos = "", 0
    for cocok in POLA_JEDA.finditer(isi):
        buf += isi[pos:cocok.start()]
        pos = cocok.end()
        teks = " ".join(buf.split())
        if teks:
            hasil.append(Kalimat(teks, int(cocok.group(1)), len(teks.split())))
        buf = ""
    sisa = " ".join((buf + isi[pos:]).split())
    if sisa:
        hasil.append(Kalimat(sisa, 0, len(sisa.split())))
    return hasil


def bungkus(teks: str, maks: int = MAKS_BARIS) -> list[str]:
    """Bagi satu kalimat jadi baris subtitle.

    Aturan, berurut menurut kepentingan:

    1. Baris terakhir tidak boleh cuma satu kata. Satu kata sendirian di baris
       kedua membuat pembacaan tersendat dan terlihat seperti salah ketik.
    2. Jangan mengakhiri baris dengan kata sambung ("di", "yang", "untuk").
    3. Jangan memecah frasa tetap ("dua puluh", "tiga belas").
    4. Di antara pilihan yang lolos semua di atas, ambil yang paling seimbang.

    Kalau aturan 1 tidak bisa dipenuhi sekaligus dengan 2 dan 3, aturan 1 menang:
    lebih baik baris kedua dibuka dengan "yang" daripada berisi satu kata saja.
    """
    teks = " ".join(teks.split())
    if len(teks) <= maks:
        return [teks]
    kata = teks.split()

    if len(teks) > maks * BARIS_PER_CUE:
        # Terlalu panjang untuk dua baris: isi per baris apa adanya.
        baris, kini = [], ""
        for k in kata:
            calon = f"{kini} {k}".strip()
            if len(calon) <= maks or not kini:
                kini = calon
            else:
                baris.append(kini)
                kini = k
        if kini:
            baris.append(kini)
        return baris

    AKHIR_DILARANG = {
        "di", "ke", "dari", "yang", "dan", "atau", "untuk", "dengan", "pada",
        "itu", "ini", "tidak", "sudah", "akan", "juga", "tapi", "agar", "saat",
        "karena", "kalau", "bukan", "masih", "hanya", "lebih", "belum", "perlu",
        "bisa", "telah", "punya", "sama", "sampai",
    }
    FRASA = {("dua", "puluh"), ("tiga", "belas"), ("sepuluh", "sampai"),
             ("lima", "sampai"), ("satu", "sama"), ("di", "atas"), ("di", "bawah")}

    pilihan = []
    for i in range(1, len(kata)):
        a, b = " ".join(kata[:i]), " ".join(kata[i:])
        if len(a) > maks or len(b) > maks:
            continue
        akhiran = kata[i - 1].lower().strip(",.;:")
        awalan = kata[i].lower().strip(",.;:")
        kata_kedua = len(kata[i:])
        skor = 0
        if kata_kedua == 1:
            skor += 1000          # satu kata di baris kedua: paling dihindari
        elif kata_kedua == 2:
            skor += 200
        if akhiran in AKHIR_DILARANG:
            skor += 100
        if (akhiran, awalan) in FRASA:
            skor += 100
        skor += abs(len(a) - len(b))   # seimbang lebih enak dibaca
        pilihan.append((skor, a, b))

    if not pilihan:
        # Tidak ada yang muat dua baris dengan lebar ini: isi per baris.
        baris, kini = [], ""
        for k in kata:
            calon = f"{kini} {k}".strip()
            if len(calon) <= maks or not kini:
                kini = calon
            else:
                baris.append(kini)
                kini = k
        if kini:
            baris.append(kini)
        return baris

    _, a, b = min(pilihan)
    return [a, b]


def pecah_cue(kal: Kalimat) -> list[tuple[str, int]]:
    """Kembalikan [(teks_cue, jumlah_kata)] supaya waktu bisa dibagi proporsional."""
    if len(kal.teks) <= MAKS_BARIS * BARIS_PER_CUE:
        return [(kal.teks, kal.kata)]
    # Utamakan potong di tanda baca, karena di situ intonasi turun.
    bagian = [b.strip() for b in re.split(r"(?<=[,;:])\s+", kal.teks) if b.strip()]
    if len(bagian) > 1 and all(len(b) <= MAKS_BARIS * BARIS_PER_CUE for b in bagian):
        return [(b, len(b.split())) for b in bagian]
    baris = bungkus(kal.teks)
    hasil = []
    for i in range(0, len(baris), BARIS_PER_CUE):
        t = " ".join(baris[i : i + BARIS_PER_CUE])
        hasil.append((t, len(t.split())))
    return hasil


def waktu(d: float) -> str:
    ms = max(0, int(round(d * 1000)))
    j, sisa = divmod(ms, 3_600_000)
    m, sisa = divmod(sisa, 60_000)
    s, ms = divmod(sisa, 1000)
    return f"{j:02d}:{m:02d}:{s:02d},{ms:03d}"


def senyap(berkas: Path, ambang: int = -35, dur: float = 0.20) -> list[tuple[float, float]]:
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostdin", "-i", str(berkas),
         "-af", f"silencedetect=noise={ambang}dB:d={dur}", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    a = [float(x) for x in re.findall(r"silence_start:\s*([\d.]+)", r.stderr)]
    b = [float(x) for x in re.findall(r"silence_end:\s*([\d.]+)", r.stderr)]
    return list(zip(a, b))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--tempo", type=float, default=3.25, help="kata per detik")
    p.add_argument("--audio", type=Path, default=None, help="folder 01.ext…07.ext hasil TTS")
    p.add_argument("--keluar", type=Path, default=HERE / "subtitle_id.srt")
    p.add_argument("--lapor", action="store_true", help="tampilkan rincian per blok")
    arg = p.parse_args()

    blok = baca_blok(SKRIP.read_text())
    timing = json.loads(TIMING.read_text())
    nama = ["pembuka", "seg1", "seg2", "seg3", "seg4", "seg5", "seg6", "tutup"]
    urut = ["01", "02", "03", "04", "05", "06", "07", "08"]

    cues: list[tuple[float, float, str]] = []
    ringkas = []

    for nomor, kunci in zip(urut, nama):
        kal = pecah(blok[nomor])
        awal = timing["mulai_di"][kunci]
        slot = timing["batas_blok"][kunci] - awal

        # Waktu berjalan di dalam blok. Jeda tidak dibuang: cue terakhir sebuah kalimat
        # diperpanjang sampai kalimat berikutnya mulai, jadi teks tetap ada selama jeda.
        awal_cue: list[tuple[float, str]] = []
        n_cue = 0
        t = awal
        for k in kal:
            dur_kal = k.kata / arg.tempo
            bagian = pecah_cue(k)
            total_kata = sum(kk for _, kk in bagian) or 1
            for teks_cue, kata_cue in bagian:
                dur_cue = dur_kal * kata_cue / total_kata
                awal_cue.append((t, teks_cue))
                t += dur_cue
            t += k.jeda_ms / 1000

        # Gabung cue yang terlalu pendek/tipis ke cue sebelumnya, tapi hanya kalau
        # hasil gabungannya masih muat dua baris. Ini yang mencegah "Ditolak." (1 kata)
        # tampil sendirian sekilas di layar.
        rapat: list[tuple[float, str]] = []
        tertunda = ""
        for mulai_cue, teks_cue in awal_cue:
            kata_cue = teks_cue.split()
            sendiri = len(kata_cue) == 1 and kata_cue[0] in KATA_DIPERTAHANKAN
            if rapat and not sendiri:
                gabung = f"{rapat[-1][1]} {teks_cue}"
                pendek = len(kata_cue) < MIN_KATA_CUE
                muat = len(gabung) <= MAKS_BARIS * BARIS_PER_CUE
                if pendek and muat:
                    rapat[-1] = (rapat[-1][0], gabung)
                    continue
            if not rapat and len(kata_cue) < MIN_KATA_CUE:
                # Cue pembuka blok yang cuma satu-dua kata tidak punya cue sebelumnya
                # untuk menampungnya. Simpan dulu, tempel ke cue berikutnya.
                tertunda = teks_cue
                continue
            if tertunda:
                teks_cue = f"{tertunda} {teks_cue}"
                tertunda = ""
            rapat.append((mulai_cue, teks_cue))
        if tertunda:
            rapat.append((awal, tertunda))
        awal_cue = rapat

        # Selesai tiap cue = awal cue berikutnya dikurangi napas. Cue terakhir blok
        # berhenti di ujung blok, jadi tidak pernah menimpa kartu diam.
        for i, (mulai_cue, teks_cue) in enumerate(awal_cue):
            if i + 1 < len(awal_cue):
                selesai = awal_cue[i + 1][0] - NAPAS
            else:
                selesai = min(t, awal + slot)
            cues.append((mulai_cue, selesai, teks_cue))
            n_cue += 1

        dipakai = t - awal
        ringkas.append((nomor, len(kal), n_cue, slot, dipakai, dipakai - slot))

    if arg.lapor:
        print(f"{'blok':5}{'kalimat':>8}{'cue':>5}{'slot':>7}{'dipakai':>9}{'lebih':>8}")
        print("-" * 44)
        for n, nk, nc, slot, dip, lebih in ringkas:
            tanda = "  <<< LEWAT" if lebih > 0 else ""
            print(f"{n:5}{nk:8d}{nc:5d}{slot:7.0f}{dip:9.1f}{lebih:+8.1f}{tanda}")

    out = []
    idx = 0
    for a, b, teks_cue in cues:
        # Cue berikutnya menentukan sisa ruang: cue ini tidak boleh melewatinya,
        # dan tidak boleh diperpanjang sampai menutupinya.
        berikut = cues[idx + 1][0] if idx + 1 < len(cues) else None
        if b - a < MIN_CUE:
            b = a + MIN_CUE
        if berikut is not None:
            b = min(b, berikut - NAPAS)
        if b - a > MAKS_CUE:
            b = a + MAKS_CUE
        out.append(f"{idx + 1}\n{waktu(a)} --> {waktu(b)}\n")
        for l in bungkus(teks_cue):
            out.append(l.rstrip() + "\n")
        out.append("\n")
        idx += 1
    arg.keluar.write_text("".join(out))

    print(f"\n{len(cues)} cue → {arg.keluar.name}")
    terpanjang = max(len(l) for _, _, t in cues for l in bungkus(t))
    print(f"baris terpanjang {terpanjang} karakter (batas {MAKS_BARIS})")
    durasi_cue = [b - a for a, b, _ in cues]
    print(f"cue terpendek {min(durasi_cue):.1f} s, terpanjang {max(durasi_cue):.1f} s")

    if arg.audio:
        print("\nverifikasi terhadap audio:")
        for nomor in urut:
            calon = sorted(arg.audio.glob(f"{nomor}.*"))
            calon = [c for c in calon if c.suffix.lower() in {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg"}]
            if not calon:
                print(f"  {nomor}: berkas tidak ada, dilewati")
                continue
            s = senyap(calon[0])
            if s:
                d = sorted(y - x for x, y in s)
                print(f"  {nomor}: {len(s)} keheningan, median {d[len(d)//2]*1000:.0f} ms")
            else:
                print(f"  {nomor}: TIDAK ada keheningan — mesin mengabaikan jeda, timing perlu dari audio")
    return 0


if __name__ == "__main__":
    sys.exit(main())
