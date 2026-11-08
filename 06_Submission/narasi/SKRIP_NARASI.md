# Skrip Narasi — EduCraft Demo (6:43)

> **USANG — jangan dipakai.** Berkas ini menggambarkan pembagian 8 blok yang ternyata tidak ada di
> video. Batas di detik 87 tidak pernah terjadi. Yang berlaku sekarang: `SKRIP_TTS_LAYAR.md`
> (7 blok, disusun dari bingkai video). Berkas ini disimpan hanya sebagai jejak.


Ditulis untuk video yang **sudah jadi**: `06_Submission/EduCraft_Demo.mp4`, 403 detik, 1366×768.
Tujuh blok rekaman. Satu blok = satu berkas = satu take.

Versi lama (`video_kit/NARASI_SKRIP_TAKE.md`, `07_Demo_Video_Script.md`, `video_kit/subtitle.srt`)
dibuat untuk video 7:55 berbasis slide yang **tidak pernah diproduksi**. Jangan dipakai. Di video
ini tidak ada diagram arsitektur, tidak ada rulebook di layar, tidak ada shot `SKILL.md`, dan tidak
ada hook kelas jam 21:47. Yang ada rekaman layar kerja agen yang sebenarnya.

---

## Peta waktu

| Blok | Mulai | Durasi | Isi layar |
|---|---|---|---|
| `01` pembuka | 0:00 | 5 s | Kartu: "12 aturan · 4 agen · 1 gerbang manusia" |
| `02` seg1 | 0:05 | 82 s | Prompt diketik → agen bertanya balik → dua panel pilihan |
| — kartu 1/5 | 1:27 | 3 s | "Agen menolak menebak" |
| `03` seg2 | 1:30 | 92 s | Dua jawaban bertentangan → minta satu konfirmasi → jawab sendiri |
| — kartu 2/5 | 3:02 | 3 s | "Empat keputusan, bukan satu" |
| `04` seg3 | 3:05 | 51 s | Persetujuan tercatat → cacat penomoran ditemukan → verifikasi visual |
| — kartu 3/5 | 3:56 | 3 s | "Agen memeriksa hasil sendiri" |
| `05` seg4 | 3:59 | 106 s | Rentetan panjang: DOCX, slide, perbaikan, `Used 8m22s` |
| — kartu 4/5 | 5:45 | 3 s | "Permintaan di luar lingkup" |
| `06` seg5 | 5:48 | 36 s | Kuis dibangun, dua cacat tata letak dicatat |
| — kartu 5/5 | 6:24 | 3 s | "Cacat ditemukan lewat pengujian" |
| `07` seg6 | 6:27 | 11 s | Halaman kuis berjalan di peramban |
| `08` tutup | 6:38 | 5 s | Kartu penutup: 4 run, 525 tag, 21 kasus uji, MIT |

**Di kartu jeda tidak ada suara.** Itu disengaja: kartunya untuk dibaca. Kalau dinarasikan, penonton
memilih antara mendengar dan membaca, dan keduanya jadi lebih buruk.

---

## Cara merekam

- **Nama berkas wajib.** Taruh di `06_Submission/narasi/`: `01.m4a`, `02.m4a`, … `08.m4a`. Format lain
  (`.wav`, `.mp3`) juga saya terima — saya cari berdasarkan nomor.
- **Satu take per blok, tanpa menyunting.** Jangan potong jeda di awal atau akhir. Jeda itu saya buang
  otomatis; kalau Anda potong manual, justru hilang acuannya.
- **Rekam satu blok berulang sampai pas**, baru pindah ke blok berikutnya. Berkas terakhir yang dipakai.
- **Mikrofon 15–20 cm**, sedikit menyamping dari mulut. Uji 5 detik dulu, dengarkan pakai headphone —
  kalau terdengar mendecit, jauhkan sedikit.
- **Puncak −6 dB, jangan sampai menyentuh 0.** Windows: Voice Recorder. macOS: QuickTime → New Audio
  Recording. Level di `loudnorm` saya yang menaikkan; Anda cukup memastikan tidak pecah.
- **Jangan perbaiki volume sendiri.** Kalau satu blok terasa lebih pelan dari yang lain, biarkan.
  `loudnorm` menyeimbangkan. Yang tidak bisa diperbaiki adalah klip yang sudah pecah.
- **Baca seperti menjelaskan ke satu orang**, bukan mengumumkan. Video ini deretan bukti, bukan iklan
  pencapaian. Nada datar lebih meyakinkan daripada nada bersemangat.
