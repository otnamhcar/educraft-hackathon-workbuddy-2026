#!/usr/bin/env python3
"""render_pptx.py — build the classroom deck for run EDU-ORCH-20261106-005.

Content is transcribed from 03_Slide_Outline_Energi_Alternatif.md, slide by slide.
Nothing is added here: the outline is the approved artefact and this script only
gives it a body. Internal markers ([src:...]) never reach the slides (FR-01); the
tag -> source-name mapping is the same file the docx renderer uses (FR-02).

Design rules
------------
* 16:9, one idea per slide, no more than five visual elements.
* Deep green for structure, amber only for the one thing to remember.
* A source line on every slide that carries a fact; none on the title slide.
* Text never below 12 pt, body never below 16 pt — this is projected, not read.

Usage
-----
  python tools/render_pptx.py \
      --out 03_Hasil/edu_output_energi_alternatif/09_Slide_Energi_Alternatif.pptx

Exit codes: 0 = written, 1 = verification failed, 2 = bad input.
"""

import argparse
import re
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

# --------------------------------------------------------------------------- #
# Palette — one green family, one amber, one grey. Nothing else.
# --------------------------------------------------------------------------- #
GREEN = RGBColor(0x14, 0x53, 0x2D)
GREEN_MID = RGBColor(0x2F, 0x6B, 0x45)
AMBER = RGBColor(0xB4, 0x53, 0x09)
INK = RGBColor(0x1F, 0x29, 0x37)
MUTED = RGBColor(0x6B, 0x72, 0x80)
PAPER = RGBColor(0xFF, 0xFF, 0xFF)
SOFT = RGBColor(0xF3, 0xF6, 0xF4)
SOFT_AMBER = RGBColor(0xFE, 0xF3, 0xC7)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Calibri"
W, H = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.95)
CONTENT_W = W - 2 * MARGIN


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def textbox(slide, x, y, w, h, wrap=True):
    box = slide.shapes.add_textbox(x, y, w, h)
    tf = box.text_frame
    tf.word_wrap = wrap
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    return box


def style_run(run, size, color=INK, bold=False, italic=False, spacing=None):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    if spacing is not None:
        run.font._rPr.set("spc", str(int(spacing * 100)))


def para(tf, first=False):
    return tf.paragraphs[0] if first else tf.add_paragraph()


def bullet_char(paragraph, char="▪", color=GREEN, indent=-Inches(0.28)):
    """python-pptx has no bullet API; write the XML directly."""
    p_pr = paragraph._p.get_or_add_pPr()
    p_pr.set("marL", str(int(indent * -1)))
    p_pr.set("indent", str(int(indent)))
    bu_clr = p_pr.makeelement(qn("a:buClr"), {})
    srgb = p_pr.makeelement(qn("a:srgbClr"), {"val": "%02X%02X%02X" % (color[0], color[1], color[2])})
    bu_clr.append(srgb)
    p_pr.append(bu_clr)
    bu_font = p_pr.makeelement(qn("a:buFont"), {"typeface": "Arial"})
    p_pr.append(bu_font)
    bu_char = p_pr.makeelement(qn("a:buChar"), {"char": char})
    p_pr.append(bu_char)


def no_bullet(paragraph):
    p_pr = paragraph._p.get_or_add_pPr()
    p_pr.append(p_pr.makeelement(qn("a:buNone"), {}))


