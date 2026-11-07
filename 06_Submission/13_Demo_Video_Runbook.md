# Runbook Produksi Demo Video — Item 7

**Target:** video 5–8 menit (skrip: **7:40**), **narasi Bahasa Indonesia**, subtitle Inggris terbakar.
**Skrip narasi:** `06_Submission/07_Demo_Video_Script.md` — **baca itu dulu**; dokumen ini hanya
cara memproduksinya.
**Deadline submission:** 7 November 2026 · **target internal: 5 November 2026**.

> Dokumen ini **bukan** pengganti skrip. Skrip menjawab "apa yang dikatakan"; runbook ini menjawab
> "bagaimana merekamnya, dengan alat apa, dalam urutan apa, dan bagaimana membuktikan hasilnya benar".

---

## 1. Status hari ini — apa yang memblokir apa

> **Diganti 7 November 2026.** Tabel "8 dari 11 adegan, 31 Okt" di bawah sudah kedaluwarsa: skill
> terpasang, screenshot lunas, subtitle dan alat penyambung siap. **Yang memblokir sekarang tinggal
> satu — rekaman panel sesi tangkap yang sudah ada di drive bersama belum disalin ke mesin perekam.**
> Lihat §10 untuk status terkini, dan §3.0 untuk daftar panel yang benar-benar perlu direkam.

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

Diperiksa 6 November 2026 di mesin Windows ini, bukan diasumsikan:

| Alat | Ada? | Dipakai untuk |
|------|------|---------------|
| `ffmpeg` 9.0.2-full_build | ✅ terpasang dan ada di PATH | potong, gabung, subtitle, normalisasi audio, export |
| `ffprobe` 9.0.2 | ✅ | **verifikasi** hasil (durasi, stream, resolusi) |
| `libx264` + `aac` + `libass` (`subtitles`) | ✅ | encoder & subtitle bakar tersedia |
| `gdigrab` | ✅ | capture layar Windows — pengganti `x11grab` |
| OBS Studio | ❌ tidak terpasang | kalau dipasang, setelan §3.1 berlaku |
| Audacity | ❌ tidak terpasang | rekam narasi; alternatif: perekam suara bawaan Windows |
| `kdenlive`, `shotcut`, `kazam`, `simplescreenrecorder` | ❌ | alat Linux — tidak ada, jangan direncanakan |

Uji encode sudah dijalankan di mesin ini dan berhasil: `1366×768`, `h264` + `aac` 48 kHz, 1 detik,
35.545 byte. Artinya rangkaian export di §6 memang bisa dieksekusi di sini.

> **Batas mesin (keputusan 6 November 2026).** Panel laptop yang dipakai merekam adalah **1366×768**,
> bukan 1920×1080. Semua angka di §3, §5, dan §6 mengikuti 1366×768. `concat_video.py` juga memakai
> 1366×768 sebagai bawaan (bisa ditimpa `--size 1920x1080` di mesin lain). Jangan memperbesar rekaman
> 1366 ke 1920 — hasilnya buram dan terbaca sebagai manipulasi.

### 2.1 Kalau `ffmpeg` tidak dikenali — biasanya terminal lama, bukan PATH rusak

Diperiksa 6 November 2026: folder `bin` paket ffmpeg **sudah ada** di PATH pengguna
(`...\Gyan.FFmpeg_...\ffmpeg-9.0.2-full_build\bin`), dan `ffmpeg`/`ffprobe` resolve dari proses
Python — jadi `concat_video.py` menemukannya. Kegagalan `'ffmpeg' is not recognized` yang muncul
biasanya berasal dari terminal atau sesi yang **lahir sebelum** PATH diperbarui: PATH dibaca sekali
saat proses dibuat, tidak ikut berubah di tengah jalan.

Urutan pemeriksaan, dari yang paling murah:

1. **Buka terminal baru**, lalu `ffmpeg -version`. Ini menyelesaikan hampir semua kasus.
2. Masih gagal? Periksa apakah folder `bin` ada di PATH:
   `$env:Path -split ';' | Select-String ffmpeg`
