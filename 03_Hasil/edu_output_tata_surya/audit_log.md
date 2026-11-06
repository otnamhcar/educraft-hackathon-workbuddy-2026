# AUDIT LOG — EduCraft Orchestrator
## Run ID: EDU-ORCH-20261105-003

---

## 1. RUN METADATA

- **Run ID:** EDU-ORCH-20261105-003
- **Topik:** Sistem Tata Surya, serta Kaitannya dengan Rotasi dan Revolusi Bumi
- **Sasaran:** Fase C (Kelas V–VI)
- **Timestamp:** 2026-11-05 07:36 GMT+7
- **Orchestrator:** EduCraft Orchestrator (Master)
- **Human requester:** Guru (don Jimat Akbar)
- **Human approver:** ✅ **APPROVED** — don Jimat Akbar (guru), 2026-11-05 15:01 GMT+7
- **Publish status:** `APPROVED_FOR_USE` — materi boleh dipakai di kelas. Publikasi/distribusi tetap
  `LOCKED` sampai permintaan eksplisit terpisah (Hard Rule: no publish without approval).

---

## 2. INPUTS

| Item | Nilai |
|------|-------|
| Source fakta | `source_material_tata_surya.md` → `[src:TS1]`–`[src:TS11]` |
| Referensi kurikulum | `assets/cp_ipas.md` — Panduan IPAS Revisi 4, 3 Okt 2025 (Puskurjar, Kemendikdasmen) |
| Rulebook | `assets/rulebook_ipas.md` — R001–R012, v2.0 |
| Konteks Aktual | **Tidak digunakan** — tidak ada `[src:CA#]` yang relevan; tautan tidak dipaksakan (R011) |

---

## 3. AGENT EXCHANGE

### 3.1 INTAKE (S0)

- **Peran:** Orchestrator
- **Keputusan:** Guru meminta topik tata surya. Intake menu memetakan ke **C5** (Fase C, CP-C.2.1.5).
- **Catatan fase:** Guru awalnya menyebut Fase B (kelas III–IV). Topik tata surya secara kanonik
  berada di Fase C. Orchestrator mengoreksi ke Fase C sesuai R004.
- **Format:** Bawaan §4.1 — RPP + kuis + slide (3 format).
- **Sumber:** `source_material_tata_surya.md` dibuat khusus untuk run ini, dikutip dari Panduan
  IPAS halaman 45–47 (bagian "e. Sistem Tata Surya").

### 3.2 PLANNER → (outline)

- **Peran:** edu-planner
- **Output:** `00_plan.md` — 3 format dipetakan ke `[src:TS#]`.
- **Decisions:** Topik C5 dipilih karena (a) guru meminta, (b) source material tersedia dari
  Panduan IPAS resmi.

### 3.3 WRITER → Draft v1

- **Peran:** edu-writer
- **Artifacts (v1):**
  - `01_RPP_Tata_Surya.md` (RPP, Fase C, CP C5)
  - `02_Kuis_PrePost_Tata_Surya.md` (5 pre-test + 10 post-test)
  - `03_Slide_Outline_Tata_Surya.md` (9 slide)
- **Tagging:** Setiap fakta bertag `[src:TS#]`. Dua entri turunan (`[src:TS10]`, `[src:TS11]`)
  ditandai eksplisit sebagai "TURUNAN TIM, BUKAN KUTIPAN".

### 3.4 REVIEWER → Pass 1: ✅ APPROVE

