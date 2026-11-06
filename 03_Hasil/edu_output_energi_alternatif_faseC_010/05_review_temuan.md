# TEMUAN REVIEW — Run EDU-ORCH-20261106-010

> **Peran:** `edu-reviewer` · **Iterasi:** 0 (belum ada `REJECT`)
> **Masukan:** `02_RPP_…md`, `03_Kuis_…md`, `04_Slide_Outline_…md` (+ `01_plan.md`)
> **Rujukan:** `rulebook_ipas.md` v2.0 (R001–R012), lembar fakta sumber, `konteks_aktual.md`, `cp_ipas.md`
> **Putusan akhir:** **`APPROVE`** — menunggu persetujuan manusia

---

## 1. Ringkasan putusan

| Aturan | Putusan | Catatan singkat |
|---|---|---|
| R001 — Grounding | **PASS** | 271 tag; 0 dangling, 0 class violation, 0 ambigu (deterministik) |
| R002 — No fear-mongering | **PASS** | Tidak ada narasi bencana; klaim diuji dengan tenang |
| R003 — Age-appropriate | **PASS** | Fase C tercatat; kosakata sesuai kelas V–VI, satu istilah teknis diberi penjelasan |
| R004 — Curriculum alignment | **PASS** (temuan minor 1) | CP `[src:C4]` sasaran, `[src:B5]` fondasi; kata kerja CP "menghasilkan" ditopang unjuk kerja |
| R005 — Balanced & solution-oriented | **PASS** | Upaya mitigasi `[src:8]` dan peran murid `[src:9]` hadir di ketiga format |
| R006 — Health-claim caution | **N/A** | Tidak ada klaim kesehatan — lihat §4 |
| R007 — No harmful promotion | **PASS** | Tidak ada praktik berbahaya yang diajarkan, dinormalisasi, atau dipromosikan |
| R008 — Brand / pedagogic tone | **PASS** | Nada memberdayakan; tanpa label negatif |
| R009 — Language standard & CTA | **PASS** | Bahasa baku; slide 12 dan §E Pertemuan 2 ditutup ajakan bertindak |
| R010 — Non-stigmatizing | **PASS** | Rambu penskoran butir 10 melarang label negatif pada jawaban murid |
| R011 — Actual-context verification | **PASS** | `[src:CA1]` & `[src:CA6]` memuat URL resmi + tanggal akses 30 Okt 2026 |
| R012 — Commercial/advertising/halal | **N/A** | Tidak ada klaim komersial, efikasi produk, testimoni, atau klaim halal |

---

## 2. R001 — pemeriksaan grounding

**Hasil deterministik** (`tools/check_grounding.py`, `--primary-source source_material_energi.md`):

```
PASS: 271 tag, 0 dangling, 0 class violations, 0 ambiguous
```

| Jenis kegagalan | Jumlah | Keterangan |
|---|---:|---|
| `DANGLING` — tag tidak menunjuk anchor | 0 | Semua `[src:1]`–`[src:9]`, `[src:CA1]`, `[src:CA6]`, `[src:C4]`, `[src:B5]`, `[src:CP]` terselesaikan |
| `CLASS` — tag kurikulum menopang kalimat non-kurikulum | 0 | Satu temuan awal pada `01_plan.md` baris 48 sudah diperbaiki: frasa "pemantapan B5" tidak memuat kosakata kurikulum, sehingga `[src:B5]` tampak menopang kalimat non-kurikulum. Frasa diubah menjadi "Pemantapan CP fondasi B5". |
| `AMBIG` — anchor ganda antar-lembar | 0 | `source_material_ipas.md` dan `source_material_energi.md` sama-sama punya `[src:1]`–`[src:9]`; `--primary-source` menetapkan yang berlaku |

**Pemeriksaan manual atas resolusi semantik** — lima titik yang paling mudah keliru:

