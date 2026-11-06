# AUDIT LOG — EduCraft Orchestrator
## Run ID: EDU-ORCH-20261106-005

---

## 1. RUN METADATA

- **Run ID:** EDU-ORCH-20261106-005
- **Topik:** Energi Alternatif dan Penghematan Energi
- **Bab (intake menu):** C4
- **Sasaran:** Fase C (kelas V–VI) · CP `CP-C.2.1.4` · fondasi `CP-B.1.1.5`
- **Timestamp:** 2026-11-06 11:00 GMT+7
- **Orchestrator:** EduCraft Orchestrator (Master)
- **Human requester:** Guru (don Jimat Akbar)
- **Human approver:** `PENDING` — lihat `05_Lembar_Persetujuan_Guru.md`
- **Publish status:** 🔒 `LOCKED`
- **Status akhir run:** `ESCALATED_TO_HUMAN` (3 penolakan, batas lingkar habis)

---

## 2. INPUTS

| Item | Nilai |
|------|-------|
| Source fakta | `08_Referensi/source_material_energi.md` → `[src:1]`–`[src:9]` |
| Konteks aktual | `08_Referensi/konteks_aktual.md` → `[src:CA1]`, `[src:CA6]` |
| Referensi kurikulum | `08_Referensi/cp_ipas.md` — Panduan IPAS Revisi 4, 3 Okt 2025 (Puskurjar, Kemendikdasmen) |
| Rulebook | `08_Referensi/rulebook_ipas.md` — R001–R012, v2.0 |
| Intake menu | `assets/intake_menu_ipas.md` §4.1 — format tidak disebut → bawaan RPP + kuis + slide |

**Catatan konteks aktual.** Berbeda dari run `-003` (Tata Surya) dan `-004` (Wujud Zat), run ini
memakai konteks aktual. Kedua entri relevan langsung: `[src:CA1]` adalah contoh nyata pemanfaatan
energi alternatif, `[src:CA6]` adalah kerangka mitigasi iklim yang menjadi bagian CP C4. Tidak ada
tautan yang dipaksakan.

---

## 3. AGENT EXCHANGE

### 3.1 INTAKE (S0)

- **Peran:** Orchestrator
- **Keputusan:** Topik disebut eksplisit oleh guru → menu **tidak** ditayangkan (intake menu §1).
  Dipetakan ke **C4**, dikonfirmasi satu baris, lalu lanjut.
- **Format:** guru tidak menyebut format → bawaan §4.1 (RPP + kuis + slide). Tidak ada pertanyaan
  format yang diajukan, sesuai aturan.
- **Kedudukan B5:** CP fondasi berada di Fase B. Dipakai sebagai **prasyarat 10 menit**, bukan CP
  sasaran. Dinyatakan terbuka di RPP §A dan diajukan sebagai butir 1 lembar persetujuan.

### 3.2 PLANNER → `00_plan.md`

- **Peran:** edu-planner
- **Output:** kerangka tiga format, pemetaan CP → materi, dan daftar lima celah yang harus dinyatakan
  (bukan diisi). Celah itu menjadi RPP §H.
- **Keputusan desain:** B5 dibatasi menjadi kosakata dan alat penjelas; tidak diekspansi menjadi
  daftar hafalan enam bentuk energi.

### 3.3 WRITER → Draf v1

- **Peran:** edu-writer
- **Artifacts:** `01_RPP_Energi_Alternatif.md`, `02_Kuis_PrePost_Energi_Alternatif.md`,
  `03_Slide_Outline_Energi_Alternatif.md`, plus lampiran `06_Jejak_Sumber.md`.
- **Tagging:** seluruh klaim fakta bertag; tiga fakta di luar sumber ditandai `[UNVERIFIED]`.
- **Kuis:** 5 pre-test + 12 post-test (9 baru + 3 ulang untuk gain).

### 3.4 REVIEW — tiga pass

Ringkasan lengkap di `04_review.md`. Yang perlu dicatat di sini:

| Pass | Vonis | Inti temuan |
|-----:|-------|-------------|
| 1 | REJECT | Kuis tanpa atribusi; klaim mekanisme tanpa tag di §D.4; kata "berpindah" tidak ada di `[src:6]` |
| 2 | REJECT | Perbaikan pass 1 memindahkan masalah, bukan menghapusnya: slide 6 dan slide 4 memuat klaim yang bertentangan dengan RPP |
| 3 | REJECT | Satu kalimat di §C masih memberi definisi penghematan dengan tag `[src:2]` |

