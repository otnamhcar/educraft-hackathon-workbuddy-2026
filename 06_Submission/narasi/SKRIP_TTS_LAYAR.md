# Skrip TTS — mengikuti layar

Versi 3. Disusun ulang **setelah** rekaman suara v2 diukur dan setiap kalimatnya dicocokkan ke
timestamp nyata, lalu dibandingkan dengan isi layar pada detik yang sama.

## Mengapa v2 masih meleset

Rekaman v2 isinya sudah benar, tetapi **terlalu cepat selesai**. Tempo terukur 2,87 kata/detik
(skrip merencanakan 2,8), sehingga blok `02` habis di detik 2:05 sementara slotnya sampai 3:02 —
54 detik layar diam tanpa suara.

Lebih penting: dua kalimat menunjuk momen yang belum terjadi. *"Materi IPAS untuk kelas dan fase
berapa"* diucapkan di detik 24, padahal pertanyaan itu baru muncul di layar detik **70**. Kalimat
soal B5/B6 diucapkan di 1:22, layarnya baru menampilkannya di **1:35**.

## Yang berubah di v3

Blok panjang dipecah di titik pergantian layar yang nyata — bukan dibagi rata. Tujuh blok menjadi
dua belas.

| v2 | v3 | Batas baru | Alasan |
|---|---|---|---|
| `02` (174 s) | `02` + `03` + `04` + `05` | 70,0 · 100,0 · 120,0 | di situlah panel pertanyaan, dua butir bertentangan, dan baris "preparing to create task" muncul |
| `03` (51 s) | `06` | — | isinya ditambah: "penulis dilarang mengarang fakta" |
| `04` (106 s) | `07` + `08` | 296,0 | setelah baris "Ditemukan cacat" |
| `05`–`07` | `09`–`12` | — | nomor bergeser |

Batas 84,0 dan 95,4 sempat saya coba dan saya batalkan: keduanya memotong alur konfirmasi di
tengah kalimat, menyisakan blok 11–14 detik yang mustahil diisi tanpa mempercepat bacaan.
Batas 100,0 dan 120,0 jatuh di antara paragraf, bukan di dalamnya.

## Peta layar — dasar pemotongan

Perubahan layar di segmen percakapan (`select='gt(scene,0.002)'`, hanya yang berjarak >0,4 s):

| Detik | Yang muncul |
|---|---|
| 5,0 | landing page "WorkBuddy, Ideas into reality" dengan kolom kosong |
| 6,7 | kolom terisi "bantu saya membuat materi IPAS" |
| 14,6 | pesan terkirim, riwayat kosong |
| 58,7 | "WorkBuddy AI · Processed 43s" — menunggu model |
| 70,0 | **"Materi IPAS ini untuk kelas/fase berapa?"** opsi 1–3 |
| 78,0 | **"Bentuk keluaran apa yang Anda butuhkan?"** opsi 1–4 |
| 86,3 | "Sebelum menyusun, saya perlu memastikan beberapa parameter" |
| 95,4 | **"Dua jawaban Anda sedikit bertentangan"** + butir B5/B6 |
| 178,7 | potong ke kartu LANGKAH 1/5 |
| 236,1 | log build sudah tampil **penuh** — tidak ada gerakan sampai 342 |
| 342,2 | kartu LANGKAH 3/5 |

**Segmen `236–342` tidak bergerak sama sekali.** Semua baris log — "Persetujuan tercatat",
"Ditemukan cacat: penomoran daftar berlanjut lintas bagian", "DOCX lolos verifikasi visual",
"Slide konten terlalu kosong" — sudah terbaca sejak detik 236. Karena itu blok `07` dan `08`
menarasikan **urutannya dari atas ke bawah**, bukan menunggu tiap baris muncul.

## Isi layar yang dipakai

1. **detik 70** — "Materi IPAS ini untuk kelas/fase berapa?" — Kelas 1–2 (Fase A),
   Kelas 3–4 (Fase B), Kelas 5–6 (Fase C). Penanda `1/3`.
2. **detik 78** — "Bentuk keluaran apa yang Anda butuhkan?" — Modul Ajar / RPP lengkap,
   Bahan ajar / bacaan siswa, LKPD + Kuis/Asesmen, Paket lengkap (semua di atas). Penanda `3/3`.
