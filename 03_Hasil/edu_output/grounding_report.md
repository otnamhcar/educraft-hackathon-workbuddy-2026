# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output`  
**Knowledge layer:** `08_Referensi`  
**Verdict:** **PASS** — 121 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `audit_log.md`

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `01_lesson_plan.md` | 32 | 0 | 0 |
| `02_quiz_pretest_posttest.md` | 39 | 0 | 0 |
| `03_slide_outline.md` | 19 | 0 | 0 |
| `04_artikel.md` | 17 | 0 | 0 |
| `05_infographic_brief.md` | 14 | 0 | 0 |
| `06_Materi_Guru_Energi_Alternatif.md` | 0 | 0 | 0 |
| `koreksi_format_rendering.md` | 0 | 0 | 0 |

## Temuan

- Tidak ada temuan. Setiap tag menunjuk anchor yang ada dan kelasnya sesuai.

## Rincian tag

### `01_lesson_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 4 | `[src:1]` | fact | **OK** | source_material_ipas.md · Identitas Modul |
| 4 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 4 | `[src:C4]` | curriculum | **OK** | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 4 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 4 | `[src:B3]` | curriculum | **OK** | cp_ipas.md · Menghasilkan solusi untuk masalah yang berkaitan dengan pelestarian su |
| 4 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 4 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 4 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 15 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 15 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 17 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 17 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 21 | `[src:2]` | fact | **OK** | source_material_ipas.md · Kelestarian Alam |
| 22 | `[src:4]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Sektor Produksi |
| 22 | `[src:5]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 23 | `[src:7]` | fact | **OK** | source_material_ipas.md · Upaya Penanggulangan |
| 24 | `[src:8]` | fact | **OK** | source_material_ipas.md · Peran Siswa |
| 25 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 25 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 29 | `[src:3]` | fact | **OK** | source_material_ipas.md · Kabut Asap (Haze) |
| 30 | `[src:4]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Sektor Produksi |
| 31 | `[src:5]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 32 | `[src:6]` | fact | **OK** | source_material_ipas.md · Dampak Kesehatan Masyarakat |
| 35 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 36 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 39 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 40 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 40 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 43 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 44 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 64 | `[src:1]` | fact | **OK** (ulang) | source_material_ipas.md · Identitas Modul |
| 64 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |

### `02_quiz_pretest_posttest.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 4 | `[src:1]` | fact | **OK** | source_material_ipas.md · Identitas Modul |
| 4 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 4 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 4 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 16 | `[src:2]` | fact | **OK** | source_material_ipas.md · Kelestarian Alam |
| 23 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 30 | `[src:7]` | fact | **OK** | source_material_ipas.md · Upaya Penanggulangan |
| 37 | `[src:5]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 44 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 51 | `[src:4]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Sektor Produksi |
| 51 | `[src:3]` | fact | **OK** | source_material_ipas.md · Kabut Asap (Haze) |
| 58 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 58 | `[src:8]` | fact | **OK** | source_material_ipas.md · Peran Siswa |
| 67 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 71 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 78 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 82 | `[src:5]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 86 | `[src:5]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 90 | `[src:5]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 94 | `[src:6]` | fact | **OK** | source_material_ipas.md · Dampak Kesehatan Masyarakat |
| 101 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 105 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 109 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 113 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 117 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 121 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 124 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 127 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 130 | `[src:4]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Sektor Produksi |
| 133 | `[src:5]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 136 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 139 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 141 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 142 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 142 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 157 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 158 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 159 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 159 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |

### `03_slide_outline.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 4 | `[src:1]` | fact | **OK** | source_material_ipas.md · Identitas Modul |
| 4 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 4 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 4 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 11 | `[src:2]` | fact | **OK** | source_material_ipas.md · Kelestarian Alam |
| 14 | `[src:4]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Sektor Produksi |
| 15 | `[src:5]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 18 | `[src:3]` | fact | **OK** | source_material_ipas.md · Kabut Asap (Haze) |
| 22 | `[src:6]` | fact | **OK** | source_material_ipas.md · Dampak Kesehatan Masyarakat |
| 23 | `[src:5]` | fact | **OK** (ulang) | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 26 | `[src:2]` | fact | **OK** (ulang) | source_material_ipas.md · Kelestarian Alam |
| 30 | `[src:7]` | fact | **OK** | source_material_ipas.md · Upaya Penanggulangan |
| 31 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 35 | `[src:8]` | fact | **OK** | source_material_ipas.md · Peran Siswa |
| 36 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 38 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 43 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 49 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 49 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |

### `04_artikel.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:1]` | fact | **OK** | source_material_ipas.md · Identitas Modul |
| 3 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 3 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 3 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 7 | `[src:1]` | fact | **OK** (ulang) | source_material_ipas.md · Identitas Modul |
| 10 | `[src:2]` | fact | **OK** | source_material_ipas.md · Kelestarian Alam |
| 13 | `[src:4]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Sektor Produksi |
| 13 | `[src:5]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 15 | `[src:6]` | fact | **OK** | source_material_ipas.md · Dampak Kesehatan Masyarakat |
| 19 | `[src:7]` | fact | **OK** | source_material_ipas.md · Upaya Penanggulangan |
| 20 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 23 | `[src:8]` | fact | **OK** | source_material_ipas.md · Peran Siswa |
| 23 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |
| 26 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 28 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 31 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 31 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |

### `05_infographic_brief.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 4 | `[src:1]` | fact | **OK** | source_material_ipas.md · Identitas Modul |
| 4 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 4 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 4 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 16 | `[src:2]` | fact | **OK** | source_material_ipas.md · Kelestarian Alam |
| 18 | `[src:4]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Sektor Produksi |
| 18 | `[src:5]` | fact | **OK** | source_material_ipas.md · Dampak Ekonomi — Pariwisata |
| 21 | `[src:7]` | fact | **OK** | source_material_ipas.md · Upaya Penanggulangan |
| 22 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 23 | `[src:8]` | fact | **OK** | source_material_ipas.md · Peran Siswa |
| 25 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 26 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 29 | `[src:7]` | fact | **OK** (ulang) | source_material_ipas.md · Upaya Penanggulangan |
| 29 | `[src:8]` | fact | **OK** (ulang) | source_material_ipas.md · Peran Siswa |

### `06_Materi_Guru_Energi_Alternatif.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|

### `koreksi_format_rendering.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
