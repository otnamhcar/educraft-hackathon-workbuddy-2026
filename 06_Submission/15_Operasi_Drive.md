# Operasi Drive — Penggantian Berkas Submission

**Dibuat:** 9 November 2026 · **Untuk:** Wawan · **Sifat:** dikerjakan di browser, bukan dari repo
**Konteks:** formulir sudah disubmit 8 November 2026. Dokumen ini menutup selisih antara apa yang
sudah diserahkan dan apa yang seharusnya diserahkan.

Alasan dokumen ini ada: tidak ada akses tulis ke Drive dari mesin ini (tanpa `rclone`, tanpa
kredensial Google). Karena itu pekerjaan Drive dilakukan manual, dan dokumen ini yang menjadi
catatan bahwa pekerjaannya benar.

---

## 0. Yang harus Anda putuskan lebih dulu: buat folder milik sendiri

Folder lama `1BB3aJrYzrasax-8d_U-6fw1U551qSvOs` **bukan milik Anda**. Kolom Owner pada 8 November
menunjukkan mayoritas berkas dimiliki `informatika.alyaku01`, dan panel Activity mencatat
*"sharing permissions were changed on 78 items"* pada 7 November 17:17. Tautan ke folder yang bukan
milik Anda bisa dicabut tanpa persetujuan Anda.

**Langkah:**

