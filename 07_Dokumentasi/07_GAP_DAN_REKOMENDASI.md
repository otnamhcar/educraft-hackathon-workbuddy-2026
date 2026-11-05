# 07 — Daftar celah dan rekomendasi

> Diurutkan berdasarkan **dampak skor per jam**, bukan berdasarkan kerapian. Setiap butir menyebut
> celahnya, bukti bahwa celah itu nyata, definisi selesai, dan apa yang terbuka karenanya.
> Tidak ada dugaan tentang apa yang diinginkan juri: setiap butir memetakan ke persyaratan atau
> dimensi yang dikutip di `06_TRACEABILITY.md`.

---

## P0 — memblokir submission atau membatasi skor

| ID | Celah | Bukti bahwa nyata | Definisi selesai | Yang terbuka |
|----|-------|-------------------|------------------|--------------|
| ~~**G1**~~ | ~~Run `-002` menempatkan 84 dari 89 tag pada entri kurikulum~~ | **DITUTUP 31 Okt** — `03_Hasil/edu_output_wujud_zat/grounding_report.md`: 115 tag, 0 dangling, 0 pelanggaran | Selesai. Isi tidak berubah; `[src:W10]`/`[src:W11]` berasal dari tim dan menunggu validasi guru (`11_Memo_Koreksi_Tag_2026-10-31.md`) | Kejujuran TC-01 di kedua run; klaim inti produk |
| ~~**G2**~~ | ~~Dua run, pernyataan status yang saling bertentangan~~ | **DITUTUP 31 Okt** — `03_Accountability_Sheet.md` kini memuat tabel per run: `-001` disetujui 4 Nov 14:49 lalu diserahkan ke guru, `-002` disetujui 30 Okt 17:19 lalu dicetak, `-003`/`-004` `PENDING`. `04_Test_Results.md` menyebut run di setiap baris | Selesai. Setiap dokumen menyebut run dan statusnya; tidak ada lagi kalimat "belum ada yang diterbitkan" tanpa kualifikasi | Menghapus kontradiksi diri yang bisa ditemukan juri dalam 2 menit |
| **G3** | 0 screenshot untuk 21 kasus uji | `05_Bukti_Proses/evidence_bundle/03_screenshots/` hanya berisi `INDEX.md`. **Penghalang yang ditemukan 31 Okt:** (a) **TERATASI** — tidak ada skill `edu-*` yang terpasang, sehingga setiap sesi tangkap akan gagal di langkah pertama; keempat skill kini terpasang lewat `tools/install_skills.py` dan cek 3 `doctor.py` lulus di path default; (b) instruksi tangkap di runbook semula khusus Windows (`Win + Shift + S`) padahal mesinnya Linux | ≥6 tertangkap, P0 lebih dulu: TC-08, TC-10, TC-14, TC-15, TC-18 (+TC-02). Runbook §1.0 kini dibuka dengan cek instalasi dan §1.4 memuat perintah `gnome-screenshot` yang terverifikasi ada di mesin ini | Item hasil uji menjadi READY; bukti kritis 1/7 → 5/7; mengangkat Technical Execution dan Responsible AI |
| **G4** | Belum ada video demo | `06_Submission/` hanya berisi skrip, tanpa berkas media. **31 Okt:** juga belum ada runbook produksi — tanpa alat, tanpa urutan rekam, tanpa spesifikasi ekspor, tanpa langkah verifikasi | **Runbook SELESAI 31 Okt** — `06_Submission/13_Demo_Video_Runbook.md`. Runbook memetakan kesepuluh scene ke kebutuhannya: **7 bisa direkam sekarang**, 3 butuh agen berjalan langsung. Sisa: perekamannya sendiri | Demo & Storytelling 3 → 8 (10 poin) |
| ~~**G5**~~ | ~~Klaim tenggat belum terverifikasi~~ | **DITUTUP 31 Okt** — `01_Dokumen/BUKTI_KOMITE_2026-10-31.md` §2: panitia memperpanjang tenggat ke **7 Nov 2026** | Selesai. Target internal: submit **5 Nov** | Membuka semua pekerjaan P0 |

