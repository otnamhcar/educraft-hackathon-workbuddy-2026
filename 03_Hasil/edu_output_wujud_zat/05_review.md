# Review Rulebook R001–R011 — "Perubahan Wujud Zat"

> **Reviewer:** edu-reviewer | **Rulebook:** `assets/rulebook_ipas.md` v R001–R011
> **Objek review:** `01_artikel.md`, `02_infographic_brief.md`, `03_video_storyboard.md`, `04_kuis_prepost.md`
> **Hasil akhir:** ✅ **APPROVE** pada iterasi 2 (dari maksimum 3)

---

## PASS 1 — Draft v1: ❌ REJECT

**Status:** REJECT | **Critical: 0 | Major: 5 | Minor: 2**

### Temuan Major

| # | Rule | Kutipan | Alasan | Perbaikan yang diminta |
|---|------|---------|--------|------------------------|
| F1 | **R001** | "Ketika suhu di sekitar zat berubah, **susunan partikel di dalamnya ikut berubah**, sehingga wujudnya pun dapat berubah." (artikel) | Mekanisme partikel tidak tercantum di `[src:B4]`. Sumber hanya menyatakan "perubahan wujud dapat disebabkan perubahan suhu". Ini fakta tambahan (meski benar secara sains) → melanggar grounding. | Hapus klaim partikel; nyatakan hanya hubungan suhu–wujud sesuai sumber. |
| F2 | **R001** | "tiga perubahan bergerak dari wujud yang **lebih rapat** ke wujud yang **lebih longgar**" (artikel) | Konsep kerapatan partikel tidak ada di sumber. | Ganti dengan deskripsi arah murni (padat→cair, cair→gas, dst.) yang dapat diturunkan langsung dari tabel sumber. |
| F3 | **R001** | Kartu wujud: "**Bentuk tetap**", "**Mengikuti wadah**", "**Memenuhi ruang**" (brief infografis) | `[src:B4]` hanya menyebut tiga wujud dan enam perubahan; ciri-ciri wujud tidak tercantum. | Ganti teks kartu menjadi contoh yang bersumber: "Contoh: es batu / air / uap air". |
| F4 | **R001** | "Es batu adalah zat padat: **bentuknya tetap**… Air adalah zat cair: **bentuknya mengikuti wadah**… Uap air adalah zat gas: **ia menyebar dan memenuhi ruang**." (artikel & narasi video) | Sama seperti F3, ciri wujud dikarang. | Pertahankan klasifikasi wujud (bersumber), hapus klaim ciri. |
| F5 | **R001** | Pre-test butir 3 ("mengikuti bentuk gelas… ciri zat") dan Post-test butir 1 ("Ciri zat gas adalah… memenuhi ruang") | Butir soal menguji fakta yang tidak bersumber. Risiko lebih tinggi karena menjadi **dasar penilaian**. | Ganti butir dengan konten bersumber (klasifikasi wujud & urutan wujud). |

### Temuan Minor

| # | Rule | Kutipan | Alasan | Tindakan |
|---|------|---------|--------|----------|
| F6 | R001 | "Jumlah kata: ± 520 kata" (artikel) | Hitungan aktual 400 kata. Ketidaksesuaian metadata. | Auto-fix: ubah menjadi "± 400 kata". |
| F7 | R008 | Visual adegan 2: "air yang bentuknya mengikuti gelas… uap yang menyebar memenuhi ruang" | Deskripsi visual mengulang klaim ciri yang tidak bersumber. | Auto-fix: netralkan deskripsi visual. |

### Catatan (bukan pelanggaran)

- **R004** — Anchor CP: topik berada di **CP-B.1.1.4 (Fase B)**, sedangkan sasaran yang diminta adalah Fase C. R004 mewajibkan penandaan `PERLU KONFIRMASI GURU` bila CP tidak tercakup. Penandaan **sudah ada** di `00_plan.md` §4 → **tidak dinilai sebagai pelanggaran**, tetapi wajib diselesaikan guru sebelum publikasi.
- **R011** — Tidak ada tautan `[src:CA#]`. Reviewer memverifikasi bahwa memang **tidak ada** entri Konteks Aktual yang relevan dengan perubahan wujud zat. Tidak memaksakan tautan = keputusan yang benar.
- **R002, R003, R005, R006, R007, R009, R010** — Lolos pada v1 (tidak ada bahasa menakutkan, kosakata sesuai usia, ada peran murid, tanpa klaim kesehatan, tanpa promosi berbahaya, narasi KBBI + CTA, bahasa soal sopan).

