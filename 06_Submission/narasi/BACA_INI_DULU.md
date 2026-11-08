# Catatan Rekaman — satu halaman

Buka juga `SKRIP_TTS_LAYAR.md` di layar kedua. Teks siap tempel ada di `audio_layar/01.txt` …
`12.txt` — salinan bersih tanpa tanda jeda.

> **Struktur berubah lagi: sekarang 12 blok, bukan 7.** Rekaman v2 Anda (7 berkas di folder ini)
> isinya benar, tapi tempo Anda 2,87 kata/detik sehingga blok `02` habis di 2:05 dari slot sampai
> 3:02 — 54 detik layar diam. Dan dua kalimat menunjuk momen yang belum terjadi: *"Materi IPAS untuk
> kelas dan fase berapa"* diucapkan di detik 24, padahal pertanyaan itu muncul di layar detik 70.
>
> Karena itu blok panjang dipecah di titik layar yang nyata. **Tujuh rekaman lama tidak bisa
> dipakai ulang** — teks blok `02` berubah total, dan nomor `03`–`07` sekarang menunjuk isi lain.

| Blok | Slot | Kata | Mulai | Isi layar saat blok ini diputar |
|---|---|---|---|---|
| `01` | 5,0 s | 11 | 0:00 | Kartu judul EduCraft |
| `02` | 65,0 s | 98 | 0:05 | Landing page kosong → brief diketik → "Processed 43s", menunggu model |
| `03` | 30,0 s | 59 | 1:10 | Panel "untuk kelas/fase berapa?" lalu "bentuk keluaran apa?" |
| `04` | 20,0 s | 46 | 1:40 | Dua butir bertentangan: B6 Gaya belum ada faktanya, B5 Energi tidak memuat gaya |
| `05` | 62,1 s | 90 | 2:00 | Keputusan tercatat → "preparing to create task" → layar diam 1 menit |
| `06` | 54,0 s | 112 | 3:02 | "Penulis dilarang mengarang fakta" → creating +295 |
| `07` | 59,9 s | 113 | 3:56 | Log build: render artefak, cacat penomoran 5–9 / 10–12 / 13–15 |
| `08` | 49,2 s | 112 | 4:56 | "Periksa halaman lain" → DOCX lolos → slide terlalu kosong |
| `09` | 39,0 s | 53 | 5:45 | Kartu 3/5, perbaikan, verifikasi ulang |
| `10` | 11,0 s | 24 | 6:24 | Kuis interaktif, dua cacat tata letak |
| `11` | 3,0 s | 4 | 6:35 | Kartu 5/5 — **satu kalimat saja** |
| `12` | 5,0 s | 12 | 6:38 | Kartu penutup "Satu sumber masuk" |

Taruh hasilnya di folder ini dengan nama persis `01.wav` … `12.wav`. `.mp3` juga boleh — saya
kenali dari nomornya. Sebelum merekam, pindahkan dulu tujuh berkas v2 ke `audio_v2_lama/` supaya
tidak tertukar.

## Tiga hal yang paling sering merusak rekaman

1. **Terlalu dekat mikrofon.** Bunyi "p" dan "b" jadi meletup. 15–20 cm, menyamping sedikit.
2. **Menormalkan volume sendiri di editor.** Jangan. Kalau satu blok lebih pelan, biarkan —
   saya yang menyeimbangkan. Yang tidak bisa saya perbaiki adalah klip yang sudah pecah.
3. **Memotong jeda di awal/akhir rekaman.** Jangan potong. Jeda itu saya buang otomatis;
   kalau dipotong manual, saya kehilangan acuan awal kalimat.

## Tempo — bagian yang menentukan cocok atau tidaknya

Tempo Anda terukur **2,87 kata/detik**, dan angka jeda di skrip sudah dihitung untuk 2,85. Artinya
kalau Anda membaca dengan kecepatan yang sama seperti rekaman v2, panjangnya akan pas.

