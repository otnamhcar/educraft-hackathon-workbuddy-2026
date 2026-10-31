#!/usr/bin/env python3
"""Re-extract the plain text of the two source PDFs.

The agents read text, not PDFs, so `extracted/*.txt` is what every quoted fact in
this project actually traces back to. This script is the step that produced them,
kept so the extraction is reproducible instead of a black box.

Usage
-----
    python3 02_Sumber/extract_pdf.py                    # Linux / macOS
    python 02_Sumber\\extract_pdf.py                     # Windows
    python3 02_Sumber/extract_pdf.py --out build/txt    # write somewhere else

Paths are resolved from this file's own location, so it works from any working
directory and on any OS. Requires PyMuPDF:  pip install pymupdf

Line endings
------------
The committed `.txt` files were produced on Windows and use CRLF. They are written
here with `newline="\\r\\n"` on purpose, so re-running the script on Linux or macOS
reproduces the same bytes rather than a whole-file diff. `.gitattributes` marks
them `-text` so git never rewrites them either.

Exit codes: 0 = extracted, 1 = a PDF failed, 2 = input problem (missing PDF or
PyMuPDF not installed).
"""

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

FILES = {
    "panduan_ipas": "Final Panduan Mata Pelajaran IPAS_03_10_2025_Revisi 4.pdf",
    "permendikdasmen_13_2025": "Permendikdasmen-no-13-tahun-2025.pdf",
}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Extract text from the source PDFs.")
    parser.add_argument(
        "--base",
        default=str(HERE),
        help="folder holding the PDFs (default: this script's folder)",
    )
    parser.add_argument(
        "--out",
        default=str(HERE / "extracted"),
        help="folder for the .txt files (default: <base>/extracted)",
    )
    args = parser.parse_args(argv)

    try:
        # PyMuPDF renamed its module in 1.24; `fitz` still works but warns.
        try:
            import pymupdf as fitz
        except ImportError:
            import fitz
    except ImportError:
        print(
            "ERROR: PyMuPDF is not installed. Run:  pip install pymupdf",
            file=sys.stderr,
        )
        return 2

    base = Path(args.base).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()

    missing = [name for name in FILES.values() if not (base / name).is_file()]
    if missing:
        print(
            "ERROR: these PDFs are not in {}:\n  {}".format(base, "\n  ".join(missing)),
            file=sys.stderr,
        )
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)
    failures = 0

    for key, name in FILES.items():
        source = base / name
        target = out_dir / (key + ".txt")
        try:
            doc = fitz.open(str(source))
            pages = doc.page_count
            # CRLF on every OS, to match the committed files byte for byte.
            with open(str(target), "w", encoding="utf-8", newline="\r\n") as handle:
                handle.write("=== {} | pages={} ===\n\n".format(name, pages))
                for index, page in enumerate(doc):
                    text = page.get_text("text")
                    handle.write("\n----- PAGE {} -----\n".format(index + 1))
                    handle.write(
                        text
                        if text.strip()
                        else "[NO TEXT LAYER - possibly scanned image]\n"
                    )
            doc.close()
            print("{}: {} pages -> {}".format(key, pages, target))
        except Exception as exc:  # a broken PDF must not abort the other one
            failures += 1
            print("{}: ERROR {}".format(key, exc), file=sys.stderr)

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
