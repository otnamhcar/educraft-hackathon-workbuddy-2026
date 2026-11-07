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
| 5 | Hasil pengujian **beserta screenshot** | WAJIB | **SIAP** | Tabel di `04_Test_Results.md` (15 PASS / 6 BY DESIGN / 1 BELUM / 1 TO RUN) + 12 berkas wajib di `03_screenshots/`, semuanya sudah diperiksa mata (`CEK_MATA_2026-11-06.md`). Satu kasus diungkap `BELUM`: TC-07 |
| 6 | Diagram arsitektur | WAJIB | **SIAP** | `architecture_diagram.png` (2720×3000) + `.html` + `05_Architecture.md` |
| 7 | Video demo, 5–8 menit | WAJIB | **BAHAN LENGKAP, FINALISASI DI LUAR REPO** | Skrip `07_Demo_Video_Script.md` (7:55) + naskah narasi siap baca `video_kit/NARASI_SKRIP_TAKE.md` + runbook `13_Demo_Video_Runbook.md` + **kit siap pakai** di `video_kit/`. Rekaman mentah sudah ada lima berkas (sesi 1, 2, 2b, 3a, 3b; 117 MB) dan **disimpan di drive bersama, tidak di dalam repo** — diunggah terpisah oleh guru. Yang belum: penyambungan final + narasi |
| 8 | Product sharing | WAJIB | **SIAP** | `06_Product_Sharing.md` |
| 9 | Kode sumber / workflow yang diekspor | WAJIB | **SIAP** | Repo publik (MIT): https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026 — 11 run, 4 skill, `doctor.py` **19 passed / 0 failed / 0 warning** |
| 10 | Gambar sampul (opsional, 16:9) | OPSIONAL | **SIAP** | `cover_image_380x216.png` + `cover_image_1280x720.png` |
| 11 | Tautan proyek (bonus) | BONUS | **DRAF LOKAL** | Halaman statis siap di `06_Submission/demo_site/` (lihat `README.md` di sana). **Belum diunggah, belum ada URL publik.** Jangan tulis tautan apa pun di formulir sebelum benar-benar hidup |

**Skor: 9 siap · 1 finalisasi di luar repo · 1 draf lokal.** Satu-satunya item wajib yang belum
tertutup adalah video demo: bahannya lengkap (lima rekaman mentah + kartu judul + alat penyambung yang
sudah teruji), tetapi rekaman final masih harus disambung dan dinarasikan sebelum diunggah. Artefak
finalnya **tidak bisa** dilengkapi dari repo ini — rekaman ada di drive bersama, penyambungan dan narasi
dikerjakan di mesin Windows. Jangan submit hanya dengan alasan jumlah dokumen sudah banyak — video
adalah item wajib.
"Draf lokal" (item 11, bonus) berarti berkasnya ada dan bisa diperiksa, tetapi belum punya URL, jadi
belum bisa ditempel ke formulir.

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
| TC-13 | `S3_escalation/TC-13_escalation-3.png` | Penghitung iterasi di angka 3 (`Iteration 3` / `MaxIter 3`), `Status: ESCALATED_TO_HUMAN`, `Publish: LOCKED`. **Berkas ini render**, bukan tangkapan UI — lihat `INDEX.md` §A |
| TC-15 | `S3_escalation/TC-15_injection-ignored.png` | Kalimat injeksi verbatim + "ditolak" + "tidak dijalankan" + arsip verbatim di `00_source_asal_verbatim.md` |
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

**TC-07 tidak punya slot screenshot** di `INDEX.md` — kasus itu **belum pernah dieksekusi**, jadi
tidak ada gambar yang bisa diambil. Statusnya `BELUM` dan diungkap di `04_Test_Results.md` §4d.
Kalau ingin ditutup: jalankan brief berisi deskripsi korban grafis, tangkap vonis `REJECT R003`,
baru tambahkan barisnya ke `INDEX.md`. Itu sesi baru, bukan foto ulang.

**Status 6 November 2026:** seluruh 12 berkas wajib ada di disk dan isinya sudah diperiksa mata
(`03_screenshots/CEK_MATA_2026-11-06.md`). Tidak ada sisa pengambilan ulang.

---

## 4. Publikasi kode — ✅ SELESAI (Opsi A)

**Repo GitHub publik:** https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026
Lisensi MIT · 267 berkas ter-track · di-push pertama 31 Oktober 2026, diperbarui 7 November 2026.

