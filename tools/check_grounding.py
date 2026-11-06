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
4. Flags three failures:
     DANGLING      the tag resolves to nothing
     CLASS         a curriculum tag carries a sentence that is not about curriculum
     AMBIG         the tag exists in more than one source sheet and no
                   --primary-source was named to break the tie

Why AMBIG exists (6 November 2026)
----------------------------------
Two source sheets number their anchors from 1: `source_material_ipas.md` and
`source_material_energi.md` both declare `## [src:1]` … `## [src:9]`. The first
version of this script stored anchors in a flat dict, so the last file in
alphabetical order silently overwrote the earlier one. The run
`EDU-ORCH-20261106-005` therefore produced a "PASS" in which every `[src:2]`
resolved to *Kelestarian Alam* instead of *Energi Alternatif* — a clean report
that proved nothing.

A tag that could mean two different sections is not a resolved tag. `AMBIG` makes
that visible instead of letting alphabetical order decide. `--primary-source`
states which sheet a run is actually built on; tags outside that sheet (CA#, CP
codes) still resolve normally.

Scope — drafts only
-------------------
Run **metadata** is skipped: `audit_log.md`, `05_review.md`, `grounding_report.md`,
`00_run_config.md`, `11_Memo_*` correction memos, and approval records (`*Persetujuan*`,
`*Approval*`). Those files quote tags as evidence, declare which tags a run uses, or record a
human decision; they do not assert a fact *with* a tag. Counting them produced four false CLASS
violations on 31 October 2026, when a run config was first added to a run folder. On 5 November
2026 an approval sheet raised the total by one for the same reason. Skipped files are named in
every report so the exclusion is visible, never silent.

Usage
-----
  python3 tools/check_grounding.py \
      --run 03_Hasil/edu_output_energi_alternatif \
      --knowledge 08_Referensi \
      --primary-source source_material_energi.md \
      --out 03_Hasil/edu_output_energi_alternatif/grounding_report.md

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
# Reviewer memos quote offending sentences verbatim, tag included. Counting them
# inflates the total and can raise false CLASS violations. Runs number their files
# differently (05_review.md on the 30 Oct run, 06_review.md / 07_review_pass2.md on
# 4 Nov), so match on the role in the name rather than on a fixed number.
# Approval records (04_Lembar_Persetujuan_Guru.md) name tags while recording a human
# decision; they are governance metadata, not drafts, so they are skipped the same way.
SKIP_ROLE_PATTERN = re.compile(r"review|persetujuan|approval", re.IGNORECASE)


def is_metadata(name: str) -> bool:
    """True for run metadata: it may name a tag without asserting a fact with it."""
    return (
        name in SKIP_FILES
        or name.startswith(SKIP_PREFIXES)
        or bool(SKIP_ROLE_PATTERN.search(name))
    )


def classify(tag: str) -> str:
    if tag.upper().startswith("CA"):
        return "actual_context"
    if tag.upper() == "CP" or re.fullmatch(r"[BC]\d+", tag, re.IGNORECASE):
        return "curriculum"
    if re.fullmatch(r"W\d+", tag, re.IGNORECASE) or tag.isdigit():
        return "fact"
    return "unknown"


