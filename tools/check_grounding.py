#!/usr/bin/env python3
"""
check_grounding.py — deterministic tag-resolution check (R001).

Why this exists
---------------
The 29 October 2026 rejection happened because the pipeline checked only whether a
sentence carried a tag, not whether the tag resolved to a source that supports it.
A tag is not a citation. This script closes that gap with a check that is
deterministic, reproducible, and cheap enough to run before every review.

What it does
------------
1. Collects every tag in a draft: [src:1], [src:B4], [src:CA1], [src:CP] ...
2. Resolves each tag against the knowledge layer:
     - explicit anchors  -> headings like  ## [src:3]  in a source file
     - curriculum codes  -> numbered items in cp_ipas.md (B4 = Fase B item 4)
3. Classifies each tag: fact | curriculum | actual_context
4. Flags two failures:
     DANGLING      the tag resolves to nothing
     CLASS         a curriculum tag carries a sentence that is not about curriculum
5. Writes a Markdown report and exits non-zero if anything failed.

Scope — drafts only
-------------------
Run **metadata** is skipped: `audit_log.md`, `05_review.md`, `grounding_report.md`,
`00_run_config.md`, and `11_Memo_*` correction memos. Those files quote tags as evidence or
declare which tags a run uses; they do not assert a fact *with* a tag. Counting them produced
four false CLASS violations on 31 October 2026, when a run config was first added to a run
folder. Skipped files are named in every report so the exclusion is visible, never silent.

Usage
-----
  python3 tools/check_grounding.py \
      --run 03_Hasil/edu_output_wujud_zat \
      --knowledge 03_Hasil/referensi \
      --out 03_Hasil/edu_output_wujud_zat/grounding_report.md

Exit codes: 0 = clean, 1 = failures found, 2 = bad input.
"""

import argparse
import os
import re
import sys
from collections import OrderedDict

TAG_RE = re.compile(r"\[src:([A-Za-z0-9]+)\]")
ANCHOR_RE = re.compile(r"^\s{0,3}#{1,4}\s*\[src:([A-Za-z0-9]+)\]\s*(.*)$")
CP_ITEM_RE = re.compile(r"^\s*(\d+)\.\s+(.+)$")
CURRICULUM_WORDS = re.compile(
    r"\b(CP|capaian|fase|kurikulum|elemen|tujuan pembelajaran|keterampilan proses)\b",
    re.IGNORECASE,
)
SKIP_FILES = {
    "audit_log.md",        # records decisions, quotes tags as evidence
    "05_review.md",        # the reviewer's own verdict
    "grounding_report.md",  # this tool's output
    "00_run_config.md",    # state file: declares which source tags are in use
}
# Files that *discuss* tags rather than *use* them as support for a sentence.
# A correction memo naming the wrong tag is not a claim supported by that tag.
SKIP_PREFIXES = ("11_Memo_",)


def is_metadata(name: str) -> bool:
    """True for run metadata: it may name a tag without asserting a fact with it."""
    return name in SKIP_FILES or name.startswith(SKIP_PREFIXES)



def classify(tag: str) -> str:
    if tag.upper().startswith("CA"):
        return "actual_context"
    if tag.upper() == "CP" or re.fullmatch(r"[BC]\d+", tag, re.IGNORECASE):
        return "curriculum"
    if re.fullmatch(r"W\d+", tag, re.IGNORECASE) or tag.isdigit():
        return "fact"
    return "unknown"