Sengaja tidak ada hash commit di sini. Hash yang ditulis di dalam berkas yang ikut berubah akan
selalu kedaluwarsa begitu berkas itu di-commit — itu sudah terjadi dua kali. Untuk memeriksa versi yang
sedang Anda baca: `git log -1 --format='%h %ad' --date=short`.

Isi yang dipublikasikan: `README.md` (halaman depan, termasuk jalur **"Jalankan sendiri"** yang
ditulis untuk guru, bukan untuk pengembang), `05_Bukti_Proses/skills_package/` (empat kontrak +
aset pengetahuan lengkap), `03_Hasil/` (sebelas folder run, laporan review di tiap folder), `06_Submission/`,
`04_Diskusi/test_cases_matrix.md`, `tools/` (cek grounding, `install_skills.py`, `doctor.py` — semuanya Python, semuanya lintas OS),
`LICENSE`, `THIRD_PARTY_NOTICES.md`.

**Juga dipublikasikan: dua PDF resmi dari kementerian** yang menjadi fondasi lapisan pengetahuan —
*Panduan Mata Pelajaran IPAS* (Revisi 4) dan *Permendikdasmen 13/2025* — beserta hasil ekstraksi teksnya, di
`02_Sumber/`. Alasannya: cek grounding hanya bisa diverifikasi kalau pembaca dapat membuka halaman
asal sebuah klaim. Keduanya berada di luar lisensi MIT dan dikecualikan secara eksplisit di `THIRD_PARTY_NOTICES.md`.

Sengaja **tidak** dipublikasikan, dengan alasan per berkas di `02_Sumber/README.md`: enam
lembar RPP dari `centralpendidikan.com`, panduan asesmen SMP, ekspor WhatsApp, handbook panitia,
`.workbuddy-ai/`, dan catatan kerja. Ditegakkan oleh `.gitignore` di akar repo.

**Terverifikasi 31 Oktober 2026, diperbarui 7 November 2026:** `git clone` baru dari `main` berhasil
memasang keempat skill dan lolos `tools/doctor.py` — exit 0. Keluaran sekarang **19 passed / 0 failed /
0 warning** (diukur 7 November 2026). Doctor memeriksa **sebelas folder** untuk sepuluh run
(121 + 121 + 115 + 212 + 109 + 269 + 134 + 199 + 44 + 22 + 271 = 1.617 tag, 0 pelanggaran; run `-001`
muncul di dua folder sehingga dihitung sekali pada angka per run, yaitu **1.496 tag**) dan tiga source
material yang identik lintas skill package. Pemeriksaan sitasi kelas hanya dijalankan pada run yang
memang memakai konvensi itu — `03_Hasil/edu_output_tata_surya` (`-003`) — dan **PASS** dengan 7
pemeriksaan; run lain tidak didaftarkan karena masih memakai tag sebaris, sehingga tidak ada `SKIP`
yang dihitung sebagai warning. Sejak 5 November 2026 `03_Hasil/edu_output` ikut diperiksa — folder itu
sebelumnya memuat draf dengan tag kurikulum untuk fakta (73 pelanggaran kelas) dan kini lulus dengan
121 tag, sama dengan `materi_ajar`.

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
- [ ] **Nama guru adalah nama samaran yang disepakati** — "Don Jimat Akbar" adalah nama anonim untuk
      guru IPAS SD yang berperan dalam demo, bukan identitas asli. Dicantumkan konsisten di repo,
      deskripsi, lembar akuntabilitas, dan video. Jangan menggantinya dengan nama asli di menit terakhir:
      satu penggantian mengharuskan 10+ berkas disunting ulang dan repo di-push ulang
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
├── 14_Lembar_Sesi_Tangkap.md         <- lembar kerja sesi tangkap (0 berkas sisa per 6 Nov)
├── video_kit/                        <- item 7 (kartu judul, concat_video.py, CUE_SHEET.md)
├── panduan/                          <- runbook Demo Day + panduan testimoni guru (pindah dari 03_Hasil/panduan 5 Nov 2026)
├── cover_image.svg                   <- item 10 (sumber)
├── cover_image_1280x720.png          <- item 10 (deck/media sosial)
└── cover_image_380x216.png           <- item 10 (unggah ke formulir)
```

**Rekaman video tidak ada di repo.** Lima berkas rekaman mentah (117 MB) disimpan dan diunggah
terpisah ke drive bersama; repo ini hanya memuat skrip, runbook, dan kit penyambungnya. Alasannya
ukuran — menggelembungkan repo yang di-clone juri tanpa manfaat, karena video dinilai dari tautan,
bukan dari isi git.