- **Peran:** edu-reviewer
- **Status:** ✅ **APPROVE** (0 Critical, 0 Major, 0 Minor blocking)
- **R001:** ✓ semua fakta ber-tag, tag resolvable, kelas tag sesuai (§0)
- **R002:** ✓ nada tenang, solutif
- **R003:** ✓ Fase C (kelas V–VI) — kosakata sesuai
- **R004:** ✓ terikat CP C5
- **R005:** ✓ peran murid ada (model tata surya, refleksi)
- **R006:** N/A — tidak ada klaim kesehatan
- **R007:** N/A — tidak ada praktik berbahaya
- **R008:** ✓ tone edukatif, memberdayakan
- **R009:** ✓ bahasa baku + CTA
- **R010:** ✓ tidak memojokkan
- **R011:** N/A beralasan — tidak ada entri konteks aktual yang relevan
- **R012:** N/A beralasan — materi edukatif murni, tanpa unsur komersial
- **Catatan:** Reviewer menandai bahwa `[src:TS10]` dan `[src:TS11]` adalah turunan tim dan
  wajib divalidasi guru. Ini bukan temuan blocking — sumber sudah jujur menandai keduanya.

### 3.5 HUMAN APPROVAL GATE

- **Status:** ✅ **APPROVED** pada 2026-11-05 15:01 GMT+7
- **Pemberi:** don Jimat Akbar (guru IPAS)
- **Keputusan:** lihat `04_Lembar_Persetujuan_Guru.md`
  1. `[src:TS10]` — disetujui sebagai fakta yang boleh diujikan
  2. `[src:TS11]` — disetujui sebagai fakta yang boleh diujikan
  3. Koreksi fase B → C — diterima
  4. Kunci butir kuis 13 — diperbaiki
- **Batas:** persetujuan mencakup pemakaian di kelas, **bukan** publikasi atau distribusi.

---

## 4. GROUNDING VERIFICATION

| Run | Tag diperiksa | Dangling | Pelanggaran kelas | Vonis |
|-----|-------------:|---------:|------------------:|-------|
| -003 (Tata Surya) | *lihat hasil check_grounding.py* | — | — | *lihat laporan* |

---

## 5. TIMELINE

| Waktu | Peristiwa | Referensi |
|-------|-----------|-----------|
| 2026-11-05 07:29 | Guru meminta RPP IPAS tata surya | Percakapan |
| 2026-11-05 07:31 | RPP dibuat di luar pipeline (output/rpp-tata-surya/) | Tanpa tag grounding |
| 2026-11-05 07:36 | Guru meminta cek kondisi proyek | — |
| 2026-11-05 07:42 | Guru meminta masukkan ke pipeline EduCraft | — |
| 2026-11-05 07:43 | Source material dibuat dari Panduan IPAS hlm. 45–47 | `source_material_tata_surya.md` |
| 2026-11-05 07:44 | Run config + plan + RPP + kuis + slide + audit log ditulis | File di `03_Hasil/edu_output_tata_surya/` |
| 2026-11-05 15:01 | **Guru menyetujui** TS10, TS11, koreksi fase, dan perbaikan kunci soal 13 | `04_Lembar_Persetujuan_Guru.md` |
| 2026-11-05 15:05 | RPP, kuis, slide, run config, audit log diperbarui sesuai keputusan guru | Berkas run ini |

---

## 6. CATATAN KOREKSI: RPP SEBELUMNYA (di luar pipeline)

RPP Tata Surya yang pertama dibuat (di `output/rpp-tata-surya/`) memiliki masalah grounding:

| Masalah | RPP di output/ | RPP di edu_output_tata_surya/ |
|---------|----------------|-------------------------------|
| Tag `[src:#]` | Tidak ada | ✓ Setiap fakta bertag `[src:TS#]` |
| Ciri planet (warna, ukuran) | Mencantumkan tanpa sumber | Tidak mencantumkan — tidak ada di source |
| Definisi rotasi/revolusi | Ditulis sebagai fakta tanpa tag | Ditandai sebagai turunan `[src:TS11]` |
| Urutan planet | Ditulis sebagai fakta tanpa tag | Ditandai sebagai turunan `[src:TS10]` |
| Konteks aktual | Tidak ada | Tidak ada (R011 N/A) |
| Reviewer pass | Tidak ada | ✓ APPROVE |
| Human approval | Tidak ada | PENDING |

**Koreksi:** RPP di `output/` tidak dihapus (bukti proses), tetapi **bukan bagian pipeline
EduCraft** dan tidak boleh disebut sebagai materi yang lolos gerbang. RPP di
`03_Hasil/edu_output_tata_surya/` adalah versi kanonik yang tergrounding.

