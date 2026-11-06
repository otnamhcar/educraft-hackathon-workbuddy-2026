# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_energi_alternatif`  
**Knowledge layer:** `08_Referensi`  
**Primary source:** `source_material_energi.md`  
**Verdict:** **PASS** — 271 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag, 0 ambigu

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `04_review.md`, `05_Lembar_Persetujuan_Guru.md`, `audit_log.md`, `grounding_report.md`

**Cara tag ditetapkan.** Tag yang hanya ada di satu berkas diselesaikan ke berkas itu (mis. `[src:CA1]` ke `konteks_aktual.md`, `[src:C4]` ke `cp_ipas.md`). Tag yang ada di lebih dari satu lembar sumber diselesaikan ke `source_material_energi.md` karena run ini dibangun di atas lembar itu.

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_plan.md` | 27 | 0 | 0 |
| `01_RPP_Energi_Alternatif.md` | 127 | 0 | 0 |
| `02_Kuis_PrePost_Energi_Alternatif.md` | 17 | 0 | 0 |
| `03_Slide_Outline_Energi_Alternatif.md` | 14 | 0 | 0 |
| `06_Jejak_Sumber.md` | 86 | 0 | 0 |

## Temuan

- Tidak ada temuan. Setiap tag menunjuk anchor yang ada, tidak ambigu, dan kelasnya sesuai.

## Rincian tag

### `00_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 15 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 15 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 16 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 16 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 17 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 23 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 23 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 23 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 23 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 23 | `[src:C4]` | curriculum | **OK** | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 23 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 31 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 32 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 33 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 34 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 35 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 36 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 37 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 38 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 39 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 39 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 40 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 41 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 50 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 51 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 61 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 98 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |

### `01_RPP_Energi_Alternatif.md`

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
| 22 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 25 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 39 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 40 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 42 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 43 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 44 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 44 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 46 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 48 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 50 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 55 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 56 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 57 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 59 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 63 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 65 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 68 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 69 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 72 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 76 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 79 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 81 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 83 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 87 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 91 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 91 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 92 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 92 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 98 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 98 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 98 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 101 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 103 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 105 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 106 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 106 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 106 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 107 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 109 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 113 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 114 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 115 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 118 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 127 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 129 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 132 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 133 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 135 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 137 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 139 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 140 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 142 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 145 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 145 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 148 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 148 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 151 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 154 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 158 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 159 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 161 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 165 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 166 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 167 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 168 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 169 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 170 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 173 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 182 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 184 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 189 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 198 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 198 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 198 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 198 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 200 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 200 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 208 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 209 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 209 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 209 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 210 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 222 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 229 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 229 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 229 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 231 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 231 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 231 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 232 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 250 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 251 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 251 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 252 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 253 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 262 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 267 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 272 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 276 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 276 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 280 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 280 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 281 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 281 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 281 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 282 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 282 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 282 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 283 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 283 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 283 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 284 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 284 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 284 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `02_Kuis_PrePost_Energi_Alternatif.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 162 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 163 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 164 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 165 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 166 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 167 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 168 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 169 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 170 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 171 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 172 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 173 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 174 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 175 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 176 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 177 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 178 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |

### `03_Slide_Outline_Energi_Alternatif.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 21 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 28 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 34 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 41 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 41 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 41 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 48 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 54 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 54 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 65 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 71 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 78 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 78 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 84 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |

### `06_Jejak_Sumber.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 9 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 9 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 10 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 10 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 11 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 11 | `[src:C4]` | curriculum | **OK** | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 11 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 19 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 20 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 21 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 22 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 23 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 24 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 25 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 26 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 26 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 26 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 27 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 28 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 29 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 30 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 31 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 32 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 33 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 34 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 35 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 36 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 37 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 38 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 39 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 40 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 41 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 42 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 42 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 43 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 44 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 45 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 46 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 47 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 48 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 49 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 50 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 51 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 52 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 53 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 54 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 55 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 56 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 57 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 57 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 59 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 65 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 66 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 67 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 68 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 69 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 70 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 71 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 72 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 73 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 74 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 75 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 76 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 77 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 78 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 79 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 80 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 81 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 88 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 89 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 90 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 90 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 91 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 92 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 93 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 94 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 95 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 95 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 96 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 102 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 102 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 103 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 103 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 104 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 104 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 104 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
- Bila beberapa lembar sumber memakai penomoran tag yang sama, `--primary-source` wajib disebut. Tanpa itu tag ditandai `AMBIG` dan run dianggap gagal — lebih baik gagal terang-terangan daripada lulus karena urutan abjad.
