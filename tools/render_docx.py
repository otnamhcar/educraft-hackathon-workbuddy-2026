#!/usr/bin/env python3
"""render_docx.py — turn an approved EduCraft draft (Markdown) into a class-facing .docx.

Why a renderer instead of a rewrite
-----------------------------------
The approved content lives in one place: the run's Markdown draft. Retyping it into
a document generator would create a second copy that drifts the moment either one
is edited — exactly the failure that produced three review rejections on run -005
("the sentence was copied to another file and its context changed").

So this script parses the draft and only *transforms* it:

  FR-01  every [src:...], [UNVERIFIED], and PERLU KONFIRMASI GURU marker is removed
  FR-02  the tags found in a section are collapsed into one "Sumber:" line, so the
         traceability that the markers carried is not lost
  FR-06  internal pipeline notes are dropped, not printed

The tag -> source-name mapping is explicit and auditable (`--map`), because
collapsing a tag into prose is a judgement call, not a string operation.

Usage
-----
  python tools/render_docx.py \
      --src 03_Hasil/edu_output_energi_alternatif/01_RPP_Energi_Alternatif.md \
      --out 03_Hasil/edu_output_energi_alternatif/08_RPP_Energi_Alternatif.docx \
      --title "Rencana Pelaksanaan Pembelajaran" \
      --subtitle "Energi Alternatif dan Penghematan Energi · IPAS Fase C (Kelas V–VI)"

Exit codes: 0 = written, 1 = the output still contains an internal marker, 2 = bad input.
"""

import argparse
import re
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# --------------------------------------------------------------------------- #
# Palette
# --------------------------------------------------------------------------- #
INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x55, 0x5F, 0x66)
BRAND = RGBColor(0x14, 0x53, 0x2D)      # deep green
ACCENT = RGBColor(0xB4, 0x5F, 0x06)     # amber, used sparingly
RULE = "C9D2CB"
FILL_HEAD = "14532D"
FILL_QUOTE = "F4F6F4"

BODY_FONT = "Calibri"
BODY_SIZE = Pt(10.5)


# --------------------------------------------------------------------------- #
# Low-level helpers
# --------------------------------------------------------------------------- #
def shade(element, hex_fill):
    """Fill a table cell or a paragraph with a solid colour."""
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    element.append(shd)


def cell_shade(cell, hex_fill):
    shade(cell._tc.get_or_add_tcPr(), hex_fill)


def para_border(paragraph, side="left", color="14532D", size=18):
    p_pr = paragraph._p.get_or_add_pPr()
    borders = p_pr.find(qn("w:pBdr"))
    if borders is None:
        borders = OxmlElement("w:pBdr")
        p_pr.append(borders)
    edge = OxmlElement("w:" + side)
    edge.set(qn("w:val"), "single")
    edge.set(qn("w:sz"), str(size))
    edge.set(qn("w:space"), "6")
    edge.set(qn("w:color"), color)
    borders.append(edge)


def para_shade(paragraph, hex_fill):
    shade(paragraph._p.get_or_add_pPr(), hex_fill)


def table_borders(table, color=RULE):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:" + edge)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tbl_pr.append(borders)


def keep_row_together(row):
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    tr_pr.append(el)


def add_page_number(paragraph):
    run = paragraph.add_run()
    for instr, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if instr:
            fld = OxmlElement("w:fldChar")
            fld.set(qn("w:fldCharType"), instr)
            run._r.append(fld)
        else:
            instr_el = OxmlElement("w:instrText")
            instr_el.set(qn("xml:space"), "preserve")
            instr_el.text = text
            run._r.append(instr_el)


