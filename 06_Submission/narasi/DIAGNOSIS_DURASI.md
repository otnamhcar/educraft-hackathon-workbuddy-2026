# Diagnosis durasi audio — status 8 Nov 2026, 01:05

Berkas ini mencatat **apa yang terukur**, bukan apa yang diperkirakan. Angka di
`SKRIP_TTS_JEDA.md` (tabel "Sisa 0,1 s" dan seterusnya) **tidak berlaku lagi** —
tabel itu dihitung dengan tempo 3,25 kata/detik ketika belum ada satu pun berkas
audio. Sekarang ada delapan, dan semuanya lebih panjang dari slotnya.

Jangan pakai tabel itu untuk memutuskan apa pun.

> **Kesimpulan akhir (diperbarui 8 Nov, 02:20):** tujuh dari delapan blok **muat**
> tanpa rekam ulang, hanya dengan memangkas senyap. Hanya `01` yang benar-benar
> kelebihan kata. Lihat bagian "Hasil akhir" di bawah.

---

## Yang terukur

Delapan blok sudah direkam. Semuanya melewati slotnya:

| Blok | Kata | Slot | Durasi | Lebih | Kecepatan bicara | Rasio jeda |
|---|---|---|---|---|---|---|
| `01` | 11 | 5,0 s | 6,17 s | **+1,2 s** | 2,60 kps | — |
| `02` | 162 | 82,0 s | 95,18 s | **+13,2 s** | 3,03 kps | 1,11× |
| `03` | 190 | 92,0 s | 118,27 s | **+26,3 s** | 2,72 kps | 1,32× |
| `04` | 77 | 51,0 s | 63,26 s | **+12,3 s** | 2,56 kps | 1,23× |
| `05` | 219 | 106,0 s | 139,87 s | **+33,9 s** | 2,72 kps | 1,37× |
| `06` | 54 | 36,0 s | 42,38 s | **+6,4 s** | 2,68 kps | 1,21× |
| `07` | 16 | 11,0 s | 13,66 s | **+2,7 s** | 2,56 kps | 1,22× |
| `08` | 12 | 5,2 s | 5,33 s | **+0,1 s** | 2,96 kps | — |

## Tiga penyebab, semuanya terukur

**1. Tempo bukan satu angka.** Saya dulu memakai 3,25 kata/detik. Mesin ini
berjalan 2,56–3,03 kata/detik, dan **berbeda-beda per blok**. Kalau dipaksa satu
rata-rata (2,76), perkiraan untuk blok `02` meleset 7 detik. Karena itu
penghitungan ulang harus per blok, bukan global.

**2. `((⏱️=…))` membengkak 1,11–1,37×.** Angka yang diminta tidak sama dengan
yang keluar, dan pembesarannya juga berbeda per blok. `((⏱️=1000))` bisa keluar
1.110 ms atau 1.370 ms tergantung bloknya.

**3. Mesin menambah senyap sendiri di dalam kalimat.** Rata-rata 3,3 detik per
blok, di tempat yang tidak ada `((⏱️))`-nya. Ini di luar kendali skrip sepenuhnya.

Akibat gabungannya: **36–52% durasi berkas adalah senyap.** Blok `05` bicara
hanya 80,5 detik dari 139,9 detik totalnya.

## Hasil akhir: senyap dipangkas, kata tidak

`pangkas_senyap.py` mencari satu ambang per blok — jeda lebih panjang dari ambang
dipangkas, jeda lebih pendek dibiarkan utuh (itu napas mesin; memotongnya menyambung
dua kata tanpa hening). Ambang dicari dengan pencarian biner supaya hasilnya tepat
menyentuh slot, tidak kurang.

| Blok | Durasi asli | Slot | Ambang jeda | Hasil | Terverifikasi |
|---|---|---|---|---|---|
| `01` | 6,17 s | 5,0 s | 115 ms | 4,70 s | **tidak muat*** |
| `02` | 95,18 s | 82,0 s | 873 ms | 81,70 s | 81,699 s |
| `03` | 118,27 s | 92,0 s | 593 ms | 91,70 s | 91,697 s |
| `04` | 63,26 s | 51,0 s | 1.322 ms | 50,70 s | 50,700 s |
| `05` | 139,87 s | 106,0 s | 478 ms | 105,70 s | 105,698 s |
| `06` | 42,38 s | 36,0 s | 1.896 ms | 35,70 s | 35,701 s |
| `07` | 13,66 s | 11,0 s | 1.650 ms | 10,70 s | 10,700 s |
| `08` | 5,33 s | 5,2 s | 318 ms | 4,93 s | 4,934 s |

Kolom "Terverifikasi" adalah `ffprobe` pada berkas hasil, bukan angka dari model.
Selisih dari prediksi ≤ 3 ms di seluruh blok.

Setiap blok menyisakan 120 ms senyap di ujung awal dan akhirnya — bukan nol, jadi
tidak ada kata yang terpotong langsung. Jeda terdalam yang tersisa: 478 ms (`05`)
sampai 1,90 s (`06`).

