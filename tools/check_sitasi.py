#!/usr/bin/env python3
"""Check the citation convention of a teaching run.

Since 5 November 2026 the class-facing documents use a different citation style
from the audit trail:

  RPP + slide   name the source in words (``Panduan IPAS, hlm. 45-47``), never a
                ``[src:...]`` code.
  quiz          names no source at all.
  traceability  ``05_Jejak_Sumber.md`` keeps the machine-readable tags for audit.

That split is easy to break by accident — one copy-pasted tag, one slide without a
``Sumber`` line, and the convention silently degrades. This checker makes the
convention executable.

Rules
-----
R1  RPP, slide, and quiz contain no ``[src:...]`` code.
R2  Every slide section carries a ``**Sumber:**`` line.
R3  Every numbered subsection of RPP §D carries a source marker (``— *...*``).
R4  The quiz carries no ``**Sumber:**`` line.
R5  The traceability file exists and maps at least one tag per document.

A run that predates the convention has none of the four files; it is reported as
``SKIP`` with exit code 0 rather than as five failed rules.

Usage
-----
  python3 tools/check_sitasi.py --run 03_Hasil/edu_output_tata_surya

Exit code is non-zero when any rule fails.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

TAG_RE = re.compile(r"\[src:[^\]]+\]")
SLIDE_HEAD_RE = re.compile(r"^###\s+Slide\b")
RPP_SUBSECTION_RE = re.compile(r"^\*\*(\d+[a-z]?)\.\s")
SOURCE_MARKER_RE = re.compile(r"—\s*\*")
SLIDE_SOURCE_RE = re.compile(r"^\s*-\s*\*\*Sumber:\*\*", re.MULTILINE)
QUIZ_SOURCE_RE = re.compile(r"^\s*-\s*\*\*Sumber:\*\*", re.MULTILINE)

DEFAULTS = {
    "rpp": "01_RPP_Tata_Surya.md",
    "quiz": "02_Kuis_PrePost_Tata_Surya.md",
    "slide": "03_Slide_Outline_Tata_Surya.md",
    "trace": "05_Jejak_Sumber.md",
}


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.notes: list[str] = []

    def fail(self, rule: str, message: str) -> None:
        self.failures.append(f"{rule} {message}")

    def note(self, message: str) -> None:
        self.notes.append(message)


def read(path: Path, report: Report) -> str | None:
    if not path.is_file():
        report.fail("R0", f"{path.name} not found")
        return None
    return path.read_text(encoding="utf-8")


def check_no_codes(name: str, text: str, report: Report) -> None:
    hits = TAG_RE.findall(text)
    if hits:
        sample = ", ".join(sorted(set(hits))[:5])
        report.fail("R1", f"{name} still carries {len(hits)} tag(s): {sample}")
    else:
        report.note(f"R1 {name}: no source codes")


def check_slides(text: str, report: Report) -> None:
    blocks: list[tuple[str, str]] = []
    current: list[str] = []
    title = "(preamble)"
    for line in text.splitlines():
        if SLIDE_HEAD_RE.match(line):
            if current:
                blocks.append((title, "\n".join(current)))
            title = line.strip("# ").strip()
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append((title, "\n".join(current)))

    missing = [t for t, body in blocks
               if t != "(preamble)" and not SLIDE_SOURCE_RE.search(body)]
    total = len([t for t, _ in blocks if t != "(preamble)"])
    if missing:
        report.fail("R2", f"{len(missing)} slide(s) without a **Sumber:** line: "
                           + "; ".join(missing[:4]))
    else:
        report.note(f"R2 {total} slide(s): each carries a source line")


def check_rpp_subsections(text: str, report: Report) -> None:
    if "## D. Materi Pembelajaran" not in text:
        report.fail("R3", "section '## D. Materi Pembelajaran' not found")
        return
    body = text.split("## D. Materi Pembelajaran", 1)[1].split("\n## ", 1)[0]
    headings = [ln for ln in body.splitlines() if RPP_SUBSECTION_RE.match(ln)]
    if not headings:
        report.fail("R3", "no numbered subsections found in section D")
        return
    missing = [h for h in headings if not SOURCE_MARKER_RE.search(h)]
    if missing:
        report.fail("R3", f"{len(missing)} subsection(s) without a source marker: "
                           + "; ".join(m[:60] for m in missing[:3]))
    else:
        report.note(f"R3 {len(headings)} subsection(s) in D: each carries a source marker")


def check_quiz(text: str, report: Report) -> None:
    hits = QUIZ_SOURCE_RE.findall(text)
    if hits:
        report.fail("R4", f"quiz carries {len(hits)} **Sumber:** line(s)")
    else:
        report.note("R4 quiz: no source line")


def check_trace(text: str, report: Report) -> None:
    tags = set(TAG_RE.findall(text))
    if len(tags) < 5:
        report.fail("R5", f"traceability file maps only {len(tags)} tag(s)")
        return
    for doc in ("RPP", "Slide", "Kuis"):
        if doc.lower() not in text.lower():
            report.fail("R5", f"traceability file has no section for {doc}")
            return
    report.note(f"R5 traceability: {len(tags)} distinct tags mapped")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the citation convention of a run.")
    parser.add_argument("--run", required=True, help="run folder, e.g. 03_Hasil/edu_output_tata_surya")
    parser.add_argument("--rpp", default=DEFAULTS["rpp"])
    parser.add_argument("--quiz", default=DEFAULTS["quiz"])
    parser.add_argument("--slide", default=DEFAULTS["slide"])
    parser.add_argument("--trace", default=DEFAULTS["trace"])
    args = parser.parse_args()

    run = Path(args.run)
    report = Report()

    # Scope guard: a run that predates the convention has none of these files.
    # Reporting four "not found" failures would read as four broken rules, when
    # the truth is that the rule set does not apply to that run at all. A run
    # with *some* of the files is still a real failure -- that is half-applied.
    wanted = [run / args.rpp, run / args.quiz, run / args.slide, run / args.trace]
    present = [p for p in wanted if p.is_file()]
    if not present:
        print(f"SKIP: {run} predates the citation convention (convention files not found)")
        return 0

    rpp = read(run / args.rpp, report)
    quiz = read(run / args.quiz, report)
    slide = read(run / args.slide, report)
    trace = read(run / args.trace, report)

    if rpp is not None:
        check_no_codes(args.rpp, rpp, report)
        check_rpp_subsections(rpp, report)
    if slide is not None:
        check_no_codes(args.slide, slide, report)
        check_slides(slide, report)
    if quiz is not None:
        check_no_codes(args.quiz, quiz, report)
        check_quiz(quiz, report)
    if trace is not None:
        check_trace(trace, report)

    for note in report.notes:
        print(f"  OK    {note}")
    for failure in report.failures:
        print(f"  FAIL  {failure}")

    if report.failures:
        print(f"\nFAILED: {len(report.failures)} rule violation(s)")
        return 1
    print(f"\nPASS: {len(report.notes)} checks, convention consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