- Kalau lidah terselip: berhenti, tarik napas, ulangi **satu kalimat itu**, lalu lanjut. Tidak usah
  ulang dari awal blok.

**Anggaran kata** (basis 4,1 kata/detik, sudah dikurangi jeda ekor):

| Blok | Slot | Maks kata | Isi skrip | Terukur | Sisa |
|---|---|---|---|---|---|
| `01` | 4 s | 16 | 12 | 3,9 s | 0,1 s |
| `02` | 81 s | 333 | 182 | 62,8 s | 18,2 s |
| `03` | 91 s | 374 | 216 | 74,8 s | 16,2 s |
| `04` | 50 s | 206 | 90 | 31,1 s | 18,9 s |
| `05` | 105 s | 432 | 261 | 92,6 s | 12,4 s |
| `06` | 35 s | 145 | 63 | 22,1 s | 12,9 s |
| `07` | 10 s | 42 | 20 | 7,5 s | 2,5 s |
| `08` | 4 s | 18 | 14 | 4,0 s | 0,0 s |

Total ~299 detik bicara dari 403 detik video: **104 detik sengaja tanpa suara** — kartu jeda, plus
ruang kosong di ujung tiap blok. Terukur = 3,5 kata/detik ditambah 0,45 s per tanda `//`.

Angka di kolom "Sisa" itu **bukan** ruang untuk menambah kalimat. Itu ruang untuk tempo Anda yang
lebih lambat dari perkiraan saya. Kalau blok `05` anda ternyata 105 detik, jangan panik — masih pas.
Kalau satu blok melewati slotnya, saya bisa geser batasnya sedikit, tapi jangan berharap banyak:
di luar batas itu narasi mulai bicara tentang hal yang sudah tidak ada di layar.

Tanda `//` = titik jeda napas. Jeda sekitar 0,4 detik. Tidak perlu dihitung, cukup berhenti.
Teks **tebal** = kata yang ditekan. Hanya satu per kalimat.

---

## `01` — Pembuka · 0:00 (4 detik bicara, 1 detik diam)

```
EduCraft. Paket ajar IPAS, yang diperiksa aturan // sebelum sampai ke kelas.
```

<sub>11 kata. Kartu di layar menulis "12 aturan · 4 agen · 1 gerbang manusia" — jangan disebut,
biar kartunya yang bicara.</sub>

---

## `02` — seg1 · 0:05–1:27 (81 detik · ~250 kata)

```
Yang saya ketik cuma satu baris. // "Bantu saya membuat materi IPAS."

Dan agennya tidak langsung menulis.

// Ia balik bertanya: kelas berapa. // Lalu topiknya apa.
Saya pilih kelas lima, fase C. // Topiknya energi dan gaya.

// Dua pertanyaan. // Itu bukan kesopanan chatbot.
Itu karena materi IPAS tanpa jenjang dan capaian pembelajaran // tidak punya acuan apa pun.
Agen menolak menebak // dan meminta dua parameter itu lebih dulu.

// Sekarang saya beri jawaban yang sengaja tidak konsisten. // Kelas lima, tapi topiknya gaya.
// Sementara di jawaban pertama saya menyebut energi.
// Ini kesalahan yang wajar dilakukan guru sungguhan. // Dua-duanya soal gerak, bedanya tipis.

// Agen menemukannya sendiri.

// "Dua jawaban Anda sedikit bertentangan, dan ini menentukan arah seluruh paket."
// Lalu ia jelaskan kenapa: // topik gaya belum punya lembar fakta.
// Topik energi sudah siap, tapi isinya bentuk dan perubahan energi — // tidak memuat jenis gaya.
// Gesek, magnet, gravitasi, pegas. // Tidak ada satu pun.

// Di sini satu-satunya yang ia minta adalah konfirmasi.
// Bukan empat pertanyaan, bukan formulir panjang. // Satu.
```

<sub>Saat blok ini, di layar: prompt diketik pada 0:15, panel "Materi IPAS ini untuk kelas berapa?"
pada 0:42, panel "Topik/tema dalam topik IPAS apa?" pada 1:05. Kalimat kutipan diambil verbatim dari
layar. Jangan diubah.</sub>

---

## `03` — seg2 · 1:30–3:02 (91 detik · ~290 kata)