3. **detik 86** — "IPAS sangat bergantung pada fase/kelas dan capaian pembelajaran yang dituju."
4. **detik 95** — "…penulis dilarang mengarang fakta — setiap pernyataan sains harus dapat
   ditelusuri ke sumber. Jadi saya butuh keputusan Anda soal pasokan fakta sebelum melanjutkan."
   Lalu dua butir: **B6 (Gaya) belum punya lembar fakta → tidak bisa langsung diproduksi tanpa
   sumber**, **B5 (Energi) sudah siap, tetapi isinya bentuk & perubahan energi — tidak memuat
   jenis gaya (gesek, magnet, gravitasi, pegas)**.
5. **detik 96** — "Baik — keputusan tercatat: B6 Gaya & Gerak, dengan lembar fakta disusun lebih
   dulu. Saya mulai dari riset dan penyusunan lembar fakta ber-tag."

**Pertentangannya B5 lawan B6, bukan "kelas berapa".**

## Empat hal yang sengaja tidak dijelaskan

1. **Kartu LANGKAH 4/5 "Permintaan di luar lingkup"** tampil 381,0–383,9 s, lalu digantikan preview
   kuis pada 384,0 s. Sebelumnya kartu ini **tidak dinarasikan sama sekali** — dan itu salah.
   Ia satu-satunya kartu yang lewat tanpa suara, padahal kartu 3/5 di detik 343 dibacakan. Sudah
   diperbaiki lewat blok `09b`. Kalimatnya sengaja **tidak** menyebut "makanan halal" secara
   harfiah: kartunya sendiri yang menanggung rincian itu, dan menyebutkan dua kali dalam 3 detik
   hanya akan membuatnya tumpang tindih dengan teks di layar.
2. **Header kuis menulis "KELAS IV · FASE B"** padahal pengguna memilih Kelas 5–6 Fase C, dan nama
   berkasnya `Kuis_IPAS_Kelas_IV_...`. Saya tidak menyebut kelas supaya tidak mengklaim yang tidak
   konsisten di layar.
3. **"5 uraian"** — hanya soal uraian 4 dan 5 yang terlihat, sisanya di luar gulir. Saya menyebut
   jumlahnya tanpa mengklaim yang tidak terlihat.
4. **"Lima format keluar"** di kartu penutup tidak saya sebutkan satu per satu, karena kartunya
   cuma 5 detik dan penonton membacanya sendiri.

## Aturan pakai

- Satu kotak = satu berkas audio. Tempel satu kotak sekali jalan.
- **Teks rekaman tiap blok ada di `audio_layar/NN.txt`** — itu yang dibaca, bukan berkas ini.
  Berkas ini hanya mencatat alasan, isi layar, dan anggaran waktu.
- Jeda hanya di antara kalimat.
- Blok `01` dan `12` pendek: slot 5 detik. Blok `11` cuma 3 detik — satu kalimat, jangan ditambah.
  Blok `09b` juga 3 detik: **7 kata, jangan ditambah satu kata pun.**
- Tempo acuan **2,70 kata/detik** — diukur dari blok `09` Anda sendiri (53 kata, 19,63 s ucapan
  murni), bukan asumsi. Angka 2,85 di versi lama terlalu optimistis dan membuat tiga blok
  kelebihan kata.
- Angka `((⏱️=…))` sudah dihitung per blok. Kalau rekaman Anda lebih lambat dari 2,70, jalankan
  `ukur_tempo.py` sebelum apa pun.

---

## `01` — 0:00 · slot 5,0 s · kartu judul

Layar: "EduCraft", "Paket ajar IPAS yang diperiksa aturan sebelum sampai ke kelas.",
chip "12 aturan · 4 agen · 1 gerbang manusia".

```
EduCraft. ((⏱️=450)) Paket ajar IPAS yang diperiksa aturan ((⏱️=450)) sebelum sampai ke kelas.
```

---

## `02` — 0:05 · slot 65,0 s · layar kosong, menunggu model

Layar: landing page (5) → mengetik "bantu saya membuat materi IPAS" (7) → terkirim (15) →
"Processed 43s", "Waiting for model" (59) → panel pertanyaan muncul (70).

