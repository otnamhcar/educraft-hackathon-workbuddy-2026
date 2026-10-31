# RULEBOOK — Konten Edukasi IPAS (Domain)

> **Versi:** 2.0 · **Tanggal:** 31 Oktober 2026 · **Status:** kanonik
> **Fungsi:** dokumen aturan tertulis yang menjadi rujukan **Reviewer Agent**. Setiap *rejection*
> wajib mengutip ID aturan di sini dan mengutip teks yang melanggar.
>
> **Kanonik vs salinan:** file ini adalah sumber kebenaran. Salinan ada di
> `05_Bukti_Proses/skills_package/edu-orchestrator/assets/` dan `.../edu-reviewer/assets/`.
> Salinan harus **byte-identik**; diverifikasi dengan checksum sebelum submit.

## Changelog

| Versi | Tanggal | Perubahan | Dampak pada putusan lama |
|-------|---------|-----------|--------------------------|
| 1.0 | 29 Okt 2026 | R001–R008 | — |
| 1.1 | 30 Okt 2026 | Tambah R009–R011 | Tidak ada; putusan lama tetap sah |
| **2.0** | **31 Okt 2026** | (a) R003–R007 dilepas dari nomor tag & topik tertentu; (b) tambah R012 (klaim komersial/halal); (c) tambah §0 Klasifikasi tag dan §0b Aturan N/A | Tidak ada. Perubahan bersifat generalisasi + penambahan; tidak ada aturan yang dilonggarkan |

---

## 0. Klasifikasi tag (wajib dipahami sebelum menilai R001)

| Kelas tag | Bentuk | Boleh menopang |
|-----------|--------|----------------|
| Fakta | `[src:1]` … `[src:n]` | Klaim faktual apa pun |
| Kurikulum | `[src:CP]`, `[src:B4]`, `[src:C4]` | Hanya pernyataan kurikulum (CP/CPL), **tidak pernah** fakta sains |
| Konteks aktual | `[src:CA1]` … | Klaim dunia nyata, dengan URL resmi + tanggal akses |

**Tag kurikulum tidak pernah boleh menggantikan tag fakta.** Ini kesalahan yang menghasilkan
penolakan 29 Oktober 2026 dan terulang pada run `-002`.

## 0b. Aturan N/A

Reviewer **wajib** menyatakan `N/A` secara eksplisit beserta alasannya, bukan melewatkan aturan.
`N/A` tanpa alasan = temuan Minor.

---

## Aturan Inti (wajib)

**R001 — Factual accuracy / grounding**
Setiap fakta, angka, atau statistik **wajib** merujuk tag `[src:#]` yang **dapat diselesaikan** ke
bagian sumber yang benar-benar memuat pernyataan itu. Dua syarat, bukan satu:
1. **Atribusi** — kalimat membawa tag.
2. **Resolusi** — tag menunjuk bagian sumber yang mendukung kalimat tersebut, dan kelas tag-nya sesuai
   (§0).
Gagal salah satu = **REJECT**. Fakta yang tidak ada di sumber harus ditulis `[UNVERIFIED]` +
`PERLU KONFIRMASI GURU`, bukan dikarang.