---

## P1 — inkonsistensi yang menggerus kredibilitas

| ID | Celah | Bukti | Definisi selesai |
|----|-------|-------|------------------|
| ~~**G6**~~ | ~~Kontrak menyebut 3 format; submission mengklaim 5 + kuis~~ | **DITUTUP 31 Okt** — `edu-orchestrator` dan `edu-writer` sudah memakai enam format kanonik; `edu-planner` belum: deskripsi, daftar tugas, dan skema JSON-nya menyebut tiga format, sehingga run empat format seperti `-002` tidak bisa direncanakan dari kontraknya | Selesai. `edu-planner/SKILL.md` kini memuat daftar enam format kanonik, aturan "subset apa pun, minimal dua", dan skema yang diperbarui. Angka "tiga" yang tersisa hanyalah nilai bawaan bila Orchestrator tidak menyebut format — konsisten dengan aturan tersebut |
| ~~**G7**~~ | ~~Penghitung perulangan berupa prosa, bukan field~~ | **DITUTUP 31 Okt** — baris `Iteration` ditambahkan ke `edu_output/00_run_config.md`; `edu_output_wujud_zat/00_run_config.md` dibuat (sebelumnya tidak ada sama sekali) | Selesai. Kedua run mencatat `iteration: 1` dari 3. Catatan jujur dipertahankan di `02_WORKFLOW.md` §4: **tercatat, belum ditegakkan** |
| ~~**G8**~~ | ~~Audit log `-001` bertentangan dengan penolakannya sendiri~~ | **DITUTUP 31 Okt** — §7 ditambahkan ke `audit_log_edu_orchestrator.md`: REJECT 29 Okt, remediasi, APPROVE 30 Okt, dan hitungan iterasi yang dikoreksi. §3.3/§3.4 dibiarkan utuh dengan penunjuk maju | Selesai. Tidak ada yang ditulis ulang; log tetap append-only |
| ~~**G9**~~ | ~~Salinan rulebook bisa melenceng~~ | **DITUTUP 31 Okt** — cek 5 `tools/doctor.py` mem-hash setiap salinan dan gagal bila ada perbedaan; hari ini ketiganya berbagi satu checksum (`9fe63368…`). Cek yang sama mencakup salinan `source_material_wujud_zat.md`, yang disinkronkan ulang setelah koreksi header. Skripnya Python, jadi cek berjalan identik di Windows | Selesai. Kemelencengan kini terdeteksi pada setiap clone, bukan lewat langkah manual sebelum submit |
| **G19** | **Lapisan pengetahuan berada di dalam folder hasil** | `03_Hasil/` memuat tiga jenis isi yang seharusnya terpisah: **hasil run** (`edu_output*`, `materi_ajar`), **laporan audit** (`audit/`), dan **lapisan pengetahuan read-only** (`referensi/` — 7 berkas: rulebook, CP, konteks aktual, 4 source material). Arsitektur `01_ARSITEKTUR.md` §1 menempatkannya di sana, dan batas kepercayaan **B1** menyatakan lapisan ini tidak boleh ditulis oleh langkah agen — tetapi secara struktural ia berada di folder yang namanya berarti "hasil", tempat orang menghapus dan menimpa | **Selesai** bila `referensi/` berada di luar `03_Hasil/` (usul: `08_Referensi/` di akar) dan `doctor.py` + `check_grounding.py` menunjuk lokasi baru. **Belum dikerjakan — sengaja.** Pindah sekarang berarti menyunting 25 berkas rujukan, 2 konstanta alat, dan meninggalkan 6 artefak append-only (audit log `-001`/`-004`, `grounding_report` ×2, `11_Memo_Koreksi_Tag`, `audit_log_edu_orchestrator.md`) dengan path yang menunjuk ke folder yang tidak ada lagi. Dua hari sebelum tenggat, mengorbankan integritas bukti demi kerapian direktori adalah pertukaran yang salah. Yang dikerjakan sekarang hanya penandaan: `03_Hasil/README.md` |
| **G10** | R012 dideklarasikan tetapi belum pernah dijalankan | `04_RULEBOOK.md` §2. **31 Okt:** ditemukan penyebab yang lebih dalam — `edu-reviewer/SKILL.md` hanya memuat R001–R011 dan "pemeriksaan khusus"-nya hanya mencakup R002/R003/R006, sehingga agen yang menegakkan rulebook tidak pernah diberi tahu R012 ada | **Separuh kontrak SELESAI 31 Okt**: Reviewer kini menyebut R001–R012, membawa cek R012 eksplisit, dan wajib mengembalikan `rules_na` beserta alasan (aturan tanpa vonis = tidak diperiksa). **Masih terbuka**: belum ada run langsung yang menjalankan R012. Kasus uji **TC-21** ditulis 31 Okt (`test_cases_matrix.md` §K): klaim khasiat bermerek + superlatif + halal yang harus di-REJECT dengan ketiga sub-klausul disebut, plus pass materi bersih yang harus mengembalikan `rules_na: R012` dengan alasan. Status tetap `TO RUN` sampai dijalankan dan ditangkap |

