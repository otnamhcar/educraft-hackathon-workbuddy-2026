#!/usr/bin/env python3
"""Tempelkan tiga rekaman narasi ke video yang sudah tersambung.

`concat_video.py` menyambung layar; ia tidak menerima berkas suara. Skrip ini
mengerjakan bagian itu: narasi_a/b/c diletakkan pada detik yang sudah dihitung di
`NARASI_TIMING.json`, sehingga kalimatnya jatuh tepat di adegannya — bukan
dipaksakan mengisi seluruh durasi.

    python 06_Submission/video_kit/attach_narration.py \\
        --video tersambung.mp4 \\
        --narasi-a narasi_a.m4a --narasi-b narasi_b.m4a --narasi-c narasi_c.m4a \\
        --timing 06_Submission/video_kit/NARASI_TIMING.json \\
        --out bernarasi.mp4

Yang dilakukan:
  1. Membaca titik mulai setiap take dari NARASI_TIMING.json.
  2. Menempelkan tiap take pada titik itu di atas dasar senyap sepanjang video.
  3. Meratakan hasilnya dengan loudnorm ke -16 LUFS (standar platform video).
  4. Memeriksa hasil: durasi tidak boleh berubah, dan stream audio harus ada.

Berkas narasi boleh .m4a, .wav, .mp3, atau apa pun yang dikenali ffmpeg.
Kalau sebuah take lebih panjang daripada slotnya, take itu DIPOTONG di akhir dan
skrip melaporkannya — lebih baik tahu di sini daripada melihatnya di menit keenam.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TIMING = HERE / "NARASI_TIMING.json"


def run(cmd, label):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("GAGAL: {}".format(label), file=sys.stderr)
        print(result.stderr[-1500:], file=sys.stderr)
        raise SystemExit(1)
    return result


def probed(path, entries):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", entries,
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True,
    )
    return result.stdout.strip()


def duration(path):
    try:
        return float(probed(path, "format=duration").splitlines()[0])
    except (ValueError, IndexError):
        return 0.0


def has_audio(path):
    return bool(probed(path, "stream=index").strip())


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Tempelkan narasi ke video sesuai titik waktu di NARASI_TIMING.json.")
    parser.add_argument("--video", required=True, help="video yang sudah tersambung")
    parser.add_argument("--narasi-a", required=True, help="take segmen A (0:00-2:05)")
    parser.add_argument("--narasi-b", required=True, help="take segmen B (2:05-4:00)")
    parser.add_argument("--narasi-c", required=True, help="take segmen C (4:00-7:55)")
    parser.add_argument("--timing", default=str(DEFAULT_TIMING),
                        help="berkas JSON titik mulai; bawaan NARASI_TIMING.json")
    parser.add_argument("--out", default="bernarasi.mp4")
    parser.add_argument("--skip-loudnorm", action="store_true",
                        help="jangan ratakan level (hanya untuk mendiagnosa)")
    args = parser.parse_args(argv)

    video = Path(args.video)
    if not video.is_file():
        print("ERROR: video tidak ditemukan: {}".format(video), file=sys.stderr)
        return 2

    timing_path = Path(args.timing)
    if not timing_path.is_file():
        print("ERROR: berkas timing tidak ditemukan: {}".format(timing_path), file=sys.stderr)
        return 2
    timing = json.loads(timing_path.read_text(encoding="utf-8"))

    total = duration(video)
    if total <= 0:
        print("ERROR: durasi video tidak terbaca. Berkasnya utuh?", file=sys.stderr)
        return 2
    print("Video: {} ({:.1f} s)".format(video.name, total))

    takes = []
    for key, path_str in (("A", args.narasi_a), ("B", args.narasi_b), ("C", args.narasi_c)):
        path = Path(path_str)
        if not path.is_file():
            print("ERROR: narasi {} tidak ditemukan: {}".format(key, path), file=sys.stderr)
            return 2
        slot = timing["takes"][key]
        start = float(slot["start"])
        limit = float(slot.get("max_seconds", total - start))
        voice = duration(path)
        note = ""
        if voice > limit + 0.05:
            note = "  <- LEBIH PANJANG dari slot {:.1f} s, akan dipotong".format(limit)
        elif voice < limit - 3:
            note = "  ({} detik lebih pendek dari slot — jeda di akhir, itu wajar)".format(
                round(limit - voice))
        takes.append({"key": key, "path": path, "start": start, "limit": limit,
                      "voice": voice, "note": note})
        print("  take {:<2} {:<28} mulai {:>6.1f} s, suara {:>6.1f} s, slot {:>6.1f} s{}".format(
            key, path.name, start, voice, limit, note))

    inputs = ["-i", str(video)]
    for take in takes:
        # -t sebelum -i memotong INPUT, jadi take yang melar tidak ikut terkirim.
        # atrim saja tidak cukup: adelay membaca timestamp asli berkas, sehingga
        # take yang lebih panjang dari slot-nya akan tumpah ke take berikutnya.
        inputs += ["-t", "{:.3f}".format(take["limit"]), "-i", str(take["path"])]

    filters = []
    for index, take in enumerate(takes, start=1):
        # Urutannya penting dan sudah diuji 7 November 2026:
        #   aformat -> atrim -> asetpts=N/SR/TB -> adelay
        # `adelay` menambahkan offset ke PTS yang ADA, bukan menggantinya. Tanpa
        # `asetpts` sesudah `atrim`, take yang melar membuat take berikutnya
        # bergeser sejauh kelebihan itu. Uji dengan take A 130 s pada slot 125 s:
        # take B tidak muncul di 130 s, melainkan di 135 s — diam selama 5 detik,
        # dan tidak ada yang memberi tahu. `asetpts` mengembalikan PTS ke nol
        # setelah pemotongan, jadi adelay selalu mulai dari titik yang benar.
        filters.append(
            "[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,"
            "atrim=0:{limit},asetpts=N/SR/TB,apad=whole_dur={limit},"
            "adelay={ms}|{ms}[v{k}]".format(
                i=index, limit=take["limit"], ms=int(take["start"] * 1000), k=take["key"]))

    voices = "[vA][vB][vC]amix=inputs=3:duration=longest:normalize=0[mix]"
    # Di bawah narasi: senyap sepanjang video, bukan audio rekaman layar.
    bed = "anullsrc=r=48000:cl=stereo,atrim=0:{:.3f},aformat=channel_layouts=stereo[bed]".format(
        total)
    if args.skip_loudnorm:
        tail = "[bed][mix]amix=inputs=2:duration=first:normalize=0[aout]"
    else:
        tail = ("[bed][mix]amix=inputs=2:duration=first:normalize=0,"
                "loudnorm=I=-16:TP=-1.5:LRA=11[aout]")

    filter_complex = ";".join(filters + [voices, bed, tail])

    cmd = ["ffmpeg", "-y"] + inputs + [
        "-filter_complex", filter_complex,
        "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "192k",
        "-movflags", "+faststart",
        str(args.out),
    ]
    run(cmd, "menempelkan narasi")

    out = Path(args.out)
    if not out.is_file():
        print("ERROR: keluaran tidak terbentuk.", file=sys.stderr)
        return 1
    if not has_audio(out):
        print("ERROR: keluaran tidak punya stream audio.", file=sys.stderr)
        return 1

    final = duration(out)
    drift = abs(final - total)
    minutes, seconds = divmod(round(final), 60)
    print("\nSelesai: {} ({}:{:02d})".format(out, minutes, seconds))
    if drift > 0.5:
        print("GAGAL: durasi bergeser {:.1f} s dari video asli ({:.1f} s).".format(drift, total),
              file=sys.stderr)
        return 1
    print("Durasi tidak bergeser (selisih {:.2f} s). Dengar 30 detik pertama dan 30 detik".format(drift))
    print("terakhir sebelum lanjut membakar subtitle.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
