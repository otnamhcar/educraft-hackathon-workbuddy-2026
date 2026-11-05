# 06_review.md — Putusan Reviewer

> **Run:** EDU-ORCH-20261104-004 · **Agen:** Reviewer
> **Fase dinilai:** Fase C (kelas V–VI) — dibaca dari `00_run_config.md`
> **Rulebook:** `rulebook_ipas.md` v2.0 (R001–R012)
> **Putusan:** ❌ **REJECT** (pass 1)

## Ringkasan

Draf sudah kuat pada disiplin tag: 171 tag, seluruhnya resolvable, tidak ada tag kurikulum yang
menopang fakta sains. Pemeriksaan deterministik `tools/check_grounding.py` menyatakan **PASS**.

Tetapi PASS itu hanya membuktikan tag *menunjuk ke suatu tempat*. Ia tidak memeriksa apakah kalimat
benar-benar didukung tempat yang ditunjuk. Di situlah ditemukan **tiga kalimat fakta yang tidak
bertag dan tidak ada di sumber**, satu di antaranya mengarang besaran waktu. Ketiganya lolos dari
pemeriksaan deterministik karena kalimat tanpa tag tidak diperiksa oleh alat itu sama sekali.

Selebihnya minor: satu salah ejaan baku, satu diksi yang berpotensi melabeli murid.

---

## Temuan

### Major — R001 (factual accuracy / grounding)

**Temuan 1 · `02_artikel.md` baris 15–16**

> **Kutipan:** "Es adalah air dalam wujud padat. Air minum adalah air dalam wujud cair. Uap yang
> mengepul dari air mendidih adalah air dalam wujud gas."

**Mengapa melanggar:** Tiga kalimat ini menyatakan fakta, tetapi **tidak satu pun membawa tag**.
Tag `[src:W1]` menempel pada kalimat sebelumnya dan hanya menopang "tiga wujud zat utama: padat,
cair, gas" — bukan pemetaan bahwa es/air/uap adalah ketiga wujud dari bahan yang sama. Sumber
`[src:W1]` tidak memuat pemetaan itu. Entri yang mendekati, `[src:W11]`, berstatus **turunan tim**,
bukan kutipan. Jadi ada dua pelanggaran sekaligus: atribusi hilang, dan resolusinya tidak ada di
kelas tag fakta kutipan.

**Saran:** Tag ketiga kalimat itu dengan `[src:W11]` **dan** beri penanda turunan sebaris, atau
pindahkan ke paragraf yang sudah menyatakan `[src:W11]` sebagai turunan. Jangan biarkan berdiri
sebagai kalimat fakta tanpa penanda.

---

**Temuan 2 · `02_artikel.md` baris 76**

> **Kutipan:** "Bedanya, di Puncak Jaya dan di kutub, jumlah esnya sangat besar sehingga perubahannya
> berlangsung dalam hitungan tahun, bukan menit."

**Mengapa melanggar:** Ini klaim besaran waktu. Sumber `[src:W5]` hanya menyebut tiga peristiwa —
hujan es, hilangnya es Puncak Jaya, mencairnya es kutub dan gletser — tanpa menyatakan skala waktu
apa pun. Kalimat ini mengarang perbandingan "tahun versus menit" yang tidak dapat diselesaikan ke
bagian sumber mana pun. Ini persis pola yang ditolak pada 29 Oktober 2026: kalimat masuk akal secara
sains, tetapi bukan isi sumber.

**Saran:** Hapus klausa perbandingan waktu, atau ganti dengan pernyataan yang memang ada di sumber,
misalnya bahwa ketiga peristiwa itu sama-sama perubahan wujud yang dipengaruhi suhu `[src:W3]`
`[src:W5]`. Bila guru ingin mempertahankan skala waktu, tandai `[UNVERIFIED]` +
`PERLU KONFIRMASI GURU` dan mintakan sumbernya.

---

**Temuan 3 · `03_slide_outline.md` baris 16**