```
Layar dibuka ke halaman kosong. ((⏱️=1550)) Satu kolom, satu kursor, beberapa contoh pertanyaan
di bawahnya. ((⏱️=1550))

Saya ketik satu baris. ((⏱️=1550)) Bantu saya membuat materi IPAS. ((⏱️=1550)) Lalu Enter.
((⏱️=1550))

Bukan perintah panjang. ((⏱️=1550)) Bukan template. ((⏱️=1550)) Satu kalimat, seperti yang
diucapkan guru di ruang guru menjelang malam. ((⏱️=1550))

Pesan itu naik ke atas. ((⏱️=1550)) Riwayat masih kosong. ((⏱️=1550)) Yang muncul cuma nama agen,
((⏱️=1550)) dan angka yang terus bertambah: processed empat puluh tiga detik.
((⏱️=1550))

Di bawahnya, satu baris kecil. ((⏱️=1550)) Waiting for model. ((⏱️=1550)) Menunggu model.
((⏱️=1550))

Itu jujur. ((⏱️=1550)) Pekerjaan yang sebenarnya terjadi tidak menarik dilihat. ((⏱️=1550)) Yang
bisa ditampilkan hanya bahwa sesuatu sedang berjalan. ((⏱️=1550))

Lalu di detik ketujuh puluh, panelnya terbuka. ((⏱️=1550))
```

> **Hening yang disengaja di blok ini.** Rekaman `02.mp3` berhenti di kalimat "Lalu di detik
> ketujuh puluh…", sehingga detik 62–70 (7,6 s) berisi hening sementara layar menampilkan
> paragraf *"Sebelum menyusun, saya perlu memastikan beberapa parameter… IPAS sangat bergantung
> pada fase/kelas…"* beserta status *Waiting for your answer*. Ini keputusan yang diambil
> sadar — bukan cacat render. Kalau ingin diisi, tambahkan kalimat tentang paragraf itu,
> rekam ulang `02`, lalu jalankan `regang_jeda.py --maks 2.6 --tulis`.

---

## `03` — 1:10 · slot 30,0 s · dua panel pertanyaan

Layar: panel "Materi IPAS ini untuk kelas/fase berapa?" — Kelas 1–2 (Fase A), Kelas 3–4 (Fase B),
Kelas 5–6 (Fase C), penanda `1/3` (70) → panel "Bentuk keluaran apa yang Anda butuhkan?" —
Modul Ajar / RPP lengkap, Bahan ajar / bacaan siswa, LKPD + Kuis/Asesmen, Paket lengkap,
penanda `3/3` (78).

```

Dan yang muncul berikutnya bukan paragraf. ((⏱️=550))

Yang muncul pertanyaan. ((⏱️=550))

Materi IPAS ini untuk kelas atau fase berapa. ((⏱️=550)) Tiga pilihan: ((⏱️=550)) kelas satu
sampai dua Fase A, ((⏱️=550)) kelas tiga empat Fase B, ((⏱️=550)) kelas lima enam Fase C.
((⏱️=550))

Lalu pertanyaan kedua. ((⏱️=550)) Bentuk keluaran apa yang dibutuhkan. ((⏱️=550)) Empat pilihan:
((⏱️=550)) modul ajar, ((⏱️=550)) bahan bacaan, ((⏱️=550)) LKPD dan kuis, ((⏱️=550)) atau paket
lengkap. ((⏱️=550))

Dua pertanyaan. ((⏱️=550)) Tidak lebih. ((⏱️=550))

```

---

## `04` — 1:40 · slot 20,0 s · dua butir bertentangan

Layar: "Sebelum menyusun, saya perlu memastikan beberapa parameter… IPAS sangat bergantung pada
fase/kelas dan capaian pembelajaran yang dituju" (86) → **"Dua jawaban Anda sedikit
bertentangan"** dengan dua butir B6 dan B5 (95) → "Baik — keputusan tercatat: B6 Gaya & Gerak"
(96).