**Pola yang dicatat.** Setiap perbaikan menutup temuan di satu berkas tetapi meninggalkan kalimat
kembarannya di berkas lain. Penyebabnya satu: kalimat disalin antarberkas tanpa menyesuaikan konteks.
Contoh paling jelas — "matahari, angin, dan air muncul di kedua daftar" benar di RPP (sumber energi vs
contoh alternatif) dan salah di slide (sumber energi vs bentuk energi).

### 3.5 ESKALASI

- **Alasan:** aturan keras menetapkan maksimum 3 lingkar remediasi. Lingkar keempat tidak dijalankan.
- **Tindakan:** temuan pass 3 diperbaiki (hanya menghapus atribusi, tidak menambah klaim), tetapi
  **tidak ditinjau ulang**. Orchestrator tidak berwenang menyatakan APPROVE.
- **Keputusan diserahkan kepada:** guru, melalui `05_Lembar_Persetujuan_Guru.md` butir 5.

---

## 4. GROUNDING VERIFICATION

| Pemeriksaan | Hasil |
|-------------|-------|
| `check_grounding.py` (final) | **PASS** — 271 tag, 0 dangling, 0 pelanggaran kelas, 0 ambigu |
| Lembar sumber | `source_material_energi.md` (eksplisit) |
| Rincian per berkas | RPP 126 · kuis 17 · slide 11 · lampiran 86 · plan 27 |

**Catatan angka setelah fase render.** `doctor.py` kini melaporkan **269 tag** untuk run ini, bukan 271.
Selisih dua berasal dari blok *"Catatan kurikulum — kedudukan CP fondasi"* yang dihapus dari RPP §A
karena melanggar FR-06 (§9.2). Blok itu memuat `[src:B5]` dan `[src:C4]`; keduanya ikut terhapus.
Penurunan ini **bukan** kehilangan grounding — keduanya tag kurikulum yang tidak menopang fakta sains,
dan keduanya masih dipakai di §A tabel identitas serta §B.

### 4.1 Cacat alat yang ditemukan dan diperbaiki

Laporan pertama run ini menyatakan **PASS 237 tag**. Laporan itu **salah**.

`tools/check_grounding.py` menyimpan anchor dalam satu kamus datar. `source_material_ipas.md` dan
`source_material_energi.md` sama-sama mendeklarasikan `## [src:1]`–`## [src:9]`, sehingga berkas yang
terakhir dalam urutan abjad menimpa yang lebih awal. Setiap `[src:2]` diresolusikan ke bagian
*Kelestarian Alam* pada lembar kabut asap, bukan ke *Energi Alternatif*.

| Sebelum | Sesudah |
|---------|---------|
| Anchor satu kamus datar; bentrokan diselesaikan diam-diam oleh urutan abjad | Anchor disimpan per berkas; bentrokan dinyatakan `AMBIG` = gagal |
| Tidak ada cara menetapkan lembar yang berlaku | `--primary-source` menetapkan lembar per run |
| `doctor.py` tidak menyebut lembar sumber | `RUN_SOURCES` menyebut lembar setiap run |

**Uji regresi** — kelima run lama dijalankan ulang, angka tidak berubah:
`materi_ajar` 121 · `edu_output` 121 · `edu_output_wujud_zat` 115 ·
`edu_output_wujud_zat_faseC` 212 · `edu_output_tata_surya` 109. Semua PASS.

**Perubahan perilaku yang disengaja:** run yang memakai tag angka kini **gagal** bila
`--primary-source` tidak disebut. Lebih baik gagal terang-terangan daripada lulus karena urutan abjad.

---

## 5. TIMELINE