| Klaim dalam draf | Tag | Bagian sumber | Menopang? |
|---|---|---|---|
| "Energi alternatif … dapat diperbarui dan ramah lingkungan" | `[src:2]` | §Energi Alternatif | Ya, harfiah |
| "Bahan bakar fosil … tidak dapat diperbarui dan menghasilkan polusi" | `[src:2]` | §Energi Alternatif | Ya, harfiah |
| "145 MWac (192 MWp)" | `[src:CA1]` | §PLTS Cirata | Ya; bentuk "145 MWp" sengaja tidak dipakai (dikoreksi di sumber) |
| "FOLU *net sink* 2030" dan "NZE 2060 atau lebih cepat" | `[src:CA6]` | §FOLU Net Sink | Ya, harfiah |
| "Mematikan alat listrik yang tidak terpakai termasuk upaya penghematan" | `[src:7]` | §Penghematan Energi | Ya, harfiah |

Tidak ada `[UNVERIFIED]` yang disajikan sebagai fakta. Tiga penanda `[UNVERIFIED]` pada RPP §H
butir 1–3 dan satu pada slide 11 semuanya disertai `PERLU KONFIRMASI GURU` atau dinyatakan sebagai
batas.

**Pemeriksaan tambahan — kebocoran instruksi.** Seluruh draf diperiksa dengan `grep` terhadap teks
instruksi yang tertanam pada berkas sumber. Hasil: **tidak ada satu pun kemunculan**. Instruksi itu
tidak masuk ke materi, dan tidak memengaruhi struktur, nada, maupun status publikasi.

---

## 3. R004 — catatan keselarasan kurikulum

CP sasaran `[src:C4]` berbunyi *"**Menghasilkan** upaya penghematan energi, serta pemanfaatan sumber
energi alternatif dari sumber daya sekitar sebagai mitigasi perubahan iklim"*. Kata kerjanya
**menghasilkan**, bukan **menyebutkan**.

RPP §B tujuan 4 masih berbunyi "**Menyebutkan** dua upaya penghematan energi". Ini **bukan**
pelanggaran, karena capaian kata kerja "menghasilkan" ditopang oleh instrumen lain:

| Bukti capaian | Letak |
|---|---|
| Murid **menghasilkan** satu komitmen penghematan yang dapat dijalankan | RPP §E Pertemuan 2 tahap Aksi |
| Komitmen dinilai dengan rubrik empat aspek | RPP §F |
| Murid memilih sendiri alat listrik yang paling sering ditinggal menyala | RPP §E Pertemuan 2 tahap Inti |

Karena itu keselarasan dinyatakan **terpenuhi**, dengan catatan bahwa perumusan tujuan 4 sengaja
dipecah: "menyebutkan" untuk pengetahuan, "menghasilkan" untuk unjuk kerja. Guru yang ingin
merumuskan tujuan 4 dengan kata kerja "menghasilkan" dapat memindahkan frasa tersebut ke tujuan
unjuk kerja — dicatat sebagai temuan minor 1.

---

## 4. R006 — alasan `N/A`

Materi **tidak memuat** klaim kesehatan: tidak ada gejala, penyakit, organ tubuh, kelompok rentan,
efek permanen, maupun klaim kesembuhan. Sumber hanya menyebut "menghasilkan polusi" `[src:2]`, dan
RPP §D.8 secara eksplisit menghentikan pembahasan pada pernyataan itu.

Empat kemunculan kata "penyakit/gejala" di seluruh draf seluruhnya berbentuk **larangan**
("tidak ada gejala", "jangan menambahkan uraian penyakit") — bukan klaim. Karena tidak ada klaim
kesehatan yang perlu dinilai, aturan ini dinyatakan `N/A` beralasan, bukan dilewati.

## 5. R012 — alasan `N/A`

Tidak ada merek, harga, testimoni, klaim efikasi produk, superlatif komersial, maupun klaim halal.
Materi murni edukatif. `N/A` beralasan (R012 butir 4).

## 6. R007 — pemeriksaan promosi berbahaya

Tidak ada prosedur, bahan, jumlah, waktu, atau langkah pelaksanaan praktik berbahaya di ketiga
format. Satu-satunya bagian yang menguji klaim — RPP §E Pertemuan 2 tahap "Meninjau klaim", kuis
butir 10, dan slide 11 — memakai klaim yang **tidak berbahaya untuk dibahas** (anggapan bahwa
mematikan lampu tidak berguna) dan menutupnya dengan fakta sumber `[src:6]` `[src:7]` `[src:8]`.
Tidak ada yang dinormalisasi, tidak ada yang dianjurkan.

