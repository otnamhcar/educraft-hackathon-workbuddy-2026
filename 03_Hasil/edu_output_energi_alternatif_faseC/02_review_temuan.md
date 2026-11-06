# Temuan Review — EDU-ORCH-20261106-006

> **Peran:** `edu-reviewer` · **Iterasi:** 1 dari maksimum 3
> **Rulebook:** `08_Referensi/rulebook_ipas.md` v2.0 (R001–R012)
> **Putusan keseluruhan:** `REJECT` **sebagian** — dua kalimat yang diminta guru ditolak;
> sisa draf `APPROVE` menunggu persetujuan manusia.

---

## 1. Ringkasan putusan

| No | Kalimat yang diminta guru | Putusan | Aturan |
|---|---------------------------|---------|--------|
| 1 | *"Asap pembakaran menyebabkan kerusakan permanen pada paru-paru anak dan tidak bisa disembuhkan."* | **REJECT** | R001, R006, R002 |
| 2 | *"Masker kain 100% mencegah ISPA."* | **REJECT** | R001, R006, R012 |

Draf RPP tanpa kedua kalimat: **APPROVE** (menunggu persetujuan guru, `PENDING`).

---

## 2. Temuan 1 — klaim kerusakan permanen paru-paru

**Teks yang diperiksa:** *"Asap pembakaran menyebabkan kerusakan permanen pada paru-paru anak dan
tidak bisa disembuhkan."*

**R001 — Factual accuracy / grounding: GAGAL.**
Kalimat tidak membawa tag. Bila diberi tag terdekat yang tersedia, `[src:2]`, tag itu tidak
**resolusi**: bagian `[src:2]` hanya menyatakan bahwa bahan bakar fosil "menghasilkan polusi".
Tidak ada kata "paru-paru", "pernapasan", "penyakit", atau "anak" di seluruh
`source_material_energi.md`. Dua syarat R001 — atribusi dan resolusi — gagal keduanya.

**R006 — Health-claim caution: GAGAL, dua kali.**
R006 melarang tiga kategori klaim yang tidak didukung sumber: efek **permanen**, **kesembuhan**,
dan **efikasi absolut**. Kalimat ini memuat dua sekaligus:
- "kerusakan **permanen**" → kategori pertama;
- "**tidak bisa disembuhkan**" → kategori kedua (klaim tentang ketidakmampuan disembuhkan adalah
  klaim medis tentang prognosis, bukan sekadar gejala umum).

R006 juga menetapkan alternatif yang sah: "Sajikan gejala umum dan kelompok rentan **bila sumber
memuatnya**." Sumber tidak memuatnya. Karena itu tidak ada versi lunak dari kalimat ini yang dapat
dibangun di atas sumber yang ada.

**R002 — No fear-mongering: GAGAL.**
Sasaran pembaca adalah kelas V–VI (Fase C). Kalimat menyatakan kerusakan yang tidak dapat
diperbaiki pada organ tubuh anak — pembaca yang dimaksud adalah anak itu sendiri. Rulebook
§Contoh kalibrasi mencatat preseden langsung:

| Draf | Putusan | Alasan |
|------|---------|--------|
| "Asap bikin anak langsung meninggal" | REJECT R006 + R002 | Klaim permanen tanpa dasar + fear-mongering |

Kalimat yang diminta guru berada pada kelas pelanggaran yang sama, dengan intensitas lebih rendah
tetapi struktur klaim identik: **akibat kesehatan berat + tanpa sumber + tanpa jalan keluar**.

**Catatan substantif (di luar rulebook).** Selain soal kepatuhan, klaim ini juga tidak akurat
secara medis sebagai pernyataan umum. Paparan asap memang berkaitan dengan gangguan pernapasan
pada anak, tetapi menyatakan seluruh kerusakan bersifat permanen dan tidak dapat disembuhkan
adalah generalisasi yang berlebihan. Menempatkannya dalam materi kurikulum tanpa sitasi akan
mengajarkan murid bahwa klaim kesehatan tidak perlu bukti — bertentangan langsung dengan
tujuan "menyebarkan informasi yang benar tentang lingkungan" `[src:9]`.

---

## 3. Temuan 2 — klaim efikasi absolut masker kain

**Teks yang diperiksa:** *"Masker kain 100% mencegah ISPA."*

**R001 — Factual accuracy / grounding: GAGAL.**
Sumber tidak memuat kata "masker", "ISPA", "infeksi", maupun klaim efikasi alat pelindung apa pun.
Tidak ada tag yang dapat menopang kalimat ini, bahkan secara longgar.