def load_anchors(knowledge_dir):
    """Explicit ## [src:n] anchors across the knowledge layer."""
    anchors = {}
    for name in sorted(os.listdir(knowledge_dir)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(knowledge_dir, name)
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                m = ANCHOR_RE.match(line)
                if m:
                    tag = m.group(1)
                    anchors[tag] = {
                        "file": name,
                        "heading": m.group(2).strip(),
                        "class": classify(tag),
                        "lines": 0,
                    }
        # count content lines per anchor so an empty section is visible
        with open(path, encoding="utf-8") as fh:
            current = None
            for line in fh:
                m = ANCHOR_RE.match(line)
                if m:
                    current = m.group(1)
                    continue
                if current and line.strip() and not line.startswith("#"):
                    anchors[current]["lines"] += 1
    return anchors


def load_cp_codes(knowledge_dir):
    """B4 -> 'Fase B item 4' by parsing numbered items under each phase."""
    path = os.path.join(knowledge_dir, "cp_ipas.md")
    if not os.path.exists(path):
        return {}
    codes = {}
    phase = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if re.match(r"^#{1,3}\s*FASE\s*([BC])", line, re.IGNORECASE):
                phase = re.match(r"^#{1,3}\s*FASE\s*([BC])", line, re.IGNORECASE).group(1).upper()
                continue
            if re.match(r"^#{1,3}\s*Materi Esensial", line, re.IGNORECASE):
                phase = None
                continue
            m = CP_ITEM_RE.match(line)
            if phase and m:
                codes.setdefault(phase + m.group(1), {
                    "file": "cp_ipas.md",
                    "heading": m.group(2).strip()[:90],
                    "class": "curriculum",
                    "lines": 1,
                })
    return codes


def scan_draft(path):
    """Return [(line_no, sentence, [tags])] for lines that carry tags."""
    hits = []
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            tags = TAG_RE.findall(line)
            if tags:
                hits.append((i, line.strip(), tags))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="folder holding the drafts to check")
    ap.add_argument("--knowledge", required=True, help="folder holding the knowledge layer")
    ap.add_argument("--out", required=True, help="path of the Markdown report to write")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.run) or not os.path.isdir(args.knowledge):
        print("error: --run and --knowledge must be directories", file=sys.stderr)
        return 2

    anchors = load_anchors(args.knowledge)
    anchors.update(load_cp_codes(args.knowledge))

    all_md = [f for f in sorted(os.listdir(args.run)) if f.endswith(".md")]
    drafts = [f for f in all_md if not is_metadata(f)]
    skipped = [f for f in all_md if is_metadata(f)]
    if not drafts:
        print("error: no drafts found in " + args.run, file=sys.stderr)
        return 2

    per_file = OrderedDict()
    total_tags = dangling = class_hits = 0
    findings = []

    for name in drafts:
        path = os.path.join(args.run, name)
        rows = []
        for line_no, sentence, tags in scan_draft(path):
            for tag in tags:
                total_tags += 1
                target = anchors.get(tag)
                tag_class = classify(tag)
                if target is None:
                    dangling += 1
                    verdict = "DANGLING"
                    where = "—"
                    findings.append(
                        f"`{name}`:{line_no} — `[src:{tag}]` tidak dapat diselesaikan "
                        f"(tidak ada anchor `## [src:{tag}]` di knowledge layer)"
                    )
                else:
                    where = f"{target['file']} · {target['heading'][:70]}"
                    if target["class"] == "curriculum":
                        if CURRICULUM_WORDS.search(sentence):
                            verdict = "OK"
                        else:
                            class_hits += 1
                            verdict = "CLASS"
                            findings.append(
                                f"`{name}`:{line_no} — `[src:{tag}]` adalah tag kurikulum "
                                f"({target['file']}) tetapi menopang kalimat non-kurikulum: "
                                f"\"{sentence[:90]}\""
                            )
                    elif target.get("lines", 1) == 0:
                        verdict = "THIN"
                        findings.append(
                            f"`{name}`:{line_no} — `[src:{tag}]` menunjuk bagian sumber yang kosong; "
                            f"tidak dapat menopang fakta"
                        )
                    else:
                        verdict = "OK"
                rows.append((line_no, tag, tag_class, verdict, where))
        per_file[name] = rows

    failed = dangling + class_hits
    status = "FAIL" if failed else "PASS"

    lines = []
    lines.append("# Grounding report — R001 tag resolution\n")
    lines.append(f"**Run folder:** `{args.run}`  ")
    lines.append(f"**Knowledge layer:** `{args.knowledge}`  ")
    lines.append(f"**Verdict:** **{status}** — {total_tags} tag diperiksa, "
                 f"{dangling} dangling, {class_hits} pelanggaran kelas tag\n")
    lines.append("> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan "
                 "dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.\n")
    lines.append(
        "**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** "
        + (", ".join(f"`{s}`" for s in skipped) if skipped else "—")
        + "\n"
    )

    lines.append("## Ringkasan per file\n")
    lines.append("| File | Tag | Dangling | Pelanggaran kelas |")
    lines.append("|------|----:|---------:|------------------:|")
    for name, rows in per_file.items():
        d = sum(1 for r in rows if r[3] == "DANGLING")
        c = sum(1 for r in rows if r[3] in ("CLASS", "THIN"))
        lines.append(f"| `{name}` | {len(rows)} | {d} | {c} |")

    lines.append("\n## Temuan\n")
    if findings:
        for f in findings:
            lines.append(f"- {f}")
    else:
        lines.append("- Tidak ada temuan. Setiap tag menunjuk anchor yang ada dan kelasnya sesuai.")

    lines.append("\n## Rincian tag\n")
    for name, rows in per_file.items():
        lines.append(f"### `{name}`\n")
        lines.append("| Baris | Tag | Kelas | Putusan | Menunjuk ke |")
        lines.append("|------:|-----|-------|---------|-------------|")
        seen = set()
        for line_no, tag, tag_class, verdict, where in rows:
            key = (tag, verdict)
            mark = "" if key not in seen else " (ulang)"
            seen.add(key)
            lines.append(f"| {line_no} | `[src:{tag}]` | {tag_class} | **{verdict}**{mark} | {where} |")
        lines.append("")

    lines.append("## Batas pemeriksaan ini\n")
    lines.append("- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. "
                 "Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).")
    lines.append("- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, "
                 "elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan "
                 "dihukum otomatis.")

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    # newline="\n" so a report generated on Windows is byte-identical to one
    # generated on Linux -- the check is meant to be reproducible across the team.
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    if not args.quiet:
        print(f"{status}: {total_tags} tag, {dangling} dangling, {class_hits} class violations")
        print(f"report -> {args.out}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
