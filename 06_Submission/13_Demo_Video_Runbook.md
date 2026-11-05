# Runbook Produksi Demo Video — Item 7

**Target:** video 5–8 menit (skrip: **7:40**), bahasa Inggris, subtitle terbakar.
**Skrip narasi:** `06_Submission/07_Demo_Video_Script.md` — **baca itu dulu**; dokumen ini hanya
cara memproduksinya.
**Deadline submission:** 7 November 2026 · **target internal: 5 November 2026**.

> Dokumen ini **bukan** pengganti skrip. Skrip menjawab "apa yang dikatakan"; runbook ini menjawab
> "bagaimana merekamnya, dengan alat apa, dalam urutan apa, dan bagaimana membuktikan hasilnya benar".

---

## 1. Status hari ini — apa yang memblokir apa

**8 dari 11 adegan bisa direkam sekarang.** Tiga sisanya butuh agen yang berjalan live.

| # | Adegan | Waktu | Butuh | Bisa direkam 31 Okt? |
|---|--------|-------|-------|----------------------|
| 1 | Hook (jam 21:47) | 0:00–0:35 | teks saja | ✅ ya |
| 2 | Masalah: chatbot salah angka | 0:35–1:10 | satu contoh paragraf (dibuat sendiri) | ✅ ya |
| 3 | Arsitektur | 1:10–2:05 | `06_Submission/architecture_diagram.png` | ✅ ya |
| 4 | **Planner live** | 2:05–3:00 | agen + skill terpasang | ❌ **terblokir** |
| 5 | Tag `[src:#]` pada RPP | 3:00–4:00 | `03_Hasil/materi_ajar/01_RPP_Energi_Alternatif.md` | ✅ ya (buka file, bukan live) |
| 6 | **STOP #1 — penolakan R006** | 4:00–5:00 | agen + skill terpasang | ❌ **terblokir** |
| 7 | **STOP #2 — eskalasi 3×** | 5:00–5:40 | agen + skill terpasang | ❌ **terblokir** |
| 8 | STOP #3 — gerbang approval | 5:40–6:20 | `03_Hasil/edu_output/00_run_config.md` | ✅ ya |
| 9 | Laporan penolakan 29 Okt | 6:20–6:55 | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-29.md` | ✅ ya |
| 10 | **Build approach + kredit guru** | 6:55–7:15 | `08_Referensi/rulebook_ipas.md` + 4 `SKILL.md` | ✅ ya |
| 11 | Penutup + paket akhir | 7:15–7:40 | PDF/PNG/HTML di `03_Hasil/` | ✅ ya |

### 1.1 Satu akar masalah untuk dua pekerjaan

Adegan 4, 6, 7 butuh agen berjalan. Agen butuh skill terpasang, dan **skill belum terpasang** di
mesin ini:

```bash
ls ~/.workbuddy-ai/skills/ | grep '^edu-'     # 31 Okt: kosong
```

Hal yang sama memblokir capture screenshot (`11_Screenshot_Capture_Runbook.md` §1.0). **Satu
instalasi 25 menit membuka dua pekerjaan sekaligus** — video dan bukti uji. Kerjakan itu lebih dulu,
jangan menunggu.

### 1.2 Yang penting: video **tidak** harus menunggu

Delapan adegan lain bisa direkam hari ini. Kalau menunggu semuanya siap, video baru mulai 4 November
dan itu terlalu mepet untuk editing + rekaman ulang. **Rekam yang tidak terblokir lebih dulu.**

---

## 2. Alat — yang benar-benar ada di mesin ini

Diperiksa 31 Okt 2026, bukan diasumsikan:

| Alat | Ada? | Dipakai untuk |
|------|------|---------------|
| `obs` (`/usr/bin/obs`) | ✅ | rekam layar + mikrofon, satu file |
| `ffmpeg` 4.4.2 | ✅ | potong, gabung, subtitle, normalisasi audio, export |
| `ffprobe` | ✅ | **verifikasi** hasil (durasi, stream, resolusi) |
| `audacity` (`/usr/bin/audacity`) | ✅ | rekam narasi terpisah, bersihkan noise |
| `libx264` + `aac` + `x11grab` | ✅ | encoder & capture X11 tersedia |
| `kdenlive`, `shotcut`, `kazam`, `simplescreenrecorder` | ❌ | tidak ada — jangan direncanakan |

Uji encode sudah dijalankan dan berhasil (`1920×1080`, `h264` + `aac`, 1 detik, 101 KB). Artinya
rangkaian export di §6 memang bisa dieksekusi di mesin ini.

> Langkah OBS di §3 berisi pengaturan GUI yang **belum** bisa saya uji dari sini. Kalau OBS tidak
> mau bekerja sama, jalur ffmpeg di §3.3 sudah terbukti mampu.

---

## 3. Merekam

### 3.1 Pengaturan OBS (rekomendasi)

| Setting | Nilai | Alasan |
|---------|-------|--------|
| Canvas & Output | 1920×1080, 30 fps | Cukup tajam untuk teks tag; 60 fps hanya memperbesar file |
| Encoder | x264, CRI 20 | Kualitas baik, ukuran wajar |
| Format rekaman | **`.mkv`** | MP4 rusak kalau OBS mati di tengah rekaman; MKV tidak |
| Audio | 1 track, 48 kHz | Satu track memudahkan sinkronisasi |
| Sumber | Window Capture (bukan Display Capture) | Menghindari notifikasi pribadi ikut terekam |
| Hotkey | Mulai/stop di satu tombol | Menghindari mouse masuk frame |

Setelah selesai, remux ke MP4 — **jangan** encode ulang:

```bash
ffmpeg -i rekaman.mkv -c copy rekaman.mp4
```

### 3.2 Aturan rekaman

1. **Rekam per adegan, bukan satu take 7 menit.** Satu take panjang berarti satu salah kata
   membuang semuanya.
2. **Sebut nomor adegan di awal tiap file** (`s05_tags.mkv`) supaya urutan editing jelas.
3. **Jangan rekam narasi bersamaan dengan layar** kecuali adegan 1–2. Lihat §4.
4. Kalau salah: berhenti, tarik napas, ulangi adegan itu. Jangan menyunting salah kata di tengah.
5. **Jangan** mempercepat gerakan kursor di editing supaya "terlihat rapi". Skrip sudah melarang
   kursor panik; mempercepat rekaman menghasilkan hal yang sama.

### 3.3 Jalur cadangan: ffmpeg tanpa OBS

Butuh `DISPLAY` aktif (sesi desktop). Rekam seluruh layar:

```bash
ffmpeg -f x11grab -video_size 1920x1080 -framerate 30 -i "$DISPLAY" \
       -f pulse -i default -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p \
       -c:a aac -b:a 128k -t 60 adegan.mp4
