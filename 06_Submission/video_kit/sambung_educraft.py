#!/usr/bin/env python3
"""Sambung dua rekaman sesi tangkap EduCraft menjadi satu video demo.

Berbeda dari video_kit/concat_video.py yang menerima segmen utuh dari luar,
skrip ini memegang sendiri rencana potongannya, dengan alasan tertulis per
segmen. Sumbernya dua berkas rekaman berdurasi total 44 menit; yang dipakai
hanya jendela di sekitar momen bukti.

Aturan yang dipegang:
  1. Total keluar harus masuk 5:00-8:00 (handbook §7). Skrip menolak menulis
     berkas akhir kalau perkiraan durasi keluar dari rentang itu.
  2. Kelima momen bukti wajib terbawa utuh. Tidak ada potongan di tengah
     jendela bukti — hanya kepala dan ekor segmen yang dipangkas.
  3. Tiap sambungan diberi kartu jembatan supaya lompatan waktu terbaca
     sebagai lompatan yang disengaja, bukan rekaman rusak.

Rekaman baru sudah bersih: panel kiri tidak menampilkan nama akun, jadi tidak
ada penutupan wilayah di skrip ini.

Jalankan dari akar repo:
    python3 06_Submission/video_kit/sambung_educraft.py

Opsi:
    --kartu 3.5     lama tiap kartu jembatan, detik (bawaan 3.5)
    --tanpa-kartu   lewati sambungan; berguna untuk memeriksa gambar mentah
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SUMBER = Path("/home/carlito/Downloads/drive-download-20261107T115650Z-1-001")
KELUAR = REPO / "06_Submission" / "EduCraft_Demo.mp4"
KERJA = Path("/home/carlito/WorkBuddy AI/2026-11-07-19-54-15/.render_edu")
KARTU_DIR = HERE / "kartu"

CARD_OPEN = HERE / "card_00_pembuka.png"
CARD_CLOSE = HERE / "card_99_penutup.png"
CARD_SECONDS = 5.0
TARGET = (1366, 768)
FPS = 30
MIN_S, MAX_S = 300, 480
TARGET_S = 466

# Lima segmen. Tiap entri: berkas, mulai, durasi, kartu jembatan sesudahnya,
# dan bukti yang dijaga.
#   file1 00:00-02:05  prompt -> papan CP -> pertanyaan balik agen
#   file1 03:00-05:40  agen menemukan dua jawaban bertentangan, minta konfirmasi
#   file1 07:15-08:50  empat keputusan guru -> persetujuan -> render artefak
#   file1 21:30-24:50  cacat penomoran -> perbaikan -> lolos verifikasi visual
#   file2 03:00-05:20  "makanan halal" di luar katalog CP -> tawarkan dua jalan
#   file2 16:30-17:12  kuis diuji -> dua cacat tata letak dicatat
SEGMEN = [
    ("videoNew_01.mp4", 0.0, 82.0, None,
     "Prompt utuh sampai papan capaian; agen bertanya balik sebelum menulis."),
    ("videoNew_01.mp4", 186.0, 92.0, "kartu_1_selisih.png",
     "Agen menemukan dua jawaban bertentangan dan minta satu konfirmasi."),
    ("videoNew_01.mp4", 463.0, 51.0, "kartu_2_keputusan.png",
     "Empat keputusan diserahkan ke guru, lalu persetujuan tercatat."),
    ("videoNew_01.mp4", 1312.0, 106.0, "kartu_3_cacat.png",
     "Cacat penomoran ditemukan sendiri, diperbaiki, lolos verifikasi visual."),
    ("videoNew_01_2.mp4", 216.0, 36.0, "kartu_4_lingkup.png",
     "Permintaan di luar katalog CP IPAS ditolak dengan alasan, bukan dikarang."),
    ("videoNew_01_2.mp4", 1013.0, 11.0, "kartu_5_kuis.png",
     "Kuis diuji; dua cacat tata letak dicatat beserta cara menilainya."),
]


def run(cmd, label):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("GAGAL: {}".format(label), file=sys.stderr)
        print(result.stderr[-2000:], file=sys.stderr)
        raise SystemExit(1)


def duration(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True,
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


def ada_audio(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
         "stream=index", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    return bool(result.stdout.strip())


def klip(src, mulai, lama, dst):
    """Potong lalu normalkan ukuran, sar, dan fps. Audio dibuat seragam."""
    vf = ",".join([
        "scale={w}:{h}:force_original_aspect_ratio=decrease".format(w=TARGET[0], h=TARGET[1]),
        "pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=black".format(w=TARGET[0], h=TARGET[1]),
        "setsar=1",
        "fps={}".format(FPS),
    ])

    cmd = ["ffmpeg", "-y", "-ss", "{:.3f}".format(mulai), "-t", "{:.3f}".format(lama),
           "-i", str(src)]
    cmd += ["-f", "lavfi", "-t", "{:.3f}".format(lama), "-i", "anullsrc=r=48000:cl=stereo"]
    cmd += [
        "-map", "0:v:0", "-map", "1:a:0",
        "-vf", vf,
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "160k",
        "-shortest", str(dst),
    ]
    run(cmd, "memotong {} @ {:.0f}s".format(Path(src).name, mulai))


def gambar_jadi_klip(gambar, lama, dst):
    run(
        ["ffmpeg", "-y", "-loop", "1", "-i", str(gambar),
         "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
         "-t", "{:.3f}".format(lama), "-r", str(FPS),
         "-vf", "scale={w}:{h},setsar=1,fps={f}".format(w=TARGET[0], h=TARGET[1], f=FPS),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "160k",
         "-shortest", str(dst)],
        "membuat kartu {}".format(gambar.name),
    )


def main():
    ap = argparse.ArgumentParser(description="Sambung rekaman EduCraft.")
    ap.add_argument("--kartu", type=float, default=3.0, help="lama kartu jembatan (detik)")
    ap.add_argument("--tanpa-kartu", action="store_true", help="lewati kartu jembatan")
    args = ap.parse_args()

    for g in (CARD_OPEN, CARD_CLOSE):
        if not g.is_file():
            print("ERROR: kartu pembuka/penutup tidak ada: {}".format(g), file=sys.stderr)
            return 2

    lama_kartu = 0.0 if args.tanpa_kartu else args.kartu
    jumlah_jembatan = 0 if args.tanpa_kartu else len(SEGMEN)

    print("Rencana potongan:")
    total_segmen = 0.0
    for i, (nama, mulai, lama, jembatan, bukti) in enumerate(SEGMEN, start=1):
        path = SUMBER / nama
        if not path.is_file():
            print("ERROR: rekaman tidak ada: {}".format(path), file=sys.stderr)
            return 2
        if mulai + lama > duration(path):
            print("ERROR: {} cuma {:.0f}s, segmen {} minta sampai {:.0f}s".format(
                nama, duration(path), i, mulai + lama), file=sys.stderr)
            return 2
        total_segmen += lama
        print("  {}. {:<18} {:>6.0f}s-{:>6.0f}s  {:>5.0f}s  {}".format(
            i, nama, mulai, mulai + lama, lama, bukti))
    total_kartu = lama_kartu * jumlah_jembatan + 2 * CARD_SECONDS
    perkiraan = total_segmen + total_kartu
    print("\n  rekaman: {:.0f}s  kartu: {:.0f}s  total: {:.0f}s ({:.0f}:{:02.0f})".format(
        total_segmen, total_kartu, perkiraan,
        *divmod(perkiraan, 60)))

    if not (MIN_S <= perkiraan <= MAX_S):
        print("GAGAL: perkiraan durasi di luar 5:00-8:00.", file=sys.stderr)
        return 1
    if abs(perkiraan - TARGET_S) > 25:
        print("PERINGATAN: total {:.0f}s, target rancangan {}s.".format(perkiraan, TARGET_S),
              file=sys.stderr)

    KERJA.mkdir(parents=True, exist_ok=True)
    KELUAR.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(dir=str(KERJA)) as tmpdir:
        tmp = Path(tmpdir)
        parts = []

        gambar_jadi_klip(CARD_OPEN, CARD_SECONDS, tmp / "00_buka.mp4")
        parts.append(tmp / "00_buka.mp4")

        for i, (nama, mulai, lama, jembatan, _b) in enumerate(SEGMEN, start=1):
            seg = tmp / "{:02d}_seg.mp4".format(i)
            klip(SUMBER / nama, mulai, lama, seg)
            parts.append(seg)
            print("  segmen {}: {:.2f}s".format(i, duration(seg)))

            if not args.tanpa_kartu and jembatan:
                gambar = KARTU_DIR / jembatan
                if not gambar.is_file():
                    print("ERROR: kartu jembatan tidak ada: {}".format(gambar), file=sys.stderr)
                    return 2
                kj = tmp / "{:02d}_jembatan.mp4".format(i)
                gambar_jadi_klip(gambar, lama_kartu, kj)
                parts.append(kj)

        gambar_jadi_klip(CARD_CLOSE, CARD_SECONDS, tmp / "99_tutup.mp4")
        parts.append(tmp / "99_tutup.mp4")

        daftar = tmp / "list.txt"
        daftar.write_text(
            "".join("file '{}'\n".format(p.as_posix()) for p in parts), encoding="utf-8"
        )

        # Loudnorm ditahap akhir supaya semua segmen dan kartu punya tingkat
        # suara yang sama, tanpa memanggilnya berkali-kali.
        run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(daftar),
             "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k",
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", str(KELUAR)],
            "menyambung dan meratakan suara",
        )

    akhir = duration(KELUAR)
    menit, detik = divmod(round(akhir), 60)
    print("\nSelesai: {} ({:.3f}s = {}:{:02d})".format(KELUAR, akhir, menit, detik))

    if not (MIN_S <= akhir <= MAX_S):
        print("GAGAL: durasi akhir {:.0f}s di luar 5:00-8:00.".format(akhir), file=sys.stderr)
        return 1
    print("Durasi masuk rentang. Tonton sekali dari awal sebelum diunggah:")
    print("  ffplay {}".format(KELUAR))
    return 0


if __name__ == "__main__":
    sys.exit(main())
