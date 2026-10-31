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
| 7 | Video demo, 5–8 menit | WAJIB | **BELUM** | Skrip `07_Demo_Video_Script.md` (7:40) + runbook produksi `13_Demo_Video_Runbook.md`. 7 dari 10 scene sudah bisa direkam sekarang; 3 butuh agen berjalan langsung |
| 8 | Product sharing | WAJIB | **SIAP** | `06_Product_Sharing.md` |
| 9 | Kode sumber / workflow yang diekspor | WAJIB | **SIAP** | Repo publik (MIT): https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026 — 119 berkas ter-track |
| 10 | Gambar sampul (opsional, 16:9) | OPSIONAL | **SIAP** | `cover_image_380x216.png` + `cover_image_1280x720.png` |
| 11 | Tautan proyek (bonus) | BONUS | **BELUM** | URL demo langsung, sifatnya opsional |

**Skor: 8 siap · 1 sebagian · 2 belum.** Sisa yang masih "sebagian" adalah bukti pengujian —
bagian yang paling berat dinilai juri — jadi jangan submit hanya dengan alasan jumlah dokumen sudah banyak.

---

## 2. Siap tempel

`10_Submission_Form_CopyPaste.txt` — blok teks polos untuk setiap isian formulir, berurutan.
Buka berkas itu di samping formulir, lalu tempel bagian per bagian. Jangan diformat ulang.

---

## 3. Screenshot — apa yang harus diambil (P0 lebih dulu)

> **Cara mengambilnya:** ikuti `11_Screenshot_Capture_Runbook.md` — 4 sesi run, ± 2 jam 45 menit,
> dengan prompt siap-tempel di `12_Capture_Prompts.txt`. Jangan menjalankan pipeline 20 kali;
> satu sesi menghasilkan beberapa screenshot sekaligus.
> Pelacak hasil: `05_Bukti_Proses/evidence_bundle/03_screenshots/INDEX.md`.

Simpan ke `05_Bukti_Proses/evidence_bundle/03_screenshots/`, dengan nama seperti tertulis.

| Prioritas | Kasus | Nama berkas | Yang wajib terlihat di frame |
|-----------|-------|-------------|------------------------------|
| P0 | TC-08 | `TC-08_reject-R006.png` | Vonis `REJECT`, aturan `R006`, kalimat yang dikutip |
| P0 | TC-10 | `TC-10_reject-R007.png` | Penolakan menulis instruksi membakar, aturan yang dirujuk |
| P0 | TC-14 | `TC-14_approval-gate.png` | `publish_status: PENDING` setelah vonis APPROVE |
| P0 | TC-15 | `TC-15_injection-ignored.png` | Instruksi sisipan diabaikan + pengguna diberi tahu |
| P0 | TC-18 | `TC-18_image-text-check.png` | Validasi teks pada gambar hasil generate |
| P1 | TC-02 | `TC-02_unverified-token.png` | `[UNVERIFIED]` muncul, bukan tebakan |
| P1 | TC-12 | `TC-12_loop-v1-v2.png` | v1 ditolak → v2 disetujui, dalam satu layar |
| P1 | TC-13 | `TC-13_escalation-3.png` | Penghitung iterasi di angka 3, pesan berhenti |
| P1 | TC-21 | `TC-21a_reject-R012.png`, `TC-21b_rules_na-R012.png` | `REJECT` yang menyebut R012 dan ketiga sub-klausulnya (klaim khasiat, halal tanpa sertifikat, superlatif); lalu `rules_na: R012` **disertai alasan** pada materi bersih |
| P2 | TC-06, TC-09, TC-11, TC-17 | — | Sesuai kesempatan |

**Aturan untuk semua screenshot:** ID aturan dan teks yang dikutip harus sama-sama terbaca pada
zoom 100% di laptop 1080p. Kalau juri harus menyipitkan mata, screenshot itu tidak dihitung.

