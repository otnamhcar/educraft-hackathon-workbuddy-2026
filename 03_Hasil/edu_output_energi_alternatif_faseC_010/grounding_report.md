# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_energi_alternatif_faseC_010`  
**Knowledge layer:** `08_Referensi`  
**Primary source:** `source_material_energi.md`  
**Verdict:** **PASS** — 271 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag, 0 ambigu

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `05_review_temuan.md`, `audit_log.md`, `grounding_report.md`

**Cara tag ditetapkan.** Tag yang hanya ada di satu berkas diselesaikan ke berkas itu (mis. `[src:CA1]` ke `konteks_aktual.md`, `[src:C4]` ke `cp_ipas.md`). Tag yang ada di lebih dari satu lembar sumber diselesaikan ke `source_material_energi.md` karena run ini dibangun di atas lembar itu.

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_source_asal_verbatim.md` | 17 | 0 | 0 |
| `01_plan.md` | 61 | 0 | 0 |
| `02_RPP_Energi_Alternatif_FaseC.md` | 138 | 0 | 0 |
| `03_Kuis_Energi_Alternatif_FaseC.md` | 17 | 0 | 0 |
| `04_Slide_Outline_Energi_Alternatif_FaseC.md` | 38 | 0 | 0 |

## Temuan

- Tidak ada temuan. Setiap tag menunjuk anchor yang ada, tidak ambigu, dan kelasnya sesuai.

## Rincian tag

### `00_source_asal_verbatim.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 8 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 8 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 9 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 9 | `[src:C4]` | curriculum | **OK** | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 9 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 9 | `[src:B3]` | curriculum | **OK** | cp_ipas.md · Menghasilkan solusi untuk masalah yang berkaitan dengan pelestarian su |
| 10 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 10 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 14 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 20 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 25 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 28 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 31 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 36 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 39 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 43 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 47 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |

### `01_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 3 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 3 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 3 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 3 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 3 | `[src:C4]` | curriculum | **OK** | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 3 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 18 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 19 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 19 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 20 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 20 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 20 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 21 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 21 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 22 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 22 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 23 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 24 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 24 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 24 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 24 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 25 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 25 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 34 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 35 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 36 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 37 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 38 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 39 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 40 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 41 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 42 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 43 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 43 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 46 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 47 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 47 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 48 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 48 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 48 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 49 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 50 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 51 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 52 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 53 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 54 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 55 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 56 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 57 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 61 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 62 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 63 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 65 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 67 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 82 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 83 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 83 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 85 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 87 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 88 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |

### `02_RPP_Energi_Alternatif_FaseC.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 13 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 14 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 15 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 16 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 17 | `[src:C4]` | curriculum | **OK** | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 18 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 19 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 20 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 20 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 29 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 30 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 32 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 33 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 34 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 35 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 37 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 39 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 40 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 42 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 42 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 43 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 48 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 49 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 50 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 52 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 56 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 58 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 61 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 62 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 65 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 66 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 70 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 73 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 75 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 77 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 81 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 85 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 85 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 86 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 86 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 92 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 92 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 92 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 95 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 97 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 99 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 100 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 100 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 101 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 103 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 105 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 109 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 110 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 111 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 114 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 119 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 121 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 124 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 125 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 127 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 129 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 131 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 132 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 134 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 137 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 137 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 140 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 140 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 143 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 146 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 150 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 151 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 153 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 155 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 163 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 167 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 168 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 169 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 170 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 171 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 172 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 175 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 182 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 184 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 189 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 197 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 197 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 198 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 198 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 200 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 200 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 201 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 201 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 209 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 210 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 210 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 211 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 211 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 211 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 212 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 213 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 224 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 231 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 231 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 231 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 233 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 233 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 233 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 234 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 252 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 253 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 254 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 255 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 256 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 257 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 268 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 273 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 275 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 277 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 287 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 287 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 291 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 291 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 292 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 292 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 292 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 293 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 293 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 293 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 294 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 294 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 295 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 295 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 295 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 296 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `03_Kuis_Energi_Alternatif_FaseC.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 88 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 89 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 90 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 91 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 92 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 93 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 94 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 95 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 96 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 97 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 97 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 97 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 103 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 104 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 105 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 105 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 105 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |

### `04_Slide_Outline_Energi_Alternatif_FaseC.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 18 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 26 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 27 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 33 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 33 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 38 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 46 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 47 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 48 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 58 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 67 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 68 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 69 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 72 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 80 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 80 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 81 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 81 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 82 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 82 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 85 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 94 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 95 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 96 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 97 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 108 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 109 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 118 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 119 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 124 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 129 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 129 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 141 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 144 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 145 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 158 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 159 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 160 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
- Bila beberapa lembar sumber memakai penomoran tag yang sama, `--primary-source` wajib disebut. Tanpa itu tag ditandai `AMBIG` dan run dianggap gagal — lebih baik gagal terang-terangan daripada lulus karena urutan abjad.