---

## PASS 2 — Draft v2: ✅ APPROVE

**Status:** APPROVE | **Critical: 0 | Major: 0 | Minor: 0**

### Verifikasi Perbaikan

| Temuan | Status | Bukti perbaikan |
|--------|--------|-----------------|
| F1 | ✅ Selesai | Kalimat partikel dihapus dari artikel (bagian "Suhu sebagai Pemicunya") dan dari narasi video adegan 4. |
| F2 | ✅ Selesai | Diganti menjadi pola arah eksplisit: "mencair (padat → cair), menguap (cair → gas), menyublim (padat → gas)…" |
| F3 | ✅ Selesai | Kartu wujud kini berbunyi "Contoh: es batu / air / uap air". |
| F4 | ✅ Selesai | Artikel & narasi video hanya menyatakan klasifikasi wujud tanpa klaim ciri. |
| F5 | ✅ Selesai | Pre-test 3 → "Uap air termasuk zat berwujud…"; Post-test 1 → "Urutan wujud yang tepat untuk es batu, air, dan uap air…" |
| F6 | ✅ Selesai | Metadata jumlah kata diperbarui (400 kata). |
| F7 | ✅ Selesai | Deskripsi visual adegan 2 dinetralkan. |

### Penilaian Akhir per Aturan

| Rule | Nama aturan | Putusan | Dasar |
|------|-------------|---------|-------|
| R001 | Factual accuracy / grounding | **PASS** | Setelah v2, seluruh klaim dapat dilacak ke `[src:B4]` atau `[src:CP]`. Contoh sehari-hari berstatus penerapan jenis perubahan yang bersumber, bukan fakta baru. |
| R002 | No fear-mongering | **PASS** | Nada tenang; tidak ada narasi bencana. |
| R003 | Age-appropriate | **PASS** | Kosakata dan panjang kalimat sesuai kelas V–VI. |
| R004 | Curriculum alignment | **PASS (bersyarat)** | Tertaut ke CP-B.1.1.4 + CP-C.2.2; gap Fase C ditandai `PERLU KONFIRMASI GURU`. Syarat: konfirmasi guru sebelum publikasi. |
| R005 | Balanced & solution-oriented | **PASS** | Ada ajakan mengamati & mencatat yang dapat dilakukan murid. |
| R006 | Health-claim caution | **N/A** | Tidak ada klaim kesehatan. |
| R007 | No harmful promotion | **PASS** | Tidak ada praktik berbahaya. |
| R008 | Brand / pedagogic tone | **PASS** | Hangat, edukatif, memberdayakan. |
| R009 | Narasi video KBBI & CTA | **PASS** | Istilah baku (mencair, melebur, membeku, menguap, mengembun, menyublim, mengkristal); tempo 135 kata/menit; CTA di akhir. |
| R010 | Bahasa soal & umpan balik | **PASS** | Tidak ambigu, tanpa jebakan, instruksi pre-test menenangkan; pedoman penilaian melarang komentar menjatuhkan. |
| R011 | Konteks aktual terverifikasi | **PASS (N/A)** | Tidak ada klaim konteks aktual; tidak ada tautan `[src:CA#]` yang dipaksakan. |

### Pemeriksaan Khusus Kuis

| Pemeriksaan | Hasil |
|-------------|-------|
| Kunci jawaban benar & konsisten | ✅ 7/7 pre-test, 20/20 post-test diverifikasi manual |
| Perhitungan skor deterministik | ✅ Pre = (skor ÷ 7) × 100; Post = (skor ÷ 20) × 100 |
| Distraktor masuk akal & tidak ambigu | ✅ Setiap butir memiliki tepat satu jawaban paling tepat |
| Tidak ada petunjuk jawaban tak sengaja | ✅ Tidak ada pola posisi kunci yang berulang mencolok |
| Butir mengukur kompetensi sasaran | ✅ 14 butir pengetahuan + 6 butir penalaran, termasuk butir 20 (Keterampilan Proses Fase C) |