```
// Dan di sinilah layar menunjukkan sesuatu yang tidak saya rencanakan.

// Di bawah dua pertanyaan yang masih saya biarkan menggantung, // agen menulis: "Baik — keputusan
tercatat."

// Ia mengonfirmasi dirinya sendiri.

// Saya sengaja tidak menghentikannya. // Karena justru di titik itu kelihatan kenapa gerbang ini
dibutuhkan. // Model bisa menulis "keputusan tercatat" kapan saja. // Yang membuat kalimat itu berarti
bukan kalimatnya — // tapi apakah ada manusia yang benar-benar menekan tombol.

// Jadi catatan itu tidak dipercaya begitu saja. // Ada lapisan lain yang memeriksanya.
// Itu sebabnya di kartu pembuka tadi tertulis empat agen // dan satu gerbang manusia.

// Setelah itu agennya jalan.

// Ia menyusun lembar fakta. // Lima belas fakta, ber-tag, dari rujukan ensiklopedis.
// Tag itu bukan hiasan. // Aturan pertama di rulebook mensyaratkan setiap fakta merujuk tag yang
// bisa diselesaikan ke sumbernya. // Kalau fakta tidak ada di sumber, harus ditulis belum terverifikasi
// dan perlu konfirmasi guru. // Bukan dikarang.

// Kenapa seketat itu.

// Karena di hari ketiga, pipeline ini pernah menolak hasil kerjanya sendiri.
// Laporan pemeriksaan 29 Oktober menyimpulkan: tolak, kritis, jangan terbit.
// Temuannya bukan fakta yang salah. // Temuannya adalah tag yang menunjuk ke capaian pembelajaran,
// bukan ke bahan sumber. // Tag yang rapi, yang tidak membuktikan apa-apa.
```

<sub>Blok terpenting di seluruh video. Kalimat "Baik — keputusan tercatat" diucapkan pelan, lalu
berhenti satu detik penuh sebelum "Ia mengonfirmasi dirinya sendiri." Berhenti itu yang membuat
penonton sempat melihat layarnya sendiri.</sub>

---

## `04` — seg3 · 3:05–3:56 (50 detik · ~150 kata)

```
// Persetujuan tercatat. Agen mulai membangun.

// Satu dokumen, lalu diperiksa. // "Ditemukan cacat: penomoran daftar berlanjut lintas bagian —
// lima sampai sembilan, lalu sepuluh sampai dua belas, lalu tiga belas sampai lima belas."

// Cacat kecil. // Jenis cacat yang biasanya lolos karena tidak ada yang menghitung.

// Yang penting bukan bahwa ia menemukannya. // Yang penting adalah ia berhenti dulu.
// "Saya periksa halaman lain sebelum memperbaiki." // Bukan langsung tambal satu tempat.

// Lalu diperbaiki, dibangun ulang, dan diverifikasi secara visual. // Bukan sekadar "sudah selesai".
```

<sub>Verifikasi visual itu artinya halaman dokumen di-render jadi gambar lalu diperiksa. Ini yang
membedakan "kode berjalan tanpa error" dari "hasilnya benar di mata".</sub>

---

## `05` — seg4 · 3:59–5:45 (105 detik · ~330 kata)

```
// Setelah dokumen, slide. // Setelah slide, kuis. // Satu sumber masuk, formatnya keluar satu per satu.

// Perhatikan pola yang berulang di bagian ini. // Bangun — periksa — temukan — perbaiki — bangun lagi.
// Bukan sekali. // Berkali-kali, sampai tidak ada yang tersisa untuk ditemukan.

// "Slide konten terlalu kosong di bagian bawah. Saya seimbangkan tata letaknya."
// // Lalu lingkaran digeser dan slide dibangun ulang.

// Di pojok, penghitungnya berhenti di delapan menit dua puluh dua detik. // Itu satu sesi penuh,
// tanpa saya sentuh.

// Dan yang perlu ditegaskan: yang diperiksa bukan cuma tata letak.

// Di salah satu iterasi, pemeriksa menolak dengan empat temuan penghalang. // Satu di antaranya:
// klaim "metode belajar kami terbukti paling ampuh di Indonesia". // Klaim pemasaran. // Tidak bisa
// dibuktikan. // Ditolak.

// Satu lagi: "seratus persen halal", // tanpa nomor sertifikat, tanpa lembaga penerbit.
// Aturan kedua belas menyebut itu dengan jelas: // klaim halal tanpa nomor sertifikat dan lembaga
// penerbit — tolak.

// Dan aturan keenam, soal klaim kesehatan: // dilarang menjanjikan efek permanen, kesembuhan, atau
// khasiat mutlak yang tidak didukung sumber.

// // Ini yang paling sulit dijelaskan ke orang yang belum melihatnya. // Sebuah sistem yang dirancang
// untuk menghasilkan materi ajar // punya kecenderungan alami menghasilkan kalimat yang menjual.
// Mantap, meyakinkan, enak dibaca. // Dan justru kalimat seperti itu yang paling sering tidak punya
// dasar.

// Rulebook-nya ada dua belas aturan. // Itu satu-satunya bagian proyek ini yang bisa langsung diadopsi
// sekolah tanpa menyentuh kode apa pun.
```