```

`-t 60` = batas 60 detik; hentikan lebih awal dengan `q`. Kalau `pulse` tidak tersedia, rekam video
saja lalu tambahkan narasi di §4.

---

## 4. Narasi

**Rekam narasi terpisah, jangan live.** Alasannya bukan estetika: narasi live memaksa Anda
mengulang seluruh adegan setiap kali salah kata, dan level audio ikut berubah-ubah.

| Langkah | Detail |
|---------|--------|
| Alat | Audacity, 48 kHz, mono |
| Level target | puncak **−6 dB**, rata-rata **−16 LUFS** |
| Jarak mic | 15–20 cm, sedikit menyamping (hindari letupan "p"/"b") |
| Ruangan | Kain/tirai di belakang; hindari ruangan bergema |
| Per take | satu adegan = satu file (`n05_tags.wav`) |
| Bersihkan | Noise Reduction sekali saja, jangan berlebihan — suara "berair" lebih buruk daripada noise |

Teks narasi ada di skrip, per adegan, dalam bahasa Inggris. Baca **persis** seperti tertulis;
kalimatnya sudah diuji panjangnya terhadap durasi.

---

## 5. Merakit

### 5.1 Gabung per adegan

```bash
# daftar file, satu per baris, urut adegan
printf "file 'v01.mkv'\nfile 'v02.mkv'\n" > daftar.txt
ffmpeg -f concat -safe 0 -i daftar.txt -c copy gabungan.mp4
```

Kalau resolusi/fps antar-adegan berbeda, `-c copy` akan gagal — encode ulang:

```bash
ffmpeg -f concat -safe 0 -i daftar.txt -c:v libx264 -crf 20 -pix_fmt yuv420p \
       -c:a aac -b:a 128k gabungan.mp4
```

### 5.2 Tambahkan narasi

```bash
ffmpeg -i gabungan.mp4 -i narasi.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 128k \
       -shortest bernarasi.mp4
```

### 5.3 Subtitle terbakar (wajib — juri mungkin menonton tanpa suara)

Siapkan `subtitle.srt`, lalu:

```bash
ffmpeg -i bernarasi.mp4 -vf "subtitles=subtitle.srt:force_style='FontSize=22,Outline=2'" \
       -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a copy final.mp4
```

Periksa satu hal spesifik: kata **"reject"** harus terbaca utuh, tidak terpotong di tepi layar.

---

## 6. Export & verifikasi

```bash
ffmpeg -i final.mp4 -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p \
       -c:a aac -b:a 128k -ar 48000 -movflags +faststart \
       EduCraft_Demo_Video.mp4
```

Lalu **verifikasi, jangan diasumsikan**:

```bash
ffprobe -v error -show_entries format=duration,size \
        -show_entries stream=codec_name,width,height,r_frame_rate \
        -of default=noprint_wrappers=1 EduCraft_Demo_Video.mp4