```

Perhatikan apa yang tidak terjadi. ((⏱️=300)) Agen tidak langsung menulis. ((⏱️=300))

Lalu layar menampilkan dua butir yang bertentangan. ((⏱️=300))

Soal gaya, belum ada lembar faktanya. ((⏱️=300)) Tidak bisa diproduksi tanpa sumber.
((⏱️=300))

Sementara soal energi sudah siap, ((⏱️=300)) tetapi isinya bentuk dan perubahan energi.
((⏱️=300)) Tidak gesek. ((⏱️=300)) Tidak magnet. ((⏱️=300)) Tidak gravitasi.
((⏱️=300)) Tidak pegas. ((⏱️=300))

```

---

## `05` — 2:00 · slot 62,1 s · keputusan tercatat, lalu menunggu

Layar: "Baik — keputusan tercatat: B6 Gaya & Gerak…" (96) → "Preparing to create task" (97) →
**layar diam 98–179**, hanya "Processed" yang bertambah dan baris *Thinking*.

```

Agen menemukannya sendiri. ((⏱️=1750)) Ia tidak memilih sendiri, ((⏱️=1750)) tidak mengarang
penengah. ((⏱️=1750)) Ia mengembalikan pertanyaan kepada orang yang berhak memutuskan.
((⏱️=1750))

Keputusan tercatat. ((⏱️=1750)) Gaya dan gerak, dengan lembar fakta disusun lebih dulu.
((⏱️=1750))

Lalu ia pergi membaca. ((⏱️=1750)) Di layar tidak ada yang berubah. ((⏱️=1750)) Tidak ada progres
bar. ((⏱️=1750)) Tidak ada daftar situs yang dikunjungi. ((⏱️=1750))

Hanya satu baris: preparing to create task. ((⏱️=1750)) Menyiapkan tugas. ((⏱️=1750))

Bagian ini berlangsung lebih dari satu menit. ((⏱️=1750)) Dan saya sengaja tidak memotongnya.
((⏱️=1750))

Karena di situlah pertanyaan yang paling sering diajukan orang tua dan kepala sekolah:
((⏱️=1750)) dari mana materinya. ((⏱️=1750)) Bukan berapa lama membuatnya. ((⏱️=1750))

```

---

## `06` — 3:02 · slot 54,0 s · aturan sumber, lembar fakta, +295

Layar: lanjutan percakapan yang sama, "Riset selesai — 15 fakta ber-tag", lalu penghitung
"Creating +295" yang naik.

```

Layar tidak bergerak. ((⏱️=650)) Yang berjalan sekarang bukan menulis, ((⏱️=650)) melainkan
menyusun bahan. ((⏱️=650))

Di titik ini agen menulis satu aturan untuk dirinya sendiri. ((⏱️=650)) Penulis dilarang
mengarang fakta. ((⏱️=650)) Setiap pernyataan sains harus dapat ditelusuri ke sumber.
((⏱️=650))

Bukan dari ingatan. ((⏱️=650)) Bukan dari pengetahuan umum. ((⏱️=650)) Bukan karena
kedengarannya benar. ((⏱️=650))

Lembar fakta itu menjadi satu-satunya sumur fakta untuk seluruh paket. ((⏱️=650)) Aturan itu
ditegakkan oleh pemeriksa, ((⏱️=650)) bukan oleh tembok. ((⏱️=650)) Artinya ia diperiksa,
((⏱️=650)) bukan dianggap. ((⏱️=650))

Angka di layar mulai naik. ((⏱️=650)) Creating. ((⏱️=650)) Dua ratus sembilan puluh lima.
((⏱️=650)) Itu bukan jumlah kata. ((⏱️=650)) Itu jumlah fakta yang sudah punya alamat.
((⏱️=650))

Pipeline yang menghemat bagian ini akan terlihat jauh lebih cepat. ((⏱️=650)) Ia juga akan
menghasilkan kalimat yang tidak bisa Anda pertanggungjawabkan di depan kelas.
((⏱️=650))

```

---

## `07` — 3:56 · slot 59,9 s · log build, cacat penomoran

Layar: kartu LANGKAH 2/5 (233–236), lalu **seluruh log build tampil penuh dan tidak bergerak**:
"Persetujuan tercatat. Saya mulai render artefak" → "Modify, Run checks: 00_run_config.md" →
"Membangun DOCX paket ajar" → "Modify, Run checks: build_docx.py" → "Ditemukan cacat: penomoran
daftar berlanjut lintas bagian (5–9, lalu 10–12, lalu 13–15). Saya periksa halaman lain sebelum
memperbaiki."