---

## 7. PENUTUPAN GERBANG APPROVAL — 5 November 2026

**Waktu:** 2026-11-05 15:01–15:05 GMT+7 · **Oleh:** Orchestrator atas keputusan guru

### 7.1 Keputusan guru

| # | Butir | Keputusan | Dampak pada berkas |
|---|-------|-----------|--------------------|
| 1 | `[src:TS10]` nama & urutan 8 planet | ✅ Disetujui boleh diujikan | RPP §D.2, kuis 7 & 8, slide 3 — penanda "wajib validasi" diganti status disetujui |
| 2 | `[src:TS11]` definisi rotasi & revolusi | ✅ Disetujui boleh diujikan | RPP §D.3–D.4, kuis 3, slide 4–5 — idem |
| 3 | Koreksi fase B → C | ✅ Diterima | Run config catatan fase dinyatakan sah |
| 4 | Kunci butir kuis 13 | ✅ Diperbaiki | Butir ditulis ulang; kunci diubah dari "tidak ada siang dan malam" menjadi "siang-malam berlangsung sangat lama" |

### 7.2 Alasan perbaikan butir 13

Kunci lama menyatakan bahwa bila bumi berhenti berotasi, "tidak ada siang dan malam". Pernyataan itu
keliru: bila rotasi berhenti namun revolusi berlanjut, bumi tetap mengalami siang dan malam, hanya
satu siklusnya berlangsung sekitar satu tahun (masing-masing fase sekitar enam bulan). Butir lama
mengajarkan miskonsepsi, sehingga ditulis ulang — bukan sekadar diganti kuncinya.

### 7.3 Temuan yang belum diselesaikan

Empat hal berikut ditemukan saat verifikasi silang dan **belum** diputuskan guru:

| # | Temuan | Lokasi | Sifat |
|---|--------|--------|-------|
| 1 | ~~§A menyatakan 2 pertemuan, §E hanya menguraikan 1 pertemuan (80 menit)~~ — **SELESAI 5 Nov 2026 15:12**: §E dipecah menjadi Pertemuan 1 dan Pertemuan 2, masing-masing 80 menit | `01_RPP_Tata_Surya.md` §E | ✅ Ditutup |
| 2 | ~~Ciri-ciri planet tidak dirinci sumber utama~~ — **SELESAI 5 Nov 2026 15:25**: ditambahkan `[src:TS12]` dari NASA + tabel ciri di §D.2a dan slide 3b | `01_RPP_Tata_Surya.md`, `03_Slide_Outline_Tata_Surya.md` | ✅ Ditutup |
| 3 | Alokasi waktu 2 × 2 JP tidak berasal dari sumber | `01_RPP_Tata_Surya.md` §A | Usulan, kini ditandai eksplisit sebagai usulan di §E |
| 4 | ~~Rubrik 4/3/2/1 tanpa tag dan tanpa penanda "usulan"~~ — **SELESAI 5 Nov 2026 15:32**: diganti rubrik berdeskriptor 4 aspek × 3 tingkat, ditandai usulan, di §F.1–F.2 | `01_RPP_Tata_Surya.md` | ✅ Ditutup |
| 5 | ~~Pre-test (soal 1–5) dan post-test (soal 6–15) memakai butir berbeda~~ — **SELESAI 5 Nov 2026 15:25**: soal 3, 4, 5 diulang sebagai post-test 16–18; skema gain ditambahkan | `02_Kuis_PrePost_Tata_Surya.md` | ✅ Ditutup |

**Catatan Orchestrator.** Butir 1, 2, dan 5 telah diselesaikan pada 5 November 2026 atas keputusan
guru. Butir 3 dan 4 tetap terbuka dan tidak menghalangi pemakaian materi.

---

## 8. Penambahan sumber dan restrukturisasi kuis — 5 November 2026, 15:25 GMT+7

### 8.1 `[src:TS12]` — ciri-ciri umum planet