```

| Yang diperiksa | Lulus kalau |
|----------------|-------------|
| Durasi | **300–480 detik** (5:00–8:00). Target 460 detik (7:40) |
| Video | `h264`, `1920×1080` |
| Audio | ada stream `aac`; **dengar 30 detik pertama dan 30 detik terakhir** |
| Subtitle | terbakar, terbaca saat dijeda |
| Putar penuh | sekali, dari awal sampai akhir, di perangkat lain (ponsel) |
| Ukuran | di bawah 500 MB — kalau lebih, naikkan CRF ke 23 |

Checklist shot list di akhir `07_Demo_Video_Script.md` tetap harus dicentang satu per satu.

---

## 7. Pengiriman — **belum terjawab handbook**

Handbook §7 mewajibkan video 5–8 menit tetapi **tidak menyebut bentuk pengirimannya**: berkas,
tautan, atau unggahan ke platform. Ini pertanyaan terbuka, bukan asumsi yang boleh saya isi sendiri.

**Tindakan yang aman (keduanya):**
1. Simpan berkas `EduCraft_Demo_Video.mp4` di `06_Submission/`.
2. Unggah sebagai **unlisted** (YouTube) atau tautan lihat-saja (Drive), lalu catat tautannya di
   `10_Submission_Form_CopyPaste.txt` bagian `[FIELD] DEMO VIDEO`.
3. Uji tautan di jendela privat — kalau tidak terbuka tanpa login, juri juga tidak bisa membukanya.

**Jangan** mengandalkan berkas lokal saja: form submission biasanya berbasis tautan, dan berkas
7 menit sering melewati batas unggahan.

---

## 8. Kalau adegan agen tidak bisa direkam

Turun satu tingkat, dan **sebutkan tingkatnya di video** kalau memakai rekaman/screenshot.

| Tingkat | Kondisi | Yang dilakukan |
|---------|---------|----------------|
| **V0** | Skill terpasang, agen menolak normal | Rekam live sesuai skrip |
| **V1** | Skill terpasang, agen lambat | Rekam, lalu potong jeda tunggu di editing. **Jangan** mempercepat percakapan |
| **V2** | Skill belum terpasang pada 4 Nov | Rekam adegan 6 dari **screenshot** (hasil G3) + narasi yang sama; nyatakan "captured in a verification run" |
| **V3** | Tidak ada screenshot sama sekali | Adegan 6 diganti narasi + tampilan laporan penolakan 29 Okt (adegan 9). Video tetap memenuhi syarat "demonstrate at least one instance" lewat **STOP #3** (gerbang approval, bukti berkas nyata) |

V3 masih memenuhi syarat handbook secara harfiah — "refuses, seeks clarification **or** awaits
approval". Tapi V3 lebih lemah, dan hanya dipakai kalau V0–V2 gagal.

---

## 9. Rencana waktu

| Hari | Kerja | Kenapa |
|------|-------|--------|
| **31 Okt** (hari ini) | Instal skill (§1.1) → rekam adegan 1, 2, 3, 5, 8, 9, 10 | 7 adegan tidak terblokir; mengerjakannya sekarang memindahkan 70% video keluar dari jalur kritis |
| **1 Nov** | Capture screenshot (G3) → sekalian dapat bahan adegan 6 | Satu sesi melayani dua item submission |
| **2 Nov** | Rekam adegan 4, 6, 7 (butuh agen) | Sisanya |
| **3 Nov** | Narasi + rakit + subtitle + export + verifikasi | Jangan menunda ke 5 Nov; editing selalu lebih lama dari perkiraan |
| **4 Nov** | Tonton ulang di ponsel, perbaiki, unggah, uji tautan | Buffer |
| **5 Nov** | Submit | — |

---

## 10. Yang belum ada (jujur)

| Item | Status | Penghalang |
|------|--------|------------|
| Skill `edu-*` terpasang | **BELUM** | `ls ~/.workbuddy-ai/skills/` kosong |
| Adegan 4, 6, 7 (agen live) | **BELUM** | idem |
| Screenshot sebagai bahan V2 | **BELUM** | `11_Screenshot_Capture_Runbook.md` belum dijalankan |
| Berkas video | **BELUM** | `06_Submission/` belum punya `.mp4` |
| Bentuk pengiriman (berkas/tautan) | **TIDAK DIKETAHUI** | Handbook tidak menyebutkannya |
| Uji OBS di mesin ini | **BELUM DIUJI** | Jalur ffmpeg sudah terverifikasi sebagai cadangan |

Empat baris pertama hilang bersamaan begitu skill dipasang. Baris kelima butuh klarifikasi panitia
atau keputusan "unggah dua-duanya" di §7.
