#!/usr/bin/env python3
"""Take one screenshot, correctly named, at full resolution, on this machine.

The capture runbook was written on a Linux box and tells you to run
``gnome-screenshot``. This machine is Windows, where that command does not
exist. This script is the replacement: it waits, grabs the screen at *physical*
pixel resolution, saves straight to the final file name, and tells you
immediately whether the result will pass ``tools/check_capture.py``.

    Windows            python tools\\capture.py --out <file.png>
    macOS / Linux      python3 tools/capture.py --out <file.png>

Why it sets DPI awareness first: Windows reports a 1366 px screen as 1093 px to
a DPI-unaware program at 125 % scaling. The saved image would then be silently
too narrow, and the only symptom is a checker failure an hour later.

Options:
    --out <path>       where to save; refuses to overwrite an existing file
    --delay <s>        countdown before the grab, default 5
    --region <l,t,r,b> crop to a box instead of the whole screen
    --all-screens      capture every monitor as one image
    --min-width <px>   width the checker expects, default 1366
    --force            overwrite an existing file (avoid: it is evidence)
    --no-color         plain text

Exit codes: 0 = saved and wide enough, 1 = saved but too narrow, 2 = cannot start.
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _report import Reporter, harden_console, use_color  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
MIN_BYTES = 8 * 1024  # below this, the frame is probably blank or a dialog


def set_dpi_awareness():
    """Ask Windows for real pixels, not scaled ones. Harmless elsewhere."""
    if sys.platform != "win32":
        return False
    try:
        import ctypes

        # 2 = PROCESS_PER_MONITOR_DPI_AWARE, available since Windows 8.1
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
        return True
    except Exception:
        try:
            import ctypes

            ctypes.windll.user32.SetProcessDPIAware()
            return True
        except Exception:
            return False


def parse_region(text):
    parts = [p.strip() for p in text.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("region must be left,top,right,bottom")
    try:
        left, top, right, bottom = (int(p) for p in parts)
    except ValueError:
        raise argparse.ArgumentTypeError("region values must be integers")
    if right <= left or bottom <= top:
        raise argparse.ArgumentTypeError("region right/bottom must exceed left/top")
    return (left, top, right, bottom)


def countdown(seconds, rep):
    if seconds <= 0:
        return
    for remaining in range(seconds, 0, -1):
        rep.plain("  capture in {} s ...".format(remaining))
        time.sleep(1)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Grab one screenshot at full resolution, straight to its final name."
    )
    parser.add_argument("--out", required=True, help="output PNG path")
    parser.add_argument("--delay", type=int, default=5, help="countdown seconds (default 5)")
    parser.add_argument("--region", type=parse_region, default=None,
                        help="crop box: left,top,right,bottom")
    parser.add_argument("--all-screens", action="store_true",
                        help="capture every monitor into one image")
    parser.add_argument("--min-width", type=int, default=1366,
                        help="width the checker expects (default 1366)")
    parser.add_argument("--force", action="store_true", help="overwrite existing file")
    parser.add_argument("--no-color", action="store_true", help="plain text")
    args = parser.parse_args(argv)

    harden_console()
    rep = Reporter(use_color(args.no_color, sys.stdout))
    out = Path(args.out)
    if not out.is_absolute():
        out = (Path.cwd() / out).resolve()

    if out.exists() and not args.force:
        rep.no("{} sudah ada -- tidak ditimpa".format(out.name))
        rep.plain("  Bukti yang sudah diambil jangan diganti diam-diam.")
        rep.plain("  Kalau memang ingin mengulang, tambahkan --force.")
        rep.summary()
        return 2

    try:
        from PIL import ImageGrab
    except ImportError:
        rep.no("Pillow tidak terpasang -- jalankan: python -m pip install pillow")
        rep.summary()
        return 2

    aware = set_dpi_awareness()
    rep.heading("Tangkap layar")
    rep.plain("  berkas : {}".format(out))
    rep.plain("  skala  : {}".format("DPI-aware (piksel fisik)" if aware else "apa adanya"))

    countdown(args.delay, rep)

    try:
        image = ImageGrab.grab(bbox=args.region, all_screens=args.all_screens)
    except Exception as exc:  # noqa: BLE001 - report, do not crash mid-session
        rep.no("gagal menangkap layar: {}".format(exc))
        rep.summary()
        return 2

    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        image.save(str(out), "PNG")
    except OSError as exc:
        rep.no("gagal menyimpan: {}".format(exc))
        rep.summary()
        return 2

    width, height = image.size
    size_kb = out.stat().st_size / 1024.0
    rep.plain("")
    rep.plain("  hasil  : {}x{} px, {:.0f} KB".format(width, height, size_kb))

    problems = 0
    if width < args.min_width:
        problems += 1
        rep.warn("lebar {} px < {} px -- check_capture.py akan menolak berkas ini"
                 .format(width, args.min_width))
        rep.plain("         Layar ini kemungkinan lebih sempit dari standar runbook.")
        rep.plain("         Lihat runbook bagian 1.4a: monitor eksternal, atau turunkan")
        rep.plain("         standar secara sadar dengan --min-width dan catat alasannya.")
    else:
        rep.ok("lebar {} px -- memenuhi standar {} px".format(width, args.min_width))

    if out.stat().st_size < MIN_BYTES:
        problems += 1
        rep.warn("berkas hanya {:.0f} KB -- mungkin kosong atau salah jendela".format(size_kb))

    rep.plain("")
    if problems:
        rep.plain("  Periksa dulu sebelum lanjut: satu tangkapan yang salah nama atau")
        rep.plain("  terlalu sempit lebih mahal daripada mengulang sekarang.")
    else:
        rep.plain("  Selesai. Jangan lupa isi kolom waktu, run ID, dan hasil di INDEX.md.")
    rep.summary()
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
