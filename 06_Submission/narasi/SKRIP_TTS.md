# Skrip Siap-TTS

> **USANG — jangan dipakai.** Berkas ini menggambarkan pembagian 8 blok yang ternyata tidak ada di
> video. Batas di detik 87 tidak pernah terjadi. Yang berlaku sekarang: `SKRIP_TTS_LAYAR.md`
> (7 blok, disusun dari bingkai video). Berkas ini disimpan hanya sebagai jejak.


Versi `SKRIP_NARASI.md` yang sudah dibersihkan untuk mesin text-to-speech. **Kalimat isinya tidak
berubah** — yang berubah hanya penanda dan cara pengucapan yang tidak bisa dibaca mesin.

Satu kotak di bawah = satu blok = satu berkas audio. Tempel satu kotak sekali jalan, jangan dicampur.

Yang sudah dibuang dari `SKRIP_NARASI.md`:
121 tanda `//`, penanda tebal, tanda kutip ganda, em dash, dan satu angka (`29 Oktober`) yang sudah
ditulis jadi kata. Keterangan di dalam `<sub>` juga tidak ikut — itu catatan untuk Anda, bukan naskah.

---

## `01` — 0:00 · slot 5 s

```
EduCraft. Paket ajar IPAS, yang diperiksa aturan sebelum sampai ke kelas.
```

---

## `02` — 0:05 · slot 82 s

```
Yang saya ketik cuma satu baris. Bantu saya membuat materi IPAS.

Dan agennya tidak langsung menulis.

Ia balik bertanya: kelas berapa. Lalu topiknya apa. Saya pilih kelas lima, fase C. Topiknya energi
dan gaya.

Dua pertanyaan. Itu bukan kesopanan chatbot. Itu karena materi IPAS tanpa jenjang dan capaian
pembelajaran tidak punya acuan apa pun. Agen menolak menebak dan meminta dua parameter itu lebih
dulu.

Sekarang saya beri jawaban yang sengaja tidak konsisten. Kelas lima, tapi topiknya gaya. Sementara di
jawaban pertama saya menyebut energi. Ini kesalahan yang wajar dilakukan guru sungguhan. Dua-duanya
soal gerak, bedanya tipis.

Agen menemukannya sendiri.

Dua jawaban Anda sedikit bertentangan, dan ini menentukan arah seluruh paket. Lalu ia jelaskan kenapa:
topik gaya belum punya lembar fakta. Topik energi sudah siap, tapi isinya bentuk dan perubahan
energi — tidak memuat jenis gaya. Gesek, magnet, gravitasi, pegas. Tidak ada satu pun.

Di sini satu-satunya yang ia minta adalah konfirmasi. Bukan empat pertanyaan, bukan formulir panjang.
Satu.
```

<sub>Kata "IPAS" di dalam kutipan prompt: kalau mesin membacanya "i-pas", ganti jadi "IPAS" yang
sudah betul saja — jangan diubah jadi "Ilmu Pengetahuan Alam dan Sosial", nanti terdengar seperti
membaca kamus.</sub>

---

## `03` — 1:30 · slot 92 s

```
Dan di sinilah layar menunjukkan sesuatu yang tidak saya rencanakan.

Di bawah dua pertanyaan yang masih saya biarkan menggantung, agen menulis: Baik, keputusan tercatat.

Ia mengonfirmasi dirinya sendiri.

Saya sengaja tidak menghentikannya. Karena justru di titik itu kelihatan kenapa gerbang ini
dibutuhkan. Model bisa menulis keputusan tercatat kapan saja. Yang membuat kalimat itu berarti bukan
kalimatnya, tapi apakah ada manusia yang benar-benar menekan tombol.

Jadi catatan itu tidak dipercaya begitu saja. Ada lapisan lain yang memeriksanya. Itu sebabnya di
kartu pembuka tadi tertulis empat agen, dan satu gerbang manusia.

Setelah itu agennya jalan.

Ia menyusun lembar fakta. Lima belas fakta, ber-tag, dari rujukan ensiklopedis. Tag itu bukan
hiasan. Aturan pertama di rulebook mensyaratkan setiap fakta merujuk tag yang bisa diselesaikan ke
sumbernya. Kalau fakta tidak ada di sumber, harus ditulis belum terverifikasi dan perlu konfirmasi
guru. Bukan dikarang.

Kenapa seketat itu.

Karena di hari ketiga, pipeline ini pernah menolak hasil kerjanya sendiri. Laporan pemeriksaan dua
puluh sembilan Oktober menyimpulkan: tolak, kritis, jangan terbit. Temuannya bukan fakta yang salah.
Temuannya adalah tag yang menunjuk ke capaian pembelajaran, bukan ke bahan sumber. Tag yang rapi, yang
tidak membuktikan apa-apa.
```

<sub>**Ini blok paling rawan di TTS.** Kalimat "Baik, keputusan tercatat." dan "Ia mengonfirmasi
dirinya sendiri." harus punya jeda jelas di antaranya — tanpa itu, dua kalimat itu menyatu dan
leluconnya hilang. Pisahkan di kalimat terpisah (sudah begitu di atas). Kalau mesinnya tetap
menyatukan, potong audio blok ini di titik itu dan sambung dengan 0,8 detik hening.

Tanda kutip di seluruh kotak sudah saya buang supaya mesin tidak bisa salah tafsir. Kalau mesin Anda
masih membaca sesuatu sebagai "tanda kutip", berarti ada yang lolos — laporkan, saya benahi.

"ber-tag" dan "rulebook" dan "pipeline" sengaja dibiarkan sebagai istilah. Kalau mesin membacanya
jadi ejaan huruf, ganti: "ber-tag" → "dengan tag", "pipeline" → "alur kerja ini".</sub>

