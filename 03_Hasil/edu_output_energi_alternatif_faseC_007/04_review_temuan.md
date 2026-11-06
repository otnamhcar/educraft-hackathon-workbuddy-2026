# TEMUAN REVIEW — Run EDU-ORCH-20261106-007

> **Peran:** `edu-reviewer` · **Iterasi:** 0 (belum ada `REJECT`)
> **Masukan:** `01_RPP_…md`, `02_Kuis_…md`, `03_Slide_Outline_…md`
> **Rujukan:** `rulebook_ipas.md` v2.0 (R001–R012), `source_material_energi.md`, `konteks_aktual.md`, `cp_ipas.md`
> **Putusan akhir:** **`APPROVE`** — menunggu persetujuan manusia

---

## 1. Ringkasan putusan

| Aturan | Putusan | Catatan singkat |
|---|---|---|
| R001 — Grounding | **PASS** | 199 tag; 0 dangling, 0 class violation, 0 ambigu (deterministik) |
| R002 — No fear-mongering | **PASS** | Tidak ada narasi bencana; §D.11 justru menahan klaim |
| R003 — Age-appropriate | **PASS** | Fase C tercatat di `00_run_config.md`; kosakata & panjang kalimat sesuai kelas V–VI |
| R004 — Curriculum alignment | **PASS** | CP `[src:C4]` sasaran, `[src:B5]` fondasi, keterampilan proses `[src:CP]` |
| R005 — Balanced & solution-oriented | **PASS** | Upaya mitigasi `[src:8]` dan peran murid `[src:9]` hadir |
| R006 — Health-claim caution | **N/A** | Materi tidak memuat klaim kesehatan apa pun — lihat §3 |
| R007 — No harmful promotion | **PASS** | Lihat §4 — bagian yang diminta guru ditolak dan disubstitusi |
| R008 — Brand / pedagogic tone | **PASS** | Nada memberdayakan; tidak ada label negatif |
| R009 — Language standard & CTA | **PASS** | Bahasa baku; slide 12 dan §E Pertemuan 2 ditutup ajakan bertindak |
| R010 — Non-stigmatizing | **PASS** | Rambu penskoran butir 10 melarang label negatif pada jawaban murid |
| R011 — Actual-context verification | **PASS** | `[src:CA1]` & `[src:CA6]` memuat URL resmi + tanggal akses 30 Okt 2026 |
| R012 — Commercial/advertising/halal | **N/A** | Tidak ada klaim komersial, efikasi produk, testimoni, atau klaim halal |

---

## 2. R001 — pemeriksaan grounding

**Hasil deterministik** (`tools/check_grounding.py`, `--primary-source source_material_energi.md`):

```
PASS: 199 tag, 0 dangling, 0 class violations, 0 ambiguous
```

| Jenis kegagalan | Jumlah | Keterangan |
|---|---:|---|
| `DANGLING` — tag tidak menunjuk anchor | 0 | Semua `[src:1]`–`[src:9]`, `[src:CA1]`, `[src:CA6]`, `[src:C4]`, `[src:B5]`, `[src:CP]` terselesaikan |
| `CLASS` — tag kurikulum menopang kalimat non-kurikulum | 0 | Satu temuan awal pada RPP baris 35 sudah diperbaiki: tag `[src:C4]` terpisah dari kata "CP" karena pemenggalan baris. Kalimat digabung satu baris. |
| `AMBIG` — anchor ganda antar-lembar | 0 | `source_material_ipas.md` dan `source_material_energi.md` sama-sama punya `## [src:1]`–`## [src:9]`; `--primary-source` menetapkan yang berlaku |

**Pemeriksaan manual atas resolusi semantik** — lima titik yang paling mudah keliru:

| Klaim dalam draf | Tag | Bagian sumber | Menopang? |
|---|---|---|---|
| "Energi alternatif … dapat diperbarui dan ramah lingkungan" | `[src:2]` | §Energi Alternatif | Ya, harfiah |
| "Bahan bakar fosil … tidak dapat diperbarui dan menghasilkan polusi" | `[src:2]` | §Energi Alternatif | Ya, harfiah |
| "145 MWac (192 MWp)" | `[src:CA1]` | §PLTS Cirata | Ya; bentuk "145 MWp" sengaja tidak dipakai (dikoreksi di sumber) |
| "FOLU *net sink* 2030" | `[src:CA6]` | §FOLU Net Sink | Ya, harfiah |
| "Tanah dan hutan termasuk SDA yang harus dijaga" | `[src:8]` | §Mitigasi & Pelestarian SDA | Ya, harfiah (sumber menyebut air, tanah, hutan, udara) |

Tidak ada `[UNVERIFIED]` yang disajikan sebagai fakta. Empat penanda `[UNVERIFIED]` pada RPP §H
butir 1–3 dan §D.11 semuanya disertai `PERLU KONFIRMASI GURU`.

---

## 3. R006 — alasan `N/A`

