import fitz, os, sys

BASE = r"D:/DataSheet/Ai_Skill/workBuddy_work/sumber hackton"
OUT = os.path.join(BASE, "extracted")
os.makedirs(OUT, exist_ok=True)

files = {
    "panduan_ipas": "Final Panduan Mata Pelajaran IPAS_03_10_2025_Revisi 4.pdf",
    "permendikdasmen_13_2025": "Permendikdasmen-no-13-tahun-2025.pdf",
}

for key, fname in files.items():
    path = os.path.join(BASE, fname)
    out_path = os.path.join(OUT, key + ".txt")
    try:
        doc = fitz.open(path)
        n = doc.page_count
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"=== {fname} | pages={n} ===\n\n")
            for i, page in enumerate(doc):
                txt = page.get_text("text")
                f.write(f"\n----- PAGE {i+1} -----\n")
                f.write(txt if txt.strip() else "[NO TEXT LAYER - possibly scanned image]\n")
        print(f"{key}: {n} pages -> {out_path}")
        doc.close()
    except Exception as e:
        print(f"{key}: ERROR {e}")
