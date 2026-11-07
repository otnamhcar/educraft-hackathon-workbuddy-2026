# Evaluasi Proyek EduCraft — 31 Oktober 2026

> **Sifat dokumen:** audit internal, bukan dokumen submission. Ditulis 7 hari sebelum deadline (7 Nov 2026).
> **Metode:** baca langsung seluruh dokumen inti, kontrak skill, audit log, dan penelusuran tag sitasi lintas file.
> **Kesimpulan satu baris:** substansi dan narasi sudah kelas finalis; yang rapuh ada di **bukti**, bukan di cerita.

---

## 1. Posisi Sekarang

| Dimensi | Kondisi | Bukti |
|---------|---------|-------|
| Kelengkapan submission | 7 READY · 2 PARTIAL · 2 TODO (dari 11) | `06_Submission/00_SUBMISSION_CHECKLIST.md` |
| Materi ajar | 2 run selesai; run 002 disetujui guru & dicetak | `03_Hasil/edu_output_wujud_zat/audit_log.md` §3.7 |
| Bukti uji | 7 PASS · 11 BY DESIGN · 2 TO RUN; critical 1/6 | `06_Submission/04_Test_Results.md` §1 |
| Screenshot | **0 file** — folder sesi masih kosong | `05_Bukti_Proses/evidence_bundle/03_screenshots/` |
| Demo video | belum ada; skrip 7:20 siap | `07_Demo_Video_Script.md` |
| Repo kode | belum ada | `00_SUBMISSION_CHECKLIST.md` §4 |
| ZIP bundel | **tidak ada di root** meski PROJECT.md mengklaim ada | `ls *.zip` → kosong |
| Ukuran proyek | 98 file · ±13 MB | `du -sh` per folder |

**Sisa waktu:** 7 hari. Tiga item yang tersisa (screenshot, video, repo) adalah tiga item yang paling berbobot di penilaian.

---

## 2. Temuan Kritis (dengan bukti)

### K1 — Rantai grounding run 002 putus: `[src:B4]` tidak menunjuk sumber fakta

Ini temuan paling serius, karena menyangkut materi yang **sudah disetujui guru dan dicetak**.

- Seluruh klaim fakta di `01_artikel.md`, `02_infographic_brief.md`, `03_video_storyboard.md`, `04_kuis_prepost.md`, dan infografis bertag `[src:B4]`.
- `[src:B4]` **tidak ada** di file sumber mana pun. Ia hanya muncul sebagai *nama topik* di `03_Hasil/referensi/cp_ipas.md` baris 27 dan 62:
  - baris 27: "Menyimpulkan proses perubahan wujud zat."
  - baris 62: "(4) Proses perubahan wujud zat"
- Artinya: `cp_ipas.md` — dokumen capaian pembelajaran — tidak memuat satu pun fakta tentang tiga wujud, enam arah perubahan, atau peran suhu. Kata "suhu" muncul **0 kali** di file itu (`grep -c "suhu"` → 0).
- Lebih jauh, `05_review.md` F1 menulis: *"Sumber hanya menyatakan 'perubahan wujud dapat disebabkan perubahan suhu'"* — kalimat itu **tidak ada** di sumber. Reviewer mengarang isi sumber untuk membenarkan vonisnya sendiri.
- Di `05_review.md` PASS 2, R001 diberi **PASS** dengan dasar *"seluruh klaim dapat dilacak ke `[src:B4]` atau `[src:CP]`"*. Yang diperiksa hanya **keberadaan tag**, bukan **resolusi tag**.

Ini persis kegagalan F-01/F-02 tanggal 29 Okt yang sudah didokumentasikan sebagai pelajaran — berulang, dan kali ini lolos ke materi cetak.

### K2 — Paket skill tidak dapat mereproduksi run yang diklaim

`05_Bukti_Proses/skills_package/` — yang di submission disebut "source code / exported workflow":

- Asset yang dikirim adalah `source_material_ipas.md` versi **karhutla** (`[src:1]`–`[src:8]`), bukan `source_material_energi.md` (`[src:1]`–`[src:9]`) yang dipakai run of record.
- `cp_ipas.md` dan `konteks_aktual.md` **tidak ada** di paket (`find` → 0 hasil), padahal `edu-orchestrator/SKILL.md` dan R011 mewajibkan keduanya.
- `[src:B4]` juga tidak ada di asset yang dikirim, jadi run 002 pun tidak bisa direproduksi.
- Empat `SKILL.md` masing-masing 28–40 baris dan hanya menyebut **3 format** (lesson plan, quiz, slide outline), sementara submission mengklaim **5 format + kuis interaktif**. Peran `edu-infographic`, `edu-video`, `edu-quiz` muncul di audit log tetapi **tidak punya SKILL.md**.

