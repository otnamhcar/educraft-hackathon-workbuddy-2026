# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_energi_alternatif_faseC_007`  
**Knowledge layer:** `08_Referensi`  
**Primary source:** `source_material_energi.md`  
**Verdict:** **PASS** — 199 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag, 0 ambigu

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `grounding_report.md`

**Cara tag ditetapkan.** Tag yang hanya ada di satu berkas diselesaikan ke berkas itu (mis. `[src:CA1]` ke `konteks_aktual.md`, `[src:C4]` ke `cp_ipas.md`). Tag yang ada di lebih dari satu lembar sumber diselesaikan ke `source_material_energi.md` karena run ini dibangun di atas lembar itu.

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `01_RPP_Energi_Alternatif_FaseC.md` | 148 | 0 | 0 |
| `02_Kuis_Energi_Alternatif_FaseC.md` | 15 | 0 | 0 |
| `03_Slide_Outline_Energi_Alternatif_FaseC.md` | 36 | 0 | 0 |

## Temuan

- Tidak ada temuan. Setiap tag menunjuk anchor yang ada, tidak ambigu, dan kelasnya sesuai.

## Rincian tag

### `01_RPP_Energi_Alternatif_FaseC.md`

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
| 33 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 34 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 34 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 34 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 36 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 38 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 40 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 42 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 42 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
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
| 72 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 75 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 77 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 79 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 83 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 87 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 87 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 88 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 88 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 94 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 94 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 94 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 97 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 99 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 101 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 102 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 102 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 103 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 105 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 107 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 111 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 112 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 113 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 116 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 121 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 123 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 126 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 127 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 129 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 131 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 133 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 134 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 136 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 139 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 139 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 142 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 142 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 145 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 148 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 152 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 153 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 155 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 157 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 166 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 166 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 170 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 174 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 175 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 176 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 177 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 178 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 179 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 182 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 189 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 191 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 194 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 194 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 194 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 208 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 209 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 210 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 218 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 219 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 228 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 236 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 236 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 237 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 237 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 238 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 238 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 238 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 239 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 239 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 240 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 240 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 248 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 249 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 249 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 249 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 250 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 250 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 250 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 251 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 252 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 263 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 270 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 270 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 270 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 272 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 272 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 272 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 273 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 291 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 292 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 293 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 294 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 295 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 307 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 312 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 316 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 318 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 338 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 338 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 342 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 342 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 343 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 343 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 343 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 344 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 344 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 344 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 345 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 345 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 346 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 346 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 346 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 347 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `02_Kuis_Energi_Alternatif_FaseC.md`

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
| 97 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 97 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 103 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 104 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 105 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 105 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |

### `03_Slide_Outline_Energi_Alternatif_FaseC.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 19 | `[src:1]` | fact | **OK** | source_material_energi.md · Identitas Modul *(primary)* |
| 27 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 28 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 34 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 34 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 40 | `[src:B5]` | curriculum | **OK** | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 48 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 49 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 50 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 60 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 69 | `[src:2]` | fact | **OK** | source_material_energi.md · Energi Alternatif *(primary)* |
| 70 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 71 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 74 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 82 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 82 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 83 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 83 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 84 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 84 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 87 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 96 | `[src:CA1]` | actual_context | **OK** | konteks_aktual.md · PLTS Terapung Cirata |
| 97 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 98 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 99 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 110 | `[src:7]` | fact | **OK** | source_material_energi.md · Penghematan Energi *(primary)* |
| 111 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 121 | `[src:8]` | fact | **OK** | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 122 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 129 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 140 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 142 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 143 | `[src:CA6]` | actual_context | **OK** | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 156 | `[src:9]` | fact | **OK** | source_material_energi.md · Peran Siswa |
| 157 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 158 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
- Bila beberapa lembar sumber memakai penomoran tag yang sama, `--primary-source` wajib disebut. Tanpa itu tag ditandai `AMBIG` dan run dianggap gagal — lebih baik gagal terang-terangan daripada lulus karena urutan abjad.
