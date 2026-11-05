# 07_review_pass2.md — Putusan Reviewer, Pass 2

> **Run:** EDU-ORCH-20261104-004 · **Agen:** Reviewer · **Pass:** 2
> **Fase dinilai:** Fase C (kelas V–VI) · **Rulebook:** v2.0 (R001–R012)
> **Putusan:** ✅ **APPROVE** — dengan tiga butir terbuka yang memblokir publikasi

## Rekapitulasi remediasi

| # | Temuan | Aturan | Tindakan Writer | Status |
|---|--------|--------|-----------------|--------|
| 1 | Tiga kalimat "es adalah air dalam wujud padat…" tanpa tag | R001 Major | Digabung menjadi satu kalimat contoh yang bertag `[src:W1]` + `[src:W11]` *(turunan)* | ✅ Tertutup |
| 2 | "berlangsung dalam hitungan tahun, bukan menit" | R001 Major | Klausa perbandingan waktu dihapus; diganti pernyataan lokus dan luas wilayah `[src:W5]`, ditambah catatan `[UNVERIFIED]` | ✅ Tertutup |
| 3 | "Kalimat kunci: wujud dapat berubah, bahannya tetap" tanpa tag | R001 Major | Ditag `[src:W11]` *(turunan tim)* | ✅ Tertutup |
| 4 | "ilmuan" | R009 Minor | Menjadi "ilmuwan" — dan kalimatnya ditulis ulang menjadi "penyelidikan berbeda dari menebak" | ✅ Tertutup |
| 5 | "penebak" melabeli murid | R010 Minor | Frasa diganti; label dihapus, pembeda kini pada perilaku (ada tidaknya catatan) | ✅ Tertutup |
| 6 | Tujuan 1 atribusi terlalu longgar | R001 Minor | Dipecah menjadi tujuan 1 (`[src:W1]`) dan tujuan 2 (`[src:W11]` turunan); nomor tujuan sesudahnya disesuaikan; pemetaan butir kuis diperbarui | ✅ Tertutup |

Pemeriksaan deterministik ulang: **PASS** — 176 tag, 0 dangling, 0 pelanggaran kelas.

> **Catatan angka.** Pada pemeriksaan pertama setelah remediasi, alat melaporkan 199 tag. Selisih itu
> berasal dari `06_review.md` dan `07_review_pass2.md` yang ikut terhitung — berkas review mengutip
> kalimat bermasalah beserta tag-nya sebagai bukti, sehingga tag di dalamnya bukan klaim fakta.
> `tools/check_grounding.py` hanya mengecualikan nama `05_review.md`, sehingga run ini yang memakai
> penomoran `06_`/`07_` tidak ternaungi. Alat sudah diperbaiki agar mengenali peran "review" pada nama
> berkas, bukan nomor tetap; angka sah untuk draf adalah **176**. Run lama diuji ulang: tetap 115 tag,
> tidak ada regresi.

## Temuan baru pada pass 2

**Tidak ada.** Draf pass 2 tidak menimbulkan pelanggaran baru.

Satu hal dicatat sebagai pengamatan, bukan temuan: penyuntingan menambah paragraf penutup bagian
"Dari gelas es ke Puncak Jaya" yang mengarahkan murid bertanya kepada guru tentang lama waktu
peristiwa. Kalimat itu tidak menyatakan fakta apa pun, sehingga tidak memerlukan tag — ia
mengundang pertanyaan, bukan mengklaim jawaban. Ini justru bentuk yang benar untuk menangani
kekosongan data: diakui terbuka, bukan diisi karangan.

## Vonis per aturan

