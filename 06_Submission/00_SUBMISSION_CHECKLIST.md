# Daftar Periksa Submission — Tencent Cloud Hackathon Indonesia 2026

**Proyek:** EduCraft · **Challenge:** C — The Creator Agent
**Tenggat:** 7 November 2026 — pesan panitia 27/10/2026 21:23, dikutip di
`01_Dokumen/BUKTI_KOMITE_2026-10-31.md` §2 · **Target submit internal: 5 November 2026** · **Disusun:** 30 Oktober 2026
**Formulir:** https://forms.gle/y1aHBH4BsrytXDxdA

Keterangan status: `SIAP` = artefaknya sudah ada di bundel ini · `BELUM` = harus dikerjakan tim · `TERBLOKIR` = menunggu pihak lain

---

## 1. Sebelas item wajib

| # | Item (handbook §7) | Sifat | Status | Berkas / tindakan |
|---|--------------------|-------|--------|-------------------|
| 1 | Judul proyek | WAJIB | **SIAP** | `01_Title_Blurb.md` |
| 2 | Blurb singkat, di bawah 10 kata | WAJIB | **SIAP** | `01_Title_Blurb.md` (8 kata, ID + EN) |
| 3 | Deskripsi proyek (4 bagian) | WAJIB | **SIAP** | `02_Project_Description.md` |
| 4 | Lembar akuntabilitas (satu halaman) | WAJIB | **SIAP** | `03_Accountability_Sheet.md` |
| 5 | Hasil pengujian **beserta screenshot** | WAJIB | **SEBAGIAN** | Tabelnya sudah ada di `04_Test_Results.md`; **screenshot masih BELUM** (§3 di bawah) |
| 6 | Diagram arsitektur | WAJIB | **SIAP** | `architecture_diagram.png` (2720×3000) + `.html` + `05_Architecture.md` |
| 7 | Video demo, 5–8 menit | WAJIB | **BELUM** | Skrip `07_Demo_Video_Script.md` (7:40) + runbook `13_Demo_Video_Runbook.md` + **kit siap pakai** di `video_kit/`: dua kartu judul, `concat_video.py` (normalkan ke **1366×768** bawaan, bisa ditimpa `--size`; sambung; `loudnorm`; jaga durasi), dan `CUE_SHEET.md` tiga segmen. Jalur sambung **sudah diuji** 6 Nov (5:10, ffmpeg 9.0.2). Yang kurang hanya rekaman layar dan narasi |
| 8 | Product sharing | WAJIB | **SIAP** | `06_Product_Sharing.md` |
| 9 | Kode sumber / workflow yang diekspor | WAJIB | **SIAP** | Repo publik (MIT): https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026 — 4 run, 4 skill, doctor.py 11/11 |
| 10 | Gambar sampul (opsional, 16:9) | OPSIONAL | **SIAP** | `cover_image_380x216.png` + `cover_image_1280x720.png` |
| 11 | Tautan proyek (bonus) | BONUS | **DRAF LOKAL** | Halaman statis siap di `06_Submission/demo_site/` (lihat `README.md` di sana). **Belum diunggah, belum ada URL publik.** Jangan tulis tautan apa pun di formulir sebelum benar-benar hidup |

**Skor: 8 siap · 1 sebagian · 1 draf lokal · 1 belum.** Sisa yang masih "sebagian" adalah bukti pengujian —
bagian yang paling berat dinilai juri — jadi jangan submit hanya dengan alasan jumlah dokumen sudah banyak.
"Draf lokal" berarti berkasnya ada dan bisa diperiksa, tetapi belum punya URL, jadi belum bisa ditempel
ke formulir.

---

## 2. Siap tempel

`10_Submission_Form_CopyPaste.txt` — blok teks polos untuk setiap isian formulir, berurutan.
Buka berkas itu di samping formulir, lalu tempel bagian per bagian. Jangan diformat ulang.

---

## 3. Screenshot — apa yang harus diambil (P0 lebih dulu)

> **Cara mengambilnya:** ikuti `11_Screenshot_Capture_Runbook.md` — 4 sesi run, ± 2 jam 45 menit,
> dengan prompt siap-tempel di `12_Capture_Prompts.txt`. Jangan menjalankan pipeline 20 kali;
> satu sesi menghasilkan beberapa screenshot sekaligus.
> **Daftar berkas di bawah ini disalin dari `INDEX.md`**, bukan disusun ulang di sini. Kalau keduanya
> berbeda, `INDEX.md` yang benar — `tools/check_capture.py` membaca berkas itu, bukan halaman ini.

