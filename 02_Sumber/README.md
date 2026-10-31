# 02_Sumber — the primary sources

These are the documents every quoted fact in this project traces back to. They are published here
**unmodified**, so that a reader can check our summaries against the original instead of trusting
them.

## What is here

| File | What it is | Pages | Published? |
|------|------------|------:|------------|
| `Final Panduan Mata Pelajaran IPAS_03_10_2025_Revisi 4.pdf` | *Panduan Mata Pelajaran IPAS*, Badan Standar, Kurikulum, dan Asesmen Pendidikan, Kemendikdasmen — Revisi 4, 3 October 2025 | 106 | ✅ yes |
| `Permendikdasmen-no-13-tahun-2025.pdf` | Regulation of the Minister of Primary and Secondary Education No. 13 of 2025 | 76 | ✅ yes |
| `extracted/panduan_ipas.txt` | Plain-text extraction of the guide, with `----- PAGE n -----` markers | 4,937 lines | ✅ yes |
| `extracted/permendikdasmen_13_2025.txt` | Plain-text extraction of the regulation | 6,322 lines | ✅ yes |
| `extract_pdf.py` | The script that produced both `.txt` files — re-runnable, no OCR | — | ✅ yes |

The `.txt` files exist because the agents read text, not PDFs. Each begins with a header naming its
source PDF and page count, so the extraction is traceable in both directions.

## What is **not** here, and why

| Excluded | Reason |
|----------|--------|
| `centralpendidikan.com 1–6. rpp 1 lembar ipa kelas 7.docx` + the `.rar` | Third-party commercial worksheets. They cover **SMP kelas 7**, outside this project's SD domain, and **no artefact depends on them**. Redistributing them would add a third-party rights question for no benefit |
| `1. Panduan Penilaian SMP - Cetakan Keempat 2017.pdf` | Same reason: SMP, unused |

Neither exclusion weakens reproducibility: every file under `03_Hasil/referensi/` derives from the
two official documents that **are** published.

## Licence

These two PDFs are official public documents issued by an Indonesian ministry. They are **not**
covered by this project's MIT licence, and nothing here claims authorship of them. See
[`../THIRD_PARTY_NOTICES.md`](../THIRD_PARTY_NOTICES.md).

The MIT licence covers the code, the contracts and the written documentation — not these PDFs.

## How the chain runs

```
02_Sumber/*.pdf
   └─ extract_pdf.py ──▶ extracted/*.txt
          └─ 03_Hasil/referensi/source_material_*.md   (quoted facts, [src:W1]…[src:W11])
                 └─ 03_Hasil/…/drafts                (every sentence carries a tag)
                        └─ tools/check_grounding.py    (resolves each tag, or fails)
```

A reviewer can start at any draft sentence, follow its tag to a `source_material_*.md` entry, follow
that entry's line reference into `extracted/panduan_ipas.txt`, and land on the page of the PDF. That
is what "grounded" means here — not that a citation exists, but that it can be walked.

To re-run the extraction yourself (needs `pip install pymupdf`):

```bash
python3 02_Sumber/extract_pdf.py        # Linux / macOS
python 02_Sumber\extract_pdf.py         # Windows
```

It resolves paths from its own location, so it works from any directory, and it writes CRLF on every
OS so the output matches the committed `.txt` files byte for byte rather than producing a whole-file
diff.