| Aturan | Vonis | Dasar |
|--------|-------|-------|
| **R001** | ✅ LULUS | 176 tag, seluruhnya resolvable ke `source_material_wujud_zat.md`. Tidak ada lagi kalimat fakta tanpa tag. Tiga kalimat bermasalah pada pass 1 sudah ditutup. Tag turunan (`[src:W10]`, `[src:W11]`) selalu berpenanda eksplisit. |
| **R002** | ✅ LULUS | Nada tenang di kelima format. Isu Puncak Jaya dan es kutub disampaikan sebagai peristiwa, tanpa kata ancaman atau bencana. |
| **R003** | ✅ LULUS | Kosakata dan panjang kalimat sesuai kelas V–VI. Fase dibaca dari `00_run_config.md` (Fase C), tidak dipatok dari asumsi. |
| **R004** | ✅ LULUS **bersyarat** | Topik di Fase B (`[src:B4]`) sementara paket diminta untuk Fase C. Penandaan `PERLU KONFIRMASI GURU` ada di tiga tempat: `00_run_config.md`, `00_plan.md` `gaps`, dan `01_lesson_plan.md` §1. R004 mengizinkan **asalkan** disetujui manusia sebelum publikasi — karena itu status tetap LOCKED. |
| **R005** | ✅ LULUS **parsial, dinyatakan terbuka** | Peran murid terpenuhi dan ter-grounding `[src:W6]` `[src:W9]`. Mitigasi tidak tersedia di sumber dan **tidak dikarang**; kekosongan dinyatakan eksplisit di `01_lesson_plan.md` §9 sebagai keputusan guru. Mengarang mitigasi akan melanggar R001 yang lebih keras — jalan yang dipilih draf ini benar. |
| **R006** | `N/A` | Tidak ada klaim kesehatan, kesembuhan, atau efikasi di kelima draf. Diperiksa dengan menyisir kata sifat efek dan klaim manfaat — nihil. |
| **R007** | `N/A` | Tidak ada praktik berbahaya yang diajarkan atau dinormalisasi. Satu-satunya penyebutan pembakaran adalah "lilin yang meleleh saat dibakar" `[src:W4]` — contoh fenomena dari sumber, bukan anjuran. |
| **R008** | ✅ LULUS | Nada ramah dan memberdayakan; tidak ada merek. |
| **R009** | ✅ LULUS | Ejaan "ilmuwan" sudah baku. Setiap materi naratif ditutup ajakan positif: artikel → tiga percobaan rumah; slide 8 → ajakan menyelidiki. |
| **R010** | ✅ LULUS | Label "penebak" sudah dihapus. Umpan balik kuis butir 11 secara eksplisit melindungi jawaban murid yang kurang presisi: "jangan potong poinnya". |
| **R011** | `N/A` beralasan | Nol tag `[src:CA#]`. `konteks_aktual.md` hanya memuat CA1 (PLTS Cirata) dan CA6 (FOLU/NZE) — tidak relevan dengan perubahan wujud zat. Tautan tidak dipaksakan, sesuai §0b. |
| **R012** | `N/A` beralasan | Materi murni edukatif. Disisir untuk nama produk, testimoni, superlatif komersial, dan klaim halal — nihil. |

## Butir terbuka — memblokir publikasi

Ketiganya **tidak dapat diselesaikan oleh Writer** karena penyelesaiannya menuntut fakta yang tidak
ada di sumber. Ini keputusan manusia, bukan cacat draf:

1. **Kedudukan kurikulum (R004).** Pakai sebagai pemantapan lintas fase untuk Fase C, atau turunkan
   ke Fase B? Tanpa jawaban ini, paket tidak boleh disebut materi Fase C.
2. **Mitigasi (R005).** Terima kekosongan, atau sediakan sumber mitigasi agar Writer dapat
   menambahkannya secara bertag?
3. **Pemetaan arah proses `[src:W10]`.** Seluruh paket sengaja tanpa diagram arah. Bila guru
   memvalidasi, ia dapat ditambahkan sebagai bagian berlabel — dan kuis dapat memperoleh butir arah
   proses.

## Kesimpulan

Draf memenuhi seluruh aturan yang dapat dipenuhi dari sumber yang tersedia. Tiga aturan (R004, R005,
R011) berstatus lulus bersyarat atau `N/A` dengan alasan yang dinyatakan — tidak ada yang dilewati
diam-diam.

**Run berhenti di approval gate.** Tidak ada publikasi. `Publish: LOCKED` tetap berlaku sampai
manusia memberi persetujuan eksplisit dan memutuskan ketiga butir terbuka di atas.

## Berkas yang diperiksa

`00_plan.md` · `01_lesson_plan.md` · `02_artikel.md` · `03_slide_outline.md` ·
`04_infographic_brief.md` · `05_kuis.md` · `00_run_config.md` · `grounding_report.md` ·
`06_review.md`