**Tujuh blok muat tanpa rekam ulang dan tanpa memotong satu kata pun.**
Ini membalik kesimpulan sebelumnya: masalahnya memang kelebihan senyap, bukan
kekurangan waktu. Blok `05` hanya memakai 48% durasinya untuk bicara; sisanya hening.

### `01` satu-satunya yang kelebihan kata

Ambangnya harus turun ke 115 ms — di bawah lantai wajar 320 ms — dan tetap
menghasilkan 4,70 s untuk slot 5,0 s **setelah** margin. Artinya kalimat pembuka
memang terlalu panjang untuk kartunya:

> "Yang saya ketik cuma satu baris. Bantu saya membuat materi IPAS."

Tiga cara, dan hanya satu yang saya sarankan:

1. **Pendekkan kalimatnya** — "Yang saya ketik cuma satu baris. Bantu buat materi IPAS."
   (membuang dua suku kata, cukup). Rekam ulang blok `01` saja, 5 detik kerja.
2. Panjangkan kartu pembuka di video — mengubah timing seluruh video, tidak sepadan
   hanya untuk 1 detik.
3. Biarkan audio 4,70 s di slot 5,0 s — ada 300 ms senyap di ujung, tidak terdengar
   salah sama sekali.

Cara 3 sebenarnya sudah cukup. Audio 4,70 s di dalam slot 5,0 s berarti pembuka
selesai 0,3 s sebelum kartu berganti — bukan masalah, malah terdengar lapang.

## Cara mengulang

```bash
python3 ukur_tempo.py                      # ukur tempo & senyap tiap blok
python3 siapkan_teks.py                    # turunkan 01.txt…08.txt dari SKRIP_TTS_JEDA.md
python3 pangkas_senyap.py                  # pratinjau: apa yang akan dipangkas
python3 pangkas_senyap.py --tulis --ekstensi wav   # tulis 01_rapi.wav…08_rapi.wav
python3 selaras_subtitle.py --audio .      # subtitle_id.srt dari audio _rapi
python3 pasang_narasi.py --audio .         # render video bernarasi + subtitle
```

`ukur_tempo.py --json` mengeluarkan angka yang sama dalam bentuk mesin, untuk
dipakai kalau nanti ada alat penyetel yang membaca hasil ukur langsung.

## Subtitle: kenapa disusun ulang

Setelah audio dipangkas, `subtitle_id.srt` lama **tidak berlaku** — ia dihitung
terhadap rekaman asli, dan blok `02` saja kini 14 detik lebih pendek. Cue terakhir
blok `02` dulu jatuh di detik 84, yang sekarang sudah masuk wilayah blok `03`.

Penyelarasan lama juga salah caranya, bukan cuma angkanya. Ia memetakan kalimat ke
keheningan **secara proporsional** — `idx = round((i+1)/n × jumlah_keheningan) − 1` —
tanpa melihat isi audio. Itu hanya benar kalau jumlah keheningan sama dengan jumlah
kalimat. Kenyataannya tidak: blok `02` punya 39 keheningan untuk 28 kalimat, karena
mesin menarik napas di tengah kalimat.

Yang dipakai sekarang:

1. Keheningan diubah menjadi **region bicara** — bagian berkas yang tidak senyap.
2. Region dikelompokkan menjadi tepat satu kelompok per kalimat, dengan pemrograman
   dinamis. Biayanya: (panjang ucapan − proporsi jumlah kata)², ditambah hukuman
   kalau batas kelompok jatuh di sel pendek (< 0,70 s) — sel pendek berarti napas di
   tengah kalimat, bukan batas kalimat.
3. Cue per kalimat dibagi lagi menurut jumlah kata, di dalam rentang kalimat itu.

Blok `01` dan `06` tidak punya cukup region untuk dipetakan (satu region untuk tiga
kalimat, sembilan untuk sembilan). Untuk yang seperti itu dipakai pembagian
menurut jumlah kata. Tanpa jalan ini, blok `01` menghasilkan semua batas di titik
yang sama, cue menumpuk, lalu meluber ke blok `02`.

Hasil yang diperiksa: 122 cue, **0 tumpang tindih**, 0 cue melewati 403,234 s,
durasi cue 0,37–7,00 s (median 3,06 s), dan subtitle tampil 90–98% durasi tiap blok.

## Gaya subtitle

`BorderStyle=3` (kotak hitam 50%, `BackColour=&H80000000`), bukan teks ber-outline.

Alasannya bukan selera: video ini rekaman layar dokumen. Hampir setiap bingkai
berisi teks abu-abu, jadi subtitle putih ber-outline hitam **bertabrakan dengan teks
halaman di sepanjang video**. Saya memeriksa bingkai pada detik 13, 150, 299, dan 300
sebelum memutuskan. Kotak memisahkan subtitle sebagai lapisan; 100% menutupi halaman,
0% kembali bertabrakan.

**Catatan untuk yang mengubah `pangkas_senyap.py`:** model durasi dan pembangun
filter wajib memakai `rentang_isi()` yang sama. Sebelumnya keduanya menghitung tepi
sendiri-sendiri dan hasilnya meleset sampai 10 detik pada blok `03` — model benar,
builder salah, dan yang terlihat di layar adalah builder.
