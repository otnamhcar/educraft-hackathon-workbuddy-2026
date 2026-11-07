# Naskah Rekaman Sederhana — satu run, satu tarikan

**Skenario:** masuk WorkBuddy → tempel satu prompt → rekam sampai agen selesai → potong.
Satu berkas, tidak ada segmen A/B/C, tidak ada tiga take narasi.

**Tapi satu hal berubah dari rencana awal, dan ini bukan pilihan gaya:** prompt-nya **satu kalimat
yang sudah ditentukan**, bukan "buatkan saya materi IPAS".

Alasannya ada di §1 di bawah — 20 detik bacaan, lalu langsung ke tabel.

---

## 1. Kenapa prompt-nya harus panjang

Prompt pendek menghasilkan video yang **gugur di dua syarat handbook**, bukan sekadar kurang bagus:

| Syarat handbook §7 | Kalau prompt = "buatkan saya materi IPAS" | Kalau prompt lengkap |
|---|---|---|
| Video harus menampilkan **minimal satu penolakan atau penantian persetujuan** | Agen berjalan mulus, `APPROVE`, selesai. **Tidak ada yang ditolak.** Syarat tidak terpenuhi | Tidak ada penolakan, **tetapi** ada `Human approver: PENDING` + `Publish: LOCKED` di akhir — memenuhi syarat "penantian persetujuan" |
| Video harus memuat **refleksi pendekatan pembangunan** dan **menyebut nama guru** | Tidak ada di dalam materi. Harus ditambahkan saat edit — dan tanpa itu nilai refleksi hilang | Masih perlu ditambahkan, tetapi materinya sudah menyebut aturan dan sumbernya |
| Materi harus **bisa diperiksa**, bukan dikarang | Model akan memakai pengetahuannya sendiri. Angka dan klaimnya tidak bisa dipertanggungjawabkan — persis kegagalan yang proyek ini klaim dicegah | Setiap kalimat bertag ke `source_material_energi.md` |

**Jadi yang diubah cuma isi prompt-nya. Cara kerjanya tetap sesederhana yang Anda rencanakan:**
satu run, satu rekaman, potong belakangan.

---

## 2. Prompt — salin apa adanya

```
Gunakan edu-orchestrator untuk membuat paket materi IPAS topik "Energi
Alternatif dan Penghematan Energi", Fase C (kelas V-VI), CP C4 (2.1.4)
dengan fondasi B5 (1.1.5).
Source: 08_Referensi/source_material_energi.md
Konteks aktual: 08_Referensi/konteks_aktual.md
Rulebook: 08_Referensi/rulebook_ipas.md
Jangan publish. Berhenti di approval gate.
```

Tujuh baris. Yang membuatnya bekerja hanya dua baris terakhir:

- `Source:` — mengunci agen ke satu berkas. Tanpa ini, agen mengarang.
- `Jangan publish. Berhenti di approval gate.` — mengunci agen supaya **tidak** menerbitkan sendiri,
  dan meninggalkan status `PENDING` di layar. Itu satu-satunya "bukti gerbang" yang akan terlihat
  di rekaman satu-run.

---

## 3. Aksi di layar — satu tabel

