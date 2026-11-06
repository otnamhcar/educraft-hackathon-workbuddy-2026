# Run Configuration — EDU-ORCH-20261026-001

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261026-001 |
| **Tanggal/Waktu** | 2026-10-26 18:35 GMT+7 |
| **Orchestrator** | EduCraft Orchestrator (Master) |
| **Domain Pack** | SD–IPAS, Kurikulum Merdeka (Fase B & C) |
| **Flow** | Core pipeline: Intake → Plan → Draft → Review → Approve → Publish → Format Rendering |
| **Topik** | Energi Alternatif dan Penghematan Energi (lintas Fase B → Fase C) |
| **Fase Sasaran** | Fase C (kelas V–VI), dengan fondasi Fase B |
| **CP Sasaran** | C4 (2.1.4): "Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi alternatif dari sumber daya sekitar sebagai mitigasi perubahan iklim" |
| **CP Fondasi** | B5 (1.1.5): "Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk energi dalam kehidupan sehari-hari" |
| **Konteks Aktual** | CA1 (PLTS Terapung Cirata, 145 MWac/192 MWp, 2023), CA6 (FOLU Net Sink 2030 / Net Zero 2060) — lihat `08_Referensi/konteks_aktual.md` |
| **Source file** | `08_Referensi/source_material_energi.md` (fakta [src:1–9]) + `08_Referensi/konteks_aktual.md` (CA1/CA6) |
| **CP reference** | `08_Referensi/cp_ipas.md` |
| **Rulebook** | `08_Referensi/rulebook_ipas.md` (R001–R012, v2.0) |
| **Format Rendering** | `05_Bukti_Proses/skills_package/edu-orchestrator/assets/format_rendering_spec.md` (Stage 6, FR-01…FR-08) — wajib untuk artefak siap pakai |
| **Intake menu** | `05_Bukti_Proses/skills_package/edu-orchestrator/assets/intake_menu_ipas.md` (S0, 20 bab + status sumber). Run ini tidak memerlukannya karena topik sudah disebut di brief; berlaku untuk run berikutnya. Bawaan format: RPP + kuis + slide (minimal 2). |
| **Iteration** | `1` of max `3` — **one rejection** recorded (29 Oct 2026); draft v2 approved 30 Oct 2026. *Review passes: 2 (pass 1 REJECT, pass 2 APPROVE) — see §7 of `audit_log_edu_orchestrator.md`.* |
| **Human approver** | ✅ APPROVED — Don Jimat Akbar (4 Nov 2026, 14:49 GMT+7) |
| **Publish status** | ✅ PUBLISHED — materi dirilis ke format siap pakai |

## Format yang dihasilkan

### Draft inti (Markdown — dari pipeline Plan → Draft → Review)
1. `01_lesson_plan.md` — RPP (Lesson Plan)
2. `02_quiz_pretest_posttest.md` — Pre-test (7 MC) + Post-test (20 soal) + kunci & skor
3. `03_slide_outline.md` — Slide Outline
4. `04_artikel.md` — Artikel pendek "Sahabat Energi" (Flow C)
5. `05_infographic_brief.md` — Brief infografis (Flow C)
6. `audit_log.md` — Log audit (Planner → Writer → Reviewer, revision history)

### Deliverable siap pakai (Format Rendering — pasca-approval)
| # | Deliverable | Sumber draft | Skill konversi | Status |
|---|-------------|-------------|----------------|--------|
| 1 | `RPP_Energi_Alternatif.docx` | `01_lesson_plan.md` → HTML terstruktur | `workbuddy-docx` (html-to-doc) | ✅ Selesai |
| 2 | `Slide_Energi_Alternatif.pptx` | `03_slide_outline.md` → slide DSL | `workbuddy-pptx` (slidep CLI) | ✅ Selesai |
| 3 | `quiz_interaktif_v2.html` | `quiz_interaktif.html` + `02_quiz_pretest_posttest.md` | Enhancement manual (dark mode, timer, CSV export) | ✅ Selesai |
| 4 | `06_Materi_Guru_Energi_Alternatif.md` | gabungan `01`–`04` (tanpa tag) | `tools/build_materi_md.py` | ✅ Selesai — *ditambahkan 5 Nov 2026, lihat `audit_log.md` §3.8* |

> **Catatan urutan (5 Nov 2026):** baris 4 ditambahkan setelah rilis. Sejak `format_rendering_spec.md`
> v1.1, `.md` adalah **lapisan konten teresolusi** dan dibangun **lebih dulu**; `.docx`, `.pptx`, dan
> `.html` seharusnya diturunkan darinya (FR-09). Pada run ini urutannya terbalik karena aturan itu
> belum ada saat run berjalan. Selisih angka yang muncul akibatnya dicatat di `audit_log.md` §3.8.3.

### Revisi pasca-konversi (4 Nov 2026)
- **Hapus Section H** (Catatan Kepatuhan Reviewer) dari RPP — permintaan guru
- **Ganti semua tag `[src:#]`** dengan kutipan sumber lengkap di RPP dan Slide — permintaan guru
- **Koreksi kapasitas PLTS Cirata** dari "145 MWp" → "145 MWac (192 MWp)" di RPP dan Slide — koreksi faktual
- **Hapus callout "Catatan Kurikulum"** dari RPP
- **Verifikasi:** `grep "[src:"` pada semua slide DSL → 0 hasil; semua 9 slide lulus `slidep lint` (0 diagnostics)

## Catatan kepatuhan
- Semua klaim fakta pada draf merujuk tag `[src:1]`–`[src:9]` dari `source_material_energi.md`.
- Klaim "konteks aktual" merujuk `[src:CA1]`/`[src:CA6]` yang terverifikasi di `konteks_aktual.md`.
- Pernyataan kurikulum merujuk `[src:C4]`/`[src:B5]`/`[src:B3]`/`[src:CP]`. Tag kurikulum **tidak boleh**
  menopang fakta sains (rulebook §0).
- Pada tahap Format Rendering, tag diselesaikan (resolved) ke kutipan sumber lengkap untuk `.docx`,
  `.pptx`, dan `.html` — lihat **Source Resolution Map** di `audit_log.md` §3.7. Draf `.md` di folder
  ini tetap bertag karena berfungsi sebagai lapisan kerja, bukan deliverable guru.
- Draf `01`–`05` di-re-tag ulang 5 November 2026 setelah sebelumnya masih memakai tag kurikulum untuk
  fakta; rinciannya di `audit_log.md` §7.4.
- Grounding R001 tetap terpenuhi: setiap klaim dapat ditelusuri ke sumber asli melalui pemetaan yang didokumentasikan.
- Tidak ada fakta di luar source; tidak ada publish tanpa approval guru.
