# REVIEW — EDU-ORCH-20261106-005

> **Peran:** edu-reviewer · **Rulebook:** `08_Referensi/rulebook_ipas.md` (R001–R012, v2.0)
> **Fase dinilai:** C (kelas V–VI) — tercatat di `00_run_config.md`
> **Jumlah pass:** 3 (batas maksimum) · **Vonis akhir:** **REJECT — dieskalasi ke guru**

## Ringkasan

| Pass | Vonis | Temuan R001 | Catatan teknis | Yang berubah sesudahnya |
|-----:|-------|------------:|---------------:|--------------------------|
| 1 | REJECT | 3 | 7 | Kuis diberi atribusi; klaim mekanisme §D.4 dihapus; klaim empiris dibuang; alokasi waktu disusun ulang |
| 2 | REJECT | 3 (baru) | 6 | Slide 6 dan 4 dikoreksi; slide 1 diberi sumber; §H, rubrik, dan §E diperbaiki |
| 3 | REJECT | 1 | 5 | §C diperbaiki — **tidak ditinjau ulang** (anggaran habis) |

Pola yang terlihat: setiap perbaikan menutup temuan di satu berkas tetapi meninggalkan kalimat
kembarannya di berkas lain. Pass 1 memperbaiki §D.4 tetapi tidak slide 6. Pass 2 memperbaiki slide 6
tetapi tidak §C. Ini bukan kebetulan — penyebabnya dicatat di §E.

---

## A. Pass 1 — REJECT

### A.1 Temuan R001

| # | Lokasi | Kutipan | Pelanggaran |
|---|--------|---------|-------------|
| 1 | RPP §D.4 | "…listrik dibuat dari sumber energi lain — sehingga menghemat listrik berarti menghemat sumber energinya." | Kalimat tanpa tag; klausa mekanisme tidak ada di sumber; bertentangan dengan §H.1 dokumen yang sama |
| 2 | Kuis, 17 butir | — | Tidak ada atribusi sama sekali; seluruh jejak bergantung pada berkas metadata |
| 3 | RPP §C | "Energi tidak pernah hilang — ia hanya berpindah dan berubah bentuk `[src:6]`." | `[src:6]` menyatakan "diubah bentuknya", bukan "berpindah" |

### A.2 Catatan teknis

1. Post-test 12 butir + refleksi dalam 5 menit — tidak layak.
2. Pre-test 5 butir tidak punya slot waktu.
3. `00_plan.md` menyebut "satu butir per tujuan inti C4" padahal tujuan inti hanya 4.
4. **`grounding_report.md` tidak sah** — tag diresolusikan ke `source_material_ipas.md`, bukan lembar energi. Lihat §D.
5. "Seluruhnya dapat ditemukan di sekolah" bertentangan dengan §G.
6. Penomoran post-test mulai 6 membingungkan bila dicetak terpisah.
7. Aritmetika 40/40 menit, skor 50/120, dan rentang gain dinyatakan **benar**.

### A.3 Yang dinyatakan kuat

§H menyatakan tiga celah sebagai `[UNVERIFIED]` dan tidak satu pun bocor ke kuis atau slide; angka
CA1/CA6 konsisten; R005 ditopang struktur, bukan tempelan.

---

## B. Pass 2 — REJECT

### B.1 Temuan R001 (baru, akibat perbaikan pass 1)

| # | Lokasi | Kutipan | Pelanggaran |
|---|--------|---------|-------------|
| 1 | Slide 6 | "Karena itu 'menghemat energi' berarti menghemat **sumbernya**…" | Baris Sumber hanya `[src:6]` yang tidak memuatnya; §D.4 justru melarang hubungan itu |
| 2 | Slide 4 | "matahari, angin, dan air muncul di **kedua** daftar" | Dua daftar di slide itu adalah sumber energi dan **bentuk** energi; matahari/angin/air tidak ada di daftar bentuk energi. Kalimat benar di RPP, salah setelah disalin |
| 3 | Slide 1 | "2 pertemuan × 40 menit" dengan Sumber "—" | Angka itu fakta `[src:1]` |

### B.2 Catatan teknis

1. §H menulis "Lima hal… **Empat** di antaranya" — hanya tiga yang bertanda `[UNVERIFIED]`.
2. Aritmetika dinyatakan benar; 17 kunci diperiksa satu per satu.
3. FOLU ditayangkan tanpa penjabaran.
4. 12 butir + refleksi dalam 12 menit ≈ 55 detik per butir.
5. Butir 6 menuntut inferensi dari satu kata pada `[src:4]`.
6. **`00_run_config.md` menulis "Pass 2: APPROVE" sebelum pass 2 berjalan.** Putusan reviewer tidak boleh ditulis lebih dulu.

### B.3 Kritik yang diterima, tidak diperbaiki

Reviewer menilai RPP memuat lebih banyak pagar ("wajib dijaga", "batas satuan") daripada langkah
mengajar. Kritik ini **diterima sebagai benar** dan **tidak diperbaiki**: dokumen ini adalah keluaran
pipeline yang harus menunjukkan batas sumbernya, dan menghapus pagar akan menyembunyikan justru
informasi yang paling dibutuhkan guru. Dicatat sebagai konsekuensi desain, bukan cacat yang diabaikan.

---

## C. Pass 3 — REJECT (vonis akhir)

### C.1 Temuan R001

| # | Lokasi | Kutipan | Pelanggaran |
|---|--------|---------|-------------|
| 1 | RPP §C | "…melainkan **memilih sumber yang dapat diperbarui** `[src:2]` dan **memakai energi seperlunya** `[src:7]`." | `[src:2]` hanya mendefinisikan energi alternatif, tidak menyatakan bahwa menghemat energi berarti memilih sumber terbarukan. Kalimat ini juga memberi definisi kedua yang bertentangan dengan §D.6 |