3. Belum ada? Tambahkan (scope user, permanen), lalu buka terminal baru:
   ```powershell
   $bin = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin"
   [Environment]::SetEnvironmentVariable("Path",
     [Environment]::GetEnvironmentVariable("Path","User") + ";$bin", "User")
   ```

> Catatan agar tidak salah diagnosa: winget meninggalkan alias **0 byte** di
> `%LOCALAPPDATA%\Microsoft\WinGet\Links\ffmpeg.exe`. Folder itu **tidak** ada di PATH, jadi alias
> rusak tersebut tidak menghalangi apa pun — jangan hapus apa pun karenanya.

> Langkah OBS di §3 berisi pengaturan GUI yang **belum** bisa diuji dari sini karena OBS belum
> terpasang. Kalau OBS tidak mau bekerja sama, jalur ffmpeg di §3.3 sudah terbukti mampu — `gdigrab`
> terverifikasi tersedia.

---

## 3. Merekam

> **Baca ini sebelum memilih alat.** OBS **tidak terpasang** di mesin perekam (§2). Jadi jalur yang
> benar-benar bisa dijalankan hari ini ada dua, dan keduanya gratis: **§3.3 ffmpeg + `gdigrab`**
> (sudah terverifikasi tersedia) atau **§3.4 perekam bawaan Windows** (nol instalasi). §3.1 tetap
> disimpan untuk berjaga kalau OBS dipasang, bukan sebagai langkah pertama.

### 3.0 Yang benar-benar perlu direkam

Rekaman layar hanya dipakai untuk **sesi tangkap**, bukan untuk seluruh video. Panel yang dibutuhkan:

| Panel | Bagian skrip | Perlu rekam layar? |
|-------|--------------|--------------------|
| Sesi 1 — Planner, Writer, Reviewer, gerbang `PENDING`, audit log, kuis | 2:05–4:00 dan 5:40–6:20 | **ya** — klik dan scroll yang bergerak |
| Sesi 2 — penolakan R006, remediasi, `APPROVE` | 4:00–5:00 | **ya** — ini bukti terkuat |
| Sesi 2b — penolakan R007 | (cadangan) | **ya** kalau dipakai |
| Sesi 3a — eskalasi berhenti di iterasi 3 | 5:00–5:40 | **ya** |
| Sesi 3b — instruksi injeksi diabaikan | (cadangan) | **ya** kalau dipakai |
| Kartu pembuka/penutup | 0:00–0:05, 7:58–8:03 | **tidak** — PNG statis, sudah ada di `video_kit/` |
| Laporan penolakan 29 Okt | 6:20–6:55 | **tidak** — cukup gambar diam |
| `rulebook_ipas.md` + `SKILL.md` | 6:55–7:15 | **tidak** — gambar diam |
| Arsitektur | 1:10–2:05 | **tidak** — `architecture_diagram.png` + pan lambat |

Jadi yang perlu ditekan tombol rekamnya: **dua sampai empat panel**, total kurang dari 4 menit layar
bergerak. Sisanya bisa dirakit dari berkas yang sudah ada di repo. Ini menghemat satu jam rekaman
dan menghilangkan sebagian besar risiko salah ucap.

### 3.1 Pengaturan OBS (hanya kalau OBS dipasang)

| Setting | Nilai | Alasan |
|---------|-------|--------|
| Canvas & Output | **1366×768**, 30 fps | Batas panel mesin ini (§2, keputusan 6 Nov 2026). Jangan merekam 1920 lalu mengecilkan — teks tag jadi tidak terbaca |
| Font aplikasi | Naikkan **satu tingkat** (16–18pt) | Menutup teks yang lebih kecil akibat resolusi 1366 |
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

1. **Rekam per panel sesi tangkap, bukan satu take 7 menit.** Satu take panjang berarti satu salah
   klik membuang semuanya. Panel yang perlu direkam ada di §3.0.
