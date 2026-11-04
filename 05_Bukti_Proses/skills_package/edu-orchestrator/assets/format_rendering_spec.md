# SPESIFIKASI FORMAT RENDERING — EduCraft Stage 6

> **Versi:** 1.0 · **Tanggal:** 4 November 2026 · **Status:** kanonik
> **Pemilik:** `edu-orchestrator` (fase pasca-approval)
> **Rujukan implementasi:** run `EDU-ORCH-20261026-001`

## 1. Tujuan

Mengubah draf Markdown yang sudah **APPROVE** menjadi artefak siap pakai di kelas
(`.docx`, `.pptx`, `.html` interaktif) dengan hasil yang **konsisten antar-run**.

Fase ini **tidak menggantikan** pipeline inti (Plan → Draft → Review). Fase ini berjalan
**setelah** persetujuan manusia dan tidak punya wewenang mengubah isi yang sudah disetujui —
hanya mengubah bentuk, menyelesaikan tag internal, dan menyiapkan sarana ekspor/cetak.

## 2. Prasyarat (gate — wajib)

Jangan mulai render bila salah satu belum terpenuhi:

1. `00_run_config.md` mencatat `Human approver` **bukan** `PENDING`.
2. `Publish status` = disetujui/diterbitkan.
3. Reviewer memberi **APPROVE** untuk setiap format yang akan dirender.
4. Tidak ada temuan `REJECT` yang belum tuntas.

Bila gate belum terpenuhi → **BERHENTI** dan eskalasi ke manusia. Jangan render "sementara".

## 3. Peta deliverable

| Format kanonik | Artefak | Alat |
|----------------|---------|------|
| `lesson_plan` | `.docx` | `workbuddy-docx` (HTML terstruktur → html-to-doc) |
| `slide_outline` | `.pptx` | `workbuddy-pptx` (`slidep create` → `upsert-dsl` → `lint`) |
| `quiz` | `.html` interaktif mandiri | enhancement inline (tanpa build step) |
| `short_article` | `.docx` / `.md` | opsional, mengikuti `lesson_plan` |
| `infographic_brief` | `.png` / `.html` | opsional |
| `video_script` | `.md` | opsional |

Satu run boleh merender subset apa pun. Format yang tidak diminta tidak menghasilkan artefak kosong.

## 4. Aturan keras (FR-01 … FR-08)

**FR-01 — Larangan tag internal pada artefak.**
Artefak yang dibaca guru atau siswa **tidak boleh** memuat `[src:#]`, `[src:CP]`, `[src:CA#]`,
`[UNVERIFIED]`, atau `PERLU KONFIRMASI GURU`. Tag adalah penanda internal pipeline, bukan
informasi bagi pembaca. Wajib diverifikasi dengan `grep`.

**FR-02 — Source Resolution Map wajib.**
Setiap kali tag internal dihapus, `audit_log.md` **wajib** memuat peta `tag → kutipan sumber`
beserta kelas tag (Fakta / Kurikulum / Konteks aktual). Tanpa peta ini, penghapusan tag
dianggap melanggar R001 (grounding) karena jejak penelusuran hilang.

**FR-03 — Tanpa dependensi eksternal untuk fungsi inti.**
HTML artefak harus berfungsi **offline**. Dilarang memuat library dari CDN untuk fungsi inti
(ekspor, cetak, penilaian). Bila sebuah kemampuan memerlukan library, tanam implementasinya
inline atau gunakan API bawaan browser.

**FR-04 — Konsistensi faktual lintas artefak.**
Satu angka, satuan, atau koreksi harus **identik** di seluruh artefak dalam satu run. Bila sumber
menyatakan `145 MWac (192 MWp)`, maka RPP, slide, kuis, dan laporan ekspor memakai bentuk yang
sama. Dilarang menormalkan satuan tanpa dasar di sumber.

**FR-05 — Kontrak interaksi kuis (baku).**
1. **Keadaan awal:** hanya tombol **Periksa Jawaban**. Tidak ada tombol ekspor/cetak.
2. **Setelah pemeriksaan:** muncul **Ulangi Kuis**, **Export PDF**, **Cetak / Save PDF**.
3. **Isi ekspor & cetak wajib memuat:** nomor soal, tipe (PG/Uraian), teks soal,
   **jawaban siswa**, dan **kunci jawaban**.