**Masalah.** `[src:TS2]` menyebut murid mempelajari "ciri-ciri umum planet", tetapi Panduan IPAS tidak
merinci satu pun ciri. RPP sebelumnya sengaja mengosongkannya.

**Keputusan guru.** Tambahkan ciri-ciri planet dengan sumber tersendiri.

**Tindakan.** Entri baru `[src:TS12]` ditambahkan ke `source_material_tata_surya.md` (keempat salinan
disinkronkan, checksum identik). Provenance dinyatakan eksplisit:

| Aspek | Isi |
|-------|-----|
| Sumber | NASA Science — *About the Planets*, *Venus Facts*, *Jupiter Facts* |
| Tanggal verifikasi | 5 November 2026 |
| Status | **Referensi tambahan**, bukan kutipan Panduan IPAS |
| Isi | Urutan + peringkat ukuran 8 planet · pengelompokan (planet dalam / raksasa gas / raksasa es) · Venus terpanas · Jupiter terbesar + Bintik Merah Besar |

**Mengapa NASA dan bukan angka karangan.** Ciri-ciri planet adalah isi paling lazim di buku pelajaran
dan justru karena itu paling mudah tergelincir menjadi klaim tanpa dasar. NASA dipilih karena
otoritatif, dapat diperiksa ulang lewat tautan, dan rumusannya sederhana enough untuk Fase C.

**Batas yang tetap berlaku.** Ciri yang tidak dikutip langsung dari NASA tidak ditulis. Angka seperti
suhu permukaan planet selain Venus, jumlah satelit per planet, dan diameter tidak dicantumkan.

### 8.2 Kuis: 3 butir pre-test diujikan ulang

**Masalah.** Pre-test memakai soal 1–5, post-test memakai soal 6–15. Seluruh butir berbeda, sehingga
gain score tidak dapat dibandingkan butir-per-butir.

**Keputusan guru.** Ambil 3 soal pre-test dan ujikan kembali di post-test.

**Tindakan.** Soal pre-test **3, 4, dan 5** diulang identik sebagai post-test **16, 17, dan 18**.

| Alasan pemilihan | Penjelasan |
|------------------|------------|
| Menyasar inti CP | Ketiganya menguji definisi rotasi, akibat rotasi, dan akibat revolusi — inti CP-C.2.1.5 |
| Bukan hafalan dangkal | Soal 1 (jumlah planet) dan 2 (pusat tata surya) sengaja tidak dipilih karena hampir semua murid sudah benar sejak awal, sehingga tidak peka terhadap perubahan |

**Skema penilaian baru.** Post-test 13 butir (6–18), skor maksimal **180**. Skor gain dihitung khusus
dari pasangan 3↔16, 4↔17, 5↔18 dengan rentang −30 s.d. +30, beserta tabel tafsir.

**Catatan pencetakan.** Label "butir ulang" harus dihapus pada lembar murid agar murid tidak menyadari
butir mana yang diulang. Label dipertahankan pada lembar guru.

### 8.3 Cakupan yang masih kosong

Tujuan pembelajaran 3 (ciri umum planet, `[src:TS12]`) **belum memiliki butir kuis**. Dicatat di
`02_Kuis_PrePost_Tata_Surya.md` §Batas cakupan kuis, bukan dibiarkan tanpa keterangan.

### 8.4 Verifikasi

```
PASS: 163 tag, 0 dangling, 0 class violations
```

Kenaikan dari 127 → 163 tag berasal dari tabel ciri planet (§D.2a), slide 3b, dan tiga butir ulang.
Total proyek: 121 + 115 + 176 + 163 = **575 tag**.

