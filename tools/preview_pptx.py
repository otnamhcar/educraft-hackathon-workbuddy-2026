#!/usr/bin/env python3
"""preview_pptx.py — rasterise a .pptx to PNG for layout QA.

Why this exists
---------------
`slidep screenshot` needs a live editor session, and LibreOffice is not installed
on this machine. Neither is a reason to hand over a deck nobody has looked at.

This renders each slide from the shape geometry PowerPoint itself stores:
position, size, fill, and text. It is a *layout* preview, not a fidelity render —
font substitution and line breaking will differ slightly from PowerPoint. That is
enough to catch the failures that matter: text overflowing its box, two shapes
colliding, a colour that disappears against its background.

Usage
-----
  python tools/preview_pptx.py --file deck.pptx --outdir /tmp/preview

Exit codes: 0 = written, 2 = bad input.
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont
from pptx import Presentation
from pptx.util import Emu

SCALE = 0.12          # px per EMU-ish unit; 13.333in -> 1600px wide
PX_PER_IN = 120
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\segoeui.ttf",
    r"C:\Windows\Fonts\calibri.ttf",
    r"C:\Windows\Fonts\arial.ttf",
]
BOLD_CANDIDATES = [
    r"C:\Windows\Fonts\segoeuib.ttf",
    r"C:\Windows\Fonts\calibrib.ttf",
    r"C:\Windows\Fonts\arialbd.ttf",
]


def font_path(bold=False):
    for path in (BOLD_CANDIDATES if bold else FONT_CANDIDATES):
        if os.path.exists(path):
            return path
    return None


def get_font(size_px, bold=False):
    path = font_path(bold)
    if path:
        try:
            return ImageFont.truetype(path, size_px)
        except OSError:
            pass
    return ImageFont.load_default()


def rgb(shape, default=(230, 230, 230)):
    try:
        if shape.fill.type is not None and shape.fill.type == 1:
            c = shape.fill.fore_color.rgb
            return (c[0], c[1], c[2])
    except (AttributeError, TypeError):
        pass
    return default


def wrap(draw, text, font, max_w):
    """Greedy wrap. Good enough to reveal overflow."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render_slide(slide, width, height):
    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    W_EMU, H_EMU = slide.part.package.presentation_part.presentation.slide_width, \
        slide.part.package.presentation_part.presentation.slide_height
    sx, sy = width / W_EMU, height / H_EMU

    for shape in slide.shapes:
        x, y = int(shape.left * sx), int(shape.top * sy)
        w, h = int(shape.width * sx), int(shape.height * sy)
        kind = str(shape.shape_type)

        if shape.shape_type == 9 or "AUTO_SHAPE" in kind:
            fill = rgb(shape)
            name = ""
            try:
                name = shape.adjustments._prstGeom.attrib.get("prst", "")
            except AttributeError:
                pass
            if "OVAL" in name.upper():
                draw.ellipse([x, y, x + w, y + h], fill=fill)
            elif "ROUNDED" in name.upper():
                draw.rounded_rectangle([x, y, x + w, y + h], radius=min(w, h) // 12, fill=fill)
            else:
                draw.rectangle([x, y, x + w, y + h], fill=fill)
        elif shape.shape_type == 1:  # picture
            draw.rectangle([x, y, x + w, y + h], outline=(200, 200, 200))

        if not shape.has_text_frame:
            continue
        tf = shape.text_frame
        pad_x = int((tf.margin_left or 0) * sx) if tf.margin_left else 0
        pad_y = int((tf.margin_top or 0) * sy) if tf.margin_top else 0
        cx = x + pad_x
        cy = y + pad_y
        avail = max(w - 2 * pad_x, 20)

        # Dua lintasan: ukur dulu tinggi seluruh teks, baru tempatkan. Tanpa ini
        # pratinjau selalu menggambar dari tepi atas kotak dan tidak pernah
        # menunjukkan efek `vertical_anchor` — gambar QA jadi menyesatkan.
        items = []
        total = 0
        for paragraph in tf.paragraphs:
            text = "".join(r.text for r in paragraph.runs)
            if not text.strip():
                total += 6
                continue
            run = paragraph.runs[0]
            size_pt = run.font.size.pt if run.font.size else 18
            bold = bool(run.font.bold)
            color = (31, 41, 55)
            try:
                if run.font.color and run.font.color.rgb:
                    c = run.font.color.rgb
                    color = (c[0], c[1], c[2])
            except (AttributeError, TypeError):
                pass

            fnt = get_font(max(int(size_pt * PX_PER_IN / 72), 8), bold)
            lines = wrap(draw, text, fnt, avail)
            align = paragraph.alignment
            for line in lines:
                lw = draw.textlength(line, font=fnt)
                dx = 0
                if align is not None and int(align) == 2:      # centre
                    dx = (avail - lw) / 2
                elif align is not None and int(align) == 3:    # right
                    dx = avail - lw
                items.append((dx, total, line, fnt, color))
                total += int(size_pt * PX_PER_IN / 72 * 1.22)
            total += int((paragraph.space_after.pt if paragraph.space_after else 0) * PX_PER_IN / 72)

        offset = 0
        try:
            anchor = tf.vertical_anchor
        except (AttributeError, TypeError):
            anchor = None
        if anchor is not None:
            ruang = max(h - 2 * pad_y, 0)
            if int(anchor) == 3:                                # tengah
                offset = max((ruang - total) // 2, 0)
            elif int(anchor) == 4:                              # bawah
                offset = max(ruang - total, 0)

        for dx, dy, line, fnt, color in items:
            draw.text((cx + dx, cy + offset + dy), line, font=fnt, fill=color)

    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--width", type=int, default=1600)
    args = ap.parse_args()

    if not os.path.isfile(args.file):
        print("error: {} not found".format(args.file), file=sys.stderr)
        return 2
    os.makedirs(args.outdir, exist_ok=True)

    prs = Presentation(args.file)
    height = int(args.width * prs.slide_height / prs.slide_width)
    for idx, slide in enumerate(prs.slides):
        img = render_slide(slide, args.width, height)
        out = os.path.join(args.outdir, "slide_{:02d}.png".format(idx + 1))
        img.save(out)
        print(out)
    print("{} slide -> {}".format(len(prs.slides), args.outdir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