4. **Pewarnaan jawaban siswa:** hijau = benar, merah = salah, abu-abu = tidak dijawab.
5. **Cetak:** `print-color-adjust: exact` agar warna ikut tercetak; laporan dirender ke
   kontainer khusus yang hanya tampil pada `@media print`.
6. **Ctrl+P langsung** harus tetap menghasilkan laporan (handler `beforeprint`).
7. **Tab aktif menentukan isi laporan** — jangan memakai state usang.

**FR-06 — Catatan internal tidak boleh tampil.**
Bagian seperti "Catatan Kepatuhan Reviewer" atau "Catatan Kurikulum" **tidak** masuk ke artefak
guru/siswa. Catatan itu tetap disimpan di `audit_log.md`.

**FR-07 — Angka & satuan mengikuti sumber.**
Jangan mengarang, membulatkan, atau menukar satuan. Bila ragu, tandai untuk konfirmasi guru
sebelum render — jangan diam-diam menormalkan.

**FR-08 — Verifikasi wajib lulus sebelum serah terima.**
Artefak yang gagal checklist §5 **tidak boleh** diserahkan. Perbaiki lalu ulangi.

## 5. Checklist verifikasi (wajib dijalankan)

| # | Pemeriksaan | Cara |
|---|-------------|------|
| 1 | Tidak ada tag internal | `grep -c "\[src:" <file>` → `0` |
| 2 | DOCX terbuka & bagian lengkap | buka file; pastikan tidak ada bagian catatan internal |
| 3 | PPTX lolos lint | `slidep lint <pptx> --dsl-file <slide> --page-index N` → 0 diagnostics |
| 4 | HTML bebas CDN | `grep -i "cdn\|jsdelivr\|unpkg\|cdnjs" <html>` → tidak ada pada fungsi inti |
| 5 | Kuis: tombol awal | hanya `Periksa Jawaban` |
| 6 | Kuis: tombol setelah periksa | `Ulangi Kuis`, `Export PDF`, `Cetak / Save PDF` |
| 7 | Ekspor menghasilkan PDF valid | unduhan ada, header `%PDF-1.4`, xref konsisten |
| 8 | Cetak menghasilkan laporan | render `@media print` memuat soal + jawaban + highlight |
| 9 | Konsistensi angka lintas artefak | bandingkan angka kunci di DOCX, PPTX, HTML |
| 10 | Audit log terisi | ada entri fase render + Source Resolution Map |

## 6. Penanganan kegagalan

- **Dependensi eksternal tidak tersedia** → ganti dengan implementasi inline; jangan
  menyerahkan tombol yang tidak bereaksi.
- **Verifikasi gagal** → perbaiki dan ulangi seluruh checklist; jangan sebagian.
- **Konflik angka antar artefak** → sumber menang; perbaiki semua artefak, catat di audit log.
- **Gate approval belum terpenuhi** → berhenti, eskalasi; jangan render.

## 7. Format pencatatan audit

Setiap fase render dicatat di `audit_log.md` dengan struktur:

```
### 3.x FORMAT RENDERING (Pasca-Approval) — <tanggal>
- Peran, pemicu (approval), tujuan
#### 3.x.1 Konversi <format> → <artefak>
#### 3.x.2 ...
#### 3.x.N Revisi pasca-konversi
#### 3.x.M Source Resolution Map
Tabel: Tag | Kelas | Resolusi Sumber
+ tabel verifikasi (uji | hasil)
```

## 8. Batas yang diakui

- Browser tidak dapat menulis langsung ke folder tertentu; unduhan masuk ke folder
  Downloads pengguna. Ini keterbatasan platform, bukan cacat artefak.
- Rendering bergantung pada skill konversi (`workbuddy-docx`, `workbuddy-pptx`). Bila skill
  tidak tersedia, fase ini tidak dapat dijalankan dan harus dieskalasi.
- Spesifikasi ini ditegakkan lewat prompt + checklist, bukan mesin verifikasi otomatis,
  kecuali pemeriksaan `grep`, `lint`, dan uji ekspor yang bersifat deterministik.
