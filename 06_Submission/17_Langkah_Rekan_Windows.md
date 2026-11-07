# Langkah Rekan — mesin Windows

**Untuk siapa:** satu orang, di depan laptop **Windows 11**. Kamu memegang tombol rekam.
**Peran kamu:** merekam layar (3 berkas), merekam suara (3 berkas), menyambung jadi satu video.
**Yang tidak perlu kamu urus:** dokumen, repo, pemeriksaan `doctor.py` — itu di mesin lain.

**Waktu:** ± 30 menit merekam + ± 15 menit menyambung.

---

## Baca ini dulu — satu paragraf

Kamu akan membuat **6 berkas rekaman**, bukan satu:
3 video layar tanpa suara (`seg_a`, `seg_b`, `seg_c`), lalu 3 suara narasi (`narasi_a`, `narasi_b`,
`narasi_c`). Keenamnya disambung jadi satu video oleh satu perintah di Langkah 7.

Kenapa dipisah begitu? Karena suara yang salah bisa diulang tanpa mengulang layar, dan satu segmen
layar yang salah tidak menghapus dua segmen lainnya. Jangan coba merekam semuanya sekali jalan.

---

# BAGIAN 1 — Ambil berkasnya (5 menit)

## Langkah 0. Siapkan tiga hal di laptop

Semua jalan dari folder repo. Kalau belum ada foldernya di laptop ini, ambil dari GitHub:

```bat
cd %USERPROFILE%\Documents
git clone https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026.git
cd educraft-hackathon-workbuddy-2026
```

Kalau **sudah pernah** ada foldernya, cukup tarik versi terbaru:

```bat
cd %USERPROFILE%\Documents\educraft-hackathon-workbuddy-2026
git pull
```

Lalu buat folder kerja untuk rekaman, **di dalam repo**:

```bat
cd %USERPROFILE%\Documents\educraft-hackathon-workbuddy-2026
mkdir rekaman
```

Sekarang buka **tiga** berkas ini di aplikasi lain (Notepad / browser) supaya bisa dibaca sambil
merekam:

| Berkas | Untuk apa | Kapan dibaca |
|--------|-----------|--------------|
| `06_Submission\16_Panduan_Rekam_Snipping_Tool.md` | cara merekam layar | sekarang, sekali |
| `06_Submission\video_kit\CUE_SHEET.md` | adegan apa di segmen mana | sambil merekam |
| `06_Submission\video_kit\NARASI_SKRIP_TAKE.md` | naskah suara | sambil merekam suara |

> Jangan buka `CUE_SHEET.md` di jendela yang ikut terekam. Pindahkan ke ponsel, atau kecilkan di
> pinggir layar setelah rekaman dimulai.

> **Kalau repo sudah ada tapi `git` tidak terpasang:** jangan pasang apa pun sekarang. Minta zip repo
> dari Wawan, ekstrak ke `Documents`, lalu langsung ke Langkah 1. Yang wajib ada hanya `python` dan
> `ffmpeg` di Langkah 7.

---

# BAGIAN 2 — Rekam layar (3 berkas, ± 20 menit)

Langkah rinci tiap tombol ada di `16_Panduan_Rekam_Snipping_Tool.md`. Di bawah ini urutan kerjanya saja.

## Langkah 1. Persiapan 5 menit — sekali untuk ketiga rekaman

1. Tekan **`Win + A`** → **mode Fokus** → **"Hanya alarm"**. Tutup WhatsApp/Telegram di taskbar.
2. Buka jendela **WorkBuddy**, maksimalkan.
3. **Ciutkan panel kiri WorkBuddy** (daftar Tasks). Di sudut kiri bawah panel itu ada nama akunmu,
   dan nama itu tidak boleh ikut terekam.
4. Kalau perlu, perbesar font WorkBuddy satu tingkat.

## Langkah 2. Rekam `seg_a` — 0:00–2:05