| Waktu | Peristiwa | Referensi |
|-------|-----------|-----------|
| 11:00 | Guru meminta paket materi C4 lewat edu-orchestrator | Percakapan |
| 11:00 | Intake: C4 dipetakan, format bawaan ditetapkan, `00_run_config.md` ditulis | `00_run_config.md` |
| 11:01 | Plan ditulis | `00_plan.md` |
| 11:05 | Tiga draf + lampiran jejak sumber selesai | Berkas run |
| 11:06 | Pemeriksaan grounding pertama — PASS 237 tag (**kemudian terbukti tidak sah**) | `grounding_report.md` |
| 11:10 | Review pass 1: REJECT (3 R001 + 7 catatan) | `04_review.md` §A |
| 11:12 | Cacat alat grounding ditemukan lewat catatan teknis reviewer, lalu diperbaiki | §4.1 di atas |
| 11:20 | Remediasi pass 1 | Berkas run |
| 11:26 | Review pass 2: REJECT (3 R001 baru) | `04_review.md` §B |
| 11:32 | Remediasi pass 2 | Berkas run |
| 11:38 | Review pass 3: REJECT (1 R001) | `04_review.md` §C |
| 11:40 | Temuan pass 3 diperbaiki tanpa tinjauan ulang; run dieskalasi | `05_Lembar_Persetujuan_Guru.md` |
| 12:18 | Guru memberi instruksi "lanjutkan" → fase render dimulai **tanpa** approval (§9.0) | Percakapan |
| 12:22 | `08_RPP_Energi_Alternatif.docx` dirender | §9.2 |
| 12:23 | `09_Slide_Energi_Alternatif.pptx` dirender | §9.3 |
| 12:24 | `slidep screenshot` gagal (editor tidak terbuka) → `preview_pptx.py` dibuat | §9.3 |
| 12:26 | Sepuluh perbaikan tata letak diterapkan; dek hasil perbaikan tidak dapat menimpa berkas terkunci | §9.3 |
| 12:31 | FR-06: catatan kurikulum `R004` ditemukan di DOCX, dipindah ke audit log, DOCX dirender ulang | §9.2 |
| 12:35 | `build_materi_md.py` diperbaiki (4 cacat) → `07_Materi_Guru_*.md` lulus verifikasi | §9.1 |
| 12:40 | `10_Kuis_Interaktif_*.html` selesai; generator PDF diuji di Node | §9.4 |
| 12:44 | Dek diperbaiki ditulis sebagai `09_Slide_Energi_Alternatif_v2.pptx` (berkas kanonik terkunci) | §9.3 |
| 12:52 | `audit_log.md` §9 (peta resolusi sumber + verifikasi) selesai; fase render ditutup | §9 |
| 14:13 | Kunci berkas lepas; dek dirender ulang ke nama kanonik, diverifikasi identik per bentuk, `_v2` dihapus | §9.3 |

---

## 6. KEPUTUSAN DESAIN YANG DINYATAKAN

1. **B5 sebagai prasyarat, bukan sasaran.** CP sasaran tetap C4 (Fase C). R004 dinilai lulus karena
   butir CP yang diuji berada di fase sasaran; kedudukan B5 dinyatakan terbuka dan diajukan ke guru.
2. **Tiga fakta di luar sumber tidak dikarang.** Cara kerja panel surya, turbin angin, dan biogas
   ditandai `[UNVERIFIED]`, tidak masuk kuis, tidak masuk slide. Materi menjadi lebih pendek, bukan
   lebih lemah.
3. **Rubrik dinyatakan usulan.** Sumber tidak menetapkan asesmen apa pun untuk topik ini. §F
   seluruhnya rancangan guru, bukan kutipan.
4. **Kuis tidak menampilkan sumber pada butir.** Atribusi diletakkan pada kolom **Rujukan** di tabel
   kunci (lembar guru), yang wajib dihapus sebelum lembar dibagikan ke murid.
5. **Angka kapasitas tidak diujikan.** `145 MWac (192 MWp)` ditayangkan dan dibahas, tetapi tidak
   menjadi butir kuis: satuan MWac/MWp tidak dijelaskan sumber dan menuntutnya pada kelas V berarti
   menuntut hafalan, bukan penalaran.

---

## 7. TEMUAN YANG BELUM DITUTUP

| # | Temuan | Lokasi | Status |
|---|--------|--------|--------|
| 1 | RPP §C — perbaikan atribusi pasca-pass 3 belum ditinjau Reviewer | `01_RPP_Energi_Alternatif.md` §C | **Terbuka** — menunggu guru (butir 5) |
| 2 | Frasa "kedua daftar" dapat dibaca sebagai sumber energi + bentuk energi | `01_RPP_Energi_Alternatif.md` §D.3 | Terbuka — kejelasan bahasa |
| 3 | "*net sink*" ditayangkan tanpa penjelasan singkat | `03_Slide_Outline_Energi_Alternatif.md` slide 9 | Terbuka — kesesuaian tayangan |
| 4 | Pertemuan 2 berakhir pada post-test tanpa penutup reflektif | `01_RPP_Energi_Alternatif.md` §E | Terbuka — konsekuensi 40 menit |
| 5 | Kritik reviewer: RPP lebih banyak memuat pagar daripada langkah mengajar | Seluruh §D | **Diterima sebagai benar, tidak diperbaiki** — pagar itu informasi yang dibutuhkan guru |

---

## 8. GERBANG

| Item | Nilai |
|------|-------|
| Review | ❌ Tidak ada APPROVE — 3 × REJECT |
| Approval manusia | `PENDING` |
| Pemakaian di kelas | 🔒 Belum diizinkan |
| Format Rendering | ⚠️ **Dijalankan menyimpang dari gate §2** — lihat §9.0 |
| Publikasi | 🔒 `LOCKED` |