| # | Aksi di layar | Yang harus terlihat |
|---|---------------|---------------------|
| 1 | `Win + A` → mode Fokus → **"Hanya alarm"**. Tutup WhatsApp/Telegram | notifikasi mati |
| 2 | Buka **WorkBuddy**, maksimalkan. **Ciutkan panel kiri** | tidak ada nama akun di sudut |
| 3 | Tekan `Win + Shift + R` → **"+ Baru"** → tarik selebar layar → **pastikan ikon mikrofon mati** → **Rekam** | rekaman mulai |
| 4 | Jendela WorkBuddy: buka kotak prompt. **Kosongkan isinya** | kotak siap |
| 5 | Tempel ketujuh baris prompt di §2 | prompt terlihat utuh sebelum Enter |
| 6 | Tahan **3 detik** sebelum menekan Enter | prompt terbaca |
| 7 | Tekan **Enter** | agen mulai bekerja |
| 8 | **Jangan sentuh apa pun.** Biarkan Planner → Writer → Reviewer berjalan | teks mengalir, status berubah |
| 9 | Saat agen berhenti: gulir pelan ke daftar **lima format** | RPP, kuis, slide, artikel, infografis |
| 10 | Tahan **4 detik** | daftar format utuh |
| 11 | Gulir ke bagian **tag `[src:`** di salah satu draf | tag terlihat |
| 12 | Tahan **4 detik** | satu kalimat + tag-nya sebaris |
| 13 | Gulir ke **`Human approver`** dan **`Publish`** | `PENDING` / `LOCKED` / `AWAITING_APPROVAL` |
| 14 | Tahan **5 detik. Ini frame terpenting di seluruh video** | status gerbang terbaca |
| 15 | Tekan `Win + Shift + Q` → simpan `rekaman\run_utama.mp4` | berkas ada |

Baris 13–14 **tidak boleh dilewat**. Itu satu-satunya bagian rekaman yang memenuhi syarat handbook.
Kalau rekaman terputus, ulangi dari baris 3.

---

## 4. Lima klip tambahan — masing-masing di bawah 1 menit

Video 5–8 menit tidak bisa diisi satu run. Lima klip ini menutup sisanya, dan **semuanya bisa
direkam tanpa agen berjalan** — cukup membuka berkas yang sudah ada. Total ± 4 menit kerja.

| # | Klip | Aksi di layar | Berkas yang dibuka | ± Lama |
|---|------|---------------|--------------------|--------|
| K1 | Pembuka | Buka gambar kartu judul, tahan | `06_Submission\video_kit\card_00_pembuka.png` | 5 s |
| K2 | Arsitektur | Buka diagram, gulir ke kotak **gerbang** di kanan, tahan | `06_Submission\architecture_diagram.png` | 20 s |
| K3 | Hasilnya terlihat | Buka RPP, gulir lambat 3 layar | `03_Hasil\edu_output_energi_alternatif_faseC_007\01_RPP_Energi_Alternatif_FaseC.md` | 40 s |
| K4 | Kuis interaktif | Buka di browser, klik **satu jawaban salah**, tunjukkan umpan baliknya | `03_Hasil\edu_output_energi_alternatif/10_Kuis_Interaktif_Energi_Alternatif.html` | 30 s |
| K5 | Penutup | Buka kartu penutup, tahan | `06_Submission\video_kit\card_99_penutup.png` | 5 s |

Semua dibuka dengan **Notepad atau browser**, bukan di dalam WorkBuddy. Jadi kelimanya boleh
direkam berurutan dalam satu kali rekam, lalu dipotong sesuai kebutuhan.

---

## 5. Suara — tiga take narasi tetap dipakai

Bagian ini tidak berubah, dan **tidak boleh dilewat**: handbook §7 mewajibkan refleksi pendekatan
pembangunan, dan itu tidak bisa disampaikan lewat teks di layar tanpa menjadi dinding tulisan.

Naskahnya ada di `06_Submission\video_kit\NARASI_SKRIP_TAKE.md`. Untuk skenario sederhana ini,
**hanya TAKE A dan TAKE C** yang wajib:

| Take | Isi | Dipakai untuk |
|------|-----|---------------|
| **A** | Kail + masalah + arsitektur | K1, K2, dan menutup awal run |
| **C** | Refleksi + nama guru **Don Jimat Akbar** + penutup | K5 dan sebelum kartu penutup |

TAKE B (Planner/Writer) boleh dilewat kalau waktunya mepet — tapi kalau ada waktu, rekam saja.
Tanpa narasi, video ini tidak lolos syarat refleksi.

---

## 6. Menyambung — perintah yang disesuaikan