**Koreksi alat, bukan angka.** Pemeriksaan pertama setelah penambahan melaporkan 165 tag, lalu 166 saat
dijalankan lewat `doctor.py`. Selisihnya berasal dari `04_Lembar_Persetujuan_Guru.md` yang ikut terpindai
sebagai draf, padahal ia catatan keputusan manusia yang menyebut tag sebagai rujukan, bukan klaim fakta.
`tools/check_grounding.py` diperbaiki agar berkas bernama `*persetujuan*` atau `*approval*` dikenali
sebagai metadata, sejalan dengan pengecualian `*review*` yang sudah ada. Uji regresi: run `-001` 121,
`-002` 115, `-004` 176 — tidak berubah. Angka sah untuk run ini adalah **163**.

---

## 9. Penggantian rubrik 4/3/2/1 — 5 November 2026, 15:32 GMT+7

### 9.1 Masalah pada rumusan lama

Rumusan lama di §F berbunyi: *"4 = menjelaskan lengkap & ter-grounding; 3 = cukup; 2 = sebagian;
1 = minimal."* Empat kelemahan:

| # | Kelemahan | Akibat |
|---|-----------|--------|
| 1 | Tingkat 3, 2, 1 tidak punya deskriptor | "cukup", "sebagian", "minimal" tidak menyatakan perilaku yang dapat diamati; dua guru dapat memberi angka berbeda untuk jawaban yang sama |
| 2 | Memakai istilah internal "ter-grounding" | Kosakata pipeline, bukan kosakata guru atau murid Fase C |
| 3 | Tidak menyebut aspek yang dinilai | Tidak jelas apakah yang dinilai urutan planet, rotasi, revolusi, atau laporan |
| 4 | Tidak berasal dari sumber dan tidak ditandai usulan | Panduan IPAS hanya menetapkan empat bentuk asesmen `[src:TS8]`, tanpa rubrik |

### 9.2 Keputusan guru

Guru memilih **opsi B**: ganti dengan rubrik berdeskriptor, bukan menerima apa adanya dan bukan
menghapus rubrik.

### 9.3 Rubrik baru

Empat aspek × tiga tingkat, setiap sel berisi perilaku yang dapat diamati:

| Aspek | Sumber rujukan |
|-------|----------------|
| Urutan & ciri planet | `[src:TS10]` `[src:TS12]` |
| Penjelasan sebab-akibat | `[src:TS3]` `[src:TS4]` `[src:TS11]` |
| Pelaksanaan penyelidikan | `[src:TS7]` |
| Kesimpulan berbasis bukti | `[src:TS7]` |

Tingkat: **Berkembang (1) · Cakap (2) · Mahir (3)** — mengikuti bentuk yang sudah dipakai run
`-004` (Perubahan Wujud Zat) agar penilaian antar-run konsisten.

**Batas yang dinyatakan.** Rubrik ditandai eksplisit sebagai *usulan rancangan guru, bukan kutipan
sumber*. Ambang kategori (10–12 Mahir, 7–9 Cakap, 4–6 Berkembang) juga ditandai usulan. Kriteria
ketuntasan dan bobot nilai tidak ditetapkan, karena sumber tidak memuatnya dan itu wewenang guru.

**Pemisahan instrumen.** Rubrik hanya untuk laporan penyelidikan Pertemuan 2. Tes tertulis tetap
memakai kunci jawaban di `02_Kuis_PrePost_Tata_Surya.md` — dua instrumen tidak dicampur.

### 9.4 Verifikasi

```
PASS: 178 tag, 0 dangling, 0 class violations
```

Tag naik 163 → 178 (+15). Kenaikan berasal dari 12 sel rubrik yang bertag, empat baris tabel aspek,
dan catatan pemakaian. Total proyek: 121 + 115 + 176 + 178 = **590 tag**.

> **Koreksi catatan.** Draf pertama bagian ini menyatakan jumlah tag tidak berubah. Itu keliru —
> penulis mengira tabel baru menggantikan satu butir lama secara imbang. Pemeriksaan ulang
> menunjukkan kenaikan 15 tag. Angka yang benar adalah 178.

---

## 10. Perubahan konvensi penulisan sumber — 5 November 2026, 15:31 GMT+7

### 10.1 Keputusan guru

Kode `[src:TS1]` dan sejenisnya dinilai mengganggu dokumen yang dipakai guru dan murid. Guru meminta:

1. RPP dan slide **menyebut nama sumber**, bukan kode.
2. Konvensi itu dijadikan **aturan tetap** untuk RPP dan slide.
3. Kuis **tidak menampilkan sumber acuan** sama sekali.

### 10.2 Konvensi baru

| Jenis sumber | Cara menulis |
|--------------|--------------|
| Dokumen kurikulum | (Panduan IPAS, hlm. 45–47) |
| Butir capaian pembelajaran | (Panduan IPAS, CP-C.2.1.5) |
| Rujukan ilmiah tambahan | (NASA, "About the Planets") |
| Turunan tim yang disetujui | (pengetahuan sains umum, disetujui guru 5 Nov 2026) |
| Rancangan guru | (usulan guru) |

**Aturan penempatan.** Sumber ditulis satu kali di awal subbagian RPP, atau pada baris **Sumber** per
slide. Sumber hanya diulang pada butir bila berbeda dari sumber subbagian. Kuis tidak memakai konvensi
ini sama sekali.

### 10.3 Berkas yang berubah

| Berkas | Perubahan |
|--------|-----------|
| `01_RPP_Tata_Surya.md` | Ditulis ulang; seluruh kode tag dihapus, diganti nama sumber per subbagian; ditambah blok "Aturan penulisan sumber" di kepala dokumen |
| `03_Slide_Outline_Tata_Surya.md` | Ditulis ulang; setiap slide mendapat baris **Sumber** |
| `02_Kuis_PrePost_Tata_Surya.md` | Seluruh kode tag dihapus; kolom "Tag" pada tabel kunci diganti "Kunci"; paragraf yang menyebut asal butir 8 dihapus |
| `05_Jejak_Sumber.md` | **Berkas baru** — lampiran pemetaan mesin antara pernyataan dan entri sumber, untuk audit |

### 10.4 Konsekuensi terhadap verifikasi — dinyatakan terbuka

Ini perubahan yang **melemahkan** pemeriksaan otomatis, dan itu harus dikatakan apa adanya:

| Sebelum | Sesudah |
|---------|---------|
| `check_grounding.py` memeriksa tag **di dalam** RPP, kuis, dan slide | `check_grounding.py` hanya memeriksa `05_Jejak_Sumber.md` |
| Kalimat tanpa tag di draf tidak terdeteksi, tetapi kalimat **bertag** diperiksa resolusinya | Kalimat di RPP tidak lagi diperiksa mesin sama sekali |

**Artinya:** bila seseorang kelak menambah pernyataan faktual ke RPP tanpa menyebut sumbernya, alat
tidak akan menangkapnya. Yang tersisa adalah pemeriksaan manual oleh reviewer.

**Mitigasi yang dipasang.** `tools/check_sitasi.py` dibuat untuk menjaga konvensi, dengan lima aturan:
R1 tidak ada kode tag di RPP/slide/kuis; R2 setiap slide punya baris Sumber; R3 setiap subbagian §D
punya penanda sumber; R4 kuis tidak punya baris Sumber; R5 lampiran jejak sumber ada dan memetakan
ketiga dokumen. Alat ini sudah diuji negatif: menyisipkan satu tag ke RPP membuatnya gagal, dan
berkas dipulihkan sesudahnya.

`tools/doctor.py` menjalankan alat itu sebagai langkah 7.

### 10.5 Verifikasi

```
check_grounding.py  : PASS: 109 tag, 0 dangling, 0 class violations
check_sitasi.py     : PASS: 7 checks, convention consistent
doctor.py           : 12 passed / 0 failed / 0 warning
```

Jumlah tag turun 178 → 109 karena tag di RPP, kuis, dan slide dihapus; yang tersisa adalah pemetaan
di lampiran. Total proyek: 121 + 115 + 176 + 109 = **521 tag**.

### 7.4 Status akhir

