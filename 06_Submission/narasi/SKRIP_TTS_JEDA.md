# Skrip TTS — jeda presisi

> **USANG — jangan dipakai.** Berkas ini menggambarkan pembagian 8 blok yang ternyata tidak ada di
> video. Batas di detik 87 tidak pernah terjadi. Yang berlaku sekarang: `SKRIP_TTS_LAYAR.md`
> (7 blok, disusun dari bingkai video). Berkas ini disimpan hanya sebagai jejak.


Versi `SKRIP_TTS.md` dengan jeda ditulis sebagai perintah mesin: `((⏱️=500))` berarti diam 500 ms.
Isi kalimat tidak berubah. Yang berubah hanya di mana jeda diletakkan dan berapa panjangnya.

---

## Satu hal yang harus saya sampaikan dulu

Versi pertama file ini salah hitung. Saya menyusun angkanya dari perkiraan lama (3,5 kata/detik
dikurangi jeda `//`), lalu menulis angka jeda di atasnya — padahal di versi baru jedanya sudah
eksplisit. Hasilnya hitung ganda: target durasi tiap blok justru **melewati** slot videonya 4–5 detik.
Kalau Anda sempat merekam dari versi itu, hasilnya akan meleset panjang. Maaf.

Versi sekarang dihitung dari nol: **tempo 3,25 kata/detik**, sisa slot dibagi ke titik-titik jeda yang
tersedia. Total 133 titik jeda. Rata-ratanya berbeda per blok dengan sengaja — blok `04` dan `06`
kalimatnya pendek-pendek sehingga butuh jeda panjang, blok `05` 216 kata sehingga harus mengalir.

> **Tabel di bawah sudah kedaluwarsa.** Angkanya dihitung dengan tempo 3,25 kata/detik
> sebelum ada satu pun berkas audio. Setelah enam blok direkam, mesin ternyata berjalan
> 2,56–3,03 kata/detik, `((⏱️=…))` membengkak 1,11–1,37×, dan mesin menambah senyap
> sendiri sekitar 3,3 detik per blok. **Semua blok melewati slotnya 1,2 sampai 33,9 detik.**
> Angka terukur ada di `DIAGNOSIS_DURASI.md`. Tabel ini dibiarkan hanya sebagai catatan
> cara berpikirnya, bukan sebagai rujukan.

| Blok | Kata | Slot | Jeda total | Rata-rata per titik | Hasil | Sisa |
|---|---|---|---|---|---|---|
| `01` | 11 | 5 s | 815 ms | 272 ms | 4,2 s | 0,8 s |
| `02` | 160 | 82 s | 32.650 ms | 1.166 ms | 81,9 s | 0,1 s |
| `03` | 187 | 92 s | 33.400 ms | 1.113 ms | 90,9 s | 1,1 s |
| `04` | 77 | 51 s | 25.458 ms | 1.591 ms | 49,2 s | 1,8 s |
| `05` | 216 | 106 s | 38.800 ms | 970 ms | 105,3 s | 0,7 s |
| `06` | 54 | 36 s | 18.285 ms | 1.828 ms | 34,9 s | 1,1 s |
| `07` | 16 | 11 s | 5.277 ms | 1.759 ms | 10,2 s | 0,8 s |
| `08` | 12 | 5 s | 508 ms | 169 ms | 4,2 s | 1,0 s |

Total 381 detik bicara dari 403 detik video. Sisa 22 detik: 0,8 detik di ujung tiap blok (napas
sebelum kartu) ditambah 15 detik lima kartu jeda yang memang tidak dinarasikan.

**Blok `02` dulu disebut paling ketat** dengan sisa 0,1 detik. Itu tidak benar dan
sudah tidak berlaku: pada berkas nyata `02.mp3` justru melewati slotnya **13,2 detik**.
Yang paling melewati adalah `05` (+33,9 detik). Lihat `DIAGNOSIS_DURASI.md`.

**Kalau mesin Anda lebih cepat dari 3,25 kata/detik**, hasilnya akan lebih pendek dari slot. Jangan
tambahkan jumlah kata; minta mesin memperlambat, atau jalankan `setel_jeda.py --tempo <hasil ukur>`
dan angkanya disetel ulang otomatis.

---

## Aturan pakai