```
Kartu ini merangkum apa yang baru saja terjadi. ((⏱️=800)) Empat keputusan, bukan satu.
((⏱️=800))

Kartunya menyebut alasannya sendiri. ((⏱️=800)) Empat keputusan ini mengubah isi materi.
((⏱️=800)) Karena itu agen tidak berwenang memutuskan sendiri. ((⏱️=800))

Persetujuan tercatat. ((⏱️=800)) Saya mulai render artefak. ((⏱️=800))

Perhatikan dua kata di depan tiap baris kecil. ((⏱️=800)) Modify. ((⏱️=800)) Run checks.
((⏱️=800)) Mengubah, lalu memeriksa. ((⏱️=800)) Bukan mengubah lalu selesai.
((⏱️=800))

Dan setiap baris menyebut berkasnya. ((⏱️=800)) Zero zero run config. ((⏱️=800)) Build docx.
((⏱️=800)) build pptx. ((⏱️=800))

Sekarang satu baris yang layak dibaca dua kali. ((⏱️=800))

Ditemukan cacat. ((⏱️=800)) Penomoran daftar berlanjut lintas bagian. ((⏱️=800)) Lima sampai
sembilan. ((⏱️=800)) Lalu sepuluh sampai dua belas. ((⏱️=800)) Lalu tiga belas sampai lima
belas. ((⏱️=800))

Itu bukan kesalahan yang Anda lihat dari jauh. ((⏱️=800)) Dari jauh, halamannya terlihat rapi.
((⏱️=800)) Anda harus menghitung untuk menemukannya. ((⏱️=800))
```

---

## `08` — 4:56 · slot 49,2 s · kalimat sesudahnya, lalu slide

Layar masih log yang sama, tidak bergerak. Baris berikutnya: "Saya periksa halaman lain sebelum
memperbaiki" → "DOCX lolos verifikasi visual. Sekarang slide deck" → "Slide konten terlalu kosong
di bagian bawah. Saya seimbangkan tata letaknya" → "Re-export slide PDF".

```
Yang lebih penting adalah kalimat sesudahnya. ((⏱️=500)) Saya periksa halaman lain sebelum
memperbaiki. ((⏱️=500))

Itu enam kata yang mengubah arti seluruhnya. ((⏱️=500)) Ia tidak memperbaiki satu tempat lalu
menyatakan beres. ((⏱️=500)) Ia bertanya dulu apakah cacat yang sama ada di tempat lain.
((⏱️=500))

Karena kalau pola penomorannya yang salah, ((⏱️=500)) yang salah bukan satu halaman.
((⏱️=500))

DOCX lolos verifikasi visual. ((⏱️=500)) Sekarang slide deck. ((⏱️=500))

Lalu cacat kedua. ((⏱️=500)) Slide konten terlalu kosong di bagian bawah. ((⏱️=500)) Saya
seimbangkan tata letaknya. ((⏱️=500))

Ini bukan kesalahan fakta. ((⏱️=500)) Tidak ada angka yang salah. ((⏱️=500)) Tidak ada aturan
yang dilanggar. ((⏱️=500)) Faktanya benar semua. ((⏱️=500))

Yang salah adalah apakah materinya layak dilihat di depan kelas. ((⏱️=500))

Kebanyakan pemeriksaan otomatis berhenti di fakta. ((⏱️=500)) Yang ini berhenti di ruang kosong
di bawah slide. ((⏱️=500))
```

---

## `09` — 5:45 · slot 39,0 s · kartu 3/5, perbaikan, verifikasi ulang

Layar: kartu "LANGKAH 3/5 — Agen memeriksa hasil sendiri", lalu build ulang dan pemeriksaan.