| Item | Nilai |
|------|-------|
| Gerbang approval | ✅ **LULUS** |
| Pemakaian di kelas | ✅ Diizinkan |
| Publikasi / distribusi | 🔒 **LOCKED** — belum diminta |
| Butir terbuka | 1 (lihat §7.3; butir 1, 2, 4, 5 sudah ditutup) |
| Berkas persetujuan | `04_Lembar_Persetujuan_Guru.md` |

---

## 11. Revisi rubrik sebelum persetujuan — 5 November 2026, 16:51 GMT+7

### 11.1 Mengapa revisi ini ada

§9 mencatat bahwa guru memilih **opsi B** (ganti skala 4/3/2/1 dengan rubrik berdeskriptor). Pilihan
itu adalah persetujuan atas **pendekatan**, bukan atas isi rubriknya. Lembar persetujuan §3 butir 2
sempat menandainya "✅ Selesai", padahal RPP §F.1 sendiri masih menulis "menunggu persetujuan guru".
Ketika rubrik ditampilkan untuk ditinjau, empat masalah ditemukan sebelum guru memutuskan.

### 11.2 Empat masalah dan perbaikannya

| # | Masalah | Perbaikan |
|---|---------|-----------|
| 1 | Aspek bernama "urutan **& ciri** planet", tetapi ketiga deskriptornya hanya menilai urutan dan pengelompokan. Tujuan pembelajaran 3 menuntut "kelompok planet dalam dan planet raksasa, **serta peringkat ukurannya**" — peringkat ukuran tidak dinilai sama sekali | Tingkat Mahir kini menuntut ketiganya: urutan benar, pengelompokan benar, **dan** peringkat ukuran. Materi §D.2a sudah memuat kolom "Peringkat ukuran", jadi tuntutan ini didukung isi |
| 2 | "…salah satunya benar" ambigu — bisa berarti "hanya satu yang benar (satunya salah)" atau "minimal satu benar" | Diganti "minimal satu dari keduanya benar" |
| 3 | Tingkat 1 aspek 1 menyatukan dua kegagalan berbeda tanpa menyatakannya | Ditulis eksplisit: "kurang dari enam planet, **atau** menyebut delapan planet tetapi urutannya keliru" |
| 4 | Aturan §F.1 no. 3 ("belum teramati → jangan beri angka") bertabrakan dengan ambang §F.2 yang mengasumsikan keempat aspek selalu teramati. Murid yang absen pada Pertemuan 2 akan tampak "Berkembang" hanya karena satu aspek tidak sempat dinilai | §F.2 mendapat tabel penyesuaian: 4 aspek dijumlahkan langsung; 3 aspek dijumlahkan lalu **÷3 ×4** dan dibulatkan; 2 aspek atau kurang **tidak diberi kategori**, dilaporkan "belum lengkap" |

### 11.3 Yang tidak berubah

Isi ketiga tingkat pada aspek 2–4, dan **ambang 10–12 / 7–9 / 4–6**, tidak diubah. Revisi ini hanya
memperbaiki apa yang diukur pada aspek 1, kejelasan satu frasa, dan aturan pengolahan skor.

### 11.4 Status persetujuan

**Rubrik disetujui guru 5 November 2026, 16:54 GMT+7** — setelah revisi 16:51 ditampilkan dan ditinjau.
Keputusan dicatat sebagai §2.5 di `04_Lembar_Persetujuan_Guru.md`; RPP §F.1 dan catatan §F.2 kini
menyatakan status disetujui, bukan lagi "menunggu persetujuan guru".

Yang **tidak** ikut disetujui: kriteria ketuntasan minimal dan bobot nilai. Keduanya tetap menjadi
wewenan guru saat memakai rubrik, karena Panduan IPAS tidak memuatnya dan tim tidak boleh mengarang.

### 11.5 Verifikasi

Rubrik memakai nama sumber dalam kata, bukan kode `[src:]`, sesuai konvensi §10. Tidak ada tag baru
dan tidak ada tag yang berubah, sehingga `check_grounding.py` tetap **PASS 109 tag** dan
`check_sitasi.py` tetap **PASS 7/7**.