Karena hanya ada **satu** rekaman utama, bukan tiga segmen, urutannya berubah:

```bat
python 06_Submission\video_kit\concat_video.py ^
  --seg-a rekaman\k1_k2_pembuka.mp4 ^
  --seg-b rekaman\run_utama.mp4 ^
  --seg-c rekaman\k3_k4_k5_hasil.mp4 ^
  --out 06_Submission\EduCraft_Demo.mp4
```

Tiga nama di atas hanyalah nama berkas — alatnya tidak peduli isinya apa. Yang penting:

| Batasan | Nilai |
|---------|-------|
| Jumlah berkas | 3 wajib + 2 opsional (`--seg-d`, `--seg-e`) |
| Durasi akhir | **300–480 detik.** Kurang dari 5 menit **ditolak skrip** |
| Resolusi | 1366×768 (bawaan). Jangan diperbesar |

Kalau hasilnya di bawah 5 menit, tambah klip K3 (gulir RPP lebih lama), bukan memperlambat video.

Setelah tersambung:

```bat
python 06_Submission\video_kit\attach_narration.py ^
  --video 06_Submission\EduCraft_Demo.mp4 ^
  --narasi-a rekaman\narasi_a.m4a ^
  --narasi-b rekaman\narasi_b.m4a ^
  --narasi-c rekaman\narasi_c.m4a ^
  --out 06_Submission\EduCraft_Demo_bernarasi.mp4
```

> Skrip ini menaruh take A di detik ke-5, B di 130, C di 245 — angka itu dihitung untuk skrip 7:55.
> Kalau video Anda jauh lebih pendek, **timpa** dengan `--timing` berkas JSON sendiri, atau potong
> audio narasinya secara manual lalu gabungkan di editor. Untuk skenario ini, cara termudah:
> susun ketiga klip supaya totalnya mendekati 7:55.

---

## 7. Yang tetap tidak boleh dilakukan

| Jangan | Kenapa |
|--------|--------|
| Meregangkan video dengan memperlambat | Terlihat, dan terbaca sebagai mengisi durasi |
| Merekam ulang prompt yang sama lalu **menggabung dua run** | Run ID berbeda. Juri membandingkan dengan screenshot; yang tidak cocok lebih merugikan daripada tidak ada |
| Menempel "seolah live" pada video hasil render berkas | Kalau ada yang bertanya, jawab apa adanya: ini rekaman, bukan siaran |
| Menghapus bagian yang gagal | Handbook §6.3: mengungkapkan kegagalan dinilai lebih tinggi daripada menyembunyikannya |
| Mengklaim video ini menampilkan penolakan | Video ini menampilkan **penantian persetujuan**, bukan penolakan. Dua hal berbeda — sebut yang benar |

---

## 8. Ringkas — tempel di samping laptop

```
SIAP   : Win+A Hanya alarm | panel kiri CIUT | WorkBuddy maksimal
REKAM  : Win+Shift+R -> + Baru -> selebar layar -> mic MATI -> Rekam
PROMPT : tempel 7 baris (12_Capture_Prompts.txt SESI 1) -> tahan 3 dtk -> Enter
DIAM   : jangan sentuh apa pun sampai agen berhenti
KUNCI  : tahan 5 dtk di Human approver: PENDING + Publish: LOCKED
STOP   : Win+Shift+Q -> rekaman\run_utama.mp4
TAMBAH : K1 kartu | K2 diagram | K3 RPP | K4 kuis | K5 penutup  (Notepad/browser)
SUARA  : TAKE A + TAKE C  (wajib - tanpa ini refleksi tidak dinilai)
```

---

**Rujukan:** `06_Submission/12_Capture_Prompts.txt` SESI 1 (prompt lengkap) ·
`06_Submission/video_kit/NARASI_SKRIP_TAKE.md` (naskah suara) ·
`06_Submission/16_Panduan_Rekam_Snipping_Tool.md` (tombol Snipping Tool).