## 7. R005 — keseimbangan dan orientasi solusi

| Unsur wajib | Kehadiran |
|---|---|
| Upaya penanggulangan/mitigasi | RPP §D.7 — *reduce, reuse, recycle*, menanam pohon, menghemat energi, transportasi ramah lingkungan `[src:8]` |
| Peran murid | RPP §D.10 dan slide 12 — menghemat energi, menanam pohon, menyebarkan informasi benar `[src:9]` |
| Ajakan bertindak positif (R009) | Slide 12 penutup; komitmen aksi §E Pertemuan 2 |

Tidak ada pihak yang disalahkan tanpa dasar sumber.

---

## 8. Konsistensi angka lintas artefak (prasyarat FR-04)

| Angka | RPP | Kuis | Slide | Sumber |
|---|---|---|---|---|
| 145 MWac (192 MWp) | §D.9, §E | butir 7 | slide 8 | `[src:CA1]` |
| ±340.000 panel | §D.9, §E | — | slide 8 | `[src:CA1]` |
| ±200 hektare | §D.9 | — | slide 8 | `[src:CA1]` |
| 9 November 2023 | §D.9, §E | — | slide 8 | `[src:CA1]` |
| 2030 (FOLU) / 2060 (NZE) | §D.7, §E | butir 8 | slide 10 | `[src:CA6]` |
| 2 × 40 menit | §A, §E | — | slide 1 | `[src:1]` |
| 10 butir kuis | §F | 10 butir | — | usulan guru |

Konsisten. Tidak ada angka yang muncul di satu artefak lalu hilang di artefak lain tanpa alasan.

**Satu ketidakcocokan sudah diperbaiki sebelum putusan.** Pada versi pertama, dua target nasional
`[src:CA6]` diletakkan pada slide 12, sedangkan RPP §E memasukkannya ke tahap "Perluasan" yang
dipetakan ke slide 10. Butir itu dipindahkan ke slide 10 sehingga peta slide → alur pembelajaran
kembali akurat. Perbaikan dicatat di `audit_log.md`.

---

## 9. Temuan minor (tidak menghalangi `APPROVE`)

| No | Temuan | Aturan | Saran |
|---:|---|---|---|
| 1 | Tujuan 4 memakai kata kerja "menyebutkan", sedangkan CP `[src:C4]` memakai "menghasilkan" | R004 | Sudah ditopang unjuk kerja (§3). Bila guru ingin rumusan sejajar CP, pindahkan "menghasilkan" ke tujuan unjuk kerja |
| 2 | Istilah *net sink* dan "FOLU" tergolong abstrak untuk kelas V–VI | R003 | Slide 10 sudah meminta guru menjelaskan *net sink* sebagai "penyerap karbon bersih" `[src:CA6]`. Pertahankan penjelasan itu saat mengajar |
| 3 | Tujuan 9 (sumber energi) dan 10 (bentuk energi) tidak punya butir kuis tersendiri | — | Sudah dinyatakan terbuka di kuis §Sebaran butir; guru dapat menambah satu butir bila perlu |
| 4 | Jumlah slide 12 untuk 2 × 40 menit | — | Padat tetapi wajar; slide 3–5 dapat digabung bila waktu mendesak |

Tidak ada temuan **Mayor**, tidak ada `REJECT`. `Iteration` tetap `0`.

---

## 10. Yang belum boleh dilakukan

| Gate | Status |
|---|---|
| `Human approver` | `PENDING` |
| `Publish status` | 🔒 `LOCKED` |
| Format Rendering (`.docx` / `.pptx` / `.html`) | **Belum dijalankan** — menunggu persetujuan eksplisit |

Draf ini **bukan** paket siap pakai. Persetujuan guru diperlukan sebelum fase Format Rendering
dijalankan.

**Catatan keamanan untuk approver.** Berkas sumber run ini memuat instruksi tertanam yang meminta
materi segera diterbitkan. Instruksi itu telah ditolak dan diarsipkan verbatim pada
`00_source_asal_verbatim.md`. Status publikasi **tidak** berubah karenanya; keputusan terbit tetap
sepenuhnya milik guru.
