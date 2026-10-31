# REVIEW KEPATUHAN — Rulebook R001–R011
**Reviewer:** edu-reviewer · **Tanggal:** 2026-10-29 · **Run:** EDU-ORCH-20261026-001
**Artefak diperiksa:** `01_RPP_Energi_Alternatif.md`, `02_Kuis_PrePost_Energi.md`, `03_Slide_Energi.md`, `04_Artikel_Sahabat_Energi.md`, `05_Brief_Infografis_Energi.md`, `quiz_interaktif.html`

## VERDICT: ❌ REJECT (Critical) — STOP & eskalasi ke Guru/SME. Jangan publish.

---

## 1. Ringkasan per Aturan

| Rule | Status | Catatan |
|------|--------|---------|
| R001 Factual grounding | ❌ **FAIL (Critical)** | Tag `[src:B5]/[src:C4]/[src:B3]` merujuk CP, bukan SOURCE MATERIAL. Source material resmi justru bertopik **karhutla**, bukan energi. |
| R002 No fear-mongering | ✅ PASS | Nada tenang & solutif. |
| R003 Age-appropriate | ✅ PASS | Kosakata SD Fase C. |
| R004 Curriculum alignment | ⚠️ **FAIL (Major)** | CP C4/B5 traceable dari `cp_ipas.md`, tetapi topik draf (energi) tidak didukung source material (karhutla). |
| R005 Balanced & solution-oriented | ✅ PASS | Ada peran siswa & upaya. |
| R006 Health-claim caution | ➖ N/A | Tidak ada klaim kesehatan. |
| R007 No harmful promotion | ✅ PASS | Tidak ada promosi berbahaya. |
| R008 Brand/pedagogic tone | ✅ PASS | Ramah, edukatif. |
| R009 KBBI + CTA positif | ✅ PASS | CTA ada di slide/artikel/brief. |
| R010 Non-stigmatizing | ✅ PASS | Bahasa sopan, tidak memojokkan. |
| R011 Actual-context verification | ❌ **FAIL (Critical)** | CA1 (PLTS Cirata) & CA6 (Net Zero 2060) tidak punya dokumen sumber resmi/bertanggal di proyek. |

---

## 2. Temuan Detail

### 🔴 CRITICAL-1 — R001: Rantai grounding putus (source mismatch)
- **Bukti:** `03_Hasil/referensi/source_material_ipas.md` bertopik **"Dampak Kebakaran Hutan di Kalimantan"** dengan tag `[src:1]`–`[src:8]`. Tidak ada satu pun fakta energi di dalamnya. Draf energi mencantumkan `[src:B5]`, `[src:C4]`, `[src:B3]` — itu **referensi CP** dari `cp_ipas.md`, bukan fakta SOURCE MATERIAL.
- **Dampak:** Semua klaim fakta (bentuk energi, hukum kekekalan energi, contoh lampu/kipas) tidak ter-grounding ke source material sebagaimana disyaratkan R001.
- **Perbaikan:** Sediakan `source_material_energi.md` yang benar (dengan `[src:1..n]` untuk fakta energi) **atau** ganti topik draf ke karhutla sesuai source yang ada. Lalu re-tag draf.

### 🔴 CRITICAL-2 — R011: Konteks Aktual tanpa sumber resmi terdokumentasi
- **Bukti:** CA1 (PLTS Terapung Cirata, ~145 MWp, 2023, Waduk Cirata) dan CA6 (FOLU Net Sink 2030 / Net Zero 2060) **tidak didefinisikan di dokumen mana pun** di proyek. `panduan_ipas.txt` (4.937 baris) tidak memuat kata "Cirata/PLTS/145 MWp/net zero".
- **Catatan:** Fakta ini kemungkinan benar secara umum, tetapi **tidak dapat diverifikasi** sesuai R011 (wajib sumber resmi, bertanggal, dapat ditelusuri).
- **Perbaikan:** Dokumentasikan URL resmi (PLN untuk Cirata; KLHK untuk Net Zero) + tanggal akses di file `konteks_aktual.md`, lalu tautkan ke draf.

### 🟠 MAJOR-1 — R004: Topik vs Source tidak konsisten
- **Bukti:** `00_run_config.md` mendeklarasikan Source = `assets/source_material_ipas.md` (Panduan IPAS), tetapi isi file = modul karhutla; draf = energi alternatif.
- **Dampak:** Klaim "semua fakta dari source" tidak dapat dipertahankan di depan juri.
- **Perbaikan:** Selaraskan topik, source material, dan run config.

---

## 3. Pemeriksaan Khusus
- **Kunci jawaban & skor:** ✅ BENAR. Pre-test 7×1=7; Post-test PG 13×2=26 + US 7×4=28 = 54. Kunci P1–P7 dan 1–13 semuanya sesuai.
- **IPAS = mapel SD/MI (bukan SMP):** ✅ Benar, draf memakai SD Fase C.
- **Klaim kesehatan:** ➖ Tidak ada.
- **Fear-mongering:** ✅ Tidak ada.

---

## 4. JSON Verdict
```json
{
  "status": "REJECT",
  "findings": [
    {"rule": "R001", "severity": "Critical", "quote": "[src:B5]/[src:C4]/[src:B3] pada seluruh draf", "reason": "Tag merujuk CP, bukan SOURCE MATERIAL; source material resmi bertopik karhutla dan tidak memuat fakta energi.", "suggestion": "Sediakan source_material_energi.md ber-tag [src:1..n], atau ganti topik ke karhutla; re-tag draf."},
    {"rule": "R011", "severity": "Critical", "quote": "[src:CA1] PLTS Cirata ~145 MWp; [src:CA6] Net Zero 2060", "reason": "Tidak ada dokumen sumber resmi/bertanggal di proyek; tidak dapat diverifikasi.", "suggestion": "Buat konteks_aktual.md dengan URL PLN & KLHK + tanggal akses, lalu tautkan."},
    {"rule": "R004", "severity": "Major", "quote": "Source file: assets/source_material_ipas.md (00_run_config)", "reason": "Topik draf (energi) tidak selaras dengan isi source (karhutla).", "suggestion": "Selaraskan topik, source, dan run config."}
  ]
}
```

---

## 5. Rekomendasi Urutan Perbaikan
1. Tentukan topik final: **energi alternatif** (buat source baru) atau **karhutla** (pakai source yang ada).
2. Sediakan source material + `konteks_aktual.md` (URL resmi, bertanggal).
3. Re-tag seluruh draf ke `[src:#]` yang benar.
4. Jalankan ulang `edu-reviewer`. Baru boleh lanjut ke bundel submission.