**Tiga hal yang membuat capture gagal walau gambarnya sudah diambil:**

1. **Simpan di subfolder yang tertulis**, bukan di akar `03_screenshots/`: `S1_golden_path/`,
   `S2_refusal_cycle/`, `S3_escalation/`, `S4_extras/`. Berkas di akar dianggap "stray", dan
   kebutuhan wajibnya tetap dihitung kosong.
2. **Lebar minimal 1366 px.** Itu lebar panel mesin ini (runbook §1.4a, keputusan 6 Nov 2026);
   jendela yang diperkecil ditolak checker.
3. **ID aturan dan kalimat yang dikutip terbaca pada zoom 100%** di laptop 1080p. Kalau juri harus
   menyipitkan mata, screenshot itu tidak dihitung.

Verifikasi: `python tools\check_capture.py` (Windows) atau `python3 tools/check_capture.py`
(Linux/macOS) → exit 0 berarti ke-12 berkas wajib sudah ada dan sah.
**Lembar kerja satu halaman untuk enam berkas yang tersisa: `14_Lembar_Sesi_Tangkap.md`.**

### Wajib — 12 berkas, tanpa ini item 5 tetap "sebagian"

| Kasus | Berkas (relatif ke `03_screenshots/`) | Yang wajib terlihat di frame |
|-------|----------------------------------------|------------------------------|
| TC-01 | `S1_golden_path/S1-02_writer_tags.png` | Draf Writer dengan tag `[src:#]` |
| — | `S1_golden_path/S1-01_planner_outline.png` | Outline Planner dari menu bab |
| TC-08 + TC-09 | `S2_refusal_cycle/TC-08_reject-R006.png` | Vonis `REJECT`, aturan `R006`, kalimat yang dikutip |
| TC-10 | `S2_refusal_cycle/TC-10_reject-R007.png` | Penolakan instruksi membakar, aturan yang dirujuk |
| TC-12 | `S2_refusal_cycle/S2-01_remediate.png` | Draf v2 setelah remediasi |
| TC-12 | `S2_refusal_cycle/S2-02_approve.png` | Vonis `APPROVE` atas v2 |
| TC-14 | `S1_golden_path/S1-04_approval_pending.png` | `publish_status: PENDING` setelah vonis `APPROVE` |
| TC-13 | `S3_escalation/TC-13_escalation-3.png` | Penghitung iterasi di angka 3, pesan berhenti |
| TC-15 | `S3_escalation/TC-15_injection-ignored.png` | Instruksi sisipan diabaikan + pengguna diberi tahu |
| TC-18 | `S4_extras/TC-18_image_text.png` | Validasi teks pada gambar hasil generate |
| TC-21 | `S2_refusal_cycle/TC-21a_reject-R012.png` | `REJECT` yang menyebut R012 dan ketiga sub-klausulnya (klaim khasiat, halal tanpa sertifikat, superlatif) |
| TC-21 | `S2_refusal_cycle/TC-21b_rules_na-R012.png` | `rules_na: R012` **disertai alasan** pada materi bersih |

### Opsional — 11 berkas, ambil kalau waktunya ada

`S1_golden_path/S1-03_reviewer_verdict.png` (TC-11), `S1_golden_path/S1-05_audit_log.png` (TC-20),
`S1_golden_path/S1-06_quiz_feedback.png` (TC-16), `S3_escalation/TC-02_unverified.png`,
`S3_escalation/TC-03_out_of_scope.png`, `S4_extras/TC-04_reject-R002.png` (TC-04 + TC-05),
`S4_extras/TC-06_reject-R003.png`, `S2_refusal_cycle/TC-12a_v1_reject.png`,
`S2_refusal_cycle/TC-12b_v2_approve.png`, `S4_extras/TC-17_bilingual.png`,
`S2_refusal_cycle/TC-19_citation.png`.

**TC-07 tidak punya slot screenshot** di `INDEX.md` — kasus itu tidak bisa dibuktikan lewat gambar.
Kalau ingin ditutup, tambahkan barisnya ke `INDEX.md` lebih dulu, baru difoto.

---

## 4. Publikasi kode — ✅ SELESAI (Opsi A)

**Repo GitHub publik:** https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026
Lisensi MIT · 170 berkas ter-track · di-push pertama 31 Oktober 2026, diperbarui 5 November 2026.

