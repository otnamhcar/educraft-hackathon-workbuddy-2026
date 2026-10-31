# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_wujud_zat`  
**Knowledge layer:** `03_Hasil/referensi`  
**Verdict:** **PASS** — 115 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `05_review.md`, `11_Memo_Koreksi_Tag_2026-10-31.md`, `audit_log.md`, `grounding_report.md`

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_plan.md` | 15 | 0 | 0 |
| `01_artikel.md` | 32 | 0 | 0 |
| `02_infographic_brief.md` | 28 | 0 | 0 |
| `03_video_storyboard.md` | 4 | 0 | 0 |
| `04_kuis_prepost.md` | 36 | 0 | 0 |

## Temuan

- Tidak ada temuan. Setiap tag menunjuk anchor yang ada dan kelasnya sesuai.

## Rincian tag

### `00_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 6 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 6 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 6 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 6 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 47 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 48 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 48 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 49 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 51 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 75 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 75 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 105 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 106 | `[src:W2]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 106 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 107 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |

### `01_artikel.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 3 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 8 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 12 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 12 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 14 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 18 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 22 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 23 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 24 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 25 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 26 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 27 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 29 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 33 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 33 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 35 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 35 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 35 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 35 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 39 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 41 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 42 | `[src:W4]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 43 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 44 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 46 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 50 | `[src:W6]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 50 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 52 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 58 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 58 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 59 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `02_infographic_brief.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 3 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 3 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 3 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 11 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 12 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 12 | `[src:W2]` | fact | **OK** | source_material_wujud_zat.md · Enam proses perubahan wujud |
| 12 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 39 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 47 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 48 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 49 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 56 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 57 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 58 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 59 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 60 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 61 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 68 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 69 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 71 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 76 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 77 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 78 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 79 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 83 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 89 | `[src:W7]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pencatatan data percobaan |
| 102 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |

### `03_video_storyboard.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 3 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 3 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 3 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |

### `04_kuis_prepost.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:W1]` | fact | **OK** | source_material_wujud_zat.md · Tiga wujud zat |
| 3 | `[src:W11]` | fact | **OK** | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 16 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 17 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 18 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 19 | `[src:W10]` | fact | **OK** | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 20 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 21 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 22 | `[src:W3]` | fact | **OK** | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 34 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 35 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 36 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 37 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 38 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 39 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 40 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 41 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 42 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 43 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 44 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 45 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 46 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 46 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 47 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 53 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 54 | `[src:W3]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Faktor pemicu: suhu |
| 54 | `[src:W4]` | fact | **OK** | source_material_wujud_zat.md · Contoh fenomena sehari-hari |
| 55 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 56 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 57 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 58 | `[src:W6]` | fact | **OK** | source_material_wujud_zat.md · Pengalaman belajar yang disarankan |
| 58 | `[src:W7]` | fact | **OK** | source_material_wujud_zat.md · Pencatatan data percobaan |
| 101 | `[src:W1]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Tiga wujud zat |
| 101 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 101 | `[src:W10]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Pemetaan arah perubahan — **TURUNAN TIM, BUKAN KUTIPAN** |
| 101 | `[src:W11]` | fact | **OK** (ulang) | source_material_wujud_zat.md · Konsep pendukung & penerapan — **TURUNAN TIM, BUKAN KUTIPAN** |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
