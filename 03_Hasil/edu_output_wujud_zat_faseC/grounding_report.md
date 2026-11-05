# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_wujud_zat_faseC`  
**Knowledge layer:** `05_Bukti_Proses/skills_package/edu-orchestrator/assets`  
**Verdict:** **PASS** — 176 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `06_review.md`, `07_review_pass2.md`, `audit_log.md`, `grounding_report.md`

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_plan.md` | 10 | 0 | 0 |
| `01_lesson_plan.md` | 49 | 0 | 0 |
| `02_artikel.md` | 28 | 0 | 0 |
| `03_slide_outline.md` | 30 | 0 | 0 |
| `04_infographic_brief.md` | 21 | 0 | 0 |
| `05_kuis.md` | 38 | 0 | 0 |

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
| 103 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 103 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 104 | `[src:B4]` | curriculum | **OK** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 104 | `[src:CP]` | curriculum | **OK** | cp_ipas.md ·  |
| 106 | `[src:B4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 108 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md ·  |

### `01_lesson_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 15 | `[src:B4]` | curriculum | **OK** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 16 | `[src:CP]` | curriculum | **OK** | cp_ipas.md ·  |
| 18 | `[src:B4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 27 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 29 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 31 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 32 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 34 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 34 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 35 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 37 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 43 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 56 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 57 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 58 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 59 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 66 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 67 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 68 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md ·  |
| 69 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 69 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 75 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 77 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 78 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md ·  |
| 83 | `[src:W8]` | fact | **OK** | source_material_wujud_zat.md · Bentuk asesmen |
| 92 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 102 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 103 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md ·  |
| 104 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 109 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 111 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 114 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 131 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 138 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 144 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 146 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 146 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 155 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 155 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 155 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 156 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 156 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 156 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 157 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 157 | `[src:W8]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Bentuk asesmen |
| 157 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 158 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 158 | `[src:B4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 158 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md ·  |

### `02_artikel.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 13 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 15 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 22 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 29 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 31 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 34 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 39 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 49 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 50 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 50 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 52 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 53 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 75 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 75 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 88 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 90 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 93 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 97 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 100 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 105 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 105 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 105 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 105 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 106 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 106 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 106 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 107 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 107 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |

### `03_slide_outline.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 9 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 14 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 15 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 16 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 20 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 22 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 27 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 28 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 33 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 35 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 39 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 50 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 51 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 52 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 54 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 58 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 58 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 60 | `[src:CP]` | curriculum | **OK** | cp_ipas.md ·  |
| 68 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 80 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 80 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 80 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 80 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 80 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 80 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 80 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 81 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 81 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 81 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 81 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md ·  |

### `04_infographic_brief.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 18 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 19 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 27 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 36 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 45 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 53 | `[src:W5]` | fact | **OK** | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 62 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 62 | `[src:W9]` | fact | **OK** | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 64 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 87 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 87 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 97 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 97 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 97 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 97 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 97 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 97 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 97 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 98 | `[src:W9]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Keterampilan proses yang dinilai |
| 98 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 98 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |

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
| 130 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 133 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 155 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 164 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 164 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 164 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 164 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 164 | `[src:W5]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konteks isu (lokal, nasional, global) |
| 164 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 164 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 165 | `[src:W8]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Bentuk asesmen |
| 165 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
