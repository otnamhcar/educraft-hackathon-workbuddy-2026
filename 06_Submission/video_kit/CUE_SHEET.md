# Cue sheet rekaman — tiga segmen, satu sesi per segmen

**Skrip lengkap:** `06_Submission/07_Demo_Video_Script.md` (7:40, 10 adegan)
**Alat penyambung:** `06_Submission/video_kit/concat_video.py`
**Kartu judul:** `card_00_pembuka.png`, `card_99_penutup.png` (1920×1080, sudah jadi)

Tiga segmen, bukan sepuluh. Alasannya praktis: salah ucap di tengah adegan ketujuh tidak
menghapus empat menit rekaman sebelumnya. Ulangi satu segmen, bukan seluruh video.

| Segmen | Rentang skrip | Durasi rekam | Isi |
|--------|---------------|--------------|-----|
| A | 0:00 – 2:05 | 125 s | Kail, masalah, arsitektur |
| B | 2:05 – 4:00 | 115 s | Planner, Writer |
| C | 4:00 – 7:40 | 220 s | Tiga perhentian, kegagalan, refleksi, penutup |

Kartu judul menambah 10 detik (5 detik di awal, 5 detik di akhir). Jadi rekam **7:30**, hasil
akhir **7:40**. Kalau salah satu segmen melar, potong di segmen itu — jangan mempercepat audio.

---

## Sebelum merekam (5 menit, sekali saja)

> **Batas mesin — diperiksa 6 November 2026.** Layar mesin ini **1366×768**, dan **`ffmpeg` belum
> terpasang**. Dua konsekuensi:
> 1. Rekaman **1920×1080 hanya mungkin lewat monitor eksternal**. Tanpa itu, rekam pada 1366×768
>    dan catat apa adanya di kartu penutup — jangan memperbesar hasil rekaman.
> 2. `concat_video.py` butuh `ffmpeg` **dan** `ffprobe` di PATH. Pasang dulu
>    (`winget install Gyan.FFmpeg`, lalu buka terminal baru), kalau tidak, penyambungan tiga segmen
>    gagal di langkah pertama — setelah semua rekaman selesai, yang paling menyakitkan.
>
> Screenshot punya batas yang sama; lihat `11_Screenshot_Capture_Runbook.md` §1.4a.

- [ ] Jendela WorkBuddy selebar **≥1600 px** — sama dengan syarat screenshot, jadi satu sesi
      menghasilkan dua jenis bukti sekaligus
- [ ] Rekaman pada **1920×1080, 30 fps**. Skrip penyambung menormalkan sendiri, tetapi sumber
      yang lebih tajam menghasilkan teks aturan yang terbaca
- [ ] Uji mikrofon 10 detik, putar ulang. Suara yang terlalu pelan tidak bisa diperbaiki
      setelah rekaman — `loudnorm` hanya meratakan, tidak menguatkan yang terekam buruk
- [ ] Tutup notifikasi. Satu pop-up di adegan penolakan merusak satu-satunya bukti terkuat
- [ ] Siapkan `12_Capture_Prompts.txt` di layar kedua

---

## Segmen A — 0:00–2:05 (125 s)

| Waktu | Adegan | Di layar | Yang diucapkan (kalimat pertama) |
|-------|--------|----------|----------------------------------|
| 0:00–0:35 | Kail | Kartu pembuka, lalu satu paket ajar utuh | "Guru IPAS menghabiskan enam sampai delapan jam untuk satu topik." |
| 0:35–1:10 | Masalah sebenarnya | Draf bertag, satu kalimat yang tag-nya menunjuk tempat salah | "Chatbot bisa menyusun ini dalam tiga puluh detik. Itu bukan bagian sulitnya." |
| 1:10–2:05 | Arsitektur | `architecture_diagram.png`, berhenti dua detik di kotak gerbang | "Empat agen, dua belas aturan, satu gerbang manusia." |

Tidak perlu agen berjalan. Bisa direkam kapan saja, termasuk sebelum sesi tangkap.