---

## P2 — menaikkan batas atas, tidak wajib

| ID | Celah | Mengapa penting | Usaha |
|----|-------|-----------------|-------|
| **G11** | Animatik tanpa audio, tanpa MP4 | UX & Accessibility; "video" tanpa suara terlihat belum jadi | Rekam narasi, render ke MP4 |
| **G12** | Belum ada tautan proyek langsung (bonus) | Poin bonus; juga panggung demo 90 detik | Terbitkan kuis + animatik sebagai halaman statis |
| **G13** | Belum ada keluaran dua bahasa (TC-17) | Bonus di Challenge C | Satu versi EN + cek fakta lintas bahasa |
| **G14** | Belum ada Reviewer kedua yang bersifat adversarial | Keterbatasan yang dinyatakan; butir peta jalan | Hanya bila waktu tersisa setelah P0 |
| **G15** | Uji kejutan belum pernah dilatih | 90 detik tidak memberi ampun. **31 Okt:** runbook Demo Day juga belum ada — format 8 menit (presentasi + uji 90 detik + tanya jawab, handbook hlm. 15) belum punya anggaran waktu, pembagian langsung/rekaman, maupun tangga cadangan | **Runbook SELESAI 31 Okt** — `03_Hasil/panduan/Runbook_Demo_Day.md`. **Masih terbuka:** dua latihan berwaktu dengan kasus yang belum pernah dilihat, dicatat di §8-nya |
| ~~**G16**~~ | ~~Catatan persetujuan memuat tiga dari empat bagian protokol~~ | **DITUTUP 5 Nov 2026.** G16 disusun dengan membaca `00_run_config.md` saja, yang memang tidak memuat kalimat verbatim. `03_Hasil/edu_output_wujud_zat/audit_log.md` §3.7 memuat keempatnya: nama penyetuju, waktu 30 Okt 17:19, cakupan yang **menyebut kunci jawaban 27 butir**, dan pernyataan verbatim **"ok saya setujui"**. Celahnya dokumenter, bukan substantif | Selesai. Bila juri bertanya: kutipan bersumber dari log run, bukan tangkapan pesan asli | Menutup satu-satunya klaim etik yang sebelumnya perlu kualifikasi |
| ~~**G17**~~ | ~~Tidak ada yang memungkinkan guru memasang dan memverifikasi pipeline dari hasil clone~~ | **DITUTUP 31 Okt** — `tools/install_skills.py` + `tools/doctor.py`. `git clone` baru memasang 4 skill dan melaporkan `8 passed / 0 failed / 0 warning`, exit 0. Ditulis ulang dalam Python pada 31 Okt karena tim terbelah Linux/Windows dan versi bash-nya menjadi program berbeda di tiap sistem | Selesai. README → "Jalankan sendiri", dengan bentuk perintah per OS dan tabel gejala/penyebab/perbaikan |
| **G18** | Dokumen dan kontrak berbahasa Inggris padahal proyek berbahasa Indonesia | Seluruh dokumen juri dan delapan dokumen teknis sudah diterjemahkan 31 Okt. Yang **masih** berbahasa Inggris: empat berkas `SKILL.md` (kontrak agen) dan `THIRD_PARTY_NOTICES.md` | Terjemahkan keempat kontrak dan tambahkan aturan eksplisit "keluaran wajib Bahasa Indonesia" di kontrak Writer dan Reviewer, sehingga bahasa keluaran menjadi kewajiban kontrak, bukan kebiasaan. `THIRD_PARTY_NOTICES.md` boleh tetap Inggris karena isinya pernyataan lisensi pihak ketiga |