**Iterasi terpakai:** 2 dari maksimum 3. Tidak diperlukan eskalasi.

---

## REVIEW — Lembar Kerja Pengamatan `10_Lembar_Kerja_Pengamatan`

**Status:** ✅ **APPROVE** setelah 2 perbaikan | Critical 0 | Major 2 | Minor 2

Konteks: permintaan guru (30 Okt 2026, 17:50) untuk lembar kerja percobaan es–air dengan tabel data kosong.
Karena ini konten baru, lembar kerja menjalani review penuh, bukan sekadar diteruskan dari paket yang sudah disetujui.

### Temuan & Perbaikan

| # | Rule | Temuan | Tindakan |
|---|------|--------|----------|
| F1 | **R001** | Risiko utama: kolom "Suhu (°C)" berpotensi terisi angka oleh agen (titik lebur/titik didih tidak ada di sumber). | **Major.** Kolom dibiarkan kosong total; ditambah catatan "Isilah dengan hasil bacaan termometer kelompokmu, bukan dengan perkiraan". Diverifikasi terprogram: **0 angka suhu** di seluruh dokumen, 8 sel suhu kosong. |
| F2 | **R001/R004** | Tabel data terbelah dua halaman; baris 5–8 terpisah dari kepala tabel sehingga data mudah tertukar saat diisi. | **Major.** Blok tabel dibungkus `break-inside: avoid`; tabel kini utuh dalam satu halaman. |
| F3 | R007 (keselamatan) | Percobaan memakai termometer; tidak ada rambu keselamatan. | **Minor.** Ditambah kotak keselamatan: gunakan termometer plastik/alkohol, jangan mengaduk, panggil guru bila pecah. |
| F4 | R008 | Kolom "Nama" muncul dua kali (lencana header dan baris identitas). | **Minor.** Lencana diganti "Percobaan 1 · Perubahan Wujud". |

### Penilaian Akhir per Aturan

| Rule | Putusan | Dasar |
|------|---------|-------|
| R001 | PASS | Satu-satunya klaim faktual ("hubungan perubahan suhu dan perubahan wujud") ber-tag `[src:B4]`. Tidak ada angka suhu, tidak ada titik lebur/didih. |
| R002 | PASS | Nada tenang, tidak ada narasi menakutkan. |
| R003 | PASS | Instruksi pendek, satu tindakan per langkah, sesuai kelas V–VI. |
| R004 | PASS (bersyarat) | Mengukur CP-B.1.1.4 + keterampilan proses Fase C (mengamati, mencatat, menyajikan grafik, menyimpulkan, mengevaluasi). Status lintas fase sudah disetujui guru. |
| R005 | PASS | Ada prediksi, analisis, dan saran perbaikan — murid berperan aktif. |
| R006 | N/A | Tidak ada klaim kesehatan. |
| R007 | PASS | Keselamatan termometer dinyatakan eksplisit. |
| R008 | PASS | Hangat, mendorong rasa ingin tahu, tanpa menyalahkan. |
| R009 | N/A | Bukan naskah video. |
| R010 | PASS | Bahasa instruksi lugas; pertanyaan refleksi tidak memojokkan ("bagian mana yang masih membuatmu bingung" — menormalkan kebingungan). |
| R011 | N/A | Tidak ada klaim konteks aktual. |

**Catatan desain:** grafik sengaja dibiarkan tanpa skala pada sumbu suhu. Memberi skala berarti memberi angka suhu yang tidak bersumber; murid menulis skala sendiri dari data kelompoknya. Ini juga menilai keterampilan menyajikan data, bukan menyalin.

---

## Status Gerbang
✅ **DISETUJUI GURU** pada 30 Oktober 2026, 17:19 GMT+7 (don Jimat Akbar).

Persetujuan mencakup:
1. Penempatan topik Fase B pada kelas V–VI (status: pemantapan lintas fase).
2. Kunci jawaban 27 butir.
3. Aset infografis final.

Gerbang publikasi dibuka. Konten didistribusikan melalui dua paket terpisah:
`08_Paket_Siswa_Cetak.pdf` (tanpa kunci) dan `09_Paket_Guru_Cetak.pdf` (dengan kunci + tabel skor).