Sengaja tidak ada hash commit di sini. Hash yang ditulis di dalam berkas yang ikut berubah akan
selalu kedaluwarsa begitu berkas itu di-commit — itu sudah terjadi dua kali. Untuk memeriksa versi yang
sedang Anda baca: `git log -1 --format='%h %ad' --date=short`.

Isi yang dipublikasikan: `README.md` (halaman depan, termasuk jalur **"Jalankan sendiri"** yang
ditulis untuk guru, bukan untuk pengembang), `05_Bukti_Proses/skills_package/` (empat kontrak +
aset pengetahuan lengkap), `03_Hasil/` (empat run, dua laporan review), `06_Submission/`,
`04_Diskusi/test_cases_matrix.md`, `tools/` (cek grounding, `install_skills.py`, `doctor.py` — semuanya Python, semuanya lintas OS),
`LICENSE`, `THIRD_PARTY_NOTICES.md`.

**Juga dipublikasikan: dua PDF resmi dari kementerian** yang menjadi fondasi lapisan pengetahuan —
*Panduan Mata Pelajaran IPAS* (Revisi 4) dan *Permendikdasmen 13/2025* — beserta hasil ekstraksi teksnya, di
`02_Sumber/`. Alasannya: cek grounding hanya bisa diverifikasi kalau pembaca dapat membuka halaman
asal sebuah klaim. Keduanya berada di luar lisensi MIT dan dikecualikan secara eksplisit di `THIRD_PARTY_NOTICES.md`.

Sengaja **tidak** dipublikasikan, dengan alasan per berkas di `02_Sumber/README.md`: enam
lembar RPP dari `centralpendidikan.com`, panduan asesmen SMP, ekspor WhatsApp, handbook panitia,
`.workbuddy-ai/`, dan catatan kerja. Ditegakkan oleh `.gitignore` di akar repo.

**Terverifikasi 31 Oktober 2026, diperbarui 5 November 2026:** `git clone` baru dari `main` berhasil
memasang keempat skill dan lolos `tools/doctor.py` — exit 0. Keluaran sekarang **13 passed / 0 failed /
4 warning**. Keempat peringatan itu bukan kegagalan: semuanya `SKIP` dari `tools/check_sitasi.py` untuk
run yang dibuat sebelum konvensi sitasi kelas berlaku — run `-003` sendiri **PASS** (7 pemeriksaan).
Doctor kini memeriksa **lima folder** untuk empat run (121 + 121 + 115 + 212 + 109 = 678 tag,
0 pelanggaran; run `-001` muncul di dua folder sehingga dihitung sekali pada angka per run, yaitu
**557 tag**) dan tiga source material yang identik lintas skill package. Sejak 5 November 2026
`03_Hasil/edu_output` ikut diperiksa — folder itu sebelumnya memuat draf dengan tag kurikulum untuk
fakta (73 pelanggaran kelas) dan kini lulus dengan 121 tag, sama dengan `materi_ajar`.

Sisa pekerjaan rumah: jalankan push lagi setelah setiap penyuntingan, supaya repo dan bundel tetap sama.

---

## 5. Gerbang etik (jangan dilewati)

| Pemeriksaan | Status |
|-------------|--------|
| Run `-002` ditinjau dan disetujui guru | **TERPENUHI untuk `-002`** — penyetuju disebut namanya, berstempel waktu 30 Okt 2026 17:19 GMT+7, cakupan tercatat di `03_Hasil/edu_output_wujud_zat/00_run_config.md` |
| Run `-001` ditinjau guru | **TERPENUHI** — disetujui 4 November 2026 pukul 14:49 GMT+7, tercatat di `03_Hasil/edu_output/00_run_config.md` dan `audit_log.md` §3.7 |
| Run `-003` ditinjau guru | **TERPENUHI** — disetujui 5 November 2026 pukul 15:01 GMT+7; cakupan dan butir yang disetujui tercatat di `03_Hasil/edu_output_tata_surya/04_Lembar_Persetujuan_Guru.md` |
| Run `-004` ditinjau guru | **TERPENUHI** — disetujui 5 November 2026 pukul 16:13 GMT+7, **ditambah 6 November 2026 pukul 09:08** (validasi `[src:W11]` dan rubrik penilaian); delapan keputusan tercatat di `03_Hasil/edu_output_wujud_zat_faseC/08_Lembar_Persetujuan_Guru.md` (run ini bernomor `-003` sampai 5 Nov, lalu pindah ke `-004`) |
| Catatan persetujuan memuat keempat bagian protokol | **TERPENUHI untuk keempat run** — nama ✓, waktu ✓, cakupan ✓ (untuk `-002` termasuk kunci jawaban 27 butir; untuk `-004` termasuk status entri turunan dan sumber tambahan), pernyataan verbatim ✓ ("ok saya setujui" untuk `-001`/`-002`, "ok setuju semua" untuk `-004`). Sumber kutipan: `audit_log.md` §3.7 run `-002`, bukan dokumen bertanda tangan. G16 ditutup 5 November 2026 |
| Tidak ada yang disebut "terbit" atau "live" di submission | **TERPENUHI** — gerbang keempat run dibuka *hanya untuk pemakaian di kelas dan distribusi terbatas ke guru*; publikasi tetap `LOCKED` di keempatnya. Tidak ada yang disebut terbit ke publik |
| Data siswa dianonimkan | **TERPENUHI** |
| Data mock dinyatakan sebagai mock | **TERPENUHI** — dinyatakan di `09_Source_Code_and_Evidence.md` §5 |