- Satu kotak = satu blok = satu berkas audio. Tempel satu kotak sekali jalan.
- Jangan mengubah angka. Angka itu hasil bagi, bukan selera.
- Jeda hanya di antara kalimat, tidak pernah di tengah kalimat.
- **Blok `01` dan `08` punya jeda pendek.** Itu bukan kelalaian. Slotnya 5 detik, kalimatnya 11–12
  kata, jadi tidak ada ruang untuk jeda panjang. Keduanya kalimat kartu — baca datar, jangan
  dipuitiskan.

---

## `01` — 0:00 · slot 5 s

```
EduCraft. ((⏱️=270)) Paket ajar IPAS, yang diperiksa aturan ((⏱️=270)) sebelum sampai ke kelas.
((⏱️=275))
```

---

## `02` — 0:05 · slot 82 s

```
Yang saya ketik cuma satu baris. ((⏱️=1100)) Bantu saya membuat materi IPAS.

((⏱️=1400)) Dan agennya tidak langsung menulis.

((⏱️=1200)) Ia balik bertanya: kelas berapa. ((⏱️=1000)) Lalu topiknya apa. ((⏱️=1100)) Saya pilih
kelas lima, fase C. ((⏱️=1000)) Topiknya energi dan gaya.

((⏱️=1300)) Dua pertanyaan. ((⏱️=1000)) Itu bukan kesopanan chatbot. ((⏱️=900)) Itu karena materi IPAS
tanpa jenjang dan capaian pembelajaran ((⏱️=1000)) tidak punya acuan apa pun. ((⏱️=900)) Agen menolak
menebak ((⏱️=900)) dan meminta dua parameter itu lebih dulu.

((⏱️=1200)) Sekarang saya beri jawaban yang sengaja tidak konsisten. ((⏱️=1100)) Kelas lima, tapi
topiknya gaya. ((⏱️=1000)) Sementara, di jawaban pertama, saya menyebut energi. ((⏱️=1000)) Ini
kesalahan yang wajar dilakukan guru sungguhan. ((⏱️=900)) Dua-duanya soal gerak, bedanya tipis.

((⏱️=1400)) Agen menemukannya sendiri.

((⏱️=1300)) Dua jawaban Anda sedikit bertentangan, dan ini menentukan arah seluruh paket.
((⏱️=1300)) Lalu ia jelaskan kenapa: ((⏱️=1250)) topik gaya belum punya lembar fakta. ((⏱️=1300))
Topik energi sudah siap, tapi isinya bentuk dan perubahan energi, tidak memuat jenis gaya.
((⏱️=1250)) Gesek, magnet, gravitasi, pegas. ((⏱️=1300)) Tidak ada satu pun.

((⏱️=1500)) Di sini satu-satunya yang ia minta adalah konfirmasi. ((⏱️=1300)) Bukan empat
pertanyaan, bukan formulir panjang. ((⏱️=1350)) Tapi hanya satu pertanyaan. ((⏱️=1400))
```

---

## `03` — 1:30 · slot 92 s