**Isi:** kartu pembuka, masalahnya, diagram arsitektur. **Tidak butuh agen berjalan** — ini layar
biasa dan gambar.

1. Tekan **`Win + Shift + R`** → klik **"+ Baru"** → tarik selebar layar → **pastikan ikon mikrofon
   mati** → **Rekam**.
2. Tampilkan sesuai `CUE_SHEET.md` § Segmen A, tiga bagian berurutan, santai saja — jedanya nanti
   dipotong.
3. Tekan **`Win + Shift + Q`** untuk berhenti. Simpan sebagai **`rekaman\seg_a.mp4`**.

## Langkah 3. Rekam `seg_b` — 2:05–4:00

**Isi:** Planner mengeluarkan outline lima format; Writer menulis artikel dengan tag `[src:]`.
**Ini butuh satu run agen berjalan.**

1. Jalankan pipeline sekali (prompt siap tempel ada di `06_Submission\12_Capture_Prompts.txt`,
   bagian **SESI 1**). Tunggu sampai selesai.
2. Mulai merekam (`Win + Shift + R`).
3. Buka `00_plan.md`, gulir pelan melewati daftar lima format. Lalu buka `01_artikel.md`, gulir
   melewati tag `[src:]`, **berhenti di satu kalimat** dan tahan 3 detik.
4. Berhenti (`Win + Shift + Q`), simpan sebagai **`rekaman\seg_b.mp4`**.

## Langkah 4. Rekam `seg_c` — 4:00–7:55

**Isi:** tiga perhentian (penolakan, eskalasi, gerbang), kegagalan, refleksi, penutup.
**Ini bagian terpenting.** Kalau waktu mepet, bagian ini yang dikerjakan lebih dulu.

1. Jalankan prompt penolakan dari `12_Capture_Prompts.txt` **§2.1** (TC-08, R006). Tunggu sampai
   agen berhenti.
2. Mulai merekam. **Tahan tabel penolakan di layar 3 detik penuh** — itu bukti terkuat di video.
3. Lanjut: eskalasi (§3.1, TC-13) → gerbang approval (§2.2, TC-14) → `04_Test_Results.md` §4
   (temuan F-01) → refleksi → kartu penutup.
4. Berhenti, simpan sebagai **`rekaman\seg_c.mp4`**.

> **Kalau segmen ini melewati 4 menit**, hentikan di tengah dan buat berkas kedua:
> `rekaman\seg_c2.mp4`. Langkah 7 punya tombol untuk menambahkan berkas keempat.
> Jangan merekam lebih dari 4 menit sekali jalan — kalau Windows mati di tengah, `.mp4`-nya rusak
> dan tidak bisa dibuka.

## Langkah 5. Periksa ketiga berkas sebelum lanjut

Buka tiap berkas (klik dua kali). Periksa **lima** hal:

- [ ] Ada gambarnya — bukan hitam.
- [ ] **Tidak ada nama akun** di sudut kiri bawah (zoom ke sudut itu).
- [ ] Tidak ada notifikasi lewat di tengah adegan.
- [ ] Teks `REJECT` / `R006` / `ESCALATED_TO_HUMAN` / `APPROVE` **terbaca**.
- [ ] Lamanya masuk akal: A ± 2 menit, B ± 2 menit, C maksimal 4 menit.

**Salah satu gagal → rekam ulang segmen itu saja.** Jangan menambal; jangan menyambung potongan.

---

# BAGIAN 3 — Rekam narasi (3 berkas, ± 15 menit)

Suara rekam **terpisah**, setelah layar selesai. Boleh di ruangan lain, boleh di hari lain.

## Langkah 6. Rekam suara

1. Buka **Voice Recorder** (Perekam Suara) dari menu Start.
2. Atur: mic **15–20 cm** dari mulut, sedikit menyamping. Ruangan berkasur/bertirai, bukan kamar kosong.
3. **Uji dulu:** rekam 10 detik, putar ulang. Kalau terlalu pelan, dekatkan mic — jangan diandalkan
   untuk diperbaiki nanti.
