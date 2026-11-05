# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_tata_surya`  
**Knowledge layer:** `03_Hasil/referensi`  
**Verdict:** **PASS** — 113 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `audit_log.md`

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_plan.md` | 15 | 0 | 0 |
| `01_RPP_Tata_Surya.md` | 37 | 0 | 0 |
| `02_Kuis_PrePost_Tata_Surya.md` | 38 | 0 | 0 |
| `03_Slide_Outline_Tata_Surya.md` | 23 | 0 | 0 |

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
| 13 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 13 | `[src:C5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sistem tata surya, serta kaitannya dengan rotasi dan revol |
| 17 | `[src:TS1]` | unknown | **OK** | source_material_tata_surya.md · Anggota tata surya |
| 18 | `[src:TS2]` | unknown | **OK** | source_material_tata_surya.md · Ciri dan urutan planet |
| 18 | `[src:TS10]` | unknown | **OK** | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 19 | `[src:TS3]` | unknown | **OK** | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 20 | `[src:TS4]` | unknown | **OK** | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 21 | `[src:TS6]` | unknown | **OK** | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 22 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 27 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 28 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 31 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 32 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 35 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 36 | `[src:TS11]` | unknown | **OK** | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 39 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 40 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 43 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 44 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 45 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 46 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 47 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 50 | `[src:TS5]` | unknown | **OK** | source_material_tata_surya.md · Pentingnya memahami tata surya |
| 56 | `[src:TS7]` | unknown | **OK** | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 56 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 56 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 56 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 60 | `[src:TS8]` | unknown | **OK** | source_material_tata_surya.md · Bentuk asesmen |
| 61 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 62 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 63 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 63 | `[src:TS9]` | unknown | **OK** | source_material_tata_surya.md · Refleksi pribadi murid |
| 67 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 67 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 71 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 74 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 74 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |

### `02_Kuis_PrePost_Tata_Surya.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 10 | `[src:TS1]` | unknown | **OK** | source_material_tata_surya.md · Anggota tata surya |
| 17 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 24 | `[src:TS3]` | unknown | **OK** | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 24 | `[src:TS11]` | unknown | **OK** | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 31 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 38 | `[src:TS4]` | unknown | **OK** | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 49 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 56 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 56 | `[src:TS10]` | unknown | **OK** | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 63 | `[src:TS2]` | unknown | **OK** | source_material_tata_surya.md · Ciri dan urutan planet |
| 63 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 70 | `[src:TS6]` | unknown | **OK** | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 77 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 84 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 91 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 98 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 98 | `[src:TS7]` | unknown | **OK** | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 105 | `[src:TS8]` | unknown | **OK** | source_material_tata_surya.md · Bentuk asesmen |
| 112 | `[src:TS9]` | unknown | **OK** | source_material_tata_surya.md · Refleksi pribadi murid |
| 120 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 121 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 122 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 122 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 123 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 124 | `[src:TS4]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 125 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 126 | `[src:TS1]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Anggota tata surya |
| 126 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 127 | `[src:TS2]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Ciri dan urutan planet |
| 127 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 128 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 129 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 130 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 131 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 132 | `[src:TS3]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 132 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 133 | `[src:TS8]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Bentuk asesmen |
| 134 | `[src:TS9]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Refleksi pribadi murid |

### `03_Slide_Outline_Tata_Surya.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 11 | `[src:TS1]` | unknown | **OK** | source_material_tata_surya.md · Anggota tata surya |
| 15 | `[src:TS2]` | unknown | **OK** | source_material_tata_surya.md · Ciri dan urutan planet |
| 15 | `[src:TS10]` | unknown | **OK** | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 20 | `[src:TS3]` | unknown | **OK** | source_material_tata_surya.md · Rotasi bumi menyebabkan siang dan malam |
| 21 | `[src:TS11]` | unknown | **OK** | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 25 | `[src:TS4]` | unknown | **OK** | source_material_tata_surya.md · Revolusi bumi menyebabkan perubahan musim |
| 26 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |
| 30 | `[src:TS6]` | unknown | **OK** | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 31 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 32 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 33 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 36 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 37 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 38 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 39 | `[src:TS6]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Topik relevan dalam kehidupan nyata |
| 42 | `[src:TS7]` | unknown | **OK** | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 43 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 44 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 45 | `[src:TS7]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Pengalaman belajar yang disarankan |
| 48 | `[src:TS8]` | unknown | **OK** | source_material_tata_surya.md · Bentuk asesmen |
| 49 | `[src:TS9]` | unknown | **OK** | source_material_tata_surya.md · Refleksi pribadi murid |
| 56 | `[src:TS10]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Delapan planet berurutan dari matahari — **TURUNAN TIM, BUKAN KUTIPAN* |
| 56 | `[src:TS11]` | unknown | **OK** (ulang) | source_material_tata_surya.md · Konsep rotasi dan revolusi — **TURUNAN TIM, BUKAN KUTIPAN** |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
