#!/usr/bin/env python3
"""Render an evidence screenshot from a run artifact.

The submission needs screenshots of scenes that only exist as files: the Planner
outline, the Writer's tagged draft, the Reviewer's verdict, the audit log. This
script renders those files as a legible document page and captures it at the
width `tools/check_capture.py` demands (1600 px).

What it does NOT do: pretend to be a screen capture of a live session. Every
page carries a banner saying the content is a rendered run artifact, because the
screenshot is evidence of the artifact, not of the UI.

    python3 tools/render_evidence.py --out out.png \
        --kicker "S2 · Siklus penolakan" \
        --title "Reviewer menolak draf v1" \
        --source 03_Hasil/edu_output_wujud_zat/05_review.md \
        --pick "## PASS 1 — Draft v1: ❌ REJECT"

Options:
    --pick "A-B"     include lines A..B (1-based, inclusive). Repeatable.
    --pick "## X"    include heading X and everything under it. Repeatable.
    Picks are applied in the order given on the command line.
    --run ID         run identifier shown in the meta line.
    --note TEXT      extra sentence in the footer.

Exit codes: 0 = png written, 1 = render failed, 2 = bad arguments.
"""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WIDTH = 1600


def find_chrome():
    """Locate a Chromium-family binary on Linux, macOS, or Windows.

    Dulu nilai ini dipaku `google-chrome`, nama paket Linux. Di mesin Windows
    proyek ini perintah itu tidak ada, sehingga setiap render gagal dengan
    WinError 2 padahal Chrome terpasang. Kegagalannya menyesatkan: pesannya
    "file not found", bukan "Chrome tidak ada".
    """
    env = os.environ.get("CHROME_BIN") or os.environ.get("CHROME_PATH")
    if env and Path(env).exists():
        return env
    absolute = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        str(Path.home() / "AppData/Local/Google/Chrome/Application/chrome.exe"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for candidate in absolute:
        if Path(candidate).exists():
            return candidate
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
                 "chrome", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    return "google-chrome"


CHROME = find_chrome()

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { width: %(w)dpx; background: #FFFFFF; color: #1F2937;
       font-family: -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
       -webkit-font-smoothing: antialiased; }
.banner { background: #1E1B4B; color: #FFFFFF; padding: 30px 64px 26px; }
.kicker { font-size: 13px; letter-spacing: 0.16em; text-transform: uppercase; color: #A5B4FC; font-weight: 600; }
.banner h1 { font-size: 34px; font-weight: 650; margin-top: 8px; line-height: 1.2; }
.meta { margin-top: 12px; font-size: 14px; color: #C7D2FE; }
.meta code { background: rgba(255,255,255,.14); color: #E0E7FF; }
.stamp { float: right; border: 1px solid #4F46E5; color: #C7D2FE; font-size: 11.5px;
         letter-spacing: 0.1em; text-transform: uppercase; padding: 6px 10px; margin-top: 4px; }
.doc { padding: 44px 64px 30px; max-width: 1420px; }
.doc h1 { font-size: 27px; font-weight: 650; margin: 0 0 18px; padding-bottom: 12px; border-bottom: 2px solid #E5E7EB; }
.doc h2 { font-size: 22px; font-weight: 650; margin: 30px 0 12px; color: #312E81; }
.doc h3 { font-size: 18px; font-weight: 650; margin: 24px 0 10px; color: #4338CA; }
.doc h4 { font-size: 16px; font-weight: 650; margin: 18px 0 8px; }
.doc p { font-size: 16px; line-height: 1.65; margin: 0 0 12px; }
.doc ul, .doc ol { margin: 0 0 14px 24px; }
.doc li { font-size: 16px; line-height: 1.6; margin-bottom: 5px; }
.doc blockquote { border-left: 3px solid #4338CA; background: #F5F3FF; padding: 12px 18px;
                  margin: 0 0 14px; color: #312E81; }
.doc blockquote p { margin: 0 0 6px; font-size: 15.5px; }
.doc blockquote p:last-child { margin-bottom: 0; }
.doc table { width: 100%%; border-collapse: collapse; margin: 0 0 18px; font-size: 14.5px; }
.doc th { text-align: left; background: #F3F4F6; font-weight: 650; padding: 9px 12px;
          border: 1px solid #D1D5DB; font-size: 13px; }
.doc td { padding: 9px 12px; border: 1px solid #E5E7EB; vertical-align: top; line-height: 1.5; }
.doc code { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; font-size: 13.5px;
            background: #F1F0EC; padding: 1px 5px; border-radius: 3px; }
.doc pre { background: #F8F7F4; border: 1px solid #E5E7EB; padding: 14px 16px; overflow: hidden;
           margin: 0 0 16px; }
.doc pre code { background: none; padding: 0; font-size: 13px; }
.tag { background: #ECFDF5; color: #065F46; border: 1px solid #A7F3D0; border-radius: 3px;
       padding: 0 4px; font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 13px; }
.rule { font-weight: 700; color: #B91C1C; }
.doc hr { border: none; border-top: 1px solid #E5E7EB; margin: 22px 0; }
.foot { padding: 16px 64px 26px; border-top: 1px solid #E5E7EB; font-size: 12.5px; color: #6B7280;
        display: flex; justify-content: space-between; }
"""


def inline(text):
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"(\[src:[^\]]+\]|\[UNVERIFIED\])", r'<span class="tag">\1</span>', text)
    text = re.sub(r"\b(R0\d\d)\b", r'<span class="rule">\1</span>', text)
    return text


def is_sep(line):
    return bool(re.match(r"^\|[\s:|-]+\|$", line.strip()))


def md_to_html(lines):
    out, i = [], 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(html.escape(lines[i]))
                i += 1
            i += 1
            out.append("<pre><code>{}</code></pre>".format("\n".join(buf)))
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            out.append("<h{0}>{1}</h{0}>".format(level, inline(m.group(2))))
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and is_sep(lines[i + 1]):
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head = "".join("<th>{}</th>".format(inline(c)) for c in header)
            body = "".join(
                "<tr>{}</tr>".format("".join("<td>{}</td>".format(inline(c)) for c in r))
                for r in rows
            )
            out.append("<table><thead><tr>{}</tr></thead><tbody>{}</tbody></table>".format(head, body))
            continue

        if stripped.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            paras = "".join("<p>{}</p>".format(inline(p)) for p in buf if p.strip())
            out.append("<blockquote>{}</blockquote>".format(paras))
            continue

        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append("<li>{}</li>".format(inline(re.sub(r"^[-*]\s+", "", lines[i].strip()))))
                i += 1
            out.append("<ul>{}</ul>".format("".join(items)))
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append("<li>{}</li>".format(inline(re.sub(r"^\d+\.\s+", "", lines[i].strip()))))
                i += 1
            out.append("<ol>{}</ol>".format("".join(items)))
            continue

        if re.match(r"^-{3,}$", stripped) or re.match(r"^\*{3,}$", stripped):
            out.append("<hr>")
            i += 1
            continue

        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^(#{1,6}\s|\||>|[-*]\s|\d+\.\s|```|-{3,}$)", lines[i].strip()
        ):
            buf.append(lines[i].strip())
            i += 1
        out.append("<p>{}</p>".format(inline(" ".join(buf))))

    return "\n".join(out)


def extract(source_lines, spec):
    if spec[0] == "lines":
        start, end = spec[1], spec[2]
        return source_lines[start - 1:end]
    heading = spec[1].strip()
    level = len(heading) - len(heading.lstrip("#"))
    start = None
    for idx, line in enumerate(source_lines):
        if line.strip() == heading:
            start = idx
            break
    if start is None:
        raise SystemExit("ERROR: heading not found: {}".format(heading))
    end = len(source_lines)
    for idx in range(start + 1, len(source_lines)):
        s = source_lines[idx].strip()
        m = re.match(r"^(#{1,6})\s", s)
        if m and len(m.group(1)) <= level:
            end = idx
            break
    return source_lines[start:end]


def chrome_height(page, tmp):
    script = page.replace(
        "</body>",
        "<script>document.title='H='+Math.ceil(document.body.getBoundingClientRect().height)</script></body>",
    )
    probe = tmp / "probe.html"
    probe.write_text(script, encoding="utf-8")
    result = subprocess.run(
        [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--virtual-time-budget=1500",
         "--window-size={},3000".format(WIDTH), "--dump-dom", probe.as_uri()],
        capture_output=True, text=True,
    )
    match = re.search(r"<title>H=(\d+)</title>", result.stdout)
    if not match:
        raise SystemExit("ERROR: could not measure page height")
    return int(match.group(1))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Render an evidence screenshot from a run artifact.")
    parser.add_argument("--out", required=True)
    parser.add_argument("--kicker", default="")
    parser.add_argument("--title", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--pick", action="append", default=[])
    parser.add_argument("--run", default="")
    parser.add_argument("--note", default="")
    args = parser.parse_args(argv)

    source = (REPO_ROOT / args.source).resolve()
    if not source.is_file():
        print("ERROR: source not found: {}".format(source), file=sys.stderr)
        return 2
    if not args.pick:
        print("ERROR: give at least one --pick (line range or heading)", file=sys.stderr)
        return 2

    source_lines = source.read_text(encoding="utf-8").splitlines()
    specs = []
    for value in args.pick:
        if re.match(r"^\d+-\d+$", value.strip()):
            start, end = value.split("-")
            specs.append(("lines", int(start), int(end)))
        else:
            specs.append(("section", value))

    picked = []
    for spec in specs:
        picked.extend(extract(source_lines, spec))
    body = md_to_html(picked)

    rel = source.relative_to(REPO_ROOT).as_posix()
    meta = "Berkas: <code>{}</code>".format(html.escape(rel))
    if args.run:
        meta += " · Run <strong>{}</strong>".format(html.escape(args.run))
    # Tanggal render dulu dipaku "5 November 2026", sehingga setiap gambar yang
    # dibuat setelah itu menyatakan tanggal yang salah pada banner buktinya.
    # Keterangan bertanggal yang keliru lebih buruk daripada tanpa tanggal.
    BULAN = ("Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
             "Agustus", "September", "Oktober", "November", "Desember")
    today = date.today()
    meta += " · Dirender {} {} {}".format(today.day, BULAN[today.month - 1], today.year)

    page = """<!DOCTYPE html><html lang="id"><head><meta charset="utf-8">
<title>{title}</title><style>{css}</style></head><body>
<div class="banner"><div class="stamp">Berkas hasil run · dirender</div>
<div class="kicker">{kicker}</div><h1>{title}</h1><div class="meta">{meta}</div></div>
<div class="doc">{body}</div>
<div class="foot"><span>Isi berkas apa adanya; tidak ada kutipan yang disunting. {note}</span>
<span>{rel}</span></div>
</body></html>""".format(
        title=html.escape(args.title),
        css=CSS % {"w": WIDTH},
        kicker=html.escape(args.kicker),
        meta=meta,
        body=body,
        note=html.escape(args.note),
        rel=html.escape(rel),
    )

    out = (REPO_ROOT / args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        height = chrome_height(page, tmp)
        page_file = tmp / "page.html"
        page_file.write_text(page, encoding="utf-8")
        result = subprocess.run(
            [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--window-size={},{}".format(WIDTH, height),
             "--screenshot={}".format(out), page_file.as_uri()],
            capture_output=True, text=True,
        )
        if not out.is_file():
            print("ERROR: screenshot failed\n{}".format(result.stderr[-800:]), file=sys.stderr)
            return 1

    head = out.read_bytes()[:24]
    w = int.from_bytes(head[16:20], "big")
    h = int.from_bytes(head[20:24], "big")
    # relative_to() melempar ValueError bila --out berada di luar repo. Dulu itu
    # membuat render yang sudah berhasil dilaporkan sebagai kegagalan, tepat pada
    # baris terakhir. Tampilkan jalur apa adanya bila di luar repo.
    try:
        shown = out.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        shown = str(out)
    print("{} -- {}x{} px".format(shown, w, h))
    return 0


if __name__ == "__main__":
    sys.exit(main())