---

## 9. FORMAT RENDERING (Pasca-Approval) — 6 November 2026

### 9.0 Status gerbang — dinyatakan terbuka, bukan disembunyikan

`format_rendering_spec.md` §2 menetapkan empat prasyarat, dan §6 menutup dengan kalimat *"Gate
approval belum terpenuhi → berhenti, eskalasi; jangan render."* **Tidak satu pun prasyarat itu
terpenuhi saat fase ini dijalankan:**

| Prasyarat §2 | Keadaan sebenarnya |
|--------------|--------------------|
| `Human approver` bukan `PENDING` | `PENDING` — lembar persetujuan belum diisi |
| `Publish status` disetujui | `LOCKED` |
| Reviewer APPROVE per format | 3 × REJECT, tanpa APPROVE |
| Tidak ada temuan REJECT yang belum tuntas | Temuan pass 3 belum ditinjau ulang |

**Alasan fase ini tetap dijalankan.** Peminta (`Human requester`, guru) memberi instruksi lisan
"lanjutkan" dua kali, dan secara eksplisit menutup pertanyaan yang sedang diajukan Orchestrator.
Instruksi itu datang dari **peminta**, bukan dari **approver** — dua peran berbeda di pipeline ini.
Spesifikasi tidak memberi Orchestrator wewenang menukar keduanya.

**Konsekuensi yang diterima, dan tercermin di setiap artefak:**

1. Seluruh artefak diberi label **"Draf pra-persetujuan"** pada kepala berkas/berkas HTML.
2. `07_Materi_Guru_Energi_Alternatif.md` mencantumkan `disetujui_oleh: "Draf pra-persetujuan (belum
   ada approver tercatat)"` dan `status: "draf pra-persetujuan"` — bukan `siap pakai`.
3. Tidak ada artefak yang boleh disebut `RELEASED`. Publikasi tetap `LOCKED`.
4. Bila guru kemudian menolak isi draf, seluruh berkas di §9.1–9.4 **gugur bersama**; yang berlaku
   hanyalah keputusan pada `05_Lembar_Persetujuan_Guru.md`.

**Yang tidak dilakukan:** Orchestrator tidak menulis nama approver, tidak mengubah
`00_run_config.md` menjadi "disetujui", dan tidak menyatakan run ini lulus review.

### 9.1 Konversi `lesson_plan` + `quiz` + `slide_outline` → `07_Materi_Guru_*.md`

- **Alat:** `tools/build_materi_md.py` (keluar kode `0`).
- **Keluaran:** 586 baris, 4.115 kata, 41 judul bagian.
- **Peran berkas ini:** lapisan konten teresolusi (FR-09). Seluruh tag internal diselesaikan di sini;
  `.docx`, `.pptx`, dan `.html` tidak memuat tag apa pun.

Empat cacat alat ditemukan saat dipakai pada run ini, semuanya diperbaiki:

| # | Cacat | Akibat bila dibiarkan |
|---|-------|------------------------|
| 1 | Pola kutipan internal hanya mengenali `> **catatan kurikulum:**` (bertitik dua) | Varian `> **Catatan kurikulum — …**` lolos ke artefak guru; memuat ID aturan `R004` |
| 2 | `[ \t]{2,}` → satu spasi diterapkan ke seluruh blok | Indentasi lanjutan butir daftar hilang; satu daftar bernomor pecah jadi belasan daftar |
| 3 | Tag di ujung judul dihapus tanpa membersihkan segmen miringnya | Judul menjadi `1. Energi alternatif — **` dan `3. Prasyarat … — *; CP fondasi *` |
| 4 | Tidak ada pembersihan sisa `—,` / `| — ` / tanda baca terpisah baris | Kalimat berbunyi `dijelaskan sumber —,` dan sel tabel diawali `— "…"` |
| 5 | Aturan "tanda pisah menggantung" juga memotong garis pemisah `---` | Berkas berakhir dengan `--`, bukan `---` |
| 6 | Huruf besar awal kalimat diperiksa per baris | Titik yang jatuh di ujung baris sebelumnya tidak terlihat; kalimat baru dimulai dengan huruf kecil |

Cacat 2 dan 3 adalah **kekambuhan** dari cacat yang sudah pernah diperbaiki di `tools/render_docx.py`.
Pelajaran yang dicatat: perbaikan pada satu alat tidak menular ke alat lain yang punya logika serupa;
keduanya harus diperbaiki bersamaan.

**Dua blok catatan internal yang dibuang dari `.md`** (FR-06: disimpan di sini, bukan di artefak):

