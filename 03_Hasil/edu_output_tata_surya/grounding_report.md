# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_tata_surya`  
**Knowledge layer:** `05_Bukti_Proses/skills_package/edu-orchestrator/assets`  
**Verdict:** **PASS** — 109 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `04_Lembar_Persetujuan_Guru.md`, `audit_log.md`, `grounding_report.md`

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_plan.md` | 15 | 0 | 0 |
| `01_RPP_Tata_Surya.md` | 0 | 0 | 0 |
| `02_Kuis_PrePost_Tata_Surya.md` | 0 | 0 | 0 |
| `03_Slide_Outline_Tata_Surya.md` | 0 | 0 | 0 |
| `05_Jejak_Sumber.md` | 94 | 0 | 0 |

## Temuan

- Tidak ada temuan. Setiap tag menunjuk anchor yang ada dan kelasnya sesuai.

## Rincian tag

### `00_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 13 | `[src:TS1]` | unknown | **OK** | source_material_tata_surya.md · Anggota tata surya |
| 13 | `[src:TS11]` | unknown | **OK** | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 28 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 29 | `[src:TS2]` | unknown | **OK** | source_material_tata_surya.md · Ciri dan urutan planet |
| 29 | `[src:TS10]` | unknown | **OK** | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 30 | `[src:TS3]` | unknown | **OK** | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 30 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 31 | `[src:TS4]` | unknown | **OK** | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 31 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 32 | `[src:TS6]` | unknown | **OK** | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 33 | `[src:TS7]` | unknown | **OK** | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 34 | `[src:TS8]` | unknown | **OK** | source_material_tata_surya.md · Bentuk asesmen |
| 34 | `[src:TS9]` | unknown | **OK** | source_material_tata_surya.md · Refleksi pribadi murid |
| 38 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 39 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |

### `01_RPP_Tata_Surya.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|

### `02_Kuis_PrePost_Tata_Surya.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|

### `03_Slide_Outline_Tata_Surya.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|

### `05_Jejak_Sumber.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 17 | `[src:TS1]` | unknown | **OK** | source_material_tata_surya.md · Anggota tata surya |
| 18 | `[src:TS2]` | unknown | **OK** | source_material_tata_surya.md · Ciri dan urutan planet |
| 19 | `[src:TS3]` | unknown | **OK** | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 20 | `[src:TS4]` | unknown | **OK** | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 21 | `[src:TS5]` | unknown | **OK** | source_material_tata_surya.md · Pentingnya memahami tata surya |
| 22 | `[src:TS6]` | unknown | **OK** | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 23 | `[src:TS7]` | unknown | **OK** | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 24 | `[src:TS8]` | unknown | **OK** | source_material_tata_surya.md · Bentuk asesmen |
| 25 | `[src:TS9]` | unknown | **OK** | source_material_tata_surya.md · Refleksi pribadi murid |
| 26 | `[src:TS10]` | unknown | **OK** | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 27 | `[src:TS11]` | unknown | **OK** | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 28 | `[src:TS12]` | unknown | **OK** | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 29 | `[src:CP]` | curriculum | **OK** | cp_ipas.md ·  |
| 30 | `[src:C5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sistem tata surya, serta kaitannya dengan rotasi dan revol |
| 36 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md ·  |
| 36 | `[src:C5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sistem tata surya, serta kaitannya dengan rotasi dan revol |
| 37 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 38 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 38 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 39 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 40 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 41 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 42 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 43 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 44 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 45 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 46 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 47 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 48 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 49 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 50 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 51 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 52 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 53 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 54 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 55 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 56 | `[src:TS5]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pentingnya memahami tata surya |
| 57 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 58 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 58 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 58 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 59 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 60 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 60 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 60 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 61 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 62 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 63 | `[src:TS9]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Refleksi pribadi murid |
| 64 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 65 | `[src:TS9]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Refleksi pribadi murid |
| 66 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 66 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 67 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 67 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 67 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 68 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 69 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 79 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 80 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 80 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 81 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 82 | `[src:TS12]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri-ciri umum planet — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IP |
| 83 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 84 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 85 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 86 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 87 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 88 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 89 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 90 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 91 | `[src:TS9]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Refleksi pribadi murid |
| 99 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 100 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 101 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 101 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 102 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 103 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 104 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 105 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 105 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 106 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 106 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 107 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 108 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 109 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 110 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 111 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 111 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 112 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 113 | `[src:TS9]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Refleksi pribadi murid |
| 114 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 114 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 115 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 116 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