- **`02`** (65 s, 98 kata): paling banyak jedanya, 1,55 detik per titik. Sengaja — layar memang
  diam selama bagian ini. Baca tenang, jangan dipercepat.
- **`05`** (62 s, 90 kata): jeda 1,75 detik. Ini bagian "menunggu", jeda lebar itu memang isinya.
- **`03`, `04`** (30 s dan 20 s): padat. Jeda cuma 0,55 dan 0,3 detik. Baca mengalir, jangan
  berhenti di tiap titik — titiknya di sini hanya untuk memisahkan gagasan.
- **`11`** (3 s, satu kalimat): rekam sekali, jangan ditambah. Kalau lewat 3 detik, kalimatnya
  terpotong di kartu berikutnya. Bilang kalau ini terlalu ketat, saya gabung ke blok `10`.

Aturan praktis: **jangan menambah atau membuang kata.** Angka jeda sudah dihitung ulang untuk
jumlah kata yang ada.

## Kutipan yang harus persis

Kalimat bertanda petik di skrip adalah teks yang benar-benar terbaca di layar.

- `04` → "Dua jawaban Anda sedikit bertentangan."
- `05` → "Baik — keputusan tercatat: B6 Gaya & Gerak."
- `06` → "Penulis dilarang mengarang fakta."
- `08` → "Saya periksa halaman lain sebelum memperbaiki."
- `10` → "Kolom jawaban terlalu sempit, judul Uraian lepas dari tabelnya."
- `12` → "Satu sumber masuk. Lima format keluar. Tidak ada yang terbit tanpa manusia."

Selain itu bebas Anda ubah. Kalau ada kalimat yang membuat lidah tersandung, ganti — skrip ini
alat, bukan naskah suci. Tapi setelah mengganti, jalankan `python3 siapkan_teks.py` supaya
`audio_layar/*.txt` ikut berubah, lalu `ukur_tempo.py` untuk memastikan masih muat slot.

## Setelah selesai

```bash
python3 ukur_tempo.py --audio audio_layar                    # tempo vs hitungan skrip, sebelum diubah
python3 regang_jeda.py --audio audio_layar --tulis           # 01_laras.wav … 12_laras.wav
python3 selaras_subtitle.py --audio audio_layar --keluar subtitle_id.srt
python3 pasang_narasi.py --audio audio_layar --cek
python3 pasang_narasi.py --audio audio_layar
```

`pangkas_senyap.py` tidak lagi dipakai di jalur ini. Alat itu memangkas jeda, sedangkan rekaman
Anda justru **kurang** panjang untuk slotnya — memangkas hanya akan memperlebar kekosongan.
`regang_jeda.py` melakukan kebalikannya: menyisipkan hening ke dalam jeda yang sudah ada, tanpa
menyentuh ucapannya sama sekali.

`regang_jeda.py` melaporkan "per titik" — berapa detik ditambahkan ke tiap jeda. Batas `--maks`
(default 1,8 s) menjaga agar jeda tidak sampai terasa seperti rekaman berhenti. Pada rekaman ini
titik terlebar 1,35 s (`09`), masih di bawah batas.

`--cek` akan menandai blok yang lewat slot dengan `<<< LEWAT`, dan blok yang menyisakan lebih dari
3 detik kosong. Yang pertama dipotong otomatis di ujung slot oleh `pasang_narasi.py`; pada rekaman
ini satu-satunya kasus (`04`, +0,9 s) seluruhnya senyap di ekor, jadi tidak ada kata yang hilang.

Urutan pemilihan berkas audio, dipakai seragam oleh ketiga skrip: `_laras` → `_rapi` → rekaman
asli. Kalau suatu saat Anda mengganti hanya sebagian rekaman, jalankan ulang `regang_jeda.py`
supaya berkas `_laras` tidak tertinggal dari rekaman barunya.