---

## Segmen B — 2:05–4:00 (115 s)

| Waktu | Adegan | Di layar | Catatan |
|-------|--------|----------|---------|
| 2:05–3:00 | Planner | `00_plan.md` run `-002`, bagian outline per format | Jalankan pipeline dengan prompt menu bab; tunjukkan pilihan format muncul |
| 3:00–4:00 | Writer | `01_artikel.md`, gulir pelan melewati tag `[src:]` | Berhenti di satu kalimat, tunjukkan tag-nya, lalu buka bagian sumber yang sama |

Segmen ini butuh satu run berjalan. Bisa digabung dengan sesi screenshot S1.

---

## Segmen C — 4:00–7:40 (220 s) — bagian yang wajib live

| Waktu | Adegan | Yang harus terlihat | Prompt |
|-------|--------|---------------------|--------|
| 4:00–5:00 | **Perhentian #1 — penolakan** | Vonis `REJECT`, ID aturan, kalimat yang dikutip. Tahan 3 detik penuh | `12_Capture_Prompts.txt` §2.1 (TC-08, R006) |
| 5:00–5:40 | **Perhentian #2 — eskalasi** | Penghitung iterasi di angka 3, pesan berhenti | §3.1 (TC-13) |
| 5:40–6:20 | **Perhentian #3 — gerbang** | `PENDING` / `TERTUTUP` setelah vonis `APPROVE` | §2.2 (TC-14) |
| 6:20–6:55 | Kegagalan yang disertakan | `04_Test_Results.md` §4, temuan F-01 | — |
| 6:55–7:15 | Refleksi + nama guru | Wajah atau layar kosong, narasi | **Sebut nama guru di sini** |
| 7:15–7:40 | Penutup | Kartu penutup | "Satu sumber masuk. Lima format keluar." |

**Satu sesi, dua keluaran.** Adegan 4:00–6:20 memakai run yang sama dengan screenshot
`TC-08_reject-R006.png`, `TC-13_escalation-3.png`, dan `S1-04_approval_pending.png`. Rekam
sekaligus saat mengambil screenshot — jangan menjalankan pipeline dua kali untuk hal yang sama.
Simpan rekaman mentahnya; kalau ada frame yang lebih bagus, ambil dari rekaman, bukan dari run baru.

**Nama guru.** Diputuskan 5 November 2026: **Don Jimat Akbar**. Sebut nama itu di adegan 6:55–7:15,
lalu lanjutkan ke kartu penutup. Segmen C tidak lagi tertunda — ketiga segmen bisa direkam hari ini.

---

## Menyambung

```bash
python3 06_Submission/video_kit/concat_video.py \
  --seg-a rekaman/seg_a.mp4 \
  --seg-b rekaman/seg_b.mp4 \
  --seg-c rekaman/seg_c.mp4 \
  --out 06_Submission/EduCraft_Demo.mp4
```

Yang dilakukan skrip, dan alasannya:

1. **Menormalkan tiap segmen** ke 1920×1080 / 30 fps / AAC 48 kHz. Rekaman dari alat berbeda punya
   parameter berbeda; menyambung tanpa menormalkan menghasilkan audio yang bergeser di sambungan.
2. **Membuat klip kartu** 5 detik tanpa suara dari dua PNG di folder ini.
3. **Menyambung** lalu meratakan suara dengan `loudnorm` (target −16 LUFS).
4. **Memeriksa durasi.** Di luar 5:00–8:00, skrip gagal dengan exit 1 — bukan peringatan yang bisa
   dilewati.

Sudah diuji 5 November 2026 dengan tiga klip uji: keluaran 1920×1080, 30 fps, audio 48 kHz,
−16,8 LUFS, dan penjaga durasi menolak hasil 34 detik sebagaimana mestinya.

**Terakhir:** tonton hasilnya sekali dari awal sampai akhir, dengan suara. Video yang tidak pernah
ditonton pembuatnya adalah video yang berhenti di menit kedua di laptop juri.