---

## 4. Publikasi kode — ✅ SELESAI (Opsi A)

**Repo GitHub publik:** https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026
Lisensi MIT · 119 berkas ter-track · di-push 31 Oktober 2026.

Sengaja tidak ada hash commit di sini. Hash yang ditulis di dalam berkas yang ikut berubah akan
selalu basi begitu berkas itu di-commit — itu sudah terjadi dua kali. Untuk memeriksa versi yang
sedang Anda baca: `git log -1 --format='%h %ad' --date=short`.

Isi yang dipublikasikan: `README.md` (halaman depan, termasuk jalur **"Jalankan sendiri"** yang
ditulis untuk guru, bukan untuk pengembang), `05_Bukti_Proses/skills_package/` (empat kontrak +
aset pengetahuan lengkap), `03_Hasil/` (dua run, dua laporan review), `06_Submission/`,
`04_Diskusi/test_cases_matrix.md`, `tools/` (cek grounding, `install_skills.py`, `doctor.py` — semuanya Python, semuanya lintas OS),
`LICENSE`, `THIRD_PARTY_NOTICES.md`.

**Juga dipublikasikan: dua PDF resmi dari kementerian** yang menjadi fondasi lapisan pengetahuan —
*Panduan Mata Pelajaran IPAS* (Revisi 4) dan *Permendikdasmen 13/2025* — beserta hasil ekstraksi teksnya, di
`02_Sumber/`. Alasannya: cek grounding hanya bisa diverifikasi kalau pembaca dapat membuka halaman
asal sebuah klaim. Keduanya berada di luar lisensi MIT dan dikecualikan secara eksplisit di `THIRD_PARTY_NOTICES.md`.

Sengaja **tidak** dipublikasikan, dengan alasan per berkas di `02_Sumber/README.md`: enam
lembar RPP dari `centralpendidikan.com`, panduan asesmen SMP, ekspor WhatsApp, handbook panitia,
`.workbuddy-ai/`, dan catatan kerja. Ditegakkan oleh `.gitignore` di akar repo.

**Terverifikasi 31 Oktober 2026:** `git clone` baru dari `main` berhasil memasang keempat skill dan
lolos `tools/doctor.py` — `8 passed / 0 failed / 0 warning`, exit 0.

Sisa pekerjaan rumah: jalankan push lagi setelah setiap penyuntingan, supaya repo dan bundel tetap sama.

---

## 5. Gerbang etik (jangan dilewati)

| Pemeriksaan | Status |
|-------------|--------|
| Run `-002` ditinjau dan disetujui guru | **TERPENUHI untuk `-002`** — penyetuju disebut namanya, berstempel waktu 30 Okt 2026 17:19 GMT+7, cakupan tercatat di `03_Hasil/edu_output_wujud_zat/00_run_config.md` |
| Run `-001` ditinjau guru | **BELUM** — masih `PENDING`; di bundel ini run tersebut tidak pernah disebut sebagai disetujui |
| Catatan persetujuan memuat keempat bagian protokol | **SEBAGIAN untuk `-002`** — nama orang ✓, stempel waktu ✓, cakupan ✓, **pernyataan verbatim ✗**. Pilih salah satu: kutip kalimat persis dari penyetuju ke dalam run config, atau nyatakan di submission bahwa catatan itu memuat tiga dari empat bagian |
| Tidak ada yang disebut "terbit" atau "live" di submission | **TERPENUHI** — gerbang `-002` dibuka *hanya untuk distribusi terbatas*; `-001` berstatus `PENDING` |
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
- [ ] **Guru yang namanya disebut sudah setuju namanya dicantumkan** — Pak Arief muncul di repo,
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
├── cover_image.svg                   <- item 10 (sumber)
├── cover_image_1280x720.png          <- item 10 (deck/media sosial)
└── cover_image_380x216.png           <- item 10 (unggah ke formulir)
```