Handbook membatasi nilai Responsible AI & Ethics maksimal 5/10 bila agen menerbitkan tanpa persetujuan.
Submission saat ini tidak mengklaim penerbitan apa pun — pertahankan begitu sampai ada manusia yang menandatangani.

---

## 6. Pra-terbang (30 menit sebelum submit)

- [ ] Kesebelas item sudah ditempel; blurb dihitung ulang dan masih di bawah 10 kata
- [ ] PNG arsitektur terbuka dalam ukuran penuh dan terbaca
- [ ] Gambar sampul 16:9, versi 380×216 tersedia
- [ ] Video berjalan dari awal sampai akhir; durasi 5:00–8:00; audio jelas
- [ ] Video menampilkan minimal satu penolakan **atau** satu penantian persetujuan (kita menampilkan tiga)
- [ ] Setiap tautan berkas di formulir bisa dibuka oleh orang di luar tim
- [ ] Tidak ada path berkas yang memuat huruf drive lokal (juri tidak bisa membuka `D:/...`)
- [ ] Laporan penolakan disertakan, tidak diam-diam dihapus
- [ ] **Guru yang namanya disebut sudah setuju namanya dicantumkan** — Don Jimat Akbar muncul di repo,
      deskripsi, lembar akuntabilitas, dan video. Konfirmasikan secara tertulis sebelum submit
- [ ] Video memuat refleksi pendekatan pembangunan dan menyebut nama guru (handbook §7 mewajibkan)
- [ ] Nama tim dan kontak di kartu penutup cocok dengan data pendaftaran
- [ ] Submit, lalu screenshot halaman konfirmasinya

---

## 7. Peta berkas bundel ini

```
06_Submission/
├── 00_SUBMISSION_CHECKLIST.md        <- berkas ini
├── 01_Title_Blurb.md                 <- item 1-2
├── 02_Project_Description.md         <- item 3
├── 03_Accountability_Sheet.md        <- item 4
├── 04_Test_Results.md                <- item 5 (tabel)
├── 05_Architecture.md                <- item 6 (teks)
├── architecture_diagram.html         <- item 6 (interaktif)
├── architecture_diagram.png          <- item 6 (unggah yang ini)
├── 06_Product_Sharing.md             <- item 8
├── 07_Demo_Video_Script.md           <- item 7 (skrip)
├── 09_Source_Code_and_Evidence.md    <- item 9
├── 10_Submission_Form_CopyPaste.txt  <- teks formulir siap tempel
├── 11_Screenshot_Capture_Runbook.md  <- cara mengambil bukti screenshot
├── 12_Capture_Prompts.txt            <- prompt siap tempel untuk sesi tangkap
├── 13_Demo_Video_Runbook.md          <- cara memproduksi video
├── 14_Lembar_Sesi_Tangkap.md         <- lembar kerja: 6 berkas sisa, dua blok sesi
├── video_kit/                        <- item 7 (kartu judul, concat_video.py, CUE_SHEET.md)
├── panduan/                          <- runbook Demo Day + panduan testimoni guru (pindah dari 03_Hasil/panduan 5 Nov 2026)
├── cover_image.svg                   <- item 10 (sumber)
├── cover_image_1280x720.png          <- item 10 (deck/media sosial)
└── cover_image_380x216.png           <- item 10 (unggah ke formulir)
```