> **Kutipan:** "- Kalimat kunci: wujud dapat berubah, bahannya tetap."

**Mengapa melanggar:** Bullet ini berdiri sebagai kalimat kunci yang akan ditayangkan tanpa tag.
Isinya bertumpu pada `[src:W11]` butir 1 — **turunan tim**, bukan kutipan. Penanda turunan muncul
pada bullet di atasnya, tetapi "kalimat kunci" ini adalah teks yang akan dibaca murid dari layar,
sehingga ia perlu penandanya sendiri. Tanpa itu, penonton menerima pernyataan turunan sebagai fakta
sumber.

**Saran:** Tambahkan `[src:W11]` *(turunan tim)* pada bullet itu, atau hapus dari daftar kalimat kunci
dan cukupkan dengan bullet bergambar yang sudah bertag.

---

### Minor — R009 (language standard)

**Temuan 4 · `02_artikel.md` baris 39**

> **Kutipan:** "Di sinilah ilmuan sejati berbeda dari penebak."

**Mengapa melanggar:** "ilmuan" bukan bentuk baku KBBI; bentuk bakunya **ilmuwan**. R009 mewajibkan
bahasa baku sesuai KBBI. Karena kata ini muncul di bahan bacaan murid, salah ejaan akan ikut
terbaca sebagai model.

**Saran:** Ganti menjadi "ilmuwan".

---

### Minor — R010 (non-stigmatizing / neutral phrasing)

**Temuan 5 · `02_artikel.md` baris 39**

> **Kutipan:** "Di sinilah ilmuan sejati berbeda dari penebak."

**Mengapa melanggar:** Kata "penebak" memberi label negatif pada cara berpikir yang justru wajar
dilakukan murid Fase C — menebak sebelum tahu. R010 meminta diksi yang tidak memojokkan murid.
Kalimat ini berisiko membuat murid yang pernah menebak merasa disalahkan, padahal seluruh alur
pembelajaran justru meminta mereka menuliskan prediksi lebih dulu `[src:W6]`.

**Saran:** Ubah menjadi pembeda perilaku, bukan pembeda orang. Misalnya: "Di sinilah penyelidikan
berbeda dari menebak." Perbedaannya terletak pada ada tidaknya catatan suhu dan waktu `[src:W7]`,
bukan pada siapa yang menebak.

---

### Minor — R001 (atribusi longgar pada tujuan pembelajaran)

**Temuan 6 · `01_lesson_plan.md` baris 27**

> **Kutipan:** "Menyebutkan tiga wujud zat — padat, cair, dan gas — dan mengenalinya pada bahan di
> sekitar `[src:W1]`."

**Mengapa melanggar:** `[src:W1]` hanya menyebut tiga wujud zat utama. Klausa "mengenalinya pada
bahan di sekitar" adalah tambahan, dan dukungan terdekatnya ada pada `[src:W11]` yang berstatus
turunan. Atribusi tunggal ke `[src:W1]` karena itu terlalu longgar.

**Saran:** Pecah menjadi dua klausa bertag berbeda, atau tambahkan `[src:W11]` *(turunan)* pada
klausa kedua.

---

## Aturan yang lulus

