#!/usr/bin/env python3
"""Are the screenshot files actually fit to submit?

The capture runbook asks for 21 screenshots. It is easy to finish capturing and
only discover at submission time that a file was saved under the wrong name, or
that it is 1280 px wide instead of 1600, or that a folder is still empty. This
script answers that question before a judge does.

It is read-only. It never renames, moves or deletes anything.

    Linux / macOS      python3 tools/check_capture.py
    Windows (cmd)      python tools\\check_capture.py

The list of expected files is parsed from the tracker itself
(``05_Bukti_Proses/evidence_bundle/03_screenshots/INDEX.md``) rather than kept in
a second list here -- two lists drift apart, one does not.

What it cannot check: whether the screenshot is readable to a human, and whether
personal data leaked into the frame. Those need eyes. See runbook section 0.

Options:
    --dir <path>       screenshot folder (default: the evidence bundle)
    --index <path>     tracker file (default: INDEX.md inside that folder)
    --min-width <px>   minimum width, default 1366 (this laptop's panel)
    --no-color         plain text, also honoured via the NO_COLOR environment

Exit codes: 0 = every mandatory shot present and valid, 1 = at least one problem,
2 = cannot start.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _report import Reporter, harden_console, use_color  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DIR = REPO_ROOT / "05_Bukti_Proses" / "evidence_bundle" / "03_screenshots"
# 1366 = this laptop's panel width. The runbook standard was 1600 until 6 Nov
# 2026; the screen cannot reach it, so the team lowered the bar deliberately
# rather than upscaling captures. See runbook section 1.4a. Override with
# --min-width on a wider machine.
MIN_WIDTH = 1366
SUSPICIOUS_BYTES = 8 * 1024  # a real screenshot is far larger than this

PNG_SIG = b"\x89PNG\r\n\x1a\n"
FILE_RE = re.compile(r"`([^`]+\.png)`")


class Expectation(object):
    __slots__ = ("name", "mandatory", "section", "result")

    def __init__(self, name, mandatory, section, result):
        self.name = name
        self.mandatory = mandatory
        self.section = section
        self.result = result

    @property
    def acknowledged(self):
        """A gap the team has already declared, not one it forgot.

        "TO RUN" and "FAIL" are legitimate answers -- the project discloses what
        it has not proven. Only silence is a problem.
        """
        return self.result.upper() in ("TO RUN", "FAIL", "BY DESIGN")


def parse_index(path):
    """Read the tracker. Returns expectations, declared total, rows, gaps.

    Section A lists the seven scenes every submission needs. Section B lists the
    21 test cases; the critical ones carry "(kritis)" in the row. One row may name
    two files, and one row (TC-07) has no file at all, so files and rows are
    counted separately.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    expectations = []
    declared_total = None
    rows = 0
    filled_rows = 0
    no_file = []
    section = None

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## A."):
            section = "A"
            continue
        if stripped.startswith("## B."):
            section = "B"
            continue
        if stripped.startswith("## C."):
            section = "C"
            continue
        if not stripped.startswith("|"):
            continue

        if section == "C":
            match = re.search(r"\*\*Total\*\*\s*\|\s*\*\*(\d+)\*\*", stripped)
            if match:
                declared_total = int(match.group(1))
            continue

        if section not in ("A", "B"):
            continue

        if section == "B" and stripped.startswith("| TC-"):
            rows += 1

        cells = stripped.split("|")
        # A: | # | scene | file | run id | time | status |
        # B: | TC | rule | file | result | note |
        result_index = 5 if section == "A" else 4
        result = ""
        if len(cells) > result_index:
            result = cells[result_index].strip()
        if section == "B" and stripped.startswith("| TC-") and result:
            filled_rows += 1

        names = FILE_RE.findall(stripped)
        if not names:
            if section == "B" and stripped.startswith("| TC-"):
                no_file.append(cells[1].strip() if len(cells) > 1 else "?")
            continue

        mandatory = section == "A" or "(kritis)" in stripped
        for name in names:
            expectations.append(Expectation(name, mandatory, section, result))

    return expectations, declared_total, rows, filled_rows, no_file


