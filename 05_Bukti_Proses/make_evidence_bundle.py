#!/usr/bin/env python3
"""
make_evidence_bundle.py
Zip an evidence bundle for the Tencent Cloud Hackathon submission.

Usage:
    python make_evidence_bundle.py --bundle evidence_bundle --out evidence_bundle.zip

The script zips the entire bundle folder (workflow, results, screenshots, audit log)
into a single archive with a top-level folder named after the bundle.
"""
import argparse
import os
import sys
import zipfile
from datetime import datetime


def zip_dir(src_dir: str, out_zip: str) -> None:
    if not os.path.isdir(src_dir):
        sys.exit(f"[ERROR] Bundle folder not found: {src_dir}")
    out_dir = os.path.dirname(os.path.abspath(out_zip))
    os.makedirs(out_dir, exist_ok=True)
    top = os.path.basename(os.path.normpath(src_dir))
    count = 0
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, files in os.walk(src_dir):
            for fn in files:
                full = os.path.join(dirpath, fn)
                arc = os.path.join(top, os.path.relpath(full, src_dir))
                z.write(full, arc)
                count += 1
    size_kb = os.path.getsize(out_zip) / 1024
    print(f"[OK] {count} files zipped -> {out_zip} ({size_kb:.1f} KB)")


def main() -> None:
    p = argparse.ArgumentParser(description="Zip an evidence bundle for hackathon submission.")
    p.add_argument("--bundle", default="evidence_bundle", help="Path to the evidence bundle folder")
    p.add_argument("--out", default=None, help="Output zip path (default: <bundle>_<timestamp>.zip)")
    args = p.parse_args()

    out = args.out
    if not out:
        ts = datetime.now().strftime("%Y%m%d_%H%M")
        out = f"{os.path.basename(os.path.normpath(args.bundle))}_{ts}.zip"

    zip_dir(args.bundle, out)


if __name__ == "__main__":
    main()