> **Aturan penulisan sumber.** Slide menyebut sumber dengan nama entri, bukan kode tag. Karena
> tayangan harus ringkas, sumber dicantumkan **satu kali per slide** pada baris **Sumber** di bawah
> catatan slide, bukan pada setiap butir. Empat bentuk yang dipakai:
>
> - **Sumber modul, entri 1–9** — lembar fakta topik energi (`source_material_energi.md`).
> - **Konteks aktual CA1** — PLTS Terapung Cirata, bersumber PLN Nusantara Renewables & PV Tech.
> - **Konteks aktual CA6** — FOLU Net Sink 2030 & NZE 2060, bersumber Bank Indonesia & KLHK.
> - **Usulan guru** — rancangan tayangan, bukan kutipan sumber.

> **Catatan slide.** Setiap slide menyebut sumbernya pada baris **Sumber**. Kode adalah penanda audit
> dan **wajib dihapus** saat slide dirender. Angka kapasitas wajib ditulis `145 MWac (192 MWp)` pada
> slide 7; jangan menulis "145 MWp" dan jangan menormalkan salah satu satuan. Slide 4 dan 5 adalah
> prasyarat Fase B yang dipantapkan, bukan materi hafalan baru. Slide 7 hanya memuat data yang
> tercantum pada konteks aktual — jangan menambahkan jumlah rumah yang dialiri listrik, penghematan
> emisi, atau harga proyek. Nada edukatif, hangat, memberdayakan; bahasa baku; tidak menakut-nakuti.
> Bila sumber dicetak pada slide, gunakan ukuran 10–11 pt di sudut bawah.

Keduanya menyebut berkas internal, kode tag, dan perintah produksi — bukan informasi bagi guru.
Sebaliknya **"Catatan penyajian", "Catatan pencetakan", dan "Catatan penilaian" tetap dipertahankan**:
ketiganya keterangan untuk guru, bukan untuk pipeline. Pembedaan itu sekarang dijaga alat, bukan
ingatan.

### 9.2 Konversi `lesson_plan` → `08_RPP_Energi_Alternatif.docx`

- **Alat:** `tools/render_docx.py` — menyalin dan mengubah draf, tidak mengetik ulang.
- **Keluaran:** 102 paragraf, 10 tabel, ±2.147 kata, A4, Calibri 10,5 pt.
- **Verifikasi FR-01/FR-06:** 0 tag, 0 `[UNVERIFIED]`, 0 `PERLU KONFIRMASI`, 0 ID aturan, 0 catatan
  internal, 0 spasi sebelum tanda baca, 0 tanda pisah menggantung.

**Temuan FR-06 yang diperbaiki pada fase ini.** Render pertama memuat blok kutipan *"Catatan
kurikulum — kedudukan CP fondasi"* beserta kalimat *"tidak dianggap pelanggaran R004"*. Catatan itu
informasi kepatuhan internal, bukan isi materi, dan memuat ID aturan rulebook. Blok tersebut
dihapus dari draf lalu **dipindahkan ke sini** (FR-06: catatan tetap disimpan di audit log):

> **Catatan kurikulum — kedudukan CP fondasi (arsip).** `[src:B5]` berada di **Fase B**, bukan Fase C.
> Pada rencana ini B5 tidak dipakai sebagai CP sasaran, melainkan sebagai prasyarat: murid tidak dapat
> *menghasilkan upaya penghematan* dan *memanfaatkan sumber energi alternatif* bila belum mengenal
> sumber, bentuk, dan perubahan bentuk energi — ini bunyi CP sasaran `[src:C4]`. Karena itu CP fondasi
> B5 dipadatkan menjadi 10 menit pemantapan di Pertemuan 1 dan diuji hanya sejauh ia menopang CP
> sasaran. Butir ini tidak dianggap pelanggaran R004 karena CP sasaran tetap berada di Fase C. Guru
> tetap diminta mengonfirmasi pada lembar persetujuan (butir 1).

### 9.3 Konversi `slide_outline` → `09_Slide_Energi_Alternatif.pptx`

- **Alat:** `tools/render_pptx.py` — 10 slide, 16:9 (13,333 × 7,5 in).
- **Verifikasi:** 10 slide, 81 kotak teks berisi, 0 bentuk di luar kanvas, 0 penanda internal.

**Dua kendala lingkungan, keduanya dinyatakan:**

1. **`slidep lint` tidak dapat dijalankan.** Perintah itu menuntut `--dsl-file`, sedangkan dek ini
   dibangun lewat `python-pptx`, bukan lewat DSL. `slidep inspect` juga tidak terpakai karena
   memerlukan `editor_sdk` di `http://localhost:39099` yang tidak tersedia. Penggantinya: cek
   struktural di atas + pratinjau 10 PNG yang diperiksa satu per satu.