**R002 — No fear-mongering**
Bahasa tenang dan tidak panik. Dilarang melebih-lebihkan bahaya ("Kalimantan akan hilang", "semua
orang sakit parah"). Narasi faktual dan solutif.

**R003 — Age-appropriate (sesuai fase sasaran)**
Kosakata, panjang kalimat, dan detail disesuaikan dengan **fase yang tercatat di `00_run_config.md`**
(Fase B: kelas III–IV; Fase C: kelas V–VI). Hindari detail traumatis. Bila fase tidak tercatat,
Reviewer menetapkan Fase C dan menandainya sebagai temuan Minor.

**R004 — Curriculum alignment**
Konten selaras dengan Capaian Pembelajaran pada `cp_ipas.md` untuk fase sasaran. Bila topik berada di
fase lain, wajib ditandai `PERLU KONFIRMASI GURU` dan disetujui manusia sebelum publikasi. Validasi
akhir tetap milik guru/SME.

**R005 — Balanced & solution-oriented**
Wajib memuat **upaya penanggulangan/mitigasi** dan **peran murid** sebagaimana tersedia di sumber.
Dilarang menyalahkan pihak tertentu tanpa dasar di sumber. Rujukan bersifat **semantik**: bagian
"upaya penanggulangan" dan "peran siswa/murid" pada sumber yang sedang dipakai — bukan nomor tag
tertentu, agar aturan tetap berlaku saat sumber diganti.

**R006 — Health-claim caution**
Dilarang klaim efek **permanen**, **kesembuhan**, atau **efikasi absolut** yang tidak didukung sumber.
Sajikan gejala umum dan kelompok rentan bila sumber memuatnya.

**R007 — No harmful promotion**
Dilarang mengajarkan, menormalisasi, atau mempromosikan praktik berbahaya (mis. pembakaran lahan,
konsumsi zat berbahaya). Arahkan ke pencegahan sesuai sumber.

**R008 — Brand / pedagogic tone**
Ramah, edukatif, memberdayakan. Bila ada panduan brand sekolah, ikuti itu.

**R009 — Language standard & positive CTA**
Bahasa baku sesuai KBBI, kalimat jelas. Setiap materi naratif (slide, video, artikel) diakhiri ajakan
bertindak positif. Hindari singkatan tidak baku dan bahasa gaul yang membingungkan.

**R010 — Non-stigmatizing / neutral phrasing**
Soal, umpan balik, dan narasi tidak memojokkan, menyalahkan, atau memberi label negatif kepada
murid/kelompok. Diksi sopan, hangat, tidak ambigu, inklusif.

**R011 — Actual-context verification**
Setiap klaim `[src:CA#]` wajib berasal dari sumber resmi, bertanggal, dan dapat ditelusuri (URL
lembaga resmi). Konteks aktual tanpa sumber resmi = **REJECT**. Tidak ada entri relevan = jangan
memaksakan tautan; nyatakan `N/A` beralasan.

**R012 — Commercial, advertising & halal claim** *(baru di v2.0)*
Berlaku bila materi memuat klaim komersial, klaim efikasi produk, testimoni, atau klaim halal.
1. Klaim penyembuhan/efikasi produk = **REJECT** (selaras R006).
2. Klaim halal tanpa nomor sertifikat dan lembaga penerbit = **REJECT**.
3. Superlatif komersial tanpa bukti ("terbaik", "nomor satu") = **REJECT**.
4. Materi edukasi murni tanpa unsur komersial = `N/A` beralasan.

*Alasan keberadaan aturan ini:* handbook Challenge C secara eksplisit menyebut *factual accuracy,
brand tone, advertising and halal requirements*. Tanpa R012, agen tidak punya dasar menolak klaim
komersial/halal — celah penilaian yang nyata.

---

## Aturan Umum (dari handbook, tetap berlaku)
- **Human approval** sebelum publikasi.
- **Escalation:** 3× `REJECT` → henti dan eskalasi ke Guru/SME dengan temuan yang tersisa.
- **Record:** simpan pertukaran antar-agen dan riwayat revisi.

---

## Contoh kalibrasi

| Draft | Putusan | Alasan |
|-------|---------|--------|
| "Asap bikin anak langsung meninggal" | REJECT R006 + R002 | Klaim permanen tanpa dasar + fear-mongering |
| "Kabut asap menurunkan kualitas udara [src:3]" | APPROVE | Ter-grounding dan tenang |
| "Karhutla bikin ekonomi Kalimantan hancur total" | REJECT R002 | Melebih-lebihkan; sumber hanya menyebut penurunan sektor tertentu |
| "Es mencair ketika suhunya naik [src:B4]" | **REJECT R001** | `[src:B4]` adalah anchor topik kurikulum, bukan sumber fakta |
| "Menurut sumber, es mencair pada suhu di atas 0 °C [src:4]" | APPROVE | Fakta + kelas tag benar |
| "Produk ini 100% halal" | REJECT R012 | Klaim halal tanpa sertifikat |
| "Siswa dapat menanam pohon [src:8]" | APPROVE | Solutif dan ter-grounding |

---

## Batas yang diakui
Aturan ini ditegakkan **lewat prompt**, bukan mesin inferensi. Konsekuensinya: kepatuhan bergantung
pada kualitas kontrak dan pada Reviewer yang mengutip teks. Mitigasi: setiap putusan wajib mengutip
teks + ID aturan, sehingga manusia dapat mengaudit audit. Pemeriksaan deterministik yang sudah ada
hanya untuk R001 (lihat `tools/check_grounding.py`).