**R006 — Health-claim caution: GAGAL.**
"100% mencegah" adalah bentuk paling murni dari **efikasi absolut** yang dilarang R006. Tidak ada
ambang ketidakpastian di dalam kalimat: klaimnya total.

**R012 — Commercial, advertising & halal claim: GAGAL.**
R012 butir 1 menyatakan "Klaim penyembuhan/efikasi produk = REJECT (selaras R006)". Masker kain
adalah produk, dan "100% mencegah" adalah klaim efikasi produk. Butir 4 (materi edukasi murni =
`N/A`) **tidak berlaku** di sini justru karena kalimat ini memasukkan unsur efikasi produk ke
dalam materi edukasi.

**Catatan substantif (di luar rulebook).** Ini klaim yang paling berisiko dalam permintaan ini.
Masker kain menyaring sebagian partikel, tetapi tidak ada masker kain yang menjamin perlindungan
total terhadap ISPA — penyakit yang penularannya juga melalui tangan dan permukaan, bukan hanya
droplet. Menyatakan "100%" kepada murid kelas V–VI berpotensi menumbuhkan rasa aman yang keliru,
dan bila materi ini dipakai mengajar, klaim tersebut menjadi tanggung jawab guru yang
menyampaikannya.

---

## 4. Yang diterima sebagai pengganti

Bagian **D.8** RPP memuat versi topik "dampak" yang seluruhnya dapat diselesaikan ke sumber:

| Langkah | Isi | Tag |
|---------|-----|-----|
| a | Bahan bakar fosil menghasilkan polusi; energi alternatif ramah lingkungan → dampak bergantung pada pilihan sumber | `[src:2]` |
| b | Udara termasuk sumber daya alam yang harus dijaga bagi generasi mendatang → polusi adalah persoalan pelestarian | `[src:8]` |

Rangkaian ini mempertahankan **maksud pedagogis** guru (murid memahami bahwa ada dampak buruk dari
pilihan energi) tanpa memuat klaim yang tidak dapat dipertanggungjawabkan. Ia juga lebih sesuai
dengan CP C4 yang berorientasi **menghasilkan upaya** `[src:C4]`, bukan menghafal daftar penyakit.

**Bila guru tetap ingin memuat klaim kesehatan**, jalur yang sah ada dua:

1. Guru menyerahkan sumber resmi (Kemenkes, WHO, atau buku IPAS yang diterbitkan resmi) beserta
   kutipan dan tanggal aksesnya. Kalimat lalu dimasukkan dengan tag baru dan tetap melewati review.
2. Guru memilih untuk tidak memuatnya, dan topik dampak kesehatan dibahas sebagai pertanyaan
   terbuka: "Menurutmu, apa yang terjadi pada udara dan tubuh kita bila udara tercemar?" — jawaban
   murid dicatat sebagai dugaan, bukan kesimpulan.

---

## 5. Aturan yang dinyatakan `N/A`

Sesuai rulebook §0b, setiap aturan yang tidak berlaku dinyatakan eksplisit:

| Aturan | Status | Alasan |
|--------|--------|--------|
| R003 Age-appropriate | LULUS | Kalimat per instruksi 12–20 kata, kosakata Fase C, tanpa detail traumatis setelah kedua kalimat dihapus |
| R004 Curriculum alignment | LULUS | CP sasaran `CP-C.2.1.4` `[src:C4]`, fase C tercatat di `00_run_config.md` |
| R005 Balanced & solution-oriented | LULUS | Memuat upaya penanggulangan `[src:8]` dan peran murid `[src:9]` |
| R007 No harmful promotion | `N/A` | Materi tidak mengajarkan atau menormalisasi praktik berbahaya |
| R008 Brand / pedagogic tone | LULUS | Nada memberdayakan; tidak ada label negatif |
| R009 Language standard | LULUS | Bahasa baku; ditutup ajakan bertindak positif pada Pertemuan 2 |
| R010 Non-stigmatizing | `N/A` | Tidak ada soal atau narasi yang menyasar kelompok tertentu |
| R011 Actual-context verification | LULUS | `[src:CA1]` dan `[src:CA6]` ber-URL resmi dan bertanggal akses |
| R012 Commercial/advertising | GAGAL pada kalimat 2, `N/A` pada sisa draf | Lihat §3 |

---

## 6. Konsekuensi pada state

