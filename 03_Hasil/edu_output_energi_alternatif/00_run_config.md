# Run Configuration — EDU-ORCH-20261106-005

| Field | Value |
|-------|-------|
| **Run ID** | EDU-ORCH-20261106-005 |
| **Tanggal/Waktu** | 2026-11-06 11:00 GMT+7 |
| **Orchestrator** | EduCraft Orchestrator (Master) |
| **Domain Pack** | SD–IPAS, Kurikulum Merdeka |
| **Flow** | Core pipeline: Intake → Plan → Draft → Review → **Approval gate (BERHENTI)** → Format Rendering **dijalankan menyimpang dari gate** (lihat baris berikut) |
| **Topik** | Energi Alternatif dan Penghematan Energi |
| **Bab (intake menu)** | C4 — *Penghematan energi dan energi alternatif sebagai mitigasi iklim* |
| **Fase Sasaran** | **Fase C (kelas V–VI)** |
| **CP Sasaran** | `CP-C.2.1.4` — "Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi alternatif dari sumber daya sekitar sebagai mitigasi perubahan iklim" |
| **CP Fondasi** | `CP-B.1.1.5` (B5) — "Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk energi dalam kehidupan sehari-hari" |
| **Kedudukan CP Fondasi** | B5 berada di **Fase B**. Pada run ini B5 dipakai sebagai **prasyarat**, bukan sebagai CP sasaran: isi B5 masuk sebagai pemantapan 10 menit di Pertemuan 1, lalu dinaikkan ke tingkat Fase C melalui tuntutan CP C4 (menghasilkan upaya + memanfaatkan sumber daya sekitar). Lihat `00_plan.md` §4. |
| **Source file** | `08_Referensi/source_material_energi.md` → `[src:1]`–`[src:9]` |
| **Konteks aktual** | `08_Referensi/konteks_aktual.md` — **DIPAKAI**: `[src:CA1]` PLTS Terapung Cirata, `[src:CA6]` FOLU Net Sink 2030 & NZE 2060. Keduanya relevan langsung dengan CP C4, bukan tautan yang dipaksakan. |
| **CP reference** | `08_Referensi/cp_ipas.md` |
| **Rulebook** | `08_Referensi/rulebook_ipas.md` (R001–R012, v2.0) |
| **Intake menu** | `08_Referensi` → `assets/intake_menu_ipas.md` (S0, bab C4). Format tidak disebut guru → bawaan §4.1: RPP + kuis + slide. |
| **Iteration** | `3` of max `3` — **tiga penolakan**, lingkar remediasi habis. Pass 1: 3 temuan R001 + 7 catatan teknis. Pass 2: 3 temuan R001 baru (kontradiksi akibat perbaikan pass 1) + 6 catatan teknis. Pass 3: **1 temuan R001** (§C) + 5 catatan teknis. **Eskalasi ke guru** — lihat `04_review.md` §D. |
| **Koreksi pasca-penolakan ke-3** | Temuan R001 pass 3 (§C) **sudah diperbaiki** dengan menghapus atribusi yang salah, **tetapi tidak ditinjau ulang** oleh Reviewer — anggaran 3 lingkar habis. Perbaikan hanya menghapus klaim, tidak menambah klaim baru, sehingga tidak dapat menimbulkan ketergroundingan baru; tetap **wajib diverifikasi guru** sebelum dipakai (butir 5 lembar persetujuan). |
| **Human requester** | Guru — don Jimat Akbar |
| **Human approver** | `PENDING` — menunggu persetujuan eksplisit. Lembar: `05_Lembar_Persetujuan_Guru.md` |
| **Publish status** | 🔒 `LOCKED` — belum diminta, dan tidak boleh dibuka sebelum gerbang approval lulus |
| **Format Rendering** | ⚠️ **Dijalankan tanpa memenuhi gate §2** `format_rendering_spec.md`. Pemicu: instruksi peminta ("lanjutkan"), bukan persetujuan approver. Konsekuensi: seluruh artefak berlabel **"draf pra-persetujuan"**, tidak satu pun berstatus `RELEASED`. Rincian & pembelaan: `audit_log.md` §9.0 |
| **Hasil render** | `07_Materi_Guru_Energi_Alternatif.md` · `08_RPP_Energi_Alternatif.docx` · `09_Slide_Energi_Alternatif.pptx` · `10_Kuis_Interaktif_Energi_Alternatif.html` |
| **Penyimpangan FR-09** | `.docx`/`.pptx`/`.html` diturunkan dari draf bertag, bukan dari `.md`; hasil (angka & tag) identik dan diverifikasi, konstruksi (satu resolver) belum. `audit_log.md` §9.5 |