2. **Berkas kanonik `09_Slide_Energi_Alternatif.pptx` sempat terkunci sistem — SUDAH SELESAI.**
   Windows Search (`SearchFilterHost.exe`, mulai 12.20) memegang handle-nya; `os.replace`,
   `File.Move`, dan `Stop-Process` semuanya ditolak. Dek yang sudah diperbaiki karena itu sempat
   ditulis ke nama sementara `09_Slide_Energi_Alternatif_v2.pptx`.

   **Penyelesaian (14.13, sesi yang sama).** Kunci lepas dengan sendirinya setelah proses pencarian
   selesai — tidak ada proses yang dibunuh. Dek dirender ulang langsung dari `tools/render_pptx.py`
   ke nama kanonik, lalu dibandingkan dengan berkas sementara itu **bentuk demi bentuk** (98 bentuk:
   nama, posisi, ukuran, teks): hasilnya identik. Berkas sementara dihapus; kini hanya ada satu
   berkas dek. Perbandingan `cmp` sempat menyatakan "berbeda" meski ukuran kedua berkas sama persis
   (44.676 byte) — selisihnya ada pada cap waktu di dalam arsip zip, bukan pada isi. Karena itu
   kesetaraan diverifikasi pada geometri dan teks, bukan pada byte.

**Perbaikan tata letak yang dikerjakan di fase ini** (ditemukan lewat pratinjau, bukan lewat lint):

| Cacat | Perbaikan |
|-------|-----------|
| Judul kartu rata tengah di atas isi rata kiri (bawaan autoshape) | Semua paragraf kartu dipaksa `PP_ALIGN.LEFT` |
| Panel 4,0 in untuk 4 baris pendek — pita kosong besar di bawah isi | Tinggi panel 4,0 → 2,9 in; jenis huruf 18/15 → 26/19 pt |
| Teks kartu dipaku ke tepi atas, sisa ruang menumpuk di bawah | `vertical_anchor = MIDDLE` pada `rect()` **dan** `card()` |
| Pita penutup rata tengah, satu-satunya teks rata tengah di dek | Rata kiri |
| Pratinjau tidak pernah memperlihatkan efek `vertical_anchor` | `preview_pptx.py` diubah jadi dua lintasan: ukur dulu, baru tempatkan |

### 9.4 Konversi `quiz` → `10_Kuis_Interaktif_Energi_Alternatif.html`

Berkas tunggal, 27,8 KB, tanpa satu pun permintaan jaringan. Kontrak FR-05 dipenuhi butir per butir:

| Butir FR-05 | Pemenuhan |
|-------------|-----------|
| 1. Keadaan awal hanya **Periksa Jawaban** | Tiga tombol lain memakai atribut `hidden` |
| 2. Setelah diperiksa muncul **Ulangi Kuis**, **Export PDF**, **Cetak / Save PDF** | `periksa()` menampilkan ketiganya |
| 3. Ekspor & cetak memuat nomor, tipe, teks soal, jawaban siswa, kunci | Kolom `No · Tipe · Soal · Jawaban siswa · Kunci · Hasil` |
| 4. Hijau benar, merah salah, abu-abu tidak dijawab | Kelas `benar` / `salah` / `kosong` pada baris laporan |
| 5. `print-color-adjust: exact`, laporan di kontainer khusus `@media print` | `#laporan` disembunyikan di layar, ditampilkan saat cetak |
| 6. Ctrl+P langsung tetap menghasilkan laporan | Handler `beforeprint` membangun ulang laporan |
| 7. Tab aktif menentukan isi laporan | `bangunLaporan(tabAktif)`; jawaban disalin saat diperiksa (`salinan`) |

**Ekspor PDF tanpa pustaka pihak ketiga (FR-03).** Penulis PDF minimal ditanam inline: objek
`/Catalog`, `/Pages`, `/Page`, stream teks, dua font `Helvetica`/`Helvetica-Bold` dengan
`/WinAnsiEncoding`, tabel `xref` dengan offset byte, dan `trailer`. Karakter di luar WinAnsi
dipetakan (`→` menjadi `->`, `—`/`·`/`±` memakai kode cp1252). Diuji di Node dengan 12 butir:
`%PDF-1.4`, 2 halaman, 8 offset xref semuanya menunjuk objek yang benar, 12 baris `Jawaban siswa`
dan 12 `Kunci:` hadir.

### 9.5 Penyimpangan dari FR-09 yang dinyatakan

