# Run Configuration — EDU-ORCH-20261030-002

> This file was written on **31 October 2026**, after the run. The run itself was executed on
> 30 October 2026 and is recorded in `audit_log.md`. It is reconstructed **only** from that log —
> no field below is inferred. Fields that the log does not support are marked `TIDAK DICATAT`
> rather than filled in.

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261030-002 |
| **Tanggal/Waktu** | 2026-10-30 16:44–16:55 GMT+7 |
| **Orchestrator** | EduCraft Orchestrator (Master) |
| **Domain Pack** | SD–IPAS, Kurikulum Merdeka (Fase B & C) |
| **Flow** | Core pipeline: Plan → Draft → Review → Approve, dilanjutkan fase aset (infografis, video, kuis) |
| **Topik** | Perubahan Wujud Zat |
| **Fase Sasaran** | Fase C (kelas V–VI) — **pemantapan lintas fase** (topik berada di CP Fase B) |
| **CP Sasaran** | `CP-B.1.1.4` (konten) + `CP-C.2.2` (kedalaman keterampilan proses) |
| **CP Fondasi** | — (tidak ada; topik diambil dari Fase B dan dinaikkan kedalamannya) |
| **Konteks Aktual** | **Tidak digunakan.** Tidak ada entri `[src:CA#]` yang relevan; tautan tidak dipaksakan (R011). |
| **Source file** | `source_material_wujud_zat.md` → `[src:W1]`–`[src:W11]` *(lihat catatan koreksi di bawah)* |
| **CP reference** | `assets/cp_ipas.md` |
| **Rulebook** | `assets/rulebook_ipas.md` (R001–R012, v2.0) |
| **Iteration** | `1` of max `3` — **one rejection** recorded (Reviewer pass 1, 5 temuan Major R001); draft v2 approved pada pass 2. *Review passes: 2.* |
| **Human requester** | Guru — don Jimat Akbar |
| **Human approver** | ✅ **don Jimat Akbar (Guru)** — 2026-10-30 17:19 GMT+7 |
| **Publish status** | 🔓 **DIBUKA** untuk distribusi terbatas (paket cetak siswa & guru) setelah persetujuan eksplisit |

## Format yang dihasilkan

| No | File | Format (kanonik) | Nama di `00_plan.md` |
|----|------|------------------|----------------------|
| 1 | `01_artikel.md` | `short_article` | `short_article` |
| 2 | `02_infographic_brief.md` → `03_infografis_wujud_zat.png` | `infographic_brief` | `infographic` |
| 3 | `03_video_storyboard.md` → `07_video_animatik.html` | `video_script` | `short_video` |
| 4 | `04_kuis_prepost.md` → `06_quiz_interaktif.html` | `quiz` | `quiz` |

> Kolom terakhir mencatat nama yang dipakai Planner pada 30 Oktober. Sejak 31 Oktober, daftar
> kanonik ada di `edu-planner/SKILL.md` (enam format). Pemetaan di atas disimpan apa adanya —
> `00_plan.md` tidak diubah.

## Catatan koreksi sumber (31 Oktober 2026)

Run ini awalnya menggantungkan seluruh klaim fakta pada `[src:B4]`, yang menunjuk **nama topik** di
`cp_ipas.md` — bukan sumber fakta. Koreksi penuh ada di `audit_log.md` §7 dan
`11_Memo_Koreksi_Tag_2026-10-31.md`.

| Item | Sebelum | Sesudah |
|------|---------|---------|
| Source fakta | `source_material_ipas.md` → `[src:B4]` | `source_material_wujud_zat.md` → `[src:W1]`–`[src:W11]` |
| Tag fakta | 84 tag `[src:B4]` | `[src:W1]`–`[src:W9]` (kutipan), `[src:W10]`–`[src:W11]` (turunan tim) |
| Verifikasi | — | `grounding_report.md`: 115 tag, 0 dangling, 0 pelanggaran kelas → **PASS** |

**Isi materi tidak berubah.** Tidak ada kalimat yang ditambah, dihapus, atau diperhalus.

## Catatan kepatuhan

- Semua klaim fakta merujuk tag `[src:W#]` yang resolvable ke `source_material_wujud_zat.md`.
- Dua entri (`[src:W10]`, `[src:W11]`) adalah **turunan tim**, bukan kutipan; keduanya menunggu
  validasi guru.
- Tidak ada klaim konteks aktual — keputusan sadar, bukan kelalaian.
- Tidak ada publish tanpa approval guru; gerbang dibuka hanya setelah persetujuan 17:19 GMT+7.