2. **Sebut bagiannya di awal tiap berkas** (`s2b_penolakan.mp4`) supaya urutan dan isinya jelas.
3. **Jangan rekam narasi bersamaan dengan layar** kecuali adegan 1–2. Lihat §4.
4. Kalau salah: berhenti, tarik napas, ulangi adegan itu. Jangan menyunting salah kata di tengah.
5. **Jangan** mempercepat gerakan kursor di editing supaya "terlihat rapi". Skrip sudah melarang
   kursor panik; mempercepat rekaman menghasilkan hal yang sama.

### 3.3 Jalur cadangan: ffmpeg tanpa OBS

Di Windows, pengganti `x11grab` adalah `gdigrab`, dan `pulse` diganti `dshow`. Rekam seluruh layar
plus mikrofon:

```bat
ffmpeg -f gdigrab -framerate 30 -video_size 1366x768 -i desktop ^
       -f dshow -i audio="<nama mikrofon>" -c:v libx264 -preset veryfast -crf 20 ^
       -pix_fmt yuv420p -c:a aac -b:a 128k -t 60 adegan.mp4
```

Cari nama perangkat audio lebih dulu:

```bat
ffmpeg -list_devices true -f dshow -i dummy
```

`-t 60` = batas 60 detik; hentikan lebih awal dengan `q`. Kalau nama mikrofon tidak ketemu atau
`dshow` menolak, **rekam video saja** — buang bagian `-f dshow -i audio=... -c:a aac -b:a 128k` — lalu
tambahkan narasi di §4. Jangan menunda rekaman hanya karena audio.

> Padanan Linux/macOS (kalau rekaman dikerjakan di mesin lain):
> `ffmpeg -f x11grab -video_size 1366x768 -framerate 30 -i "$DISPLAY" -f pulse -i default ...`

### 3.4 Jalur tanpa instalasi: perekam bawaan Windows

Paling cepat kalau ffmpeg terasa terlalu teknis. Tidak ada yang perlu dipasang.

| Alat | Cara membuka | Catatan |
|------|--------------|---------|
| **Xbox Game Bar** (Win+G) | Tekan `Win+G`, tekan tombol rekam | Rekam **satu jendela** lewat tombol kamera di bilah Game Bar. Hasil `.mp4` di `Videos\Captures`. Batas praktisnya panjang, tetapi tidak bisa merekam seluruh desktop |
| **Snipping Tool** (Win+Shift+S → ikon kamera) | Windows 11 23H2 ke atas | Merekam **area** atau seluruh layar, hasil `.mp4`. Lebih mudah dipotong daripada Game Bar |
| Snipping Tool mode pita | Pilih "Rekam" lalu tarik kotak | Untuk rekaman yang hanya perlu area panel |

Aturan yang tetap berlaku apa pun alatnya:

1. **Nonaktifkan notifikasi lebih dulu** — `Win+A` → mode Fokus → "Hanya alarm". Satu pop-up di
   panel penolakan merusak bukti terkuat di video.
2. **Jangan rekam audio di tahap ini** kecuali Anda yakin. Narasi direkam terpisah (§4), jadi rekaman
   layar yang senyap **lebih baik** — tidak ada suara klik keyboard yang harus dibersihkan.
3. **Sebut bagiannya di awal berkas** (`s2b_penolakan.mp4`), jangan pakai nama bawaan "Rekaman layar
   2026-11-07 1324". Anda akan menebak-nebak saat menyambung.
4. **Rekor ulang seluruh panel, jangan menyambung potongan.** Dua take yang ditempel di tengah panel
   membuat kursor terlihat melompat — juri membaca itu sebagai rekayasa.

Konsekuensi format yang harus diterima: Game Bar dan Snipping Tool menghasilkan `.mp4`, bukan `.mkv`.
Kalau proses merekam terhenti di tengah (listrik, Windows update), berkas `.mp4` sering tidak bisa
dibuka. Rekam panel pendek (di bawah 2 menit) supaya kerugiannya kecil kalau itu terjadi.

---

## 4. Narasi

