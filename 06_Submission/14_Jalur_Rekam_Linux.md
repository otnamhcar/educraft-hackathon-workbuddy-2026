# Jalur rekam di Linux — bisa, tetapi jangan untuk bukti yang sama

> **Pertanyaan:** kalau saya rekam di Linux saya, apakah bisa?
>
> **Jawaban:** bisa merekam, **tidak bisa** menghasilkan bukti yang sama. Yang Anda hasilkan adalah
> **run baru pada tanggal baru** — dan itu mengubah sifat videonya dari demonstrasi menjadi penciptaan
> ulang. Dokumen ini menjelaskan batasnya dan satu jalur yang jujur kalau Windows benar-benar macet.

---

## 1. Yang sudah diperiksa di mesin Linux, bukan diasumsikan

Diperiksa 7 November 2026, 18:05.

| Yang diperiksa | Hasil | Artinya |
|---|---|---|
| `workbuddy` di PATH | **ada** (`/usr/local/bin/workbuddy`) | agen bisa dijalankan |
| Skill `edu-*` | **4 terpasang** (`edu-orchestrator`, `-planner`, `-writer`, `-reviewer`) | pipeline lengkap |
| `08_Referensi/` | **7 berkas** (source, konteks, CP, rulebook, 3 sumber topik) | sumber fakta utuh |
| Run hasil sesi tangkap | **`-007` s.d. `-010` ada di `03_Hasil/`** | berkas hasilnya tersedia |
| `ffmpeg` | 4.4.2 | ada, tetapi berbeda versi dari 9.0.2 yang diuji |
| `$DISPLAY` | **kosong** — `xrandr` tidak mengembalikan apa pun | **tidak ada layar untuk direkam** |

Kesimpulan teknis: **pipeline bisa dijalankan di sini, layarnya tidak bisa direkam dari sesi ini.**
Rekaman harus dilakukan manual dari desktop Anda sendiri — dan itu membawa masalah di §2.

---

## 2. Kenapa "menjalankan lagi" bukan sekadar "merekam lagi"

Ini bagian yang menentukan, dan bukan soal alat.

Screenshot yang akan dikirim berasal dari run **6 November**: `EDU-CAP-20261106-01` sampai `-05` dan
`EDU-ORCH-20261106-005`, `-008`, `-009`, `-010`. Setiap run punya **run ID yang tercetak di layar**,
**timestamp**, dan **teks vonis yang dihasilkan pada saat itu**.

Kalau pipeline dijalankan ulang di Linux pada 7 November, yang muncul di layar adalah:

```
EDU-ORCH-20261107-xxx      ← tanggal berbeda
2026-11-07 xx:xx GMT+7     ← timestamp berbeda
```

Tiga akibatnya:

1. **Video memperlihatkan sesi yang tidak sama dengan bukti uji.** Juri yang membandingkan
   `TC-08_reject-R006.png` (run `-006`, 6 Nov) dengan video (run 7 Nov) akan menemukan dua run berbeda.
   Itu bukan penipuan — tetapi juga bukan bukti yang saling menguatkan. Yang seharusnya saling
   mengunci jadi saling menjauh.
2. **Teks vonis tidak dijamin identik.** Reviewer adalah model, bukan fungsi deterministik. Nomor
   aturan yang disebut dan kalimat yang dikutip bisa sama, bisa bergeser. Video dan screenshot lalu
   memuat dua kutipan berbeda untuk kasus yang sama.
3. **Jejaknya jadi bercabang.** `11_Screenshot_Capture_Runbook.md` §1.3 dan `CEK_MATA` §5 melarang
   memberi Run ID baru untuk foto ulang. Alasan yang sama berlaku untuk rekaman: run adalah bukti,
   bukan panggung.

> **Yang boleh dan tidak boleh.** Menjalankan pipeline lagi untuk **mencoba** sesuatu: boleh, dan sudah
> sering dilakukan (`-010` lahir begitu). Menjalankannya lagi lalu **menyebutnya bukti yang sama**:
> tidak boleh. Bedanya bukan pada perbuatan, tetapi pada klaim.

---

## 3. Kalau tetap merekam di Linux — yang harus dilakukan