4. Buka `NARASI_SKRIP_TAKE.md`, bacalah **TAKE A** dari atas ke bawah, satu kali. Berhenti.
   Simpan sebagai **`rekaman\narasi_a.m4a`**.
5. Ulangi untuk **TAKE B** → `narasi_b.m4a`, lalu **TAKE C** → `narasi_c.m4a`.

Tiga hal yang sering keliru:

- **Jangan** bilang "halo, tes tes" di awal rekaman. Mulai langsung dari kalimat pertama.
- **Jangan** mengisi seluruh durasi dengan suara. Diam di tengah narasi itu disengaja.
- Tanda `[src:4]` **diucapkan** "src empat"; `[src:CA1]` diucapkan "C-A satu". Jangan mengeja tanda baca.

---

# BAGIAN 4 — Sambung jadi satu video (2 perintah)

## Langkah 7. Periksa `ffmpeg` ada

```bat
ffmpeg -version
```

Kalau keluar nomor versi (mis. `9.0.2`), lanjut. Kalau muncul **"tidak dikenali"**, buka jendela
Command Prompt baru lalu coba lagi — PATH dibaca sekali saat jendela dibuka.

## Langkah 8. Sambung video

Dari folder repo:

```bat
python 06_Submission\video_kit\concat_video.py ^
  --seg-a rekaman\seg_a.mp4 ^
  --seg-b rekaman\seg_b.mp4 ^
  --seg-c rekaman\seg_c.mp4 ^
  --out 06_Submission\EduCraft_Demo.mp4
```

Kalau segmen C dipecah dua, tambahkan satu baris:

```bat
python 06_Submission\video_kit\concat_video.py ^
  --seg-a rekaman\seg_a.mp4 ^
  --seg-b rekaman\seg_b.mp4 ^
  --seg-c rekaman\seg_c.mp4 ^
  --seg-d rekaman\seg_c2.mp4 ^
  --out 06_Submission\EduCraft_Demo.mp4
```

**Yang harus keluar:** baris "Durasi masuk rentang 5:00-8:00". Kalau skrip bilang **GAGAL** dengan
durasi di luar rentang, artinya ada segmen yang kepanjangan — potong di segmen itu, jangan
mempercepat audio.