```
((⏱️=1200)) Dan di sinilah layar menunjukkan sesuatu yang tidak saya rencanakan.

((⏱️=1300)) Di bawah dua pertanyaan yang masih saya biarkan menggantung, ((⏱️=1050)) agen menulis:
((⏱️=950)) Baik, keputusan tercatat.

((⏱️=1600)) Ia mengonfirmasi dirinya sendiri.

((⏱️=1300)) Saya sengaja tidak menghentikannya. ((⏱️=1050)) Karena justru di titik itu kelihatan
kenapa gerbang ini dibutuhkan. ((⏱️=1000)) Model bisa menulis keputusan tercatat kapan saja.
((⏱️=1050)) Yang membuat kalimat itu berarti bukan kalimatnya, ((⏱️=1000)) tapi apakah ada manusia
yang benar-benar menekan tombol.

((⏱️=1250)) Jadi catatan itu tidak dipercaya begitu saja. ((⏱️=1000)) Ada lapisan lain yang
memeriksanya. ((⏱️=1050)) Itu sebabnya di kartu pembuka tadi tertulis empat agen, ((⏱️=900)) dan satu
gerbang manusia.

((⏱️=1350)) Setelah itu agennya jalan.

((⏱️=1250)) Ia menyusun lembar fakta. ((⏱️=1000)) Lima belas fakta, ber-tag, dari rujukan
ensiklopedis. ((⏱️=1050)) Tag itu bukan hiasan. ((⏱️=1000)) Aturan pertama di rulebook mensyaratkan
setiap fakta merujuk tag yang bisa diselesaikan ke sumbernya. ((⏱️=1050)) Kalau fakta tidak ada di
sumber, harus ditulis belum terverifikasi dan perlu konfirmasi guru. ((⏱️=1000)) Bukan dikarang.

((⏱️=1350)) Kenapa seketat itu.

((⏱️=1250)) Karena di hari ketiga, pipeline ini pernah menolak hasil kerjanya sendiri. ((⏱️=1100))
Laporan pemeriksaan dua puluh sembilan Oktober menyimpulkan: ((⏱️=950)) tolak, kritis, jangan terbit.
((⏱️=1050)) Temuannya bukan fakta yang salah. ((⏱️=1000)) Temuannya adalah tag yang menunjuk ke
capaian pembelajaran, ((⏱️=1000)) bukan ke bahan sumber. ((⏱️=1100)) Tag yang rapi, yang tidak
membuktikan apa-apa. ((⏱️=1200))
```

<sub>Jeda 1600 ms sesudah "Baik, keputusan tercatat." adalah yang terpanjang di seluruh video.
Itu momen di mana penonton sempat melihat layar dan menyadari apa yang barusan terjadi: yang menulis
"keputusan tercatat" adalah agen itu sendiri. Kalau mesin Anda punya batas panjang jeda, jangan
turunkan yang ini lebih dulu — turunkan yang lain.</sub>

---

## `04` — 3:05 · slot 51 s

```
((⏱️=1500)) Persetujuan tercatat. ((⏱️=1500)) Agen mulai membangun.

((⏱️=1700)) Satu dokumen, lalu diperiksa. ((⏱️=1500)) Ditemukan cacat: penomoran daftar berlanjut
lintas bagian. ((⏱️=1450)) Lima sampai sembilan, ((⏱️=1450)) lalu sepuluh sampai dua belas,
((⏱️=1450)) lalu tiga belas sampai lima belas.

((⏱️=1800)) Cacat kecil. ((⏱️=1600)) Jenis cacat yang biasanya lolos karena tidak ada yang menghitung.

((⏱️=1900)) Yang penting bukan bahwa ia menemukannya. ((⏱️=1600)) Yang penting adalah ia berhenti
dulu. ((⏱️=1500)) Saya periksa halaman lain sebelum memperbaiki. ((⏱️=1600)) Bukan langsung tambal
satu tempat.

((⏱️=1700)) Lalu diperbaiki, dibangun ulang, dan diverifikasi secara visual. ((⏱️=1600)) Bukan
sekadar sudah selesai. ((⏱️=1608))
```

<sub>Jeda di blok ini lebih panjang dari blok lain karena kalimatnya pendek-pendek. Kalimat pendek
yang diucapkan beruntun tanpa jeda terdengar seperti daftar belanja, padahal isinya pembuktian.</sub>

---

## `05` — 3:59 · slot 106 s