<sub>Bagian ini bicara tentang penolakan yang **tidak tampil di layar** video. Jangan pernah
mengatakan "seperti yang Anda lihat". Kalimat pembuka sudah mengalihkan perhatian ke pola, bukan
ke gambar. Itu satu-satunya cara jujur menyampaikan bagian ini.</sub>

---

## `06` — seg5 · 5:48–6:24 (35 detik · ~105 kata)

```
// Kuisnya sendiri diuji seperti artefak lain.

// "Konten terlalu tinggi. Dan dua cacat tata letak: penanda huruf sumbu, dan penomoran halaman yang
// tampak terpotong."

// Lalu satu kalimat yang menurut saya paling menentukan: // "Saya perbaiki agar uji coba cetak tidak
// mengulang."

// Bukan diperbaiki supaya kelihatan rapi. // Diperbaiki supaya kesalahan yang sama tidak terulang
// waktu guru mencetaknya.
```

<sub>Bacaan terakhir agak lebih pelan. Ini penutup argumen, bukan daftar temuan.</sub>

---

## `07` — seg6 · 6:27–6:38 (10 detik · ~18 kata)

```
// Hasilnya jalan di peramban. // Sepuluh soal pilihan ganda, lima isian. // Bisa dicetak, bisa dipakai
// besok pagi.
```

<sub>18 kata untuk 10 detik berarti tempo normal, tanpa jeda panjang. Jangan menambahkan kalimat.</sub>

---

## `08` — Tutup · 6:38 (4 detik bicara)

```
Satu sumber masuk. // Lima format keluar. // Tidak ada yang terbit tanpa manusia.
```

<sub>14 kata, ~4 detik terukur. Kalimat ini ada di kartu penutup — ucapkan sama persis seperti
tulisan di kartu, lalu diam sampai video habis. Jangan menambahkan "terima kasih".</sub>

---

## Yang **tidak** boleh diucapkan

Semua ini sudah saya periksa terhadap rekaman dan terhadap berkas bukti. Menyebutnya akan membuat
narasi bertentangan dengan gambar.

| Jangan bilang | Kenapa |
|---|---|
| "lima agen" | Kartu pembuka menulis **4 agen**. `README.md` menyebut empat kontrak agen. |
| "seperti yang bisa Anda lihat" saat membahas "makanan halal" | Adegan penolakan itu **tidak ada di video**. Yang ada hanya kartu 4/5 di 5:45. Buktinya ada di `agent_nolak.png`, di luar rekaman. |
| "diagram arsitektur" / "rulebook di layar" | Tidak ada shot itu di video ini. |
| Hook ruang kelas jam 21:47, empat puluh satu murid | Tidak ada di rekaman. Prompt aslinya tiga kata: "bantu saya membuat materi IPAS". |
| "tag 525, nol dangling" diucapkan sebagai klaim Anda | Angka itu benar dan ada di kartu penutup (6:38). Sebut hanya kalau memang mau; jangan dikarang angkanya. |
| "otomatis sepenuhnya" | Gerbang persetujuan manusianya nyata dan dijalankan. Mengklaim otomatis penuh justru menghapus nilai jualnya. |

---

## Sebelum merekam

Baca `02`, `03`, `05` masing-masing dua kali tanpa mikrofon. Kalau ada kalimat yang membuat Anda
tersandung, **ganti kalimatnya** — skrip ini alat, bukan naskah suci. Yang tidak boleh diubah hanya
kutipan bertanda petik, karena itu teks yang benar-benar ada di layar.

Setelah semua berkas ada di `06_Submission/narasi/`, saya jalankan:

```bash
python3 06_Submission/narasi/pasang_narasi.py --cek     # pratinjau: durasi vs waktu di layar
python3 06_Submission/narasi/pasang_narasi.py           # hasil akhir + subtitle
```

Skrip itu belum saya tulis — saya tunggu audionya, supaya pengaturannya mengikuti panjang rekaman
yang sebenarnya, bukan perkiraan.