Konsekuensi: juri yang mengikuti instruksi `09_Source_Code_and_Evidence.md` §5 akan mendapat hasil berbeda dari yang diklaim.

### K3 — Submission berjangkar di run 001, padahal bukti terkuat ada di run 002

| | Run 001 (Energi) | Run 002 (Wujud Zat) |
|---|---|---|
| Siklus reject→remediate→approve | tidak terekam di audit log | **ada**, 5 temuan Major → APPROVE iterasi 2 |
| Approval manusia | PENDING | **nyata**, 30 Okt 17:19, nama guru |
| Artefak | 5 draf + HTML | 13 file termasuk 3 PDF cetak |
| Dipakai di submission | **ya** | hanya disebut di PROJECT.md §6A |

Akibatnya muncul dua kontradiksi yang bisa ditemukan juri:

1. `03_Accountability_Sheet.md` menyatakan **"NOT PUBLISHED"**, sedangkan audit log run 002 menyatakan **"publish status: TERBUKA untuk distribusi terbatas"** dan paket sudah dicetak.
2. `04_Test_Results.md` TC-20 diberi **PASS** dengan bukti "log memuat revisi v1→v2", padahal `audit_log_edu_orchestrator.md` §3.4 justru menulis *"Iterasi 1: APPROVE (tidak ada rejection)"*. Log tidak memuat rejection 29 Okt maupun v2.

### K4 — Rulebook belum benar-benar "domain-parameterised"

`02_Project_Description.md` §3.4 mengklaim: *"swap source_material_*.md, cp_*.md, rulebook_*.md dan agen yang sama menghasilkan materi untuk mapel lain"*. Yang terjadi sebaliknya:

- R005 mengunci `[src:7]` (upaya penanggulangan) dan `[src:8]` (peran siswa) — nomor tag khas sumber karhutla.
- R006 mengunci `[src:6]` (dampak kesehatan), R007 mengunci `[src:7]`–`[src:8]`.
- R003 mengunci "SD kelas 5–6", padahal cakupan proyek Fase B (III–IV) **dan** Fase C.
- Header rulebook menyatakan aturan advertising/halal "tidak relevan", padahal handbook §Challenge C menyebut reviewer wajib mengecek *factual accuracy, brand tone, advertising & halal*. Tidak ada aturan halal sama sekali.

---

## 3. Evaluasi per Dimensi

### 3.1 Arsitektur — **kuat secara konsep, lemah secara penegakan**

Yang benar dan layak dipamerkan:
- Pemisahan **veto (Reviewer) dari rewrite (Writer)** — argumen terbaik di seluruh proyek, dan alasannya jujur ("agen yang boleh menilai dan memperbaiki karyanya sendiri akan menilai dirinya murah hati").
- Empat batas kepercayaan (read-only assets, human authority, publish authority, source-as-data) — lebih matang daripada kebanyakan submission hackathon.
- Trade-off ditulis sebagai biaya, bukan sebagai kelebihan (`05_Architecture.md` §4). Ini yang membedakan dokumen engineering dari brosur.

Yang rapuh:
- **Guardrail-nya prosa, bukan mekanisme.** Counter iterasi "2/3" dicatat oleh model sendiri di audit log. Tidak ada file state yang menulis counter itu, jadi TC-13 (halt di iterasi 3) tidak bisa didemokan secara deterministik.
- **Tidak ada gerbang resolusi tag.** Ini gerbang yang justru dibutuhkan, dan ketiadaannya sudah terbukti menggigit dua kali (F-01, lalu K1).
- Peran generator (infografis/video/kuis) berada di luar kontrak → tidak ada aturan yang mengikat output visual.

### 3.2 Design — **paling matang di proyek ini**

- Infografis 1080×1350: hierarki jelas, enam panah terbaca, CTA di kaki, kredit sumber tercantum. Layak dipakai di kelas.
- Keputusan **memisahkan paket siswa (7 hlm, tanpa kunci) dari paket guru (4 hlm, dengan kunci)** adalah desain produk yang benar dan jarang terpikirkan tim hackathon.
- Lembar kerja pengamatan dengan tabel suhu **kosong** + verifikasi terprogram "0 pola angka+suhu" — ini bukti disiplin, bukan klaim.
- Kuis HTML single-file 16 KB, animatik 4:45.

Yang belum: animatik belum bersuara dan belum MP4; PDF dihasilkan lewat Chrome headless (rapuh bila di-render ulang di mesin lain).

### 3.3 Goal — **tajam, tapi ada satu penyimpangan rubrik**