```
((⏱️=930)) Setelah dokumen, slide. ((⏱️=880)) Setelah slide, kuis. ((⏱️=930)) Satu sumber masuk,
((⏱️=880)) formatnya keluar satu per satu.

((⏱️=1130)) Perhatikan pola yang berulang di bagian ini. ((⏱️=930)) Bangun, periksa, temukan,
perbaiki, bangun lagi. ((⏱️=930)) Bukan sekali. ((⏱️=930)) Berkali-kali, sampai tidak ada yang
tersisa untuk ditemukan.

((⏱️=1130)) Slide konten terlalu kosong di bagian bawah. ((⏱️=930)) Saya seimbangkan tata letaknya.
((⏱️=930)) Lalu lingkaran digeser dan slide dibangun ulang.

((⏱️=1130)) Di pojok, penghitungnya berhenti di delapan menit dua puluh dua detik. ((⏱️=1030)) Itu
satu sesi penuh, tanpa saya sentuh.

((⏱️=1180)) Dan yang perlu ditegaskan: ((⏱️=880)) yang diperiksa bukan cuma tata letak.

((⏱️=1130)) Di salah satu iterasi, pemeriksa menolak dengan empat temuan penghalang. ((⏱️=980)) Satu
di antaranya: ((⏱️=880)) klaim metode belajar kami terbukti paling ampuh di Indonesia. ((⏱️=930))
Klaim pemasaran. ((⏱️=880)) Tidak bisa dibuktikan. ((⏱️=930)) Ditolak.

((⏱️=1130)) Satu lagi: ((⏱️=880)) seratus persen halal, ((⏱️=880)) tanpa nomor sertifikat, tanpa
lembaga penerbit. ((⏱️=980)) Aturan kedua belas menyebut itu dengan jelas: ((⏱️=880)) klaim halal
tanpa nomor sertifikat dan lembaga penerbit, tolak.

((⏱️=1130)) Dan aturan keenam, soal klaim kesehatan: ((⏱️=930)) dilarang menjanjikan efek permanen,
((⏱️=880)) kesembuhan, ((⏱️=880)) atau khasiat mutlak yang tidak didukung sumber.

((⏱️=1180)) Ini yang paling sulit dijelaskan ke orang yang belum melihatnya. ((⏱️=980)) Sebuah
sistem yang dirancang untuk menghasilkan materi ajar ((⏱️=880)) punya kecenderungan alami
menghasilkan kalimat yang menjual. ((⏱️=930)) Mantap, ((⏱️=880)) meyakinkan, ((⏱️=880)) enak
dibaca. ((⏱️=930)) Dan justru kalimat seperti itu yang paling sering tidak punya dasar.

((⏱️=1180)) Rulebook-nya ada dua belas aturan. ((⏱️=980)) Itu satu-satunya bagian proyek ini yang
bisa langsung diadopsi sekolah tanpa menyentuh kode apa pun. ((⏱️=930))
```

<sub>Blok terpanjang, tapi jeda per titiknya paling pendek (968 ms). Dengan 216 kata, blok ini
memang harus mengalir — kalau diberi jeda sepanjang blok `04`, totalnya akan lewat 20 detik.</sub>

---

## `06` — 5:48 · slot 36 s

```
((⏱️=1800)) Kuisnya sendiri diuji seperti artefak lain.

((⏱️=1900)) Konten terlalu tinggi. ((⏱️=1800)) Dan dua cacat tata letak: ((⏱️=1800)) penanda huruf
sumbu, ((⏱️=1800)) dan penomoran halaman yang tampak terpotong.

((⏱️=1900)) Lalu satu kalimat yang menurut saya paling menentukan: ((⏱️=1800)) Saya perbaiki agar uji
coba cetak tidak mengulang.

((⏱️=1900)) Bukan diperbaiki supaya kelihatan rapi. ((⏱️=1800)) Diperbaiki supaya kesalahan yang
sama tidak terulang waktu guru mencetaknya. ((⏱️=1785))
```

---

## `07` — 6:27 · slot 11 s

```
Hasilnya jalan di peramban. ((⏱️=1750)) Sepuluh soal pilihan ganda, lima isian. ((⏱️=1750)) Bisa
dicetak, bisa dipakai besok pagi. ((⏱️=1777))
```

---

## `08` — 6:38 · slot 5 s

```
Satu sumber masuk. ((⏱️=170)) Lima format keluar. ((⏱️=170)) Tidak ada yang terbit tanpa manusia.
((⏱️=168))
```

---

## Kalau hasilnya meleset

Angka di atas berlaku untuk mesin dengan tempo 3,25 kata/detik. Mesin lain bisa 3,6 (lebih cepat)
atau 2,9 (lebih lambat). Karena jedanya kini terukur, selisihnya juga terukur — dan bisa diperbaiki
tanpa menyentuh kalimat:

```bash
python3 setel_jeda.py --tempo 3.6        # lihat selisih tiap blok
python3 setel_jeda.py --tempo 3.6 --tulis # tulis ulang angkanya
```

Kalau ada satu blok yang tetap tidak muat pada tempo mesin Anda, itu tanda blok itu kelebihan kata,
bukan kurang jeda. Bilang saja, saya yang usulkan kalimat mana yang dibuang.