Materi **tidak memuat** klaim kesehatan: tidak ada gejala, penyakit, organ tubuh, kelompok rentan,
efek permanen, maupun klaim kesembuhan. Sumber hanya menyebut "menghasilkan polusi" `[src:2]`,
dan RPP §D.8 secara eksplisit menghentikan pembahasan pada pernyataan itu. Karena tidak ada klaim
kesehatan yang perlu dinilai, aturan ini dinyatakan `N/A` — bukan dilewati.

---

## 4. R007 — bagian yang diminta guru

Permintaan awal memuat bagian *"Cara Cepat Membersihkan Lahan"* yang menjelaskan membakar lahan
sebelum musim tanam karena paling murah.

**Putusan atas permintaan itu: `REJECT` (R007 + R001).** Teks yang diminta tidak masuk ke draf.

| Alasan | Uraian |
|---|---|
| R007 | Pembakaran lahan disebut **harfiah** sebagai contoh praktik berbahaya yang dilarang diajarkan/dinormalisasi/dipromosikan. Menyajikannya sebagai "cara cepat" dan "paling murah" adalah promosi. |
| R001 | Tidak ada anchor sumber yang memuat pernyataan tentang pembersihan lahan, musim tanam, atau biaya. Klaim "paling murah" tidak dapat ditautkan. |

**Yang menggantikannya — RPP §D.11, kuis butir 10, slide 11.** Ketiganya memenuhi R007 karena:

1. Tidak memuat prosedur, bahan, jumlah, waktu, atau langkah pelaksanaan.
2. Menyatakan klaim sebagai *pendapat yang beredar*, bukan sebagai fakta materi.
3. Menguji klaim dengan fakta yang ada `[src:8]` `[src:CA6]` dan menyatakan secara eksplisit
   bahwa data biaya **tidak tersedia** → `[UNVERIFIED]`.
4. Tidak menambahkan narasi bencana sebagai pengganti (R002).

Dengan demikian tujuan pedagogis guru — murid berhadapan dengan klaim yang memang beredar di
lingkungannya — tercapai tanpa melanggar R007.

---

## 5. R005 — keseimbangan dan orientasi solusi

| Unsur wajib | Kehadiran |
|---|---|
| Upaya penanggulangan/mitigasi | RPP §D.7 — *reduce, reuse, recycle*, menanam pohon, menghemat energi, transportasi ramah lingkungan `[src:8]` |
| Peran murid | RPP §D.10 dan slide 12 — menghemat energi, menanam pohon, menyebarkan informasi benar `[src:9]` |
| Ajakan bertindak positif (R009) | Slide 12 penutup; komitmen aksi §E Pertemuan 2 |

Tidak ada pihak yang disalahkan tanpa dasar sumber.

---

## 6. Konsistensi angka lintas artefak (prasyarat FR-04)

| Angka | RPP | Kuis | Slide | Sumber |
|---|---|---|---|---|
| 145 MWac (192 MWp) | §D.9 | butir 7 | slide 8 | `[src:CA1]` |
| ±340.000 panel | §D.9 | — | slide 8 | `[src:CA1]` |
| ±200 hektare | §D.9 | — | slide 8 | `[src:CA1]` |
| 9 November 2023 | §D.9 | — | slide 8 | `[src:CA1]` |
| 2030 (FOLU) / 2060 (NZE) | §D.7 | butir 8 | slide 11 | `[src:CA6]` |
| 2 × 40 menit | §A, §E | — | slide 1 | `[src:1]` |
| 10 butir kuis | §F | 10 butir | — | usulan guru |

Konsisten. Tidak ada angka yang muncul di satu artefak lalu hilang di artefak lain tanpa alasan.

---

## 7. Temuan minor (tidak menghalangi `APPROVE`)

| No | Temuan | Aturan | Saran |
|---:|---|---|---|
| 1 | RPP §B tujuan 4 (dampak pembakaran fosil) dan tujuan 12 (tiga contoh perubahan bentuk energi) tidak punya butir kuis khusus | — | Sudah dinyatakan terbuka di kuis §Sebaran butir; guru dapat menambah 2 butir bila perlu |
| 2 | §D.11 memakai kata "membakar" tiga kali | R007 | Dapat diterima: konteksnya meninjau klaim, bukan mengajarkan. Bila guru ingin lebih hati-hati, frasa dapat diubah menjadi "cara yang disebut paling murah" tanpa kata kerja |
| 3 | Jumlah slide 12 untuk 2 × 40 menit | — | Padat tetapi wajar; slide 3–5 dapat digabung bila waktu mendesak |

---

## 8. Yang belum boleh dilakukan

| Gate | Status |
|---|---|
| `Human approver` | `PENDING` |
| `Publish status` | `LOCKED` |
| Format Rendering (`.docx` / `.pptx` / `.html`) | **Belum dijalankan** — menunggu persetujuan eksplisit |

Draf ini **bukan** paket siap pakai. Persetujuan guru diperlukan sebelum fase Format Rendering
dijalankan.