def png_size(path):
    """Width and height straight from the IHDR chunk. No Pillow required."""
    try:
        with open(str(path), "rb") as handle:
            head = handle.read(24)
    except OSError:
        return None
    if len(head) < 24 or not head.startswith(PNG_SIG) or head[12:16] != b"IHDR":
        return None
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def check_files(rep, folder, expectations, min_width):
    rep.heading("1. Screenshots listed in INDEX.md")
    if not expectations:
        rep.no("INDEX.md lists no .png files -- is the table intact?")
        return

    seen = set()
    missing_mandatory = []
    missing_optional = []
    declared_gaps = []

    for item in expectations:
        if item.name in seen:
            continue
        seen.add(item.name)
        path = folder / item.name

        if not path.is_file():
            if item.acknowledged:
                declared_gaps.append((item.name, item.result.upper()))
            elif item.mandatory:
                missing_mandatory.append(item.name)
            else:
                missing_optional.append(item.name)
            continue

        size = png_size(path)
        if size is None:
            rep.no("{} -- not a valid PNG".format(item.name))
            continue
        width, height = size
        if width < min_width:
            rep.no(
                "{} -- {}x{} px, needs at least {} px wide".format(
                    item.name, width, height, min_width
                )
            )
            continue
        if path.stat().st_size < SUSPICIOUS_BYTES:
            rep.warn(
                "{} -- {}x{} px but only {:.0f} KB, check it is not blank".format(
                    item.name, width, height, path.stat().st_size / 1024.0
                )
            )
            continue
        rep.ok("{} -- {}x{} px".format(item.name, width, height))

    if missing_mandatory:
        for name in missing_mandatory:
            rep.no("{} -- missing (mandatory)".format(name))
    if declared_gaps:
        for name, label in declared_gaps:
            rep.warn("{} -- declared {}, no file".format(name, label))
    if missing_optional:
        rep.warn(
            "{} optional shot(s) not taken: {}".format(
                len(missing_optional), ", ".join(missing_optional)
            )
        )


def check_orphans(rep, folder, expectations):
    rep.heading("2. Files on disk that INDEX.md does not list")
    known = {item.name for item in expectations}
    # as_posix(), bukan str(): INDEX.md menulis garis miring biasa, sedangkan str() di
    # Windows menghasilkan garis miring terbalik. Tanpa ini setiap berkas dilaporkan
    # sebagai "not in INDEX.md" di Windows, dan laporannya jadi tidak bisa dipercaya.
    on_disk = sorted(
        p.relative_to(folder).as_posix() for p in folder.rglob("*.png")
    )
    orphans = [name for name in on_disk if name not in known]
    if not orphans:
        rep.ok("no stray files")
        return
    for name in orphans[:10]:
        rep.warn("{} -- not in INDEX.md, rename or add a row".format(name))
    if len(orphans) > 10:
        rep.warn("... and {} more".format(len(orphans) - 10))


def check_tracker(rep, expectations, declared_total, rows, filled_rows, no_file):
    rep.heading("3. Tracker arithmetic")
    if declared_total is None:
        rep.warn("INDEX.md section C has no declared total")
        return
    if declared_total != rows:
        rep.no(
            "section C declares {} test cases, section B has {} rows".format(
                declared_total, rows
            )
        )
    else:
        rep.ok("section C total matches the {} rows in section B".format(rows))

    distinct = len({item.name for item in expectations})
    rep.ok("{} distinct screenshot files across {} rows".format(distinct, rows))

    if no_file:
        rep.warn(
            "row(s) with no screenshot at all: {} -- cannot be evidenced".format(
                ", ".join(no_file)
            )
        )

    if filled_rows == 0:
        rep.warn("no result column filled in yet -- fill it as you capture")
    else:
        rep.ok("{}/{} rows have a result recorded".format(filled_rows, rows))


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check whether the captured screenshots are fit to submit."
    )
    parser.add_argument("--dir", help="screenshot folder")
    parser.add_argument("--index", help="tracker file")
    parser.add_argument("--min-width", type=int, default=MIN_WIDTH)
    parser.add_argument("--no-color", action="store_true", help="plain text output")
    args = parser.parse_args(argv)

    harden_console()

    folder = Path(args.dir).expanduser().resolve() if args.dir else DEFAULT_DIR
    index = Path(args.index).expanduser().resolve() if args.index else folder / "INDEX.md"

    if not index.is_file():
        print("ERROR: {} not found.".format(index), file=sys.stderr)
        return 2
    try:
        readable = folder.is_dir()
    except OSError as exc:
        print("ERROR: cannot read {}: {}".format(folder, exc), file=sys.stderr)
        return 2
    if not readable:
        print("ERROR: {} not found.".format(folder), file=sys.stderr)
        return 2

    expectations, declared_total, rows, filled_rows, no_file = parse_index(index)

    rep = Reporter(use_color(args.no_color, sys.stdout))
    print("Screenshots: {}".format(folder))
    print("Tracker    : {}".format(index))

    check_files(rep, folder, expectations, args.min_width)
    check_orphans(rep, folder, expectations)
    check_tracker(rep, expectations, declared_total, rows, filled_rows, no_file)

    rep.summary()

    if rep.failed > 0:
        print("  Not submittable yet. Fix the FAIL lines above.")
        return 1
    print("  Every mandatory screenshot is present and readable at 100%.")
    print("  Still check by eye: rule ID legible, quoted sentence visible, no")
    print("  student names or contact details in the frame (runbook section 0).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