| Aturan | Dasar |
|--------|-------|
| **R002** — no fear-mongering | Isu Puncak Jaya dan es kutub disampaikan sebagai peristiwa faktual, tanpa kata bencana, tanpa ancaman. Nada konsisten tenang di kelima format. |
| **R003** — age-appropriate | Kosakata dan panjang kalimat sesuai kelas V–VI. Fase dibaca dari `00_run_config.md` = Fase C, bukan dipatok tetap. Tidak ada detail traumatis. |
| **R004** — curriculum alignment | Topik memang berada di Fase B (`[src:B4]`), dan itu **sudah ditandai** `PERLU KONFIRMASI GURU` di `00_run_config.md`, `01_lesson_plan.md` §1, dan `00_plan.md` `gaps`. R004 mengizinkan kondisi ini **asalkan** ditandai dan disetujui manusia sebelum publikasi. Penandaan ada; persetujuan belum — karena itu run berhenti di gate, bukan lolos diam-diam. |
| **R005** — balanced & solution-oriented | Peran murid terpenuhi dan ter-grounding: mengamati, memprediksi, merencanakan, melakukan, menyimpulkan `[src:W6]` `[src:W9]`. **Mitigasi tidak tersedia di sumber** dan hal itu dinyatakan terbuka di `01_lesson_plan.md` §9 alih-alih dikarang. Lihat "Butir terbuka" di bawah — ini keputusan guru, bukan cacat draf. |
| **R008** — brand / pedagogic tone | Ramah dan memberdayakan; tidak ada merek, tidak ada nada menakut-nakuti. |
| **R009** — positive CTA | Setiap materi naratif ditutup ajakan bertindak positif: artikel menutup dengan tiga percobaan rumah, slide 8 dengan ajakan menyelidiki. Satu cacat ejaan tercatat sebagai Temuan 4. |

## Aturan yang dinyatakan N/A

| Aturan | Alasan |
|--------|--------|
| **R006** — health-claim caution | N/A. Tidak ada klaim kesehatan, kesembuhan, atau efikasi apa pun di kelima draf. Yang diperiksa: kelima draf dibaca baris per baris untuk kata sifat efek dan klaim manfaat — tidak ditemukan. |
| **R007** — no harmful promotion | N/A. Tidak ada praktik berbahaya yang diajarkan atau dinormalisasi. Satu-satunya penyebutan pembakaran adalah "lilin yang meleleh saat dibakar" `[src:W4]`, yaitu contoh fenomena dari sumber, bukan anjuran melakukan pembakaran. |
| **R011** — actual-context verification | N/A beralasan. Tidak ada satu pun tag `[src:CA#]` di kelima draf. `konteks_aktual.md` hanya memuat CA1 (PLTS Cirata) dan CA6 (FOLU/NZE), keduanya tidak relevan dengan perubahan wujud zat. Tautan tidak dipaksakan — sesuai §0b, ini dinyatakan eksplisit, bukan dilewati. |
| **R012** — commercial / halal | N/A beralasan. Materi murni edukatif: tidak ada nama produk, testimoni, superlatif komersial, atau klaim halal. Yang diperiksa: kelima draf disisir untuk nama merek dan klaim sertifikasi — tidak ditemukan. |

---

## Butir terbuka untuk guru (bukan temuan, tetapi memblokir publikasi)

Tiga hal ini **tidak bisa diselesaikan Writer** karena penyelesaiannya menuntut fakta yang tidak ada
di sumber. Ketiganya harus diputuskan manusia di approval gate:

1. **Kedudukan kurikulum.** Topik perubahan wujud zat berada di Fase B `[src:B4]`, sementara paket ini
   diminta untuk Fase C. Guru perlu menyatakan apakah paket ini dipakai sebagai pemantapan lintas
   fase, ataukah topiknya diturunkan ke Fase B.
2. **Mitigasi (R005).** Sumber tidak memuat upaya penanggulangan. Menambahkannya berarti mengarang.
   Guru perlu memutuskan: terima kekosongan ini, atau sediakan sumber mitigasi (mis. penghematan
   energi) agar Writer dapat menambahkannya secara bertag.
3. **Pemetaan arah proses `[src:W10]`.** Seluruh paket sengaja tidak memuat diagram arah. Bila guru
   memvalidasi pemetaan turunan itu, ia dapat ditambahkan sebagai bagian berlabel — dan kuis dapat
   memperoleh butir arah proses.

## Berkas yang diperiksa

`00_plan.md` · `01_lesson_plan.md` · `02_artikel.md` · `03_slide_outline.md` ·
`04_infographic_brief.md` · `05_kuis.md` · `00_run_config.md` · `grounding_report.md`

## Tindak lanjut

Dikembalikan ke Writer dengan 6 temuan (3 Major R001, 3 Minor). Iterasi berikutnya: **1** dari
maksimum 3.