> Di PowerShell, ganti `^` dengan backtick (`` ` ``) di akhir baris.

## Langkah 9. Tempelkan narasi

Semua argumen wajib ditulis lengkap — skrip ini tidak punya nilai bawaan untuk nama berkas:

```bat
python 06_Submission\video_kit\attach_narration.py ^
  --video 06_Submission\EduCraft_Demo.mp4 ^
  --narasi-a rekaman\narasi_a.m4a ^
  --narasi-b rekaman\narasi_b.m4a ^
  --narasi-c rekaman\narasi_c.m4a ^
  --out 06_Submission\EduCraft_Demo_bernarasi.mp4
```

Skrip ini menaruh `narasi_a` di detik ke-5, `narasi_b` di detik ke-130, `narasi_c` di detik ke-245,
lalu memeriksa durasinya tidak bergeser. **Kalau muncul pesan durasi bergeser, jangan diakali** —
laporkan, itu artinya ada segmen yang lebih panjang dari jatahnya.

Kalau ada take yang lebih panjang daripada slotnya, skrip **memotongnya di akhir dan mengatakannya**.
Kalau itu terjadi, jangan diamkan: rekam ulang take itu lebih pendek, atau periksa apakah narasinya
memang dibaca lebih lambat dari 120 kata/menit.

## Langkah 10. Bakar subtitle

```bat
ffmpeg -i 06_Submission\EduCraft_Demo_bernarasi.mp4 ^
  -vf "subtitles=06_Submission/video_kit/subtitle.srt" ^
  -c:a copy 06_Submission\EduCraft_Demo_final.mp4
```

Perhatikan: path di dalam `subtitles=` memakai **garis miring biasa** (`/`), bukan backslash —
ffmpeg membacanya sebagai filter, dan backslash harus di-escape. Kalau muncul galat
`Unable to open subtitle`, ganti dengan path lengkap: `subtitles=C\\:/Users/.../subtitle.srt`.

## Langkah 11. Tonton sekali dari awal sampai habis

Ini bukan formalitas. Yang diperiksa:

- [ ] Suara terdengar di detik ke-6, bukan menumpuk di awal.
- [ ] Tidak ada detik yang kosong padahal seharusnya ada suara.
- [ ] Subtitle **Inggris**, posisinya di bawah, tidak menutupi teks panel.
- [ ] Lamanya **5:00–8:00** (target 7:55).
- [ ] Tidak ada nama akun, tidak ada notifikasi di seluruh video.

---

# Bagian 5 — Menyerahkan hasil

## Langkah 12. Unggah, jangan dikirim lewat chat

Video 8 menit biasanya **100–200 MB** — terlalu besar untuk WhatsApp dan akan dikompres sampai teks
panel tidak terbaca.

1. Buka `https://drive.google.com` → **Baru** → **Unggah berkas** → pilih
   `06_Submission\EduCraft_Demo_final.mp4`.
2. Klik kanan berkasnya → **Bagikan** → **Siapa saja yang memiliki link** → **Peninjau**.
3. Salin link-nya, kirim ke Wawan.

Kalau kamu memakai **Google Drive yang sama** dengan Wawan, cukup taruh di folder bersama dan
**jangan** kirim link baru — file yang sama akan terlihat oleh keduanya.

**Jangan menyerahkan file mentah** (`seg_a`, `narasi_a`, dst.) lewat chat. Yang diserahkan hanya
`EduCraft_Demo_final.mp4`. Kalau ternyata salah satu segmen perlu direkam ulang, itu urusan berikutnya —
berkas mentahnya tetap ada di folder `rekaman` kalau diminta.

**Jangan commit video 8 menit ke git.** Repo-nya publik dan berkas sebesar itu tidak untuk di-push;
cukup unggahan Drive.

---

# Yang TIDAK perlu kamu kerjakan

| Hal | Siapa yang mengerjakan |
|-----|------------------------|
| Edit `.md`, `doctor.py`, `check_capture.py` | mesin Linux |
| Commit & push repo | mesin Linux |
| Form submission (11 item) | Wawan |
| Unggah `demo_site` (item 11) | Wawan |

---

## Kalau ada yang macet

| Gejala | Perbaikan |
|--------|-----------|
| `python` tidak dikenali | Coba `py` atau `python3` |
| `ffmpeg` tidak dikenali | Buka Command Prompt baru; kalau tetap, cek folder `ffmpeg\bin` ada di PATH |
| `ModuleNotFoundError` | Skrip ini hanya butuh Python standar — pastikan yang jalan Python 3.8+ |
| Video hasil begitu kecil/hitam | Area rekam meleset. Ulangi segmen itu. |
| Suara tidak muncul di video akhir | Cek `narasi_*.m4a` bisa diputar di Voice Recorder |
| Skrip bilang GAGAL durasi | Ada segmen kepanjangan; potong di segmen itu |

**Kalau macet lebih dari 10 menit: berhenti, kirim pesan.** Jangan mengakali dengan menyambung
potongan atau mempercepat video — keduanya terlihat, dan di bagian ini kejujuran justru yang dinilai.

---

**Rujukan:** `06_Submission/16_Panduan_Rekam_Snipping_Tool.md` (tombol Snipping Tool) ·
`06_Submission/video_kit/CUE_SHEET.md` (adegan) · `06_Submission/video_kit/NARASI_SKRIP_TAKE.md`
(naskah suara) · `06_Submission/13_Demo_Video_Runbook.md` §5 (penyambungan, untuk yang mau detail).
