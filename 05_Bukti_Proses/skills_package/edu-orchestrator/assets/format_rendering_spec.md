# SPESIFIKASI FORMAT RENDERING — EduCraft Stage 6

> **Versi:** 1.1 · **Tanggal:** 5 November 2026 · **Status:** kanonik
> **Pemilik:** `edu-orchestrator` (fase pasca-approval)
> **Rujukan implementasi:** run `EDU-ORCH-20261026-001`
>
> **Perubahan v1.1 (5 Nov 2026):** fase ini dinyatakan **wajib**, bukan opsional; set deliverable
> minimum menjadi empat format termasuk `.md`; `.md` ditetapkan sebagai **lapisan konten teresolusi**
> yang menjadi sumber ketiga format lain (FR-09).

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

Fase ini **wajib** dijalankan pada setiap run yang berstatus terbit. Set minimum yang harus ada
sebelum sebuah run boleh disebut `RELEASED` adalah **empat artefak** di bawah. Run yang hanya
menghasilkan draf bertag belum selesai — draf adalah bahan, bukan materi siap pakai.

| # | Artefak | Format kanonik asal | Alat | Status |
|---|---------|---------------------|------|--------|
| 1 | `Materi_Guru_<topik>.md` | gabungan seluruh draf | `tools/build_materi_md.py` | **WAJIB** |
| 2 | `RPP_<topik>.docx` | `lesson_plan` | `workbuddy-docx` (HTML terstruktur → html-to-doc) | **WAJIB** |
| 3 | `Slide_<topik>.pptx` | `slide_outline` | `workbuddy-pptx` (`slidep create` → `upsert-dsl` → `lint`) | **WAJIB** |
| 4 | `quiz_<topik>.html` | `quiz` | enhancement inline (tanpa build step) | **WAJIB** |
| 5 | `Artikel_<topik>.docx` | `short_article` | mengikuti `lesson_plan` | opsional |
| 6 | infografis `.png` / `.html` | `infographic_brief` | — | opsional |
| 7 | skrip video `.md` | `video_script` | — | opsional |

**Urutan produksi wajib: 1 → 2 → 3 → 4.** Artefak 1 dibangun lebih dulu karena ia lapisan
konten teresolusi (FR-09); artefak 2–4 diturunkan darinya, bukan dari draf bertag.

**Satu-satunya alasan sah untuk tidak merender salah satu dari 1–4:** guru menyatakan secara
eksplisit bahwa format itu tidak dibutuhkan. Penolakan itu dicatat di `00_run_config.md` dengan
nama, tanggal, dan kalimatnya. Tidak ada jalan lain — "tidak diminta" bukan alasan, karena
keempatnya adalah bawaan.


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

**FR-09 — Satu lapisan konten teresolusi, banyak format.**
`Materi_Guru_<topik>.md` dibangun lebih dulu dan menjadi **satu-satunya sumber** bagi `.docx`,
`.pptx`, dan `.html`. Larangan:
1. `.docx`, `.pptx`, dan `.html` **tidak boleh** diturunkan langsung dari draf bertag. Draf bertag
   adalah bahan; resolusi tag terjadi sekali, di lapisan `.md`.
2. Koreksi pasca-render yang disetujui guru ditulis ke `koreksi_format_rendering.md` dalam bentuk
   `SEBELUM => SESUDAH`, lalu diterapkan oleh alat — bukan disunting per artefak.
3. Alat **gagal dengan kode 1** bila masih ada tag internal, bila ada bagian catatan internal yang
   lolos, atau bila ada koreksi yang belum diterapkan. Kegagalan alat berarti run tidak boleh lanjut.

**Kenapa aturan ini ada.** Sampai v1.0, tag diselesaikan tiga kali secara terpisah (docx lewat HTML,
pptx lewat DSL, kuis lewat suntingan JavaScript). Tiga resolusi independen berarti tiga peluang
berbeda untuk salah. Buktinya ada di run `-001`: koreksi `145 MWp → 145 MWac (192 MWp)` masuk ke
`.docx` dan `.pptx`, tetapi draf `.md` tetap memuat angka lama. Selama `.md` bukan deliverable,
selisih itu tidak terlihat; begitu `.md` diserahkan ke guru, ia menjadi kontradiksi terbuka di
tangan pengguna. FR-09 menutupnya dengan konstruksi, bukan dengan disiplin.

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
| 11 | Empat artefak wajib ada | `Materi_Guru_*.md`, `RPP_*.docx`, `Slide_*.pptx`, `quiz_*.html` |
| 12 | `.md` bebas catatan internal | `grep -i "catatan\|R0[0-9][0-9]\|assets/\|Reviewer"` → 0 |
| 13 | `.md` dibangun oleh alat, bukan tangan | `tools/build_materi_md.py` keluar dengan kode `0` |

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
- Sejak v1.1, butir 1–3 pada §5 (bebas tag, bebas catatan internal, dibangun oleh alat) **ditegakkan
  mesin**: `tools/build_materi_md.py` menolak menulis keluaran dan keluar dengan kode 1 bila gagal.
  Butir 4–13 masih bergantung pada pemeriksaan manual yang tercatat di tabel verifikasi audit log.