**Rekam narasi terpisah, jangan live.** Alasannya bukan estetika: narasi live memaksa Anda
mengulang seluruh adegan setiap kali salah kata, dan level audio ikut berubah-ubah.

| Langkah | Detail |
|---------|--------|
| Alat | Audacity — **tidak terpasang di mesin ini** (§2). Alternatif: perekam suara bawaan Windows |
| Level target | puncak **−6 dB**, rata-rata **−16 LUFS** |
| Jarak mic | 15–20 cm, sedikit menyamping (hindari letupan "p"/"b") |
| Ruangan | Kain/tirai di belakang; hindari ruangan bergema |
| Per take | tiga take, satu per segmen (`narasi_a.wav`, `narasi_b.wav`, `narasi_c.wav`) — sesuai `CUE_SHEET.md`, bukan per adegan |
| Bersihkan | Noise Reduction sekali saja, jangan berlebihan — suara "berair" lebih buruk daripada noise |

Teks narasi ada di skrip, per adegan, **dalam Bahasa Indonesia**. Baca persis seperti tertulis;
kalimatnya sudah diuji panjangnya terhadap durasi. Subtitle yang dibakar berbahasa Inggris — itu
terjemahannya, dan dibuat dari narasi yang sama, bukan narasi terpisah.

---

## 5. Merakit

### 5.1 Gabung per adegan

```powershell
# daftar file, satu per baris, urut adegan (PowerShell)
@("file 'v01.mkv'","file 'v02.mkv'") | Set-Content daftar.txt -Encoding ascii
ffmpeg -f concat -safe 0 -i daftar.txt -c copy gabungan.mp4
```

```bash
# padanan Git Bash / Linux / macOS
printf "file 'v01.mkv'\nfile 'v02.mkv'\n" > daftar.txt
ffmpeg -f concat -safe 0 -i daftar.txt -c copy gabungan.mp4
```

`Set-Content -Encoding ascii` dipakai supaya berkas tidak membawa BOM — demuxer `concat` menolak
BOM di awal baris pertama.

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

> **Jebakan Windows:** di dalam filter `subtitles=`, tanda titik dua memisahkan opsi — jalur absolut
> `C:\...` akan gagal. Jalankan perintah dari folder yang memuat `subtitle.srt` dan sebut namanya
> saja seperti di atas, atau tulis `subtitles='C\:/video/subtitle.srt'`.

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
| Video | `h264`, `1366×768` (atau ukuran `--size` yang dipakai) |
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

## 10. Yang belum ada (diperbarui 7 November 2026)

Rencana waktu di §9 sudah **kedaluwarsa**: tanggal 31 Okt–5 Nov lewat. Yang tersisa dikerjakan hari ini.

| Item | Status | Penghalang |
|------|--------|------------|
| Skill `edu-*` terpasang | **SUDAH** (4 skill, 5 Nov) | — |
| Screenshot 12 wajib | **SUDAH** (`check_capture.py` 20/0/2) | — |
| `subtitle.srt` | **SUDAH** (68 blok, teruji bakar) | — |
| `concat_video.py` 5 segmen | **SUDAH** (teruji 5 klip sintetis) | — |
| Rekaman panel sesi tangkap | **BELUM** — 5 berkas mentah di drive bersama | Rekaman di mesin Windows, belum disalin |
| Berkas video final | **BELUM** | Potong → sambung → narasi → bakar subtitle |
| Bentuk pengiriman (berkas/tautan) | **BELUM PASTI** | Formulir punya bidang deskripsi; siapkan berkas + unggahan unlisted |
| OBS terpasang | **TIDAK** | Pakai §3.3 `gdigrab` atau §3.4 perekam bawaan Windows |
| `ffmpeg`/`ffprobe` | **SUDAH** 9.0.2-full_build | — |
| Audacity | **TIDAK** | Pakai perekam suara bawaan Windows |

**Menit-menit ini, urutannya:** nonaktifkan notifikasi → rekam panel (§3.0) → potong per sesi → sambung
(§5) → rekam narasi 3 take (§4) → bakar subtitle (§5.3) → `ffprobe` (§6).
