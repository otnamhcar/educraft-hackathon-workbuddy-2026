# Run Configuration — EDU-ORCH-20261105-003

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261105-003 |
| **Tanggal/Waktu** | 2026-11-05 07:36 GMT+7 |
| **Orchestrator** | EduCraft Orchestrator (Master) |
| **Domain Pack** | SD–IPAS, Kurikulum Merdeka (Fase B & C) |
| **Flow** | Core pipeline: Intake → Plan → Draft → Review → Approve → Publish → Format Rendering |
| **Topik** | Sistem Tata Surya, serta Kaitannya dengan Rotasi dan Revolusi Bumi |
| **Fase Sasaran** | Fase C (kelas V–VI) — topik berada di CP Fase C (C5) |
| **CP Sasaran** | `CP-C.2.1.5`: "Menjelaskan sistem tata surya, serta kaitannya dengan rotasi dan revolusi bumi" |
| **CP Fondasi** | — (tidak ada; topik khusus Fase C) |
| **Konteks Aktual** | **Tidak digunakan.** Tidak ada entri `[src:CA#]` yang relevan; tautan tidak dipaksakan (R011). |
| **Source file** | `source_material_tata_surya.md` → `[src:TS1]`–`[src:TS12]` |
| **CP reference** | `assets/cp_ipas.md` |
| **Rulebook** | `assets/rulebook_ipas.md` (R001–R012, v2.0) |
| **Intake menu** | `assets/intake_menu_ipas.md` (S0, bab C5). Bawaan format: RPP + kuis + slide (minimal 2). |
| **Catatan fase** | Guru awalnya meminta Fase B (kelas III–IV). Topik tata surya secara kanonik berada di Fase C (CP-C.2.1.5), bukan Fase B. Orchestrator mengoreksi ke Fase C sesuai R004 (curriculum alignment). |
| **Iteration** | `1` of max `3` — tidak ada rejection pada pass ini. |
| **Human requester** | Guru — don Jimat Akbar |
| **Human approver** | ✅ **APPROVED** — don Jimat Akbar, 2026-11-05 15:01 GMT+7 (lihat `04_Lembar_Persetujuan_Guru.md`) |
| **Publish status** | `APPROVED_FOR_USE` — materi boleh dipakai di kelas; **publikasi/distribusi tetap LOCKED** sampai permintaan eksplisit |

## Format yang dihasilkan

| No | File | Format (kanonik) |
|----|------|------------------|
| 1 | `01_RPP_Tata_Surya.md` | `lesson_plan` |
| 2 | `02_Kuis_PrePost_Tata_Surya.md` | `quiz` |
| 3 | `03_Slide_Outline_Tata_Surya.md` | `slide_outline` |

> Bawaan format (§4.1 intake menu): RPP + kuis + slide (3 format). Urutan produksi: lesson_plan → quiz → slide_outline.

## Catatan kepatuhan

- Semua klaim fakta merujuk tag `[src:TS#]` yang resolvable ke `source_material_tata_surya.md`.
- Dua entri (`[src:TS10]`, `[src:TS11]`) adalah **turunan tim** dan **telah disetujui guru** pada
  5 November 2026 — sah dipakai dan diujikan.
- `[src:TS12]` adalah **referensi tambahan dari NASA** (bukan Panduan IPAS), ditambahkan 5 November
  2026 atas keputusan guru untuk mengisi kekosongan ciri-ciri planet. Provenance dinyatakan di source
  material.
- Koreksi fase B → C **diterima guru** pada 5 November 2026.
- Butir kuis 13 **diperbaiki** pada 5 November 2026 (kunci lama keliru secara fisika).
- Kuis 5 November 2026: 3 butir pre-test (3, 4, 5) diujikan ulang sebagai post-test 16–18 untuk
  mengukur gain secara langsung.
- Rubrik 5 November 2026: skala 4/3/2/1 tanpa deskriptor diganti rubrik 4 aspek × 3 tingkat;
  ditandai eksplisit sebagai usulan rancangan guru, bukan kutipan sumber. **Disetujui guru 5 Nov 2026
  16:54** (lembar persetujuan §2.5) setelah revisi 16:51 pada aspek 1 dan aturan aspek belum teramati.
- **Konvensi penulisan sumber (5 Nov 2026):** RPP dan slide menyebut nama sumber dalam kata
  ("Panduan IPAS, hlm. 45–47", "NASA"), tanpa kode `[src:]`. Kuis tidak menampilkan sumber sama sekali.
  Pemetaan mesin dipindahkan ke `05_Jejak_Sumber.md`. Dijaga oleh `tools/check_sitasi.py` (langkah 7
  pada `doctor.py`).
- Tidak ada klaim konteks aktual — keputusan sadar, bukan kelalaian (R011 `N/A` beralasan).
- Gerbang approval: ✅ LULUS. Publikasi belum diminta dan tetap terkunci.
- RPP sebelumnya dibuat di luar pipeline (di `output/rpp-tata-surya/`) tanpa tag grounding.
  RPP ini (`01_RPP_Tata_Surya.md`) adalah versi yang melalui pipeline dan tergrounding.