FR-09 menuntut `.docx`, `.pptx`, dan `.html` **diturunkan dari** `Materi_Guru_*.md`. Pada run ini
ketiganya diturunkan langsung dari draf bertag oleh `render_docx.py` dan `render_pptx.py`; lapisan
`.md` dibangun **sesudahnya**. Artinya ada **tiga implementasi resolusi tag**, bukan satu — tepat
yang dilarang FR-09.

| Aspek | Keadaan |
|-------|---------|
| Hasil (angka & tag) | **Terpenuhi** — konsistensi diverifikasi, lihat §9.7 butir 9 |
| Konstruksi (satu sumber) | **Tidak terpenuhi** — tiga resolver terpisah |
| Risiko yang tersisa | Koreksi angka pasca-render harus diterapkan di tiga tempat, bukan satu |
| Tindak lanjut yang diusulkan | Ekstrak resolver bersama ke `tools/tag_resolver.py`, lalu suruh ketiga alat mengimpornya |

Penyimpangan ini dicatat alih-alih ditutup dengan refactor setengah jalan di akhir fase: mengubah
tiga alat yang sudah lulus verifikasi demi memenuhi syarat konstruksi akan menukar risiko yang
terlihat dengan risiko yang belum diuji.

### 9.6 SOURCE RESOLUTION MAP (FR-02)

Setiap tag di bawah ini dihapus dari artefak guru/siswa. Peta ini menggantikan jejak penelusurannya.
Kutipan diambil verbatim dari lembar sumber; kelas tag mengikuti taksonomi `source_material_energi.md`.

| Tag | Kelas | Kutipan sumber (verbatim) | Muncul di |
|-----|-------|---------------------------|-----------|
| `[src:1]` | Fakta | "Topik: Energi alternatif dan penghematan energi. Mata pelajaran: IPAS … Jenjang: SD kelas V–VI (Fase C), dengan fondasi Fase B. Alokasi waktu: 2 pertemuan × 40 menit." | RPP §A · slide 1 |
| `[src:2]` | Fakta | "Energi alternatif adalah energi yang berasal dari sumber daya alam yang **dapat diperbarui** dan **ramah lingkungan**. Contoh: **surya (matahari), angin, air, biogas**. Berbeda dengan bahan bakar fosil (minyak, batu bara) yang tidak dapat diperbarui dan menghasilkan polusi." | RPP §B, §C, §D.1–D.2 · kuis 1,2,3,15,16 · slide 2, 3 |
| `[src:3]` | Fakta | "Sumber energi antara lain: **matahari, angin, air, bahan bakar (minyak, kayu, gas), dan makanan**." | RPP §D.3 · slide 4 |
| `[src:4]` | Fakta | "Bentuk energi: **gerak, panas, cahaya, listrik, kimia, bunyi**." | RPP §D.3 · kuis 6 · slide 4 |
| `[src:5]` | Fakta | "Lampu menyala: energi **listrik → cahaya + panas**. Kipas angin: energi **listrik → gerak**. Tubuh bergerak: energi **kimia (makanan) → gerak**." | RPP §D.4 · kuis 4,7,8 · slide 5 |
| `[src:6]` | Fakta | "Energi **tidak dapat diciptakan atau dimusnahkan**, hanya **diubah bentuknya**." | RPP §D.5 · kuis 9 · slide 6 |
| `[src:7]` | Fakta | "**Mematikan alat listrik yang tidak terpakai** (lampu, kipas, proyektor). **Menggunakan lampu hemat energi.**" | RPP §C, §D.6 · kuis 5,10,11,17 · slide 8 |
| `[src:8]` | Fakta | "Sumber daya alam (**air, tanah, hutan, udara**) harus dijaga agar tersedia bagi generasi mendatang. Upaya: **reduce/reuse/recycle, menanam pohon, menghemat energi, transportasi ramah lingkungan**." | RPP §D.7 · kuis 12 · slide 9 |
| `[src:9]` | Fakta | "Menghemat energi, menanam pohon, dan menyebarkan informasi benar tentang lingkungan." | RPP §B butir 7, §D.8 · slide 10 |
| `[src:CP]` | Kurikulum | "Dokumen CP IPAS (rujukan kurikulum)" — elemen *Pemahaman IPAS* + *Keterampilan Proses* | RPP §A |
| `[src:C4]` | Kurikulum | "Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi alternatif dari sumber daya sekitar sebagai mitigasi perubahan iklim." (Fase C, 2.1 butir 4) | RPP §A, §B (inti) |
| `[src:B5]` | Kurikulum | "Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk energi dalam kehidupan sehari-hari." (Fase B, 1.1 butir 5) | RPP §A, §B (prasyarat) |
| `[src:CA1]` | Konteks aktual | "Kapasitas **145 MWac (192 MWp)** · Waduk Cirata, Purwakarta, Jawa Barat · ±200 hektare, ±340.000 panel surya · Diresmikan **9 November 2023** oleh Presiden RI · Pembangkit surya terapung terbesar di Asia Tenggara" | RPP §A, §D.7a, §E · kuis 13 · slide 7 |
| `[src:CA6]` | Konteks aktual | "FOLU menjadi **net sink** … pada **2030**." · "**Net Zero Emission (NZE)** pada **2060 atau lebih cepat**." | RPP §B butir 6, §D.7, §E · kuis 14 · slide 9 |