# --------------------------------------------------------------------------- #
# Inline markdown
# --------------------------------------------------------------------------- #
INLINE = re.compile(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|\*[^*]+?\*|`[^`]+?`)")


FILE_LABELS = {
    "02_Kuis_PrePost_Energi_Alternatif.md": "Lembar kuis (lampiran)",
    "03_Slide_Outline_Energi_Alternatif.md": "Tayangan (lampiran)",
    "06_Jejak_Sumber.md": "Lampiran jejak sumber",
}
FILE_LABEL = re.compile("|".join(re.escape(k) for k in FILE_LABELS))

TIDY_PUNCT = re.compile(r"\s+([.,;:!?])")
TIDY_CAP = re.compile(r"([.!?]\s+)(belum ada|belum terverifikasi|perlu konfirmasi)")


def tidy(text):
    """Final pass over assembled text.

    Paragraphs are joined from several source lines, so a tag that sat at the
    start of a line leaves the join with a space before the punctuation. Fixing
    that per line (as strip_markers does) is not enough -- it has to happen after
    the join.
    """
    text = FILE_LABEL.sub(lambda m: FILE_LABELS.get(m.group(0), m.group(0)), text)
    text = TIDY_PUNCT.sub(r"\1", text)
    text = TIDY_CAP.sub(
        lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], text)
    return re.sub(r"[ \t]{2,}", " ", text)


def add_runs(paragraph, text, size=BODY_SIZE, color=INK, bold_all=False):
    """Render **bold**, *italic*, ***both***, `code` into runs."""
    text = tidy(text)
    text = text.replace("\\*", "\u0001")  # protect escaped asterisks
    for piece in INLINE.split(text):
        if not piece:
            continue
        bold = italic = False
        body = piece
        if piece.startswith("***") and piece.endswith("***") and len(piece) > 6:
            bold = italic = True
            body = piece[3:-3]
        elif piece.startswith("**") and piece.endswith("**") and len(piece) > 4:
            bold = True
            body = piece[2:-2]
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            italic = True
            body = piece[1:-1]
        elif piece.startswith("`") and piece.endswith("`") and len(piece) > 2:
            body = piece[1:-1]
        body = body.replace("\u0001", "*")
        run = paragraph.add_run(body)
        run.font.name = BODY_FONT
        run.font.size = size
        run.font.color.rgb = color
        run.bold = bold or bold_all
        run.italic = italic
    return paragraph


# --------------------------------------------------------------------------- #
# Source-marker handling (FR-01 / FR-02)
# --------------------------------------------------------------------------- #
TAG = re.compile(r"`?\[src:([A-Za-z0-9]+)\]`?")

# A tag that opens a sentence is doing grammatical work: "**Catatan…** `[src:B5]`
# berada di Fase B" loses its subject if the tag is simply deleted. Those become a
# short noun phrase instead. Trailing tags are still removed outright.
SUBJECT_LABEL = {
    "B5": "Butir B5",
    "C4": "Butir C4",
    "CP": "Panduan IPAS",
}
SUBJECT_TAG = re.compile(
    r"(?m)(^|>\s*|\.\**\s+)`?\[src:([A-Za-z0-9]+)\]`?\s+(?=[a-z])")

# "not in the source" is a real message for the teacher. Deleting the two markers
# would leave a dangling dash, so they are rewritten as prose (FR-01, FR-06).
UNVERIFIED_PAIR = re.compile(
    r"`?\[UNVERIFIED\]`?\s*[—–,-]\s*`?PERLU KONFIRMASI GURU`?", re.IGNORECASE)


def names_for(tags, mapping):
    """Collapse a set of tags into an ordered, human-readable list."""
    seen, out = set(), []
    for tag in tags:
        label = mapping.get(tag, "Sumber modul")
        if label not in seen:
            seen.add(label)
            out.append(label)
    return "; ".join(out)


def strip_markers(text):
    """Remove internal markers, line by line, preserving indentation.

    Indentation matters: the Markdown parser uses it to tell a list item's
    continuation line from a new paragraph. Collapsing runs of spaces across the
    whole block (an earlier version did) silently un-indented every continuation
    and turned one numbered list into a dozen single-item lists.
    """
    out = []
    for line in text.split("\n"):
        m = re.match(r"^(\s*)(.*)$", line)
        indent, body = m.group(1), m.group(2)
        body = UNVERIFIED_PAIR.sub("belum terverifikasi", body)
        body = TAG.sub("", body)
        body = body.replace("`[UNVERIFIED]`", "belum terverifikasi")
        body = body.replace("[UNVERIFIED]", "belum terverifikasi")
        body = body.replace("`PERLU KONFIRMASI GURU`", "perlu konfirmasi guru")
        body = body.replace("PERLU KONFIRMASI GURU", "perlu konfirmasi guru")
        body = re.sub(r"[ \t]{2,}", " ", body)
        body = re.sub(r"\s+([.,;:!?])", r"\1", body)
        body = re.sub(r"\(\s*\)", "", body)
        # Capitalise a replacement that landed at the start of a sentence.
        body = re.sub(r"([.!?]\s+)(belum tersedia|belum terverifikasi|perlu konfirmasi)",
                      lambda m: m.group(1) + m.group(2)[0].upper() + m.group(2)[1:], body)
        body = re.sub(r"—\s*—", "—", body)
        out.append(indent + body.rstrip())
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Markdown block parser
# --------------------------------------------------------------------------- #
def parse(md_text):
    """Yield (kind, payload) blocks. Kinds: h1 h2 h3 p ul ol quote table hr meta."""
    lines = md_text.split("\n")
    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            yield ("hr", None)
            i += 1
            continue

        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            yield ("h{}".format(level), m.group(2).strip())
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            rows = []
            header = [c.strip() for c in stripped.strip("|").split("|")]
            rows.append(header)
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            yield ("table", rows)
            continue

        if stripped.startswith(">"):
            chunk = []
            while i < n and lines[i].strip().startswith(">"):
                chunk.append(re.sub(r"^\s*>\s?", "", lines[i].rstrip()))
                i += 1
            yield ("quote", " ".join(c.strip() for c in chunk if c.strip()))
            continue

        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                item = re.sub(r"^[-*]\s+", "", lines[i].strip())
                i += 1
                # continuation lines are indented and belong to the same bullet
                while i < n and lines[i].startswith("  ") and lines[i].strip():
                    cont = lines[i].strip()
                    item += ("" if cont[:1] in ".,;:!?" else " ") + cont
                    i += 1
                items.append(item)
            yield ("ul", items)
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                i += 1
                while i < n and lines[i].startswith("  ") and lines[i].strip():
                    cont = lines[i].strip()
                    item += ("" if cont[:1] in ".,;:!?" else " ") + cont
                    i += 1
                items.append(item)
            yield ("ol", items)
            continue

        # paragraph: gather until blank / structural line
        chunk = []
        while i < n:
            s = lines[i].strip()
            if (not s or s == "---" or s.startswith("#") or s.startswith("|")
                    or s.startswith(">") or re.match(r"^[-*]\s+", s)
                    or re.match(r"^\d+\.\s+", s)):
                break
            chunk.append(s)
            i += 1
        yield ("p", " ".join(chunk))
    return


# --------------------------------------------------------------------------- #
# Document builder
# --------------------------------------------------------------------------- #
def setup_document():
    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(1.9)
    section.left_margin = Cm(2.3)
    section.right_margin = Cm(2.1)

    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = BODY_SIZE
    normal.font.color.rgb = INK
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.12
    # make the font stick for East Asian fallback too
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:eastAsia"), BODY_FONT)
    return doc


def add_footer(doc, label):
    footer = doc.sections[0].footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(label + "  ·  halaman ")
    run.font.size = Pt(8)
    run.font.color.rgb = MUTED
    run.font.name = BODY_FONT
    add_page_number(p)
    for r in p.runs:
        r.font.size = Pt(8)
        r.font.color.rgb = MUTED
        r.font.name = BODY_FONT


def add_cover(doc, title, subtitle, kicker):
    band = doc.add_table(rows=1, cols=1)
    band.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = band.rows[0].cells[0]
    cell_shade(cell, FILL_HEAD)
    cell.width = Cm(16.6)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(kicker.upper())
    r.font.size = Pt(9)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0xD9, 0xE8, 0xDC)
    r.font.name = BODY_FONT

    p2 = cell.add_paragraph()
    p2.paragraph_format.space_after = Pt(4)
    r2 = p2.add_run(title)
    r2.font.size = Pt(20)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    r2.font.name = BODY_FONT

    p3 = cell.add_paragraph()
    p3.paragraph_format.space_after = Pt(16)
    r3 = p3.add_run(subtitle)
    r3.font.size = Pt(10.5)
    r3.font.color.rgb = RGBColor(0xE8, 0xF0, 0xEA)
    r3.font.name = BODY_FONT

    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(2)


def add_heading(doc, level, text):
    if level == 2:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(7)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.size = Pt(13.5)
        r.font.bold = True
        r.font.color.rgb = BRAND
        r.font.name = BODY_FONT
        para_border(p, "bottom", RULE, 6)
    elif level == 3:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(11)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = INK
        r.font.name = BODY_FONT
    else:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(9)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.color.rgb = MUTED
        r.font.name = BODY_FONT


def add_para(doc, text, indent=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.left_indent = Cm(0.6)
    add_runs(p, text)
    return p


def add_quote(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.right_indent = Cm(0.3)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(8)
    para_shade(p, FILL_QUOTE)
    para_border(p, "left", "14532D", 18)
    add_runs(p, text, size=Pt(9.5), color=RGBColor(0x33, 0x3D, 0x38))
    return p


def add_list(doc, items, ordered):
    for idx, item in enumerate(items, 1):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.75)
        p.paragraph_format.first_line_indent = Cm(-0.45)
        p.paragraph_format.space_after = Pt(3)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        marker = "{}. ".format(idx) if ordered else "•  "
        r = p.add_run(marker)
        r.font.name = BODY_FONT
        r.font.size = BODY_SIZE
        r.font.color.rgb = BRAND if ordered else MUTED
        r.bold = ordered
        add_runs(p, item)


def add_table(doc, rows):
    header, body = rows[0], rows[1:]
    table = doc.add_table(rows=len(rows), cols=len(header))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    table_borders(table)

    for c, text in enumerate(header):
        cell = table.rows[0].cells[c]
        cell_shade(cell, FILL_HEAD)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        add_runs(p, text, size=Pt(9), color=RGBColor(0xFF, 0xFF, 0xFF), bold_all=True)

    for r, row in enumerate(body, 1):
        keep_row_together(table.rows[r])
        for c in range(len(header)):
            text = row[c] if c < len(row) else ""
            cell = table.rows[r].cells[c]
            if r % 2 == 0:
                cell_shade(cell, "FAFBFA")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2.5)
            p.paragraph_format.space_after = Pt(2.5)
            add_runs(p, text, size=Pt(9))

    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(2)
    return table


# --------------------------------------------------------------------------- #
# Main transform
# --------------------------------------------------------------------------- #
def build(src, out, title, subtitle, kicker, mapping, footer_label):
    with open(src, encoding="utf-8") as fh:
        raw = fh.read()

    # Everything above the first section heading is pipeline furniture: run id,
    # status line, reviewer note. It must not reach the classroom (FR-06).
    head_start = raw.find("\n## ")
    raw = raw[head_start + 1:] if head_start != -1 else raw
    raw = re.split(r"(?m)^##\s+Sumber yang dipakai", raw)[0]

    # A tag that opens a sentence is doing grammatical work; give it a noun.
    raw = SUBJECT_TAG.sub(
        lambda m: "{}{} ".format(m.group(1), SUBJECT_LABEL.get(m.group(2), "Sumber")), raw)

    # Heading suffixes carry tags, e.g. "### 1. Energi alternatif — *`[src:2]`*".
    # Move them into a "Sumber:" line so the heading stays clean.
    section_sources = {}

    def fix_heading(m):
        level, text = m.group(1), m.group(2)
        tags = TAG.findall(text)
        # "### 3. Prasyarat … — *`[src:3]` `[src:4]`; CP fondasi `[src:B5]`*"
        # The whole trailing italic segment is a source note, not a title.
        clean = re.sub(r"\s*[—–-]\s*\*[^*]*\[src:[^\]]+\][^*]*\*\s*$", "", text)
        clean = TAG.sub("", clean)
        clean = re.sub(r"\s*[—–-]\s*\*?\s*\*?\s*$", "", clean)
        clean = re.sub(r"\s*;\s*$", "", clean)
        clean = re.sub(r"[ \t]{2,}", " ", clean).strip()
        if tags:
            section_sources[clean] = tags
        return "{} {}".format(level, clean)

    raw = re.sub(r"^(#{2,4})\s+(.*)$", fix_heading, raw, flags=re.M)

    # Collapse remaining inline tags per section.
    parts = re.split(r"(?m)^(##\s+.*)$", raw)
    rebuilt = [parts[0]]
    for i in range(1, len(parts), 2):
        head, body = parts[i], parts[i + 1] if i + 1 < len(parts) else ""
        tags = TAG.findall(head + body)
        # A section whose subsections each carry their own source line does not
        # need a second, aggregate one: it would only repeat itself.
        sub_heads = [ln for ln in body.split("\n") if ln.startswith("### ")]
        subs_have_sources = any(ln.strip().lstrip("#").strip() in section_sources
                                for ln in sub_heads)
        rebuilt.append(head)
        if tags and not (sub_heads and subs_have_sources):
            rebuilt.append("\n*Sumber: {}.*\n".format(names_for(tags, mapping)))
        rebuilt.append(strip_markers(body))
    raw = "".join(rebuilt)

    doc = setup_document()
    add_footer(doc, footer_label)
    add_cover(doc, title, subtitle, kicker)

    for kind, payload in parse(raw):
        if kind == "h2":
            add_heading(doc, 2, payload)
            if payload in section_sources:
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(5)
                add_runs(p, "*Sumber: {}.*".format(names_for(section_sources[payload], mapping)),
                         size=Pt(8.5), color=MUTED)
        elif kind == "h3":
            add_heading(doc, 3, payload)
            if payload in section_sources:
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(5)
                add_runs(p, "*Sumber: {}.*".format(names_for(section_sources[payload], mapping)),
                         size=Pt(8.5), color=MUTED)
        elif kind == "h4":
            add_heading(doc, 4, payload)
        elif kind == "p":
            if payload.startswith("*Sumber:") and payload.endswith("*"):
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(6)
                add_runs(p, payload, size=Pt(8.5), color=MUTED)
            else:
                add_para(doc, payload)
        elif kind == "quote":
            add_quote(doc, payload)
        elif kind == "ul":
            add_list(doc, payload, ordered=False)
        elif kind == "ol":
            add_list(doc, payload, ordered=True)
        elif kind == "table":
            add_table(doc, payload)
        elif kind == "hr":
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            para_border(p, "bottom", RULE, 4)

    doc.core_properties.title = title
    doc.core_properties.subject = subtitle
    doc.core_properties.author = "EduCraft · EDU-ORCH-20261106-005"
    doc.core_properties.comments = (
        "Dirender dari draf 01_RPP_Energi_Alternatif.md. Jejak sumber: 06_Jejak_Sumber.md."
    )
    doc.save(out)

    # FR-01 gate: the artifact must not carry an internal marker.
    probe = Document(out)
    text = "\n".join(p.text for p in probe.paragraphs)
    for table in probe.tables:
        for row in table.rows:
            for cell in row.cells:
                text += "\n" + cell.text
    leftovers = re.findall(r"\[src:|\[UNVERIFIED\]|PERLU KONFIRMASI GURU", text)
    if leftovers:
        print("FAIL: {} internal marker(s) survived: {}".format(len(leftovers), set(leftovers)))
        return 1

    words = len(text.split())
    print("OK  {} paragraphs, {} tables, ~{} kata".format(len(probe.paragraphs), len(probe.tables), words))
    print("->  " + out)
    return 0


def load_mapping(path):
    mapping = {}
    if not path:
        return mapping
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, value = line.partition("=")
            mapping[key.strip()] = value.strip()
    return mapping


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", required=True)
    ap.add_argument("--kicker", default="Rencana Pelaksanaan Pembelajaran")
    ap.add_argument("--map", default=None, help="file of tag=label lines")
    ap.add_argument("--footer", default="IPAS Fase C · Energi Alternatif dan Penghematan Energi")
    args = ap.parse_args()

    try:
        return build(args.src, args.out, args.title, args.subtitle, args.kicker,
                     load_mapping(args.map), args.footer)
    except FileNotFoundError as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