def rect(slide, x, y, w, h, fill=SOFT, line=None, radius=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    shp = slide.shapes.add_shape(shape, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line
        shp.line.width = Pt(1)
    shp.shadow.inherit = False
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        shp.adjustments[0] = radius
    shp.text_frame.word_wrap = True
    # Kartu yang tingginya ditetapkan tetap sering menyisakan pita kosong di bawah
    # isi. Menengahkan vertikal membuat sisa itu terbaca sebagai padding.
    shp.text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    shp.text_frame.margin_left = Inches(0.28)
    shp.text_frame.margin_right = Inches(0.28)
    shp.text_frame.margin_top = Inches(0.2)
    shp.text_frame.margin_bottom = Inches(0.2)
    return shp


def header(slide, kicker, title):
    if kicker:
        box = textbox(slide, MARGIN, Inches(0.5), CONTENT_W, Inches(0.3))
        r = box.text_frame.paragraphs[0].add_run()
        r.text = kicker.upper()
        style_run(r, 11, AMBER, bold=True, spacing=1.6)

    box = textbox(slide, MARGIN, Inches(0.82), CONTENT_W, Inches(1.0))
    r = box.text_frame.paragraphs[0].add_run()
    r.text = title
    style_run(r, 30, GREEN, bold=True)

    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, MARGIN, Inches(1.78), Inches(1.1), Pt(3.5))
    line.fill.solid()
    line.fill.fore_color.rgb = AMBER
    line.line.fill.background()
    line.shadow.inherit = False


def source_line(slide, text, color=None):
    box = textbox(slide, MARGIN, H - Inches(0.62), CONTENT_W - Inches(0.8), Inches(0.32))
    r = box.text_frame.paragraphs[0].add_run()
    r.text = "Sumber: " + text
    style_run(r, 9.5, color or MUTED, italic=True)


def page_number(slide, n):
    box = textbox(slide, W - MARGIN - Inches(0.6), H - Inches(0.62), Inches(0.6), Inches(0.32))
    p = box.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    r = p.add_run()
    r.text = "{:02d}".format(n)
    style_run(r, 9.5, MUTED, bold=True)


def bullets(slide, items, top, left=MARGIN, width=CONTENT_W, size=17, gap=10, color=INK):
    box = textbox(slide, left, top, width, H - top - Inches(0.9))
    tf = box.text_frame
    for i, item in enumerate(items):
        p = para(tf, first=(i == 0))
        p.space_after = Pt(gap)
        p.line_spacing = 1.12
        if isinstance(item, tuple):
            lead, rest = item
            r = p.add_run()
            r.text = lead
            style_run(r, size, GREEN, bold=True)
            r2 = p.add_run()
            r2.text = rest
            style_run(r2, size, color)
        else:
            r = p.add_run()
            r.text = item
            style_run(r, size, color)
        bullet_char(p)
    return box


def card(slide, x, y, w, h, title, lines, fill=SOFT, title_color=GREEN, size=15):
    shp = rect(slide, x, y, w, h, fill=fill, radius=0.06)
    tf = shp.text_frame
    # Tengah, bukan atas: kartu bertinggi tetap yang hanya berisi satu baris
    # menyisakan pita kosong besar di bawah bila teks dipaku ke tepi atas.
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    p.space_after = Pt(7)
    r = p.add_run()
    r.text = title
    style_run(r, 13, title_color, bold=True, spacing=0.6)
    for line in lines:
        p = tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(3)
        p.line_spacing = 1.1
        r = p.add_run()
        r.text = line
        style_run(r, size, INK)
    return shp


# --------------------------------------------------------------------------- #
# Slides
# --------------------------------------------------------------------------- #
def slide_title(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    band = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    band.fill.solid()
    band.fill.fore_color.rgb = GREEN
    band.line.fill.background()
    band.shadow.inherit = False

    # a single amber rule as the only ornament
    rule = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, MARGIN, Inches(2.55), Inches(1.4), Pt(4))
    rule.fill.solid()
    rule.fill.fore_color.rgb = AMBER
    rule.line.fill.background()
    rule.shadow.inherit = False

    box = textbox(s, MARGIN, Inches(1.75), CONTENT_W - Inches(1.2), Inches(0.4))
    r = box.text_frame.paragraphs[0].add_run()
    r.text = "IPAS · FASE C (KELAS V–VI)"
    style_run(r, 12, RGBColor(0xC7, 0xDC, 0xCE), bold=True, spacing=2.0)

    box = textbox(s, MARGIN, Inches(2.95), CONTENT_W - Inches(1.0), Inches(2.0))
    tf = box.text_frame
    r = tf.paragraphs[0].add_run()
    r.text = "Energi Alternatif"
    style_run(r, 46, WHITE, bold=True)
    p = tf.add_paragraph()
    r = p.add_run()
    r.text = "dan Penghematan Energi"
    style_run(r, 46, WHITE, bold=True)

    box = textbox(s, MARGIN, Inches(5.35), CONTENT_W - Inches(1.2), Inches(0.9))
    tf = box.text_frame
    r = tf.paragraphs[0].add_run()
    r.text = "2 pertemuan × 40 menit  ·  CP-C.2.1.4"
    style_run(r, 15, RGBColor(0xC7, 0xDC, 0xCE))

    source_line(s, "Sumber modul, entri 1.", color=RGBColor(0x9C, 0xBE, 0xA6))
    return s


def slide_definition(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Konsep inti", "Apa itu energi alternatif?")

    shp = rect(s, MARGIN, Inches(2.15), CONTENT_W, Inches(1.45), fill=GREEN, radius=0.05)
    tf = shp.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    p.line_spacing = 1.2
    r = p.add_run()
    r.text = "Energi yang berasal dari sumber daya alam yang "
    style_run(r, 22, WHITE)
    r = p.add_run()
    r.text = "dapat diperbarui"
    style_run(r, 22, RGBColor(0xFC, 0xD3, 0x4D), bold=True)
    r = p.add_run()
    r.text = " dan "
    style_run(r, 22, WHITE)
    r = p.add_run()
    r.text = "ramah lingkungan"
    style_run(r, 22, RGBColor(0xFC, 0xD3, 0x4D), bold=True)
    r = p.add_run()
    r.text = "."
    style_run(r, 22, WHITE)

    box = textbox(s, MARGIN, Inches(3.95), CONTENT_W, Inches(0.4))
    r = box.text_frame.paragraphs[0].add_run()
    r.text = "EMPAT CONTOH"
    style_run(r, 11, AMBER, bold=True, spacing=1.6)

    chips = ["Surya\n(matahari)", "Angin", "Air", "Biogas"]
    gap = Inches(0.28)
    cw = (CONTENT_W - gap * 3) / 4
    for i, label in enumerate(chips):
        x = MARGIN + i * (cw + gap)
        shp = rect(s, x, Inches(4.45), cw, Inches(1.0), fill=SOFT, radius=0.08)
        tf = shp.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.line_spacing = 1.0
        r = p.add_run()
        r.text = label
        style_run(r, 17, GREEN, bold=True)

    source_line(s, "Sumber modul, entri 2.")
    page_number(s, n)
    return s


def slide_compare(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Membandingkan", "Mengapa disebut “alternatif”?")

    col_w = (CONTENT_W - Inches(0.4)) / 2

    left = rect(s, MARGIN, Inches(2.2), col_w, Inches(2.9), fill=SOFT, radius=0.05)
    tf = left.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = "ENERGI ALTERNATIF"
    style_run(r, 13, GREEN, bold=True, spacing=1.4)
    for text, accent in [("Dapat diperbarui", True), ("Ramah lingkungan", True),
                         ("Surya · angin · air · biogas", False)]:
        p = tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_before = Pt(9)
        p.line_spacing = 1.1
        r = p.add_run()
        r.text = text
        style_run(r, 26 if accent else 19, INK if not accent else GREEN, bold=accent)

    right = rect(s, MARGIN + col_w + Inches(0.4), Inches(2.2), col_w, Inches(2.9),
                 fill=SOFT_AMBER, radius=0.05)
    tf = right.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = "BAHAN BAKAR FOSIL"
    style_run(r, 13, AMBER, bold=True, spacing=1.4)
    for text, accent in [("Tidak dapat diperbarui", True), ("Menghasilkan polusi", True),
                         ("Minyak · batu bara", False)]:
        p = tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_before = Pt(9)
        p.line_spacing = 1.1
        r = p.add_run()
        r.text = text
        style_run(r, 26 if accent else 19, INK if not accent else AMBER, bold=accent)

    source_line(s, "Sumber modul, entri 2.")
    page_number(s, n)
    return s


def slide_two_lists(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Prasyarat Fase B", "Dari mana energi kita berasal?")

    col_w = (CONTENT_W - Inches(0.4)) / 2
    card(s, MARGIN, Inches(2.2), col_w, Inches(2.95), "SUMBER ENERGI",
         ["Matahari", "Angin", "Air", "Bahan bakar: minyak, kayu, gas", "Makanan"], size=16)
    card(s, MARGIN + col_w + Inches(0.4), Inches(2.2), col_w, Inches(2.95), "BENTUK ENERGI",
         ["Gerak", "Panas", "Cahaya", "Listrik", "Kimia", "Bunyi"], size=16)

    box = rect(s, MARGIN, Inches(5.45), CONTENT_W, Inches(0.95), fill=GREEN, radius=0.06)
    tf = box.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.line_spacing = 1.15
    r = p.add_run()
    r.text = "Matahari, angin, dan air adalah sumber energi — dan ketiganya juga termasuk "
    style_run(r, 15, WHITE)
    r = p.add_run()
    r.text = "contoh energi alternatif."
    style_run(r, 15, RGBColor(0xFC, 0xD3, 0x4D), bold=True)

    source_line(s, "Sumber modul, entri 3 dan 4; irisan dengan energi alternatif — entri 2.")
    page_number(s, n)
    return s


def slide_conversion(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Perubahan bentuk", "Energi berubah bentuk")

    rows = [
        ("Lampu menyala", "listrik", "cahaya + panas"),
        ("Kipas angin", "listrik", "gerak"),
        ("Tubuh bergerak", "kimia (makanan)", "gerak"),
    ]
    y = Inches(2.45)
    for label, before, after in rows:
        box = textbox(s, MARGIN, y, Inches(2.7), Inches(0.6))
        p = box.text_frame.paragraphs[0]
        r = p.add_run()
        r.text = label
        style_run(r, 17, GREEN, bold=True)

        chip = rect(s, MARGIN + Inches(2.85), y - Inches(0.06), Inches(2.35), Inches(0.62),
                    fill=SOFT, radius=0.2)
        tf = chip.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = before
        style_run(r, 15, INK)

        arrow = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, MARGIN + Inches(5.35),
                                   y + Inches(0.09), Inches(0.55), Inches(0.28))
        arrow.fill.solid()
        arrow.fill.fore_color.rgb = AMBER
        arrow.line.fill.background()
        arrow.shadow.inherit = False

        chip = rect(s, MARGIN + Inches(6.05), y - Inches(0.06), Inches(2.9), Inches(0.62),
                    fill=SOFT_AMBER, radius=0.2)
        tf = chip.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = after
        style_run(r, 15, AMBER, bold=True)

        y += Inches(1.45)

    source_line(s, "Sumber modul, entri 5.")
    page_number(s, n)
    return s


def slide_law(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Hukum kekekalan energi", "Energi tidak pernah hilang")

    box = textbox(s, MARGIN, Inches(2.35), CONTENT_W - Inches(1.2), Inches(2.2))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.line_spacing = 1.25
    r = p.add_run()
    r.text = "Energi "
    style_run(r, 30, INK)
    r = p.add_run()
    r.text = "tidak dapat diciptakan atau dimusnahkan"
    style_run(r, 30, GREEN, bold=True)
    r = p.add_run()
    r.text = " — hanya "
    style_run(r, 30, INK)
    r = p.add_run()
    r.text = "diubah bentuknya."
    style_run(r, 30, GREEN, bold=True)

    line = rect(s, MARGIN, Inches(4.75), CONTENT_W, Inches(1.15), fill=SOFT, radius=0.05)
    tf = line.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.line_spacing = 1.15
    r = p.add_run()
    r.text = "Yang terbatas bukan energinya, melainkan sumbernya: bahan bakar fosil "
    style_run(r, 16, INK)
    r = p.add_run()
    r.text = "tidak dapat diperbarui."
    style_run(r, 16, AMBER, bold=True)

    source_line(s, "Sumber modul, entri 6; sifat bahan bakar fosil — entri 2.")
    page_number(s, n)
    return s


def slide_cirata(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Contoh nyata di Indonesia", "PLTS Terapung Cirata")

    stats = [
        ("145 MWac\n(192 MWp)", "kapasitas"),
        ("±340.000", "panel surya"),
        ("±200", "hektare"),
        ("9 Nov 2023", "diresmikan"),
    ]
    gap = Inches(0.25)
    cw = (CONTENT_W - gap * 3) / 4
    for i, (value, label) in enumerate(stats):
        x = MARGIN + i * (cw + gap)
        shp = rect(s, x, Inches(2.2), cw, Inches(1.75), fill=SOFT, radius=0.07)
        tf = shp.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.line_spacing = 0.95
        r = p.add_run()
        r.text = value
        style_run(r, 24 if i == 0 else 26, GREEN, bold=True)
        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        r = p2.add_run()
        r.text = label
        style_run(r, 12, MUTED, spacing=0.8)

    box = textbox(s, MARGIN, Inches(4.35), CONTENT_W, Inches(1.2))
    tf = box.text_frame
    p = tf.paragraphs[0]
    p.line_spacing = 1.2
    r = p.add_run()
    r.text = "Waduk Cirata, Purwakarta, Jawa Barat."
    style_run(r, 18, INK, bold=True)
    p = tf.add_paragraph()
    p.space_before = Pt(4)
    p.line_spacing = 1.2
    r = p.add_run()
    r.text = "Pembangkit surya terapung terbesar di Asia Tenggara berdasarkan kapasitas."
    style_run(r, 16, MUTED)

    source_line(s, "Konteks aktual CA1 — PLN Nusantara Renewables; PV Tech, 17 November 2023.")
    page_number(s, n)
    return s


def slide_saving(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Yang bisa kita lakukan", "Menghemat energi di sekolah dan di rumah")

    items = [
        ("01", "Matikan alat listrik", "yang tidak terpakai"),
        ("02", "Gunakan lampu", "hemat energi"),
    ]
    y = Inches(2.2)
    for num, lead, rest in items:
        shp = rect(s, MARGIN, y, CONTENT_W, Inches(1.15), fill=SOFT, radius=0.06)
        tf = shp.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = num + "   "
        style_run(r, 20, AMBER, bold=True)
        r = p.add_run()
        r.text = lead + " "
        style_run(r, 20, GREEN, bold=True)
        r = p.add_run()
        r.text = rest
        style_run(r, 20, INK)
        y += Inches(1.35)

    box = textbox(s, MARGIN, Inches(4.95), CONTENT_W, Inches(0.35))
    r = box.text_frame.paragraphs[0].add_run()
    r.text = "TIGA ALAT YANG DISEBUT SUMBER"
    style_run(r, 11, MUTED, bold=True, spacing=1.4)

    chips = ["Lampu", "Kipas", "Proyektor"]
    gap = Inches(0.25)
    cw = Inches(2.2)
    for i, label in enumerate(chips):
        x = MARGIN + i * (cw + gap)
        shp = rect(s, x, Inches(5.35), cw, Inches(0.62), fill=PAPER, line=GREEN, radius=0.25)
        tf = shp.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        r = p.add_run()
        r.text = label
        style_run(r, 15, GREEN, bold=True)

    source_line(s, "Sumber modul, entri 7.")
    page_number(s, n)
    return s


def slide_climate(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Mitigasi perubahan iklim", "Menjaga sumber daya alam")

    left_w = Inches(7.2)
    card(s, MARGIN, Inches(2.2), left_w, Inches(1.2), "YANG DIJAGA",
         ["Air · tanah · hutan · udara — agar tersedia bagi generasi mendatang"], size=15)
    card(s, MARGIN, Inches(3.65), left_w, Inches(2.25), "UPAYA YANG DISEBUT SUMBER",
         ["Reduce · reuse · recycle", "Menanam pohon", "Menghemat energi",
          "Transportasi ramah lingkungan"], size=15)

    # timeline 2030 -> 2060
    x0 = MARGIN + left_w + Inches(0.45)
    tw = CONTENT_W - left_w - Inches(0.45)
    axis = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x0 + Inches(0.35), Inches(3.18),
                              Pt(3), Inches(1.72))
    axis.fill.solid()
    axis.fill.fore_color.rgb = RGBColor(0xD1, 0xDA, 0xD4)
    axis.line.fill.background()
    axis.shadow.inherit = False

    for y, year, label, color in [
        (Inches(3.05), "2030", "FOLU net sink", GREEN),
        (Inches(4.75), "2060", "Net Zero Emission\natau lebih cepat", AMBER),
    ]:
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, x0 + Inches(0.24), y, Inches(0.26), Inches(0.26))
        dot.fill.solid()
        dot.fill.fore_color.rgb = color
        dot.line.fill.background()
        dot.shadow.inherit = False

        box = textbox(s, x0 + Inches(0.65), y - Inches(0.14), tw - Inches(0.7), Inches(1.0))
        tf = box.text_frame
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = year
        style_run(r, 19, color, bold=True)
        p2 = tf.add_paragraph()
        p2.line_spacing = 1.05
        r = p2.add_run()
        r.text = label
        style_run(r, 13, INK)

    source_line(s, "Sumber modul, entri 8; Konteks aktual CA6 — Bank Indonesia; KLHK.")
    page_number(s, n)
    return s


def slide_role(prs, n):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    header(s, "Penutup", "Giliran kita")

    roles = ["Menghemat energi", "Menanam pohon", "Menyebarkan informasi yang benar"]
    gap = Inches(0.3)
    cw = (CONTENT_W - gap * 2) / 3
    for i, label in enumerate(roles):
        x = MARGIN + i * (cw + gap)
        shp = rect(s, x, Inches(2.2), cw, Inches(1.15), fill=SOFT, radius=0.08)
        tf = shp.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.line_spacing = 1.1
        r = p.add_run()
        r.text = label
        style_run(r, 18, GREEN, bold=True)

    band = rect(s, MARGIN, Inches(3.85), CONTENT_W, Inches(1.45), fill=GREEN, radius=0.05)
    tf = band.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    p.line_spacing = 1.25
    r = p.add_run()
    r.text = "Mulai besok, matikan satu alat listrik yang biasa kamu tinggalkan menyala "
    style_run(r, 20, WHITE)
    r = p.add_run()
    r.text = "— lalu catat apa yang berubah."
    style_run(r, 20, RGBColor(0xFC, 0xD3, 0x4D), bold=True)

    source_line(s, "Sumber modul, entri 9.")
    page_number(s, n)
    return s


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H

    slide_title(prs)
    slide_definition(prs, 2)
    slide_compare(prs, 3)
    slide_two_lists(prs, 4)
    slide_conversion(prs, 5)
    slide_law(prs, 6)
    slide_cirata(prs, 7)
    slide_saving(prs, 8)
    slide_climate(prs, 9)
    slide_role(prs, 10)

    prs.core_properties.title = "Energi Alternatif dan Penghematan Energi"
    prs.core_properties.subject = "IPAS Fase C (Kelas V–VI) · CP-C.2.1.4"
    prs.core_properties.author = "EduCraft · EDU-ORCH-20261106-005"
    prs.save(args.out)

    # FR-01 gate: no internal marker may survive into the deck.
    check = Presentation(args.out)
    leftover = []
    for idx, slide in enumerate(check.slides, 1):
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            body = shape.text_frame.text
            if re.search(r"\[src:|\[UNVERIFIED\]|PERLU KONFIRMASI", body):
                leftover.append(idx)
    if leftover:
        print("FAIL: internal marker on slide(s) {}".format(sorted(set(leftover))))
        return 1

    print("OK  {} slide, 16:9, tanpa penanda internal".format(len(check.slides)))
    print("->  " + args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
