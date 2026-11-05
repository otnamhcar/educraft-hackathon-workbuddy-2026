# Run Configuration — EDU-ORCH-20261104-004

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261104-004 |
| **ID sebelumnya** | ditulis `…-003` saat run dibuka 4 Nov; **diubah 5 Nov 2026** karena nomor `-003` pada tanggal itu bersinggungan dengan run Tata Surya `EDU-ORCH-20261105-003`. Lihat §Riwayat koreksi di bawah |
| **Tanggal/Waktu** | 2026-11-04 13:52 GMT+7 (dibuka) |
| **Orchestrator** | EduCraft Orchestrator (Master) |
| **Domain Pack** | SD–IPAS, Kurikulum Merdeka |
| **Flow** | Core pipeline: Plan → Draft → Review → **Approval gate (BERHENTI)** |
| **Topik** | Perubahan Wujud Zat |
| **Fase Sasaran** | **Fase C (kelas V–VI)** |
| **CP Sasaran (konten)** | `CP-B.1.1.4` — "Menyimpulkan proses perubahan wujud zat" |
| **CP Sasaran (kedalaman proses)** | `[src:CP]` — keterampilan proses Fase C. **Bukan** `CP-C.2.2`: butir 2 Fase C berisi hubungan biotik–abiotik, bukan keterampilan proses, sehingga kode itu salah resolusi untuk maksud ini. |
| **Status kurikulum topik** | ⚠️ **Topik berada di Fase B, bukan Fase C.** Fase C tidak memuat butir perubahan wujud zat (lihat `cp_ipas.md` §FASE C 2.1). R004 mewajibkan penandaan `PERLU KONFIRMASI GURU`. |
| **Source file** | `03_Hasil/referensi/source_material_wujud_zat.md` → `[src:W1]`–`[src:W11]` |
| **Konteks aktual** | `03_Hasil/referensi/konteks_aktual.md` — **tidak dipakai.** Tidak ada entri `[src:CA#]` yang relevan dengan perubahan wujud zat (hanya CA1 PLTS Cirata, CA6 FOLU/NZE). Tautan tidak dipaksakan → R011 dinilai `N/A` beralasan. |
| **CP reference** | `03_Hasil/referensi/cp_ipas.md` |
| **Rulebook** | `03_Hasil/referensi/rulebook_ipas.md` (R001–R012, v2.0) |
| **Iteration** | `1` of max `3` — **satu penolakan** (Review pass 1: 6 temuan — 3 Major R001, 3 Minor R009/R010). Pass 2: **APPROVE**. *Review passes: 2.* |
| **Human requester** | Wawan |
| **Human approver** | ⏳ **BELUM ADA** — menunggu persetujuan eksplisit |
| **Publish status** | 🔒 **TERTUTUP** — dilarang publish pada run ini |

## Format yang diminta

| No | Format kanonik | Alasan pemilihan |
|----|----------------|------------------|
| 1 | `lesson_plan` | Paket mengajar utuh untuk guru Fase C |
| 2 | `quiz` | Asesmen tertulis sesuai `[src:W8]` |
| 3 | `short_article` | Bahan bacaan murid, latihan menyimpulkan (`[src:W9]`) |
| 4 | `slide_outline` | Kerangka tayangan untuk pembelajaran di kelas |
| 5 | `infographic_brief` | Ringkasan visual enam proses (`[src:W2]`) |

Lima format diminta; `video_script` **tidak** diminta pada run ini.

## Aturan pemakaian sumber

- Setiap klaim fakta wajib merujuk `[src:W#]` yang **resolvable** ke `source_material_wujud_zat.md`.
- `[src:W10]` dan `[src:W11]` adalah **TURUNAN TIM**, bukan kutipan. Boleh dipakai hanya bila
  ditandai eksplisit, dan **tidak boleh menopang butir ujian** tanpa persetujuan guru.
- `[src:CP]` / `[src:B4]` / `[src:C2]` hanya boleh menopang pernyataan kurikulum, **tidak pernah**
  fakta sains (rulebook §0).
- Sumber tidak memuat angka suhu apa pun. Angka suhu = `[UNVERIFIED]` + `PERLU KONFIRMASI GURU`.
- Sumber tidak memuat ciri-ciri wujud (bentuk tetap, mengikuti wadah, memenuhi ruang). Klaim semacam
  itu dilarang kecuali ditandai turunan.

## State mesin

```
Run:        EDU-ORCH-20261104-004
Phase:      Fase C
Iteration:  1
MaxIter:    3
Status:     AWAITING_APPROVAL
Publish:    LOCKED
```

## Riwayat koreksi berkas ini

| Tanggal | Perubahan | Alasan |
|---------|-----------|--------|
| 5 Nov 2026 | Run ID `EDU-ORCH-20261104-003` → `EDU-ORCH-20261104-004` | Dua run berbeda memakai akhiran nomor `-003`. Run Tata Surya (`EDU-ORCH-20261105-003`) sudah dirujuk enam dokumen submission, sehingga run inilah yang pindah nomor — bukan sebaliknya. Jejak audit, tag, dan isi draf tidak berubah; hanya penomoran run |
| 5 Nov 2026 | `grounding_report.md` dibuat ulang (PASS, 176 tag) | Laporan pertama mencatat 9 tag `[src:CP]` dangling. Penyebabnya bukan draf, tetapi knowledge layer: anchor `## [src:CP]` belum pernah ada, padahal `cp_ipas.md` §1.2 memperkenalkan tag itu sebagai rujukan dokumen CP. Anchor ditambahkan di ketiga salinan `cp_ipas.md`; keenam draf tidak diubah |