```
Langkah tiga. ((⏱️=1800)) Agen memeriksa hasil sendiri. ((⏱️=1800))

Kartunya menyebut alasannya: ((⏱️=1800)) verifikasi tidak berhenti di satu temuan.
((⏱️=1800))

Setelah memperbaiki, ia memeriksa ulang. ((⏱️=1800)) Supaya cacat sejenis tidak lolos di halaman
lain. ((⏱️=1800))

Dua kali. ((⏱️=1800)) Tiga kali. ((⏱️=1800)) Bangun, periksa, temukan, perbaiki, bangun lagi.
((⏱️=1800))

Bukan sekali jadi. ((⏱️=1800))

Dan yang membuat hasilnya bisa dipercaya justru bagian yang tidak mulus itu.
((⏱️=1800))
```

---

## `09b` — 6:21 · slot 3,0 s · kartu 4/5 "Permintaan di luar lingkup"

Kartu ini tampil **381,20–384,20 s** — tiga detik saja. Sebelum versi ini kartu itu **lewat tanpa
satu kata pun**; kata "makanan", "halal", "katalog", "menolak", "dua jalan" nol kemunculan di
seluruh `subtitle_id.srt`. Penonton mendengar blok `09` habis di 380,4 s, lalu hening 3,4 s, lalu
blok `10` sudah membicarakan kuis. Itu yang terasa sebagai lompatan.

**Sebabnya bukan lupa, tapi tumpang tindih slot.** `TIMING.json` mencatat `batas_blok.seg4` =
381,20, tetapi blok `09` diberi slot sampai 384,20 — ia memakan 3,0 s milik jendela kartu. Kartu
itu tidak pernah punya slot audio. Sudah diperbaiki: blok `09` dipotong di 381,20, blok `09b`
diisi 381,20–384,20.

Satu kalimat, tujuh kata: sebut **apa yang terjadi** (di luar katalog), **apa jawabannya**
(ditolak), **apa tawarannya** (dua jalan). Kartunya sendiri menanggung "makanan halal" — jangan
diulang di audio, 3 detik tidak cukup untuk dua kali.

```
Di luar katalog: ((⏱️=700)) ditolak, lalu dua jalan.
```

**Kenapa tepat 7 kata.** Tempo rekaman Anda 2,70 kata/detik (diukur dari blok `09`: 53 kata,
19,63 s ucapan murni). 7 kata = 2,59 s, sisa 0,41 s di slot 3,0 s. Versi 8 kata = 2,96 s dan hanya
menyisakan 0,04 s — satu tarikan napas saja sudah melewati slot, lalu `pasang_narasi.py` memotong
kata terakhir. **Jangan ditambah.** Batas keras: 7 kata.

Jangan pula memperpanjang slot kartu dengan menggeser `seg5`: preview kuis sudah tampil penuh di
384,0 s, jadi narasi yang masih jalan setelah itu akan menunjuk hal yang salah.



---

## `10` — 6:24 · slot 11,0 s · kuis interaktif

Layar terbelah. Kanan: kuis "Gaya di Sekitar Kita", satu berkas 29 kilobyte, 10 pilihan ganda dan
5 uraian. Kiri: log "Kuis berfungsi. Satu label perlu diperbaiki agar tidak menyesatkan" →
"Laporan cetak berfungsi, tetapi ada dua cacat tata letak: kolom jawaban terlalu sempit dan judul
Uraian terpisah dari tabelnya".

```
Kuis dibuat sebagai satu berkas. ((⏱️=400)) Jalan tanpa internet. ((⏱️=400))

Lalu ia menguji kuisnya sendiri. ((⏱️=400)) Kolom jawaban terlalu sempit, ((⏱️=400)) judul
Uraian lepas dari tabelnya. ((⏱️=400)) Dua-duanya dicatat. ((⏱️=400))
```

---

## `11` — 6:35 · slot 3,0 s · kartu 5/5

Layar: kartu "LANGKAH 5/5 — Cacat ditemukan lewat pengujian".

```

Cacat ditemukan lewat pengujian. ((⏱️=1350))

```

---

## `12` — 6:38 · slot 5,0 s · kartu penutup

Layar: kartu penutup **"Satu sumber masuk. Lima format keluar. Tidak ada yang terbit tanpa
manusia."**

```
Satu sumber masuk, ((⏱️=250)) lima format keluar, ((⏱️=250)) tidak ada yang terbit tanpa
manusia. ((⏱️=250))
```