- `Iteration` di `00_run_config.md` dinaikkan ke `1` (menghitung penolakan, bukan pass review).
- Karena penolakan terjadi pada **tahap intake** — sebelum draf ditulis — tidak ada lingkar
  remediasi Writer yang terpakai. Anggaran 3 iterasi masih utuh.
- `Human approver` tetap `PENDING`. Draf tidak boleh dipublikasikan.

---

## 7. Remediasi pass 2 — 15:18 GMT+7

Guru menerima temuan §2 dan §3 dan memerintahkan perbaikan dengan satu syarat tambahan yang
dicatat sebagai batasan: **kekosongan sumber tidak boleh diisi dengan fakta baru.** Sumber tidak
memuat gejala maupun kelompok rentan, jadi keduanya tidak boleh muncul sebagai pengganti. Yang
tersisa hanya satu pernyataan: pembakaran bahan bakar fosil menghasilkan polusi `[src:2]`.

### 7.1 Perubahan yang dilakukan

| Lokasi | Sebelum | Sesudah |
|--------|---------|---------|
| §B tujuan 4 | "Menjelaskan mengapa polusi … berkaitan dengan kewajiban menjaga udara sebagai SDA `[src:8]`" | "Menyatakan bahwa pembakaran bahan bakar fosil menghasilkan polusi `[src:2]`" |
| §D.8 judul | `[src:2]` `[src:8]` | `[src:2]` saja |
| §D.8 isi | Dua langkah turunan: (a) polusi dari pilihan sumber, (b) udara sebagai SDA yang dijaga | Satu pernyataan sumber + pernyataan batas. Langkah (b) dihapus karena merupakan **inferensi**, bukan pernyataan sumber |
| §D.8 catatan | "Batas keras" menyebut paru-paru, ISPA, masker | "Yang boleh dan tidak boleh ditambahkan" — larangan dinyatakan tanpa menyebut topik terlarang |
| §E Pertemuan 1 | Guru memandu dua langkah D.8 | Guru menyampaikan satu pernyataan sumber; tidak menambah uraian penyakit/gejala/alat pelindung |
| §H butir 6–7 | Memuat **kutipan verbatim** kedua kalimat yang diminta guru | Kutipan dihapus; hanya rujukan aturan (R001, R006, R012, R002) yang tersisa |

### 7.2 Alasan langkah (b) ikut dihapus

Langkah (b) — "udara yang tercemar adalah sumber daya alam yang harus dijaga" — memang bertumpu
pada `[src:8]`, jadi ia bukan fakta karangan. Tetapi ia adalah **inferensi dua langkah**: sumber
menyatakan udara harus dijaga, bukan bahwa polusi pembakaran fosil merusak udara. Instruksi guru
"cukup nyatakan bahwa pembakaran bahan bakar fosil menghasilkan polusi" menutup celah itu. Menjaga
materi tetap pada satu pernyataan langsung membuat setiap kalimat dapat ditunjuk balik ke satu
baris sumber, tanpa rantai penalaran di antaranya.

Konsekuensi yang diterima: topik "dampak" kini sangat tipis — satu kalimat. Itu bukan kekurangan
penyusunan, melainkan **cermin dari sumber** yang memang hanya menyebut satu dampak `[src:2]`.
Guru yang ingin materi lebih kaya perlu memasok sumber tambahan; RPP tidak boleh menambalnya
sendiri.

### 7.3 Verifikasi ulang

| Pemeriksaan | Hasil |
|---|---|
| `check_grounding.py` | **PASS** — 134 tag, 0 dangling, 0 kelas, 0 ambigu |
| Sisa kata "paru", "ISPA", "masker", "100%" di draf | **0** — hanya frasa aturan "klaim efek permanen dan klaim kesembuhan dilarang R006" pada §H yang tersisa, dan itu pernyataan larangan, bukan klaim |
| Total menit Pertemuan 1 & 2 | tetap 40 + 40 |
| Tag `[src:8]` yang hilang dari §D.8 | masih dipakai di §D.7, §C, dan §B tujuan 5 — tidak ada tag yatim |

### 7.4 Putusan pass 2

**`APPROVE`** untuk draf. Tidak ada klaim kesehatan permanen, tidak ada klaim efikasi absolut, dan
tidak ada fakta pengganti yang dikarang. Status tetap `AWAITING_APPROVAL`: persetujuan manusia
belum diberikan, dan RPP belum boleh dipublikasikan.

`Iteration` tetap **1** — remediasi bukan penolakan baru.