---

## `04` — 3:05 · slot 51 s

```
Persetujuan tercatat. Agen mulai membangun.

Satu dokumen, lalu diperiksa. Ditemukan cacat: penomoran daftar berlanjut lintas bagian. Lima sampai
sembilan, lalu sepuluh sampai dua belas, lalu tiga belas sampai lima belas.

Cacat kecil. Jenis cacat yang biasanya lolos karena tidak ada yang menghitung.

Yang penting bukan bahwa ia menemukannya. Yang penting adalah ia berhenti dulu. Saya periksa halaman
lain sebelum memperbaiki. Bukan langsung tambal satu tempat.

Lalu diperbaiki, dibangun ulang, dan diverifikasi secara visual. Bukan sekadar sudah selesai.
```

---

## `05` — 3:59 · slot 106 s

```
Setelah dokumen, slide. Setelah slide, kuis. Satu sumber masuk, formatnya keluar satu per satu.

Perhatikan pola yang berulang di bagian ini. Bangun, periksa, temukan, perbaiki, bangun lagi. Bukan
sekali. Berkali-kali, sampai tidak ada yang tersisa untuk ditemukan.

Slide konten terlalu kosong di bagian bawah. Saya seimbangkan tata letaknya. Lalu lingkaran digeser
dan slide dibangun ulang.

Di pojok, penghitungnya berhenti di delapan menit dua puluh dua detik. Itu satu sesi penuh, tanpa
saya sentuh.

Dan yang perlu ditegaskan: yang diperiksa bukan cuma tata letak.

Di salah satu iterasi, pemeriksa menolak dengan empat temuan penghalang. Satu di antaranya: klaim
metode belajar kami terbukti paling ampuh di Indonesia. Klaim pemasaran. Tidak bisa dibuktikan.
Ditolak.

Satu lagi: seratus persen halal, tanpa nomor sertifikat, tanpa lembaga penerbit. Aturan kedua belas
menyebut itu dengan jelas: klaim halal tanpa nomor sertifikat dan lembaga penerbit, tolak.

Dan aturan keenam, soal klaim kesehatan: dilarang menjanjikan efek permanen, kesembuhan, atau khasiat
mutlak yang tidak didukung sumber.

Ini yang paling sulit dijelaskan ke orang yang belum melihatnya. Sebuah sistem yang dirancang untuk
menghasilkan materi ajar punya kecenderungan alami menghasilkan kalimat yang menjual. Mantap,
meyakinkan, enak dibaca. Dan justru kalimat seperti itu yang paling sering tidak punya dasar.

Rulebook-nya ada dua belas aturan. Itu satu-satunya bagian proyek ini yang bisa langsung diadopsi
sekolah tanpa menyentuh kode apa pun.
```

<sub>Kalimat "klaim metode belajar kami terbukti paling ampuh" dan "seratus persen halal" itu kutipan
temuan, bukan klaim. Nada bacanya harus datar dan agak menjauh — kalau ditekankan, penonton mengira
video ini yang mengklaim.</sub>

---

## `06` — 5:48 · slot 36 s

```
Kuisnya sendiri diuji seperti artefak lain.

Konten terlalu tinggi. Dan dua cacat tata letak: penanda huruf sumbu, dan penomoran halaman yang
tampak terpotong.

Lalu satu kalimat yang menurut saya paling menentukan: Saya perbaiki agar uji coba cetak tidak
mengulang.

Bukan diperbaiki supaya kelihatan rapi. Diperbaiki supaya kesalahan yang sama tidak terulang waktu
guru mencetaknya.
```

---

## `07` — 6:27 · slot 11 s

```
Hasilnya jalan di peramban. Sepuluh soal pilihan ganda, lima isian. Bisa dicetak, bisa dipakai besok
pagi.
```

---

## `08` — 6:38 · slot 5 s

```
Satu sumber masuk. Lima format keluar. Tidak ada yang terbit tanpa manusia.
```

---

## Catatan pemakaian

**Satu kotak, satu berkas.** Simpan sebagai `01.mp3` … `08.mp3` (atau `.wav`) di folder ini. Jangan
gabung semua kotak jadi satu tempelan — mesin akan melanjutkan tanpa jeda di antara blok, dan blok
`01`/`08` yang cuma 4 detik akan melewati slotnya.

**Suara yang dipilih menentukan hasilnya lebih besar daripada teksnya.** Untuk video ini, yang cocok
adalah suara Indonesia dengan tempo agak lambat dan tanpa intonasi iklan. Kalau pilihannya ada "news"
vs "conversational", ambil conversational. Ini video bukti, bukan promosi.

**Kalau tidak ada opsi kecepatan,** minta mesin membaca sedikit lebih lambat dari default — sekitar
0,9×. Hitungan saya: 822 kata dalam ~299 detik berarti ~2,7 kata/detik, lebih lambat dari tempo
bicara normal. Tanpa ini, blok `05` akan selesai jauh sebelum 106 detiknya dan ada jeda canggung
di layar yang tidak menunjukkan apa-apa.

**Jangan percaya durasi hasil TTS sebelum diukur.** Mesin sering meleset 10–15% dari perkiraan. Serahkan
berkasnya, saya ukur dengan `ffprobe`, laporkan blok mana yang lewat slot, lalu baru dipasang. Kalau
ada yang lewat, ada dua jalan: perlambat blok itu saja, atau saya geser batas bloknya.

**Transparansi.** Kalau video ini dinilai juri hackathon, suara sintetis sebaiknya disebut. Bukan
karena diwajibkan, tapi karena seluruh isi video ini soal tidak mengklaim lebih dari yang terbukti —
dan itu berlaku untuk cara membuatnya juga. Satu baris di deskripsi video sudah cukup.
