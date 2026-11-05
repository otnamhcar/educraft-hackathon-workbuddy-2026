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
| **Source file** | `source_material_tata_surya.md` → `[src:TS1]`–`[src:TS11]` |
| **CP reference** | `assets/cp_ipas.md` |
| **Rulebook** | `assets/rulebook_ipas.md` (R001–R012, v2.0) |
| **Intake menu** | `assets/intake_menu_ipas.md` (S0, bab C5). Bawaan format: RPP + kuis + slide (minimal 2). |
| **Catatan fase** | Guru awalnya meminta Fase B (kelas III–IV). Topik tata surya secara kanonik berada di Fase C (CP-C.2.1.5), bukan Fase B. Orchestrator mengoreksi ke Fase C sesuai R004 (curriculum alignment). |
| **Iteration** | `1` of max `3` — tidak ada rejection pada pass ini. |
| **Human requester** | Guru — don Jimat Akbar |
| **Human approver** | PENDING (guru/SME) — belum ada konfirmasi |
| **Publish status** | PENDING — menunggu approval eksplisit (Hard Rule: no publish without approval) |

## Format yang dihasilkan

| No | File | Format (kanonik) |
|----|------|------------------|
| 1 | `01_RPP_Tata_Surya.md` | `lesson_plan` |
| 2 | `02_Kuis_PrePost_Tata_Surya.md` | `quiz` |
| 3 | `03_Slide_Outline_Tata_Surya.md` | `slide_outline` |

> Bawaan format (§4.1 intake menu): RPP + kuis + slide (3 format). Urutan produksi: lesson_plan → quiz → slide_outline.

## Catatan kepatuhan

- Semua klaim fakta merujuk tag `[src:TS#]` yang resolvable ke `source_material_tata_surya.md`.
- Dua entri (`[src:TS10]`, `[src:TS11]`) adalah **turunan tim**, bukan kutipan; keduanya menunggu
  validasi guru.
- Tidak ada klaim konteks aktual — keputusan sadar, bukan kelalaian (R011 `N/A` beralasan).
- Tidak ada publish tanpa approval guru; gerbang masih PENDING.
- RPP sebelumnya dibuat di luar pipeline (di `output/rpp-tata-surya/`) tanpa tag grounding.
  RPP ini (`01_RPP_Tata_Surya.md`) adalah versi yang melalui pipeline dan tergrounding.