def load_anchors(knowledge_dir):
    """Explicit ## [src:n] anchors, kept per file.

    Returns (anchors_by_file, tag_files):
      anchors_by_file  {filename: {tag: {file, heading, class, lines}}}
      tag_files        {tag: [filenames]}  -- len > 1 means the tag is ambiguous
    """
    anchors_by_file = {}
    tag_files = {}
    for name in sorted(os.listdir(knowledge_dir)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(knowledge_dir, name)
        per_file = {}
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                m = ANCHOR_RE.match(line)
                if m:
                    tag = m.group(1)
                    per_file[tag] = {
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
                    per_file[current]["lines"] += 1
        if not per_file:
            continue
        anchors_by_file[name] = per_file
        for tag in per_file:
            tag_files.setdefault(tag, []).append(name)
    return anchors_by_file, tag_files


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


def resolve(tag, anchors_by_file, tag_files, primary):
    """Return (info, verdict, where). verdict in OK | DANGLING | AMBIG."""
    files = tag_files.get(tag)
    if not files:
        return None, "DANGLING", "—"
    if len(files) == 1:
        info = anchors_by_file[files[0]][tag]
        return info, "OK", "{} · {}".format(info["file"], info["heading"][:70])
    if primary and primary in files:
        info = anchors_by_file[primary][tag]
        return info, "OK", "{} · {} *(primary)*".format(info["file"], info["heading"][:70])
    info = anchors_by_file[files[-1]][tag]
    return info, "AMBIG", "ambigu: " + ", ".join(files)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="folder holding the drafts to check")
    ap.add_argument("--knowledge", required=True, help="folder holding the knowledge layer")
    ap.add_argument("--out", required=True, help="path of the Markdown report to write")
    ap.add_argument(
        "--primary-source",
        default=None,
        help="filename of the source sheet this run is built on; breaks ties when "
             "two sheets share a tag (e.g. source_material_energi.md)",
    )
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(args.run) or not os.path.isdir(args.knowledge):
        print("error: --run and --knowledge must be directories", file=sys.stderr)
        return 2

    anchors_by_file, tag_files = load_anchors(args.knowledge)
    cp_codes = load_cp_codes(args.knowledge)
    if cp_codes:
        anchors_by_file.setdefault("cp_ipas.md", {}).update(cp_codes)
        for tag in cp_codes:
            tag_files.setdefault(tag, ["cp_ipas.md"])

    primary = args.primary_source
    if primary and primary not in anchors_by_file:
        print(
            "error: --primary-source {} not found among the knowledge files".format(primary),
            file=sys.stderr,
        )
        return 2

    all_md = [f for f in sorted(os.listdir(args.run)) if f.endswith(".md")]
    drafts = [f for f in all_md if not is_metadata(f)]
    skipped = [f for f in all_md if is_metadata(f)]
    if not drafts:
        print("error: no drafts found in " + args.run, file=sys.stderr)
        return 2

    per_file = OrderedDict()
    total_tags = dangling = class_hits = ambiguous = 0
    findings = []

    for name in drafts:
        path = os.path.join(args.run, name)
        rows = []
        for line_no, sentence, tags in scan_draft(path):
            for tag in tags:
                total_tags += 1
                target, verdict, where = resolve(tag, anchors_by_file, tag_files, primary)
                tag_class = classify(tag)
                if verdict == "DANGLING":
                    dangling += 1
                    findings.append(
                        "`{}`:{} — `[src:{}]` tidak dapat diselesaikan "
                        "(tidak ada anchor `## [src:{}]` di knowledge layer)".format(
                            name, line_no, tag, tag
                        )
                    )
                elif verdict == "AMBIG":
                    ambiguous += 1
                    findings.append(
                        "`{}`:{} — `[src:{}]` ambigu: anchor yang sama ada di {}. "
                        "Jalankan ulang dengan `--primary-source` untuk menetapkan sumber "
                        "yang berlaku".format(name, line_no, tag, " dan ".join(tag_files[tag]))
                    )
                else:
                    if target["class"] == "curriculum":
                        if CURRICULUM_WORDS.search(sentence):
                            verdict = "OK"
                        else:
                            class_hits += 1
                            verdict = "CLASS"
                            findings.append(
                                "`{}`:{} — `[src:{}]` adalah tag kurikulum "
                                "({}) tetapi menopang kalimat non-kurikulum: "
                                "\"{}\"".format(name, line_no, tag, target["file"], sentence[:90])
                            )
                    elif target.get("lines", 1) == 0:
                        verdict = "THIN"
                        findings.append(
                            "`{}`:{} — `[src:{}]` menunjuk bagian sumber yang kosong; "
                            "tidak dapat menopang fakta".format(name, line_no, tag)
                        )
                rows.append((line_no, tag, tag_class, verdict, where))
        per_file[name] = rows

    failed = dangling + class_hits + ambiguous
    status = "FAIL" if failed else "PASS"

    lines = []
    lines.append("# Grounding report — R001 tag resolution\n")
    lines.append("**Run folder:** `{}`  ".format(args.run))
    lines.append("**Knowledge layer:** `{}`  ".format(args.knowledge))
    lines.append(
        "**Primary source:** {}  ".format(
            "`{}`".format(primary) if primary else "_tidak ditetapkan_"
        )
    )
    lines.append(
        "**Verdict:** **{}** — {} tag diperiksa, "
        "{} dangling, {} pelanggaran kelas tag, {} ambigu\n".format(
            status, total_tags, dangling, class_hits, ambiguous
        )
    )
    lines.append(
        "> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan "
        "dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.\n"
    )
    lines.append(
        "**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** "
        + (", ".join("`{}`".format(s) for s in skipped) if skipped else "—")
        + "\n"
    )
    if primary:
        lines.append(
            "**Cara tag ditetapkan.** Tag yang hanya ada di satu berkas diselesaikan ke berkas "
            "itu (mis. `[src:CA1]` ke `konteks_aktual.md`, `[src:C4]` ke `cp_ipas.md`). Tag yang "
            "ada di lebih dari satu lembar sumber diselesaikan ke `{}` karena run ini dibangun "
            "di atas lembar itu.\n".format(primary)
        )

    lines.append("## Ringkasan per file\n")
    lines.append("| File | Tag | Dangling | Pelanggaran kelas |")
    lines.append("|------|----:|---------:|------------------:|")
    for name, rows in per_file.items():
        d = sum(1 for r in rows if r[3] == "DANGLING")
        c = sum(1 for r in rows if r[3] in ("CLASS", "THIN", "AMBIG"))
        lines.append("| `{}` | {} | {} | {} |".format(name, len(rows), d, c))

    lines.append("\n## Temuan\n")
    if findings:
        for f in findings:
            lines.append("- " + f)
    else:
        lines.append(
            "- Tidak ada temuan. Setiap tag menunjuk anchor yang ada, tidak ambigu, "
            "dan kelasnya sesuai."
        )

    lines.append("\n## Rincian tag\n")
    for name, rows in per_file.items():
        lines.append("### `{}`\n".format(name))
        lines.append("| Baris | Tag | Kelas | Putusan | Menunjuk ke |")
        lines.append("|------:|-----|-------|---------|-------------|")
        seen = set()
        for line_no, tag, tag_class, verdict, where in rows:
            key = (tag, verdict)
            mark = "" if key not in seen else " (ulang)"
            seen.add(key)
            lines.append(
                "| {} | `[src:{}]` | {} | **{}**{} | {} |".format(
                    line_no, tag, tag_class, verdict, mark, where
                )
            )
        lines.append("")

    lines.append("## Batas pemeriksaan ini\n")
    lines.append(
        "- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. "
        "Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012)."
    )
    lines.append(
        "- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, "
        "elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan "
        "dihukum otomatis."
    )
    lines.append(
        "- Bila beberapa lembar sumber memakai penomoran tag yang sama, `--primary-source` "
        "wajib disebut. Tanpa itu tag ditandai `AMBIG` dan run dianggap gagal — lebih baik "
        "gagal terang-terangan daripada lulus karena urutan abjad."
    )

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    # newline="\n" so a report generated on Windows is byte-identical to one
    # generated on Linux -- the check is meant to be reproducible across the team.
    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    if not args.quiet:
        print(
            "{}: {} tag, {} dangling, {} class violations, {} ambiguous".format(
                status, total_tags, dangling, class_hits, ambiguous
            )
        )
        print("report -> " + args.out)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