Tujuan yang dipilih ("pain point-nya bukan menulis, tapi memeriksa") adalah positioning terkuat yang bisa diambil di Kategori C, dan seluruh artefak konsisten dengan itu. Kejujuran angka (7/11/2, bukan 20/20) adalah aset, bukan kelemahan — handbook menghukum penyembunyian lebih berat daripada kegagalan.

Penyimpangan yang perlu ditutup:
- Kategori C menuntut pemeriksaan **klaim advertising & halal**. Rulebook menyatakan itu tidak relevan. Bila juri menguji "klaim halal tanpa sertifikasi" atau "testimoni menyembuhkan", tidak ada aturan yang menangkapnya.
- Handbook menyebut setiap kategori punya **±20 test case resmi** dan dataset bersama. 20 TC di proyek ini **disusun sendiri**. Perlu dipastikan apakah test case resmi sudah dibagikan; bila ya, TC sendiri tidak menggantikannya.
- **Live surprise test 90 detik** di Demo Day belum disiapkan sama sekali — belum ada jalur cepat "brief masuk → putusan dalam 90 detik".

### 3.4 Workflow — **rapi untuk manusia, rapuh untuk mesin**

Kekuatan: satu run = satu folder = satu audit log; setiap serah-terima adalah file Markdown yang bisa dibuka juri. Ini "filesystem-as-state" yang jujur dan mudah diaudit.

Kelemahan: karena state ada di prosa, konsistensi bergantung pada disiplin penulisan. Buktinya sudah ada — audit log run 001 tidak pernah diperbarui setelah rejection 29 Okt, sehingga artefak yang dijadikan bukti TC-20 justru menyangkal TC-12.

---

## 4. Rencana 7 Hari (urut dampak skor)

| Hari | Tindakan | Alasan |
|------|----------|--------|
| 31 Okt | **Tutup K1 secara jujur**: buat `source_material_wujud_zat.md` berisi fakta bertag `[src:1..n]` dari sumber resmi; re-tag artefak digital; tulis memo koreksi untuk paket cetak yang sudah beredar | Materi sudah sampai ke murid; yang bisa diperbaiki adalah ketertelusuran, dan itu harus dinyatakan, bukan didiamkan |
| 31 Okt | Tambah **R012 — advertising/halal claim**; lepas kunci nomor tag di R005/R006/R007 (ganti jadi deskriptif: "bagian upaya penanggulangan", bukan `[src:7]`) | Menutup celah rubrik + membuat klaim "domain-parameterised" benar |
| 1 Nov | **Screenshot P0** (TC-08, 10, 14, 15, 18) sesuai runbook | Critical 1/6 → bila gagal, Responsible AI di-cap 5/10 |
| 2 Nov | Rekam **demo video** sesuai skrip | Item wajib yang belum ada |
| 3 Nov | Publikasikan **repo** (paket skill + asset lengkap: cp_ipas, konteks_aktual, source per topik) + LICENSE | Menutup K2 sekaligus |
| 4 Nov | **Tulis ulang `04_Test_Results.md`** berjangkar pada dua run; perbaiki audit log run 001 (tambahkan rejection 29 Okt + v2); selaraskan accountability sheet dengan status run 002 | Menutup K3 — kontradiksi internal adalah temuan termudah bagi juri |
| 5 Nov | Rebuild **ZIP** (memuat run 002), perbarui checklist yang sudah kedaluwarsa (ethics gate masih TODO padahal sudah disetujui 30 Okt) | Kebersihan bundel |
| 6 Nov | Latih **surprise test 90 detik** + rehearsal deck | Dimensi Demo & Storytelling |
| 7 Nov | Submit + screenshot halaman konfirmasi | — |

---

## 5. Perkiraan Posisi Rubrik (10 dimensi × 10)

| Dimensi | Estimasi | Alasan |
|---------|----------|--------|
| Impact & Relevance | 8 | Masalah guru nyata, ada bukti lapangan |
| Human-Centered Design | 8 | Pemisahan paket siswa/guru, bahasa tenang |
| AI Interaction (agentic) | 8 | 4 agen + loop, jelas bukan single-pass |
| Technical Execution | 5 | Guardrail prosa, paket tidak reproducible |
| Feasibility | 7 | Jalan tanpa infrastruktur berat |
| Demo & Storytelling | 5→8 | Skrip bagus, video belum ada |
| Innovation | 7 | "Tag ≠ sitasi" adalah insight asli |
| UX & Accessibility | 7 | Cetak + digital, tapi buta audio |
| Responsible AI & Ethics | 5→9 | **Ditentukan screenshot critical** |
| Overall Impression | 7 | Kejujuran menonjol |

Rentang realistis saat ini **±67**; dengan screenshot + video + repo + penutupan K1/K3, wajar bergerak ke **±80**.
