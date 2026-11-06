#!/usr/bin/env python3
"""Gabungkan tiga rekaman layar + dua kartu judul menjadi satu video demo.

Tim ini lintas OS (Linux Mint dan Windows), jadi alatnya Python, bukan .sh —
aturan yang sama dengan `tools/`. Skrip ini hanya menyambung rekaman yang sudah
ada; ia tidak merekam apa pun.

    python 06_Submission/video_kit/concat_video.py ^
        --seg-a rekaman/seg_a.mp4 ^
        --seg-b rekaman/seg_b.mp4 ^
        --seg-c rekaman/seg_c.mp4 ^
        --out 06_Submission/EduCraft_Demo.mp4

(Garis miring biasa diterima di Windows; di PowerShell ganti `^` dengan backtick; di Linux/macOS
pakai `python3`.)

Yang dilakukan, berurutan:
  1. Setiap segmen dinormalkan ke ukuran yang sama / 30 fps / AAC 48 kHz. Rekaman dari
     OBS, Teams, dan QuickTime punya parameter berbeda; menyambung tanpa
     menormalkan lebih dulu menghasilkan audio yang bergeser di sambungan.
  2. Dua kartu judul dijadikan klip 5 detik tanpa suara.
  3. Semua disambung, lalu audio diratakan dengan loudnorm (target -16 LUFS,
     standar platform video).
  4. Durasi akhir diperiksa: 5:00-8:00. Di luar itu, skrip gagal.

Ukuran bawaan 1366x768 -- batas panel laptop yang dipakai merekam (keputusan 6 Nov
2026). Di mesin dengan layar lebih lebar, timpa dengan `--size 1920x1080`; jangan
perbesar rekaman 1366 ke 1920, hasilnya buram tanpa menambah informasi.

Butuh `ffmpeg` dan `ffprobe` di PATH. Di Windows keduanya terpasang (9.0.2) dan folder `bin`-nya
sudah ada di PATH pengguna; kalau sebuah terminal lama bilang tidak dikenali, buka terminal baru —
PATH dibaca sekali saat proses lahir (lihat `06_Submission/13_Demo_Video_Runbook.md` §2.1).
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CARD_OPEN = HERE / "card_00_pembuka.png"
CARD_CLOSE = HERE / "card_99_penutup.png"
CARD_SECONDS = 5
TARGET = (1366, 768)  # batas panel mesin perekam; timpa dengan --size
FPS = 30
MIN_S, MAX_S = 300, 480


def run(cmd, label):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("GAGAL: {}".format(label), file=sys.stderr)
        print(result.stderr[-1200:], file=sys.stderr)
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


def has_audio(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
         "stream=index", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    return bool(result.stdout.strip())


def normalise(src, dst):
    """Satu format untuk semua: ukuran, fps, sample rate, dua kanal."""
    vf = (
        "scale={w}:{h}:force_original_aspect_ratio=decrease,"
        "pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1"
    ).format(w=TARGET[0], h=TARGET[1])
    cmd = ["ffmpeg", "-y", "-i", str(src)]
    if not has_audio(src):
        cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
    cmd += [
        "-vf", vf, "-r", str(FPS),
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k",
        "-shortest", str(dst),
    ]
    run(cmd, "menormalkan {}".format(Path(src).name))


def card_clip(image, dst):
    run(
        ["ffmpeg", "-y", "-loop", "1", "-i", str(image),
         "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
         "-t", str(CARD_SECONDS), "-r", str(FPS),
         "-vf", "scale={}:{},setsar=1".format(*TARGET),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-ar", "48000", "-ac", "2", str(dst)],
        "membuat kartu {}".format(image.name),
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sambung rekaman demo menjadi satu video.")
    parser.add_argument("--seg-a", required=True, help="0:00-2:05 kail, masalah, arsitektur")
    parser.add_argument("--seg-b", required=True, help="2:05-4:00 planner, writer")
    parser.add_argument("--seg-c", required=True, help="4:00-7:40 tiga perhentian, refleksi, penutup")
    parser.add_argument("--out", default=str(HERE.parent / "EduCraft_Demo.mp4"))
    parser.add_argument("--skip-cards", action="store_true", help="tanpa kartu judul")
    parser.add_argument("--size", default=None,
                        help="ukuran keluaran LEBARxTINGGI, mis. 1920x1080")
    args = parser.parse_args(argv)

    global TARGET
    if args.size:
        try:
            w, h = (int(part) for part in args.size.lower().split("x"))
        except ValueError:
            print("ERROR: --size harus berbentuk LEBARxTINGGI, mis. 1366x768", file=sys.stderr)
            return 2
        TARGET = (w, h)

    segments = [Path(args.seg_a), Path(args.seg_b), Path(args.seg_c)]
    for path in segments:
        if not path.is_file():
            print("ERROR: rekaman tidak ditemukan: {}".format(path), file=sys.stderr)
            return 2

    print("Masukan:")
    total = 0.0
    for path in segments:
        seconds = duration(path)
        total += seconds
        print("  {:<40} {:>7.1f} s".format(path.name, seconds))
    print("  total rekaman: {:.1f} s".format(total))
    if total < MIN_S - 10:
        print("  PERINGATAN: rekaman belum mencapai 5 menit; tambah materi, jangan dipercepat.")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        parts = []

        if not args.skip_cards:
            card_clip(CARD_OPEN, tmp / "00_card.mp4")
            parts.append(tmp / "00_card.mp4")

        for index, path in enumerate(segments, start=1):
            target = tmp / "{:02d}_seg.mp4".format(index)
            normalise(path, target)
            parts.append(target)

        if not args.skip_cards:
            card_clip(CARD_CLOSE, tmp / "99_card.mp4")
            parts.append(tmp / "99_card.mp4")

        listing = tmp / "list.txt"
        listing.write_text(
            "".join("file '{}'\n".format(p.as_posix()) for p in parts), encoding="utf-8"
        )

        run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(listing),
             "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k",
             "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", str(out)],
            "menyambung dan meratakan suara",
        )

    final = duration(out)
    minutes, seconds = divmod(round(final), 60)
    print("\nSelesai: {} ({:.0f} menit {:02d} detik)".format(out, minutes, seconds))

    if not (MIN_S <= final <= MAX_S):
        print("GAGAL: durasi {:.0f} s di luar rentang 5:00-8:00.".format(final), file=sys.stderr)
        return 1
    print("Durasi masuk rentang 5:00-8:00. Tonton sekali dari awal sebelum diunggah.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