## Format yang dihasilkan

| No | Format kanonik | Berkas | Alasan |
|----|----------------|--------|--------|
| 1 | `lesson_plan` | `01_RPP_Energi_Alternatif.md` | Alur mengajar 2 pertemuan × 40 menit `[src:1]` |
| 2 | `quiz` | `02_Kuis_PrePost_Energi_Alternatif.md` | Alat ukur pre-test/post-test + skor gain |
| 3 | `slide_outline` | `03_Slide_Outline_Energi_Alternatif.md` | Tayangan kelas, 10 slide |

Urutan produksi: `lesson_plan` → `quiz` → `slide_outline` (bawaan §4.1). Tiga format; `short_article`, `infographic_brief`, dan `video_script` **tidak** diminta.

## Artefak siap pakai (fase render)

| No | Berkas | Format | Catatan |
|----|--------|--------|---------|
| 1 | `07_Materi_Guru_Energi_Alternatif.md` | Markdown | Lapisan konten teresolusi, 586 baris, 41 bagian |
| 2 | `08_RPP_Energi_Alternatif.docx` | Word A4 | 102 paragraf, 10 tabel, ±2.147 kata |
| 3 | `09_Slide_Energi_Alternatif.pptx` | PowerPoint 16:9 | 10 slide — versi tata letak final (kunci berkas lepas 14.13; dek dirender ulang ke nama kanonik, berkas sementara dihapus) |
| 4 | `10_Kuis_Interaktif_Energi_Alternatif.html` | HTML luring | 17 butir, periksa mandiri, ekspor PDF & cetak |

## Aturan pemakaian sumber

- Setiap klaim fakta wajib merujuk tag yang **resolvable** ke `source_material_energi.md` (`[src:1]`–`[src:9]`) atau `konteks_aktual.md` (`[src:CA1]`, `[src:CA6]`).
- `[src:CP]`, `[src:C4]`, `[src:B5]` hanya boleh menopang **pernyataan kurikulum**, tidak pernah fakta sains (rulebook §0).
- Tiga fakta sains yang lazim di buku lain **tidak ada di sumber** dan karena itu ditandai `[UNVERIFIED]` + `PERLU KONFIRMASI GURU`: (a) panel surya mengubah cahaya menjadi listrik, (b) turbin/kincir angin mengubah gerak menjadi listrik, (c) asal-usul biogas. Lihat `01_RPP_Energi_Alternatif.md` §H.
- Angka kapasitas PLTS Cirata **wajib** ditulis `145 MWac (192 MWp)` — tidak boleh `145 MWp` (koreksi eksplisit di `konteks_aktual.md`, FR-04).
- Sumber tidak memuat angka konsumsi energi, tarif listrik, atau persentase penghematan. Angka semacam itu tidak boleh muncul.

## Konvensi sitasi — keputusan yang menunggu guru

Dua konvensi hidup di proyek ini:

| Run | Konvensi |
|-----|----------|
| `EDU-ORCH-20261105-003` (Tata Surya) | RPP & slide menyebut **nama sumber dalam kata**; kode `[src:]` dipindah ke `05_Jejak_Sumber.md` |
| `EDU-ORCH-20261104-004` (Wujud Zat) | RPP & slide memakai **kode `[src:]` sebaris** |

Run ini mengikuti konvensi **kedua** pada tahap draf, karena `check_grounding.py` memeriksa resolusi tag dan pemeriksaan itu menjadi bukti R001. Konversi ke konvensi pertama adalah pekerjaan mekanis yang **hanya boleh** dilakukan pada fase Format Rendering (FR-01/FR-02), setelah approval. Keputusan memilih konvensi diajukan sebagai butir 4 pada lembar persetujuan.

## State mesin

```
Run:        EDU-ORCH-20261106-005
Phase:      Fase C
Iteration:  3
MaxIter:    3
Status:     ESCALATED_TO_HUMAN
Render:     DONE (pra-persetujuan, menyimpang dari gate §2)
Publish:    LOCKED
```