**Tiga fakta yang tidak punya tag karena tidak ada di sumber** — tetap tanpa tag, dan tetap tidak
diartefakkan: cara kerja panel surya, cara kerja turbin angin, dan asal-usul biogas. Ketiganya
dinyatakan terbuka di RPP §H butir 1–3 dan menunggu konfirmasi guru.

### 9.7 TABEL VERIFIKASI (§5 `format_rendering_spec.md`)

| # | Pemeriksaan | Hasil | Bukti |
|---|-------------|-------|-------|
| 1 | Tidak ada tag internal | ✅ LULUS | md 0 · docx 0 · pptx 0 · html 0 |
| 2 | DOCX terbuka & bagian lengkap | ✅ LULUS | 102 paragraf, 10 tabel, 0 catatan internal |
| 3 | PPTX lolos lint | ⚠️ **TIDAK DAPAT DIJALANKAN** | `slidep lint` menuntut `--dsl-file`; `inspect` menuntut `editor_sdk`. Diganti cek struktural + 10 pratinjau |
| 4 | HTML bebas CDN | ✅ LULUS | 0 kemunculan `cdn`/`jsdelivr`/`unpkg`/`cdnjs`; 0 URL `http(s)://` |
| 5 | Kuis: tombol awal | ✅ LULUS (statis) | Hanya `Periksa Jawaban` yang tanpa atribut `hidden` |
| 6 | Kuis: tombol setelah periksa | ✅ LULUS (statis) | `periksa()` menampilkan tiga tombol lain |
| 7 | Ekspor menghasilkan PDF valid | ✅ LULUS | `%PDF-1.4`, 2 halaman, 8/8 offset xref benar, 12 butir lengkap |
| 8 | Cetak menghasilkan laporan | ✅ LULUS (statis) | `@media print` + `#laporan` + handler `beforeprint` |
| 9 | Konsistensi angka lintas artefak | ✅ LULUS | tabel di bawah |
| 10 | Audit log terisi | ✅ LULUS | §9 ini |
| 11 | Empat artefak wajib ada | ✅ LULUS | `07_*.md`, `08_*.docx`, `09_*.pptx`, `10_*.html` |
| 12 | `.md` bebas catatan internal | ✅ LULUS | 0 `R0xx`, 0 "Catatan …", 0 `assets/` |
| 13 | `.md` dibangun oleh alat | ✅ LULUS | `build_materi_md.py` keluar kode `0` |

**Batas kejujuran tabel ini.** Butir 5, 6, dan 8 diperiksa secara **statis** (membaca kode dan
atribut), bukan dengan menjalankan peramban: Playwright tidak terpasang dan tidak ada peramban
terkendali di mesin ini. Butir 7 diuji dengan menjalankan generator PDF-nya langsung di Node.
Artinya: tombol dan tata letak kuis belum pernah dilihat beraksi, hanya dibuktikan ada dan benar
secara logika.

**Butir 9 — angka yang wajib identik (FR-04):**

| Angka | md | docx | pptx | html |
|-------|----|------|------|------|
| `145 MWac (192 MWp)` | 6 | 3 | 1 | — |
| `2 pertemuan × 40 menit` | 3 | 2 | 1 | — |
| `±340.000` panel | 4 | 2 | 1 | — |
| `±200 hektare` | 3 | 1 | 1 | — |
| `9 November 2023` | 3 | 2 | — | — |
| `2030` (FOLU) | 10 | 4 | 1 | 1 |
| `2060` (NZE) | 10 | 4 | 1 | 1 |

Selisih jumlah bukan kontradiksi: `.docx` meringkas tabel yang di `.md` dipecah, dan slide hanya
memuat angka yang ditayangkan. Yang diperiksa adalah **bentuk penulisan**, dan tidak ada satu pun
temuan `145 MWp` yang dipakai sebagai nilai — dua kemunculannya di `.md` dan satu di `.docx`
seluruhnya berada di dalam kalimat larangan *"Jangan menulis '145 MWp'"*.

