# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_energi_alternatif_faseC`  
**Knowledge layer:** `08_Referensi`  
**Primary source:** `source_material_energi.md`  
**Verdict:** **PASS** — 134 tag diperiksa, 0 dangling, 0 pelanggaran kelas tag, 0 ambigu

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

**Tidak diperiksa (metadata — boleh menyebut tag tanpa mengklaim fakta dengannya):** `00_run_config.md`, `02_review_temuan.md`, `grounding_report.md`

**Cara tag ditetapkan.** Tag yang hanya ada di satu berkas diselesaikan ke berkas itu (mis. `[src:CA1]` ke `konteks_aktual.md`, `[src:C4]` ke `cp_ipas.md`). Tag yang ada di lebih dari satu lembar sumber diselesaikan ke `source_material_energi.md` karena run ini dibangun di atas lembar itu.

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `01_RPP_Energi_Alternatif_FaseC.md` | 134 | 0 | 0 |

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
| 45 | `[src:3]` | fact | **OK** | source_material_energi.md · Sumber Energi *(primary)* |
| 46 | `[src:4]` | fact | **OK** | source_material_energi.md · Bentuk Energi *(primary)* |
| 47 | `[src:5]` | fact | **OK** | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 49 | `[src:6]` | fact | **OK** | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 53 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 55 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 58 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 59 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 62 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 66 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 69 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 71 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 73 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 77 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 81 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 81 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 82 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 82 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 88 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 88 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 88 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 91 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 93 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 95 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 95 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 95 | `[src:B5]` | curriculum | **OK** (ulang) | cp_ipas.md · Menjelaskan sumber dan bentuk energi, serta proses perubahan bentuk en |
| 95 | `[src:C4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menghasilkan upaya penghematan energi, serta pemanfaatan sumber energi |
| 97 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 99 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 103 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 104 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 105 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 108 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 113 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 115 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 118 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 119 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 121 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 123 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 125 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 126 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 128 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 131 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 131 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 134 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 134 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 137 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 140 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 144 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 145 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 147 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 149 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 158 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 158 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 162 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 166 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 167 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 168 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 169 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 170 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 171 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 174 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 181 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 183 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 188 | `[src:1]` | fact | **OK** (ulang) | source_material_energi.md · Identitas Modul *(primary)* |
| 196 | `[src:3]` | fact | **OK** (ulang) | source_material_energi.md · Sumber Energi *(primary)* |
| 196 | `[src:4]` | fact | **OK** (ulang) | source_material_energi.md · Bentuk Energi *(primary)* |
| 197 | `[src:5]` | fact | **OK** (ulang) | source_material_energi.md · Perubahan Bentuk Energi *(primary)* |
| 197 | `[src:6]` | fact | **OK** (ulang) | source_material_energi.md · Hukum Kekekalan Energi *(primary)* |
| 198 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 198 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 198 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 199 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 200 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 200 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 208 | `[src:7]` | fact | **OK** (ulang) | source_material_energi.md · Penghematan Energi *(primary)* |
| 209 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 209 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
| 209 | `[src:CA6]` | actual_context | **OK** (ulang) | konteks_aktual.md · FOLU Net Sink 2030 & Net Zero Emission 2060 |
| 210 | `[src:9]` | fact | **OK** (ulang) | source_material_energi.md · Peran Siswa |
| 211 | `[src:8]` | fact | **OK** (ulang) | source_material_energi.md · Mitigasi Perubahan Iklim & Pelestarian SDA *(primary)* |
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
| 264 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 269 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
| 273 | `[src:CA1]` | actual_context | **OK** (ulang) | konteks_aktual.md · PLTS Terapung Cirata |
| 275 | `[src:2]` | fact | **OK** (ulang) | source_material_energi.md · Energi Alternatif *(primary)* |
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

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
- Bila beberapa lembar sumber memakai penomoran tag yang sama, `--primary-source` wajib disebut. Tanpa itu tag ditandai `AMBIG` dan run dianggap gagal — lebih baik gagal terang-terangan daripada lulus karena urutan abjad.