Kalau Anda memutuskan jalan ini, tiga hal wajib, tanpa pengecualian:

1. **Rekam dari desktop Anda, bukan dari sesi agen ini.** Tidak ada `$DISPLAY`; `ffmpeg -f x11grab`
   akan gagal dengan `Cannot open display`. Alat yang tersedia di Linux Mint: `SimpleScreenRecorder`,
   `Kazam`, `OBS`, atau `ffmpeg x11grab` dari terminal desktop Anda.
2. **Rekam di resolusi asli panel Anda.** `concat_video.py` menormalkan ke 1366×768 saat menyambung.
   Jangan paksa 1366 di panel yang lebih lebar; jangan perkecil panel yang lebih sempit — teks tag
   harus terbaca saat dijeda.
3. **Sebutkan secara eksplisit di video dan di deskripsi** bahwa perhentian diperlihatkan dari run
   rekaman baru bertanggal 7 November, bukan dari run 6 November yang screenshot-nya disertakan.
   Satu kalimat: *"This walkthrough was captured on 7 November on a second machine; the screenshot
   evidence in the submission comes from the 6 November verification runs."* Tanpa kalimat itu,
   Anda mengklaim kesinambungan yang tidak ada.

**Tambahan konsekuensi:** berkas rekaman lalu lahir di Linux dan narasi di Windows (atau sebaliknya).
Itu memperbesar risiko di `CUE_SHEET.md`: dua mesin memotong video yang sama. Pilih satu mesin untuk
seluruh rantai potong → sambung → subtitle.

---

## 4. Jalur yang saya sarankan kalau Windows macet: V2

Ini bukan rekaman layar. Ini **gambar diam dari bukti yang sudah Anda punya**, dipadukan dengan narasi
yang sama. Sudah ada tingkatan resminya di `13_Demo_Video_Runbook.md` §8 — namanya **V2**.

| Yang dibutuhkan | Sudah ada? |
|---|---|
| Frame penolakan R006 | ✅ `S2_refusal_cycle/TC-08_reject-R006.png` |
| Frame eskalasi iterasi 3 | ✅ `S3_escalation/TC-13_escalation-3.png` |
| Frame gerbang `APPROVE` + `PENDING` | ✅ `S2_refusal_cycle/S2-02_approve.png` |
| Frame Planner | ✅ `S1_golden_path/S1-01_planner_outline.png` |
| Frame tag `[src:]` | ✅ `S1_golden_path/S1-02_writer_tags.png` |
| Narasi | ✅ `video_kit/NARASI_SKRIP_TAKE.md`, tiga take |

Yang hilang hanya **gerakan kursor**. Yang tetap ada: aturan yang disebut, kalimat yang dikutip,
penghitung iterasi, status `LOCKED`. Itu justru inti dari yang dinilai.

**Wajib:** setiap gambar diam diberi banner kecil di sudut — *"berkas hasil run · dirender"* atau
*"screenshot sesi EDU-CAP-20261106-02"*. Tanpa banner, ini bukan pengungkapan, ini penyamaran.
`tools/render_evidence.py` sudah menambahkan banner itu untuk `TC-21a`/`TC-21b`/`TC-13`/`TC-15` —
pola yang sama bisa dipakai untuk merender ulang frame yang lebih besar.

**Kapan V2 lebih buruk daripada menunggu Windows:** kalau teman Anda bisa merekam dalam 1–2 jam ke
depan. Rekaman asli selalu lebih kuat, dan Anda masih punya waktu satu malam.

---

## 5. Jawaban satu paragraf

Rekam di Linux **bisa secara teknis**, tetapi rekaman itu akan memperlihatkan run 7 November sementara
screenshot submission Anda dari 6 November — dua sesi berbeda untuk kasus yang sama. Itu harus
dinyatakan, dan setelah dinyatakan nilainya lebih rendah daripada rekaman asli. Kalau Windows bisa
dipakai malam ini, pakai Windows. Kalau tidak, jangan memaksakan rekaman baru: pakai **V2** dengan
screenshot yang sudah lolos cek mata plus narasi yang sama, dan beri banner pengungkapan. Yang tidak
boleh dilakukan sama sekali: merekam run baru lalu menyebutnya sesi 6 November.