1. Buka [drive.google.com](https://drive.google.com) dengan akun yang sama seperti saat submit.
2. **New → Folder**, beri nama `EduCraft_Hackathon_2026_Submission`.
3. Buka folder itu → **Share** → *General access* → ubah menjadi
   **"Anyone with the link"** dan peran **Viewer**. Ini wajib: juri tidak punya akun Google Anda.
4. Salin tautannya (`https://drive.google.com/drive/folders/...`). Tautan ini yang menggantikan
   tautan lama di formulir.

**Jangan** memindahkan folder lama. Biarkan ia apa adanya — kalau nanti panitia memverifikasi versi
yang Anda submit pertama, jejaknya masih ada.

---

## 1. Unggah video final — satu berkas, ukuran harus tepat

| | |
|---|---|
| **Berkas** | `06_Submission/narasi/EduCraft_Demo_narasi_bakar.mp4` |
| **Ukuran target** | **13.880.615 byte** (tampil **13,2 MB** di Drive) |
| **SHA256** | `2c45b3e2e2d02aa2524e47c46915f5c133f3924fc09484a0ff036568347e60b9` |
| Durasi | 403,234 s (6:43) |
| Resolusi | 1366×768, H.264 + AAC |
| Audio | −19,9 dB rata-rata, −1,5 dB puncak |
| Subtitle | ter-burn, 122 cue |

**Cara unggah:** buka folder baru → **New → File upload** → pilih berkas di atas → tunggu sampai
"Upload complete".

**Verifikasi setelah terunggah — tiga hal, jangan dilewati:**

1. **Ukuran tampil 13,2 MB.** Kalau yang muncul 6,8 MB, Anda mengambil berkas lama. Kalau 12,2 MB,
   itu `EduCraft_Demo_narasi.mp4` yang tanpa subtitle. Hentikan, ulangi.
2. **Putar di browser, di menit 0:20–0:40.** Anda harus **mendengar suara**. Video yang senyap
   (−91 dB) adalah `EduCraft_Demo.mp4` — berkas yang salah.
3. **Lompat ke detik 6:21.** Kartu "Permintaan di luar lingkup" harus **ada narasinya**. Ini
   perbaikan blok `09b` di versi 9 November; kalau di detik itu tidak ada suara, Anda mengunggah
   render lama.

> Berkas yang **jangan** diunggah: `06_Submission/EduCraft_Demo.mp4` (5,8 MB, audio senyap total)
> dan `06_Submission/narasi/EduCraft_Demo_narasi.mp4` (12,2 MB, tanpa subtitle).

---

## 2. Hapus sembilan berkas dari folder lama

Folder lama masih memuat bahan mentah yang membuat bundel terlihat berantakan. Rekaman mentah
**tidak wajib** diserahkan — handbook §7 hanya meminta video 5–8 menit, bukan bahannya.

| Berkas di Drive lama | Ukuran | Alasan dihapus |
|---|---|---|
| `video_01.mp4` | 40,4 MB | rekaman mentah klip 1 |
| `video_02_1.mp4` | 29,2 MB | rekaman mentah klip 2a |
| `video_02_2.mp4` | 25,0 MB | rekaman mentah klip 2b |
| `video_03_1.mp4` | 3,8 MB | rekaman mentah klip 3a |
| `video_03_2.mp4` | 16,7 MB | rekaman mentah klip 3b |
| `videoNew_01.mp4` | 144,0 MB | rekaman ulang, mentah |
| `videoNew_01_2.mp4` | 84,2 MB | rekaman ulang, mentah |
| `EduCraft_Hackathon_2026.7z` | 11,2 MB | arsip 30 Oktober — kedaluwarsa |
| `README.md` | 4 KB | versi 27 Oktober, repo sudah punya yang 24 KB |
| `EduCraft_Demo.mp4` | 6,8 MB | **berkas salah** — ganti dengan yang di §1 |

**Total ± 354 MB + 4 KB.** Kalau tidak ada di Trash, tautan folder lama yang sudah tersebar tidak
bisa diakses lagi — tidak apa-apa, karena tautan penggantinya ada di §4.

Arsip `.7z` itu paling penting untuk dihapus. Isinya snapshot 30 Oktober: sebelum video final,
sebelum run `-006` sampai `-011`, sebelum checklist dikoreksi. Siapa pun yang mengunduhnya akan
membaca angka yang sudah tidak berlaku.

---

## 3. Salin tiga subfolder ini ke folder baru

Subfolder di folder lama bertanggal **27 Oktober** — kedaluwarsa. Ambil versi terbaru dari repo:

| Folder di repo | Isi | Ukuran |
|---|---|---|
| `05_Bukti_Proses/evidence_bundle/03_screenshots/` | 16 PNG, termasuk 12 wajib | 2,5 MB |
| `06_Submission/architecture_diagram.png` | diagram arsitektur | 0,6 MB |
| `06_Submission/cover_image_380x216.png` + `cover_image_1280x720.png` | gambar sampul | 0,5 MB |

**Saat mengunggah screenshot, pertahankan empat subfolder** `S1_golden_path/`, `S2_refusal_cycle/`,
`S3_escalation/`, `S4_extras/`. `tools/check_capture.py` menolak berkas yang diletakkan langsung di
akar folder sebagai *stray*, dan itu membuat bukti item 5 dianggap tidak lengkap kalau diverifikasi
ulang.

Di browser, unggah per subfolder: buka `S1_golden_path/` di Drive → **New → File upload** → pilih
isi folder itu. Ulangi untuk tiga subfolder lain.

---

## 4. Kirim koreksi tautan ke panitia

Formulir sudah terkirim, jadi tautan tidak bisa diedit sendiri. Kirim pesan lewat kanal resmi
(grup WhatsApp trek, atau email panitia bila ada). Teks siap pakai:

> Selamat pagi, tim panitia Tencent Cloud Hackathon Indonesia 2026.
>
> Kami tim peserta Challenge C (EduCraft) ingin mengoreksi satu tautan pada submission yang kami
> kirim 8 November 2026.
>
> Tautan video demo yang kami cantumkan sebelumnya mengarah ke berkas draf di folder bersama. Berkas
> yang benar adalah versi final dengan narasi dan subtitle lengkap, durasi 6 menit 43 detik:
>
> **[TAUTAN FOLDER BARU]**
>
> Berkas: `EduCraft_Demo_narasi_bakar.mp4` (13,2 MB)
>
> Selain tautan video, isi submission kami tidak berubah. Terima kasih.

Ganti `[TAUTAN FOLDER BARU]` dengan tautan dari §0 langkah 4. Kalau panitia meminta satu tautan
langsung ke berkas, bukan folder: buka berkasnya di Drive → **⋮ → Share → Copy link**.

---

## 5. Daftar centang

- [ ] Folder baru dibuat dengan akun sendiri, nama `EduCraft_Hackathon_2026_Submission`
- [ ] Izin folder sudah *Anyone with the link → Viewer*
- [ ] Video 13,2 MB terunggah, **bukan** berukuran 6,8 MB atau 12,2 MB
- [ ] Video diputar menit 0:20–0:40 — **suara terdengar**
- [ ] Video dilompat ke detik 6:21 — **kartu 4/5 ada narasinya**
- [ ] Sembilan berkas di §2 dihapus dari folder lama
- [ ] 16 screenshot terunggah, empat subfolder dipertahankan
- [ ] Diagram arsitektur + dua gambar sampul terunggah
- [ ] Tautan folder baru diuji di **jendela privat** (mode incognito) — bisa dibuka tanpa login
- [ ] Pesan koreksi terkirim ke panitia
- [ ] Balasan panitia disimpan sebagai tangkapan layar di `06_Submission/`

---

## 6. Kalau ada yang tidak cocok

| Gejala | Kemungkinan penyebab | Tindakan |
|---|---|---|
| Video 6,8 MB | mengambil `EduCraft_Demo.mp4` | hapus, unggah `narasi/EduCraft_Demo_narasi_bakar.mp4` |
| Video 12,2 MB | mengambil versi tanpa subtitle | hapus, ambil dari folder `narasi/` |
| Video senyap | berkas lama | ganti dengan versi 13,2 MB |
| Detik 6:21 tanpa narasi | render sebelum 9 November | render ulang, ulangi §1 |
| Juri tidak bisa membuka tautan | izin folder masih *Restricted* | ulangi §0 langkah 3 |
| Folder hilang dari daftar | izin dicabut pemilik folder lama | tidak relevan — Anda sudah punya folder sendiri |
