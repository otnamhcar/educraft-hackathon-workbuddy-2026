# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_wujud_zat_faseC`  
**Knowledge layer:** `08_Referensi`  
**Verdict:** **PASS** — 212 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `06_review.md`, `07_review_pass2.md`, `08_Lembar_Persetujuan_Guru.md`, `audit_log.md`, `grounding_report.md`

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_plan.md` | 10 | 0 | 0 |
| `01_lesson_plan.md` | 56 | 0 | 0 |
| `02_artikel.md` | 31 | 0 | 0 |
| `03_slide_outline.md` | 36 | 0 | 0 |
| `04_infographic_brief.md` | 27 | 0 | 0 |
| `05_kuis.md` | 52 | 0 | 0 |

## Temuan

- Tidak ada temuan. Setiap tag menunjuk anchor yang ada dan kelasnya sesuai.

## Rincian tag

### `00_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 5 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 5 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 103 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 103 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 103 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 103 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 104 | `[src:B4]` | curriculum | **OK** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 104 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 106 | `[src:B4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 108 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `01_lesson_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 15 | `[src:B4]` | curriculum | **OK** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 16 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 18 | `[src:B4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 27 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 29 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 30 | `[src:W12]` | fact | **OK** | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 32 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 33 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 34 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 36 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 36 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 37 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 39 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 45 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 58 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 59 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 60 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 60 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 61 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 67 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 74 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 75 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 76 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 77 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 77 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 83 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 84 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 85 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 86 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 91 | `[src:W8]` | fact | **OK** | source_material_wujud_zat.md · Bentuk asesmen |
| 100 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 110 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 111 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 112 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 117 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 119 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 122 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 141 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 147 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 157 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 159 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 159 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 170 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 170 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 170 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 171 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 171 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 171 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 172 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 172 | `[src:W8]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Bentuk asesmen |
| 172 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 173 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 173 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 174 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 174 | `[src:B4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 174 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `02_artikel.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 13 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 15 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 19 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 21 | `[src:W12]` | fact | **OK** | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 35 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 42 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 44 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 47 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 52 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 62 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 63 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 63 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 65 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 66 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 88 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 88 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 101 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 105 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 105 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 110 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 114 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 117 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 122 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 122 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 122 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 122 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 123 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 123 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 123 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 124 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 124 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |

### `03_slide_outline.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 9 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 14 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 15 | `[src:W12]` | fact | **OK** | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 23 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 25 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 26 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 27 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 31 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 32 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 52 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 53 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 58 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 60 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 64 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 75 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 76 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 77 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 79 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 83 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 83 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 85 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 95 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 95 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 105 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 113 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 113 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 113 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 113 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 113 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 113 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 113 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 114 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 114 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 114 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 115 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 115 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `04_infographic_brief.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 18 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 18 | `[src:W12]` | fact | **OK** | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 19 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 19 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 20 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 27 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 28 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 36 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 45 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 53 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 62 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 62 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 64 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 86 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 92 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 97 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 101 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 101 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 101 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 101 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 101 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 101 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 101 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 102 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 102 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 102 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 103 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |

### `05_kuis.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 5 | `[src:W8]` | fact | **OK** | source_material_wujud_zat.md · Bentuk asesmen |
| 19 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 27 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 34 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 42 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 50 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 57 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 68 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 70 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 72 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 79 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 82 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 83 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 93 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 94 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 95 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 96 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 97 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 98 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 102 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 104 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 107 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 113 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 117 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 118 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 122 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 132 | `[src:W12]` | fact | **OK** | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 139 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 146 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 146 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 153 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 153 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 164 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 165 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 166 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 166 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 167 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 167 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 178 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 178 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |
| 192 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 202 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 206 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 206 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 206 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 206 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 206 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 206 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 206 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 207 | `[src:W8]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Bentuk asesmen |
| 207 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** ✅ |
| 207 | `[src:W12]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Ciri-ciri wujud zat — **REFERENSI TAMBAHAN, BUKAN KUTIPAN PANDUAN IPAS |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