### C.2 Catatan teknis

1. Aritmetika benar: P1 40 menit, P2 40 menit, skor 50/120, gain −30…+30, rubrik 4×3 = 12.
2. Angka lintas berkas konsisten; tidak ada "145 MWp" sebagai nilai.
3. §D.3 masih memakai frasa "kedua daftar" yang dapat dibaca sebagai sumber + bentuk energi.
4. Slide 9 memakai "*net sink*" tanpa penjelasan singkat.
5. Pertemuan 2 berakhir pada post-test tanpa penutup/refleksi.

### C.3 Tindakan Orchestrator

Temuan C.1 **diperbaiki** dengan memisahkan dua gagasan yang tertumpuk: definisi penghematan
(`[src:7]`) berdiri sendiri, dan pernyataan tentang energi alternatif (`[src:2]`) menjadi paragraf
terpisah. Perbaikan ini **hanya menghapus atribusi yang salah dan tidak menambah klaim baru**.

Perbaikan itu **tidak ditinjau ulang**. Aturan keras pipeline menetapkan maksimum tiga lingkar
remediasi; lingkar keempat tidak dijalankan, dan Orchestrator tidak berwenang menyatakan dirinya
APPROVE. Karena itu status run adalah **ESCALATED_TO_HUMAN**, bukan APPROVE.

### C.4 Catatan teknis yang dibiarkan terbuka

Butir C.2 nomor 3, 4, dan 5 **tidak** diperbaiki. Ketiganya bukan pelanggaran rulebook, dan setiap
suntingan tambahan sesudah pass terakhir hanya akan menambah isi yang belum ditinjau. Ketiganya
dicatat sebagai butir terbuka pada lembar persetujuan.

---

## D. Cacat alat yang ditemukan pass 1 — dan diperbaiki

**Temuan.** `tools/check_grounding.py` menyimpan anchor dalam satu kamus datar. Dua lembar sumber
memakai penomoran yang sama (`source_material_ipas.md` dan `source_material_energi.md` sama-sama
mendeklarasikan `## [src:1]`–`## [src:9]`), sehingga berkas yang terakhir dalam urutan abjad menimpa
yang lebih awal. Akibatnya laporan pertama run ini menyatakan **PASS 237 tag** padahal setiap
`[src:2]` diresolusikan ke bagian *Kelestarian Alam* pada lembar yang salah.

Laporan yang bersih tetapi menunjuk sumber yang keliru lebih berbahaya daripada laporan yang gagal:
ia memberi rasa aman yang tidak berdasar.

**Perbaikan.** Anchor kini disimpan per berkas, dan tag yang muncul di lebih dari satu lembar
dinyatakan `AMBIG` — kegagalan, bukan tebakan. Opsi `--primary-source` menetapkan lembar yang
berlaku bagi satu run. `tools/doctor.py` kini menyebutkan lembar sumber setiap run secara eksplisit.

**Uji regresi.** Kelima run lama dijalankan ulang dengan `--primary-source` masing-masing dan
hasilnya tidak berubah: `materi_ajar` 121, `edu_output` 121, `edu_output_wujud_zat` 115,
`edu_output_wujud_zat_faseC` 212, `edu_output_tata_surya` 109 — semuanya PASS.

**Konsekuensi yang dinyatakan.** Tanpa `--primary-source`, run mana pun yang memakai tag angka akan
sekarang **gagal**, bukan lulus secara keliru. Ini perubahan perilaku yang disengaja.

---

## E. Penyebab berulangnya temuan

Tiga penolakan berurutan berakar pada satu kebiasaan: **kalimat disalin antarberkas tanpa menyesuaikan
konteksnya**. Kalimat "matahari, angin, dan air muncul di kedua daftar" benar di RPP (sumber energi vs
contoh alternatif) dan salah di slide (sumber energi vs bentuk energi). Hubungan "hemat energi =
hemat sumber" dilarang di §D.4, tetapi tetap hidup di §C dan slide 6.

Pelajaran untuk run berikutnya: setiap perbaikan satu kalimat harus disertai pencarian kalimat
kembarannya di seluruh berkas run, bukan hanya di tempat temuan disebutkan.

## F. Vonis per aturan — pass 3

| Aturan | Vonis | Dasar |
|--------|-------|-------|
| R001 | **PELANGGARAN** | §C mengatribusikan definisi penghematan kepada `[src:2]` yang tidak memuatnya |
| R002 | LULUS | Tidak ada bahasa panik; target iklim disampaikan sebagai target, bukan ancaman |
| R003 | LULUS | Fase C tercatat; istilah asing dijelaskan atau dinyatakan batas |
| R004 | LULUS | CP-C.2.1.4 ada di Fase C; B5 ditandai prasyarat + gerbang manusia |
| R005 | LULUS | Empat upaya mitigasi `[src:8]` dan tiga peran murid `[src:9]` hadir secara semantik |
| R006 | N/A | Tidak ada klaim kesehatan sama sekali; diperiksa §C, §D, kuis, dan 10 slide |
| R007 | LULUS | Tidak ada praktik berbahaya; arahnya pencegahan `[src:7]` `[src:8]` |
| R008 | LULUS | Nada hangat dan memberdayakan |
| R009 | LULUS | Bahasa baku; ajakan bertindak ada di slide 10 |
| R010 | LULUS | Butir 11 menilai perilaku, bukan murid; tidak ada label negatif |
| R011 | LULUS | CA1/CA6 resmi, bertanggal, URL tercatat; tidak ada tautan dipaksakan |
| R012 | N/A | Tidak ada klaim komersial/halal; "terbesar di Asia Tenggara" adalah status faktual `[src:CA1]` |
