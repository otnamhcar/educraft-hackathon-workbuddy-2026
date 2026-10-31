# Grounding report — R001 tag resolution

**Run folder:** `03_Hasil/edu_output_wujud_zat`  
**Knowledge layer:** `03_Hasil/referensi`  
**Verdict:** **FAIL** — 89 tag diperiksa, 0 dangling, 84 pelanggaran kelas tag

> Dihasilkan oleh `tools/check_grounding.py`. Pemeriksaan ini deterministik dan dapat dijalankan ulang; ia memeriksa **resolusi** tag, bukan sekadar keberadaannya.

## Ringkasan per file

| File | Tag | Dangling | Pelanggaran kelas |
|------|----:|---------:|------------------:|
| `00_plan.md` | 9 | 0 | 9 |
| `01_artikel.md` | 27 | 0 | 24 |
| `02_infographic_brief.md` | 23 | 0 | 23 |
| `03_video_storyboard.md` | 1 | 0 | 1 |
| `04_kuis_prepost.md` | 29 | 0 | 27 |

## Temuan

- `00_plan.md`:6 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "> **Sumber fakta:** `assets/source_material_ipas.md` → `[src:B4]` (satu-satunya sumber fak"
- `00_plan.md`:47 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "2. Tiga wujud zat + ciri yang bisa diamati `[src:B4]`."
- `00_plan.md`:48 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "3. Enam perubahan wujud berpasangan (mencair↔membeku, menguap↔mengembun, menyublim↔mengkri"
- `00_plan.md`:49 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "4. Peran suhu sebagai pemicu `[src:B4]`."
- `00_plan.md`:51 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "6. Penutup solutif + ajakan mengamati di rumah `[src:B4]`."
- `00_plan.md`:75 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- Setiap butir ber-tag `[src:B4]`; kunci + pedoman skor untuk guru."
- `00_plan.md`:105 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: ""Tiga wujud zat dan ciri teramati [src:B4]","
- `00_plan.md`:106 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: ""Enam perubahan wujud berpasangan [src:B4]","
- `00_plan.md`:107 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: ""Suhu sebagai pemicu perubahan [src:B4]","
- `01_artikel.md`:8 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Pernahkah kamu memegang gelas berisi es, lalu melihat butiran air muncul di bagian luar ge"
- `01_artikel.md`:12 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Zat di sekitar kita hadir dalam tiga wujud, yaitu **padat, cair, dan gas**. `[src:B4]` Ket"
- `01_artikel.md`:12 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Zat di sekitar kita hadir dalam tiga wujud, yaitu **padat, cair, dan gas**. `[src:B4]` Ket"
- `01_artikel.md`:14 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Yang menarik, ketiga wujud ini bukan tiga zat yang berbeda. Es, air, dan uap air dapat ber"
- `01_artikel.md`:18 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Perubahan wujud selalu punya arah. Karena itu, perubahan wujud dipelajari berpasangan. `[s"
- `01_artikel.md`:22 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| Padat | Cair | mencair (melebur) | es menjadi air `[src:B4]` |"
- `01_artikel.md`:23 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| Cair | Padat | membeku | air menjadi es `[src:B4]` |"
- `01_artikel.md`:24 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| Cair | Gas | menguap | air menjadi uap `[src:B4]` |"
- `01_artikel.md`:25 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| Gas | Cair | mengembun | uap menjadi air `[src:B4]` |"
- `01_artikel.md`:26 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| Padat | Gas | menyublim | — `[src:B4]` |"
- `01_artikel.md`:27 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| Gas | Padat | mengkristal | — `[src:B4]` |"
- `01_artikel.md`:29 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Perhatikan polanya: mencair (padat → cair), menguap (cair → gas), dan menyublim (padat → g"
- `01_artikel.md`:33 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Apa yang membuat wujud berubah? Perubahan wujud dapat disebabkan oleh **perubahan suhu**. "
- `01_artikel.md`:33 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Apa yang membuat wujud berubah? Perubahan wujud dapat disebabkan oleh **perubahan suhu**. "
- `01_artikel.md`:35 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Inilah sebabnya es mencair ketika dibiarkan di ruangan yang lebih hangat, dan air membeku "
- `01_artikel.md`:35 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Inilah sebabnya es mencair ketika dibiarkan di ruangan yang lebih hangat, dan air membeku "
- `01_artikel.md`:39 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Kamu tidak perlu laboratorium untuk mengamati perubahan wujud. `[src:B4]`"
- `01_artikel.md`:41 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- **Minuman dingin.** Es mencair menjadi air, dan uap air di udara mengembun menjadi butir"
- `01_artikel.md`:42 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- **Air yang dipanaskan.** Air menguap menjadi uap air. `[src:B4]`"
- `01_artikel.md`:43 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- **Air di dalam cetakan.** Air membeku menjadi es. `[src:B4]`"
- `01_artikel.md`:44 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- **Pakaian basah yang dijemur.** Air di kain menguap, sehingga kain menjadi kering. `[src"
- `01_artikel.md`:46 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Semua kejadian itu adalah perubahan wujud yang sama, hanya berbeda arah dan berbeda benda."
- `01_artikel.md`:50 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Sains dimulai dari kebiasaan mengamati dengan teliti. Mulai hari ini, coba lakukan satu ha"
- `01_artikel.md`:58 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- `[src:B4]` Perubahan Wujud Zat — `assets/source_material_ipas.md` (Panduan Mata Pelajara"
- `02_infographic_brief.md`:3 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "> **Untuk:** `edu-infographic` | **Sumber fakta:** `[src:B4]` saja"
- `02_infographic_brief.md`:11 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "**Satu kalimat:** Zat berubah wujud karena suhunya berubah. `[src:B4]`"
- `02_infographic_brief.md`:12 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "**Kalimat pendukung:** Tiga wujud, enam arah perubahan, satu pemicu. `[src:B4]`"
- `02_infographic_brief.md`:39 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- Subjudul: *Zat berubah wujud karena suhunya berubah.* `[src:B4]`"
- `02_infographic_brief.md`:47 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| **PADAT** | kubus es | "Contoh: es batu" `[src:B4]` |"
- `02_infographic_brief.md`:48 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| **CAIR** | gelas air | "Contoh: air" `[src:B4]` |"
- `02_infographic_brief.md`:49 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| **GAS** | uap naik | "Contoh: uap air" `[src:B4]` |"
- `02_infographic_brief.md`:56 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| oranye | Mencair / melebur | padat → cair `[src:B4]` |"
- `02_infographic_brief.md`:57 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| oranye | Menguap | cair → gas `[src:B4]` |"
- `02_infographic_brief.md`:58 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| oranye | Menyublim | padat → gas `[src:B4]` |"
- `02_infographic_brief.md`:59 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| biru | Membeku | cair → padat `[src:B4]` |"
- `02_infographic_brief.md`:60 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| biru | Mengembun | gas → cair `[src:B4]` |"
- `02_infographic_brief.md`:61 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| biru | Mengkristal | gas → padat `[src:B4]` |"
- `02_infographic_brief.md`:68 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- **Suhu naik** (oranye): mencair · menguap · menyublim `[src:B4]`"
- `02_infographic_brief.md`:69 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- **Suhu turun** (biru): membeku · mengembun · mengkristal `[src:B4]`"
- `02_infographic_brief.md`:71 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "Catatan kaki blok: "Perubahan wujud dapat disebabkan perubahan suhu." `[src:B4]`"
- `02_infographic_brief.md`:76 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "1. Es dalam minuman → **mencair** `[src:B4]`"
- `02_infographic_brief.md`:77 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "2. Air dipanaskan → **menguap** `[src:B4]`"
- `02_infographic_brief.md`:78 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "3. Butir air di luar gelas dingin → **mengembun** `[src:B4]`"
- `02_infographic_brief.md`:79 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "4. Air di cetakan freezer → **membeku** `[src:B4]`"
- `02_infographic_brief.md`:83 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- Instruksi: "Catat: sebelum → sesudah, dan apakah suhu berubah." `[src:B4]`"
- `02_infographic_brief.md`:89 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- Tidak menampilkan angka suhu/derajat apa pun — sumber tidak memuatnya `[src:B4]`."
- `02_infographic_brief.md`:102 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- [ ] Footer mencantumkan sumber: Panduan IPAS Revisi 4/2025 `[src:B4]`"
- `03_video_storyboard.md`:3 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "> **Untuk:** `edu-video` | **Sumber fakta:** `[src:B4]` saja"
- `04_kuis_prepost.md`:16 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 1 | Ada berapa wujud zat yang kita pelajari? | Satu | Dua | **Tiga** | Empat | C `[src:B"
- `04_kuis_prepost.md`:17 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 2 | Es batu termasuk zat berwujud apa? | **Padat** | Cair | Gas | Uap | A `[src:B4]` |"
- `04_kuis_prepost.md`:18 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 3 | Air yang dipanaskan akan menguap menjadi uap air. Uap air termasuk zat berwujud… | P"
- `04_kuis_prepost.md`:19 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 4 | Es yang dibiarkan di ruangan hangat berubah menjadi air. Perubahan ini disebut… | Me"
- `04_kuis_prepost.md`:20 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 5 | Air yang dipanaskan lama-lama akan berubah menjadi uap. Perubahan ini disebut… | Men"
- `04_kuis_prepost.md`:21 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 6 | Air yang dimasukkan ke dalam freezer berubah menjadi es. Perubahan ini disebut… | Me"
- `04_kuis_prepost.md`:22 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 7 | Menurutmu, apa yang menyebabkan wujud zat dapat berubah? | Warna benda | **Perubahan"
- `04_kuis_prepost.md`:34 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 1 | Urutan wujud yang tepat untuk es batu, air, dan uap air adalah… | Es (gas) – air (ca"
- `04_kuis_prepost.md`:35 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 2 | Perubahan dari padat menjadi cair disebut… | Membeku | **Mencair atau melebur** | Me"
- `04_kuis_prepost.md`:36 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 3 | Perubahan dari cair menjadi padat disebut… | **Membeku** | Mencair | Mengembun | Men"
- `04_kuis_prepost.md`:37 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 4 | Perubahan dari cair menjadi gas disebut… | Mengembun | Membeku | **Menguap** | Menyu"
- `04_kuis_prepost.md`:38 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 5 | Perubahan dari gas menjadi cair disebut… | Menguap | **Mengembun** | Mencair | Mengk"
- `04_kuis_prepost.md`:39 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 6 | Perubahan dari padat menjadi gas disebut… | Mengkristal | Membeku | **Menyublim** | "
- `04_kuis_prepost.md`:40 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 7 | Perubahan dari gas menjadi padat disebut… | Menyublim | Mencair | Menguap | **Mengkr"
- `04_kuis_prepost.md`:41 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 8 | Pasangan perubahan wujud yang arahnya berlawanan adalah… | Menguap dan menyublim | *"
- `04_kuis_prepost.md`:42 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 9 | Ketika suhu di sekitar zat naik, perubahan yang mungkin terjadi adalah… | Membeku, m"
- `04_kuis_prepost.md`:43 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 10 | Ketika suhu di sekitar zat turun, perubahan yang mungkin terjadi adalah… | **Membek"
- `04_kuis_prepost.md`:44 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 11 | Es, air, dan uap air dapat berasal dari bahan yang sama. Yang berubah adalah… | Jen"
- `04_kuis_prepost.md`:45 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 12 | Butiran air muncul di dinding luar gelas yang berisi minuman dingin. Perubahan wuju"
- `04_kuis_prepost.md`:46 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 13 | Pernyataan yang paling tepat tentang perubahan wujud adalah… | Perubahan wujud hany"
- `04_kuis_prepost.md`:47 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 14 | Rani mengamati es di gelas mengecil, sementara dinding gelas menjadi basah. Kesimpu"
- `04_kuis_prepost.md`:53 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 15 | Sebutkan tiga wujud zat. | Menyebut **padat, cair, gas** (ketiganya benar). `[src:B"
- `04_kuis_prepost.md`:54 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 16 | Mengapa es dapat mencair ketika dibiarkan di ruangan yang lebih hangat? | Menyebut "
- `04_kuis_prepost.md`:55 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 17 | Tuliskan dua contoh perubahan wujud yang pernah kamu lihat di rumah, lengkap dengan"
- `04_kuis_prepost.md`:56 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 18 | Pakaian basah yang dijemur menjadi kering. Perubahan wujud apa yang terjadi, dan da"
- `04_kuis_prepost.md`:57 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "| 19 | Lengkapi urutan berikut beserta nama perubahannya: padat → … → gas. | **Padat → cai"
- `04_kuis_prepost.md`:101 — `[src:B4]` adalah tag kurikulum (cp_ipas.md) tetapi menopang kalimat non-kurikulum: "- Seluruh 27 butir bersumber tunggal dari `[src:B4]`; tidak ada butir yang membutuhkan fak"

## Rincian tag

### `00_plan.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 6 | `[src:B4]` | curriculum | **CLASS** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 47 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 48 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 49 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 51 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 75 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 105 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 106 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 107 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |

### `01_artikel.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:B4]` | curriculum | **OK** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 8 | `[src:B4]` | curriculum | **CLASS** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 12 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 12 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 14 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 18 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 22 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 23 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 24 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 25 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 26 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 27 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 29 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 33 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 33 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 35 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 35 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 39 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 41 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 42 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 43 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 44 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 46 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 50 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 52 | `[src:CP]` | curriculum | **OK** | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |
| 58 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 59 | `[src:CP]` | curriculum | **OK** (ulang) | cp_ipas.md · Dokumen CP IPAS (rujukan kurikulum) |

### `02_infographic_brief.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:B4]` | curriculum | **CLASS** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 11 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 12 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 39 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 47 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 48 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 49 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 56 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 57 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 58 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 59 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 60 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 61 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 68 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 69 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 71 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 76 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 77 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 78 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 79 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 83 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 89 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 102 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |

### `03_video_storyboard.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:B4]` | curriculum | **CLASS** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |

### `04_kuis_prepost.md`

| Baris | Tag | Kelas | Putusan | Menunjuk ke |
|------:|-----|-------|---------|-------------|
| 3 | `[src:B4]` | curriculum | **OK** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 16 | `[src:B4]` | curriculum | **CLASS** | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 17 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 18 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 19 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 20 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 21 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 22 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 34 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 35 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 36 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 37 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 38 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 39 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 40 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 41 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 42 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 43 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 44 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 45 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 46 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 47 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 53 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 54 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 55 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 56 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 57 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 58 | `[src:B4]` | curriculum | **OK** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |
| 101 | `[src:B4]` | curriculum | **CLASS** (ulang) | cp_ipas.md · Menyimpulkan proses perubahan wujud zat. |

## Batas pemeriksaan ini

- Ia memeriksa **resolusi tag dan kelas tag**, bukan kebenaran isi kalimat. Kalimat yang salah tetapi bertag benar tetap lolos; itu tugas Reviewer (R001–R012).
- Deteksi kelas memakai penanda kata kurikulum (CP, capaian, fase, kurikulum, elemen, tujuan pembelajaran). Kalimat ambigu ditandai untuk ditinjau, bukan dihukum otomatis.