---

## Jadwal — 31 Oktober sampai 5 November (tanggal submit)

Tenggat terkonfirmasi **7 November 2026** (`BUKTI_KOMITE_2026-10-31.md` §2). Target internal
**5 November**, menyisakan dua hari untuk kegagalan unggah dan masalah formulir.

| Hari | Pekerjaan | Mengapa urutannya begitu |
|------|-----------|--------------------------|
| **31 Okt** | ✅ **SELESAI** — G1 (lembar fakta, penandaan ulang, grounding PASS, memo koreksi); G5 ditutup (tenggat terverifikasi); U1–U3 diselesaikan; **G6–G8 ditarik maju dan ditutup**; **G3 dibuka penghalangnya** (pra-terbang instalasi skill + perintah tangkap Linux); G2, G9, G17 ditutup; seluruh dokumen diterjemahkan ke Bahasa Indonesia (G18 separuh) | G1 satu-satunya butir P0 yang mengubah kebenaran produk; G6–G8 mekanis dan berada di depan G3, jadi mengerjakannya lebih awal membeli satu hari penyangga untuk video |
| **1 Nov** | G3 — tangkap 5 screenshot kritis (TC-08, 10, 14, 15, 18) + TC-02 + TC-21. Skill **sudah terpasang** (31 Okt, cek 3 `doctor.py` lulus) | Bukti kritis 1/7 → 5/7 (6/7 dengan TC-21); membuka batas Responsible AI |
| **2 Nov** | G4 — rekam video 5–8 menit dari skrip yang sudah ada | Keuntungan dimensi terbesar dalam satu langkah (3 → 8) |
| **3 Nov** | *Penyangga* — G6–G8 sudah selesai. Pakai harinya untuk pass tangkap kedua (S3/S4) atau G10 | Menyerap kelebihan waktu yang selalu muncul di sesi tangkap |
| **4 Nov** | G10 + G15 — satu kasus uji R012 dijalankan, dua latihan berwaktu memakai `Runbook_Demo_Day.md` §8 | Kesiapan Demo Day; murah. Demo Day 27 Nov dan hanya berlaku bila lolos seleksi 10 Nov, jadi ini yang pertama dilepas |
| **5 Nov** | Rekonsiliasi akhir: hitungan uji, checksum, tautan, ZIP, submit + screenshot halaman konfirmasi | Poin mekanis yang gratis |

Bila ada hari yang meleset, lepas dengan urutan ini: G10 → G15 → G13. Jangan pernah melepas G1 atau G3.

---

## Arti "selesai" untuk submission

Submission selesai bila semua hal berikut benar, dan masing-masing bisa diperiksa oleh orang yang tidak
ikut di ruangan:

1. Kesebelas item punya artefak, dan tautan di formulir bisa dibuka orang luar.
2. Hitungan di `06_Submission/04_Test_Results.md` cocok dengan `03_screenshots/INDEX.md`.
3. Tidak ada dokumen yang mengklaim perilaku yang tidak bisa didemonstrasikan berkas di repo.
4. Setiap run yang disebut disertai statusnya (`PENDING` / `RELEASED`).
5. Log cacat ada dan spesifik (D1, D2).
6. `check_grounding.py` sudah dijalankan pada artefak final dan keluarannya disertakan.
7. Checksum rulebook cocok di ketiga salinan.

Butir 2–7 semuanya mekanis. Itu poin termurah di kompetisi ini.
