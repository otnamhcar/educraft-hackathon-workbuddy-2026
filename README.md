# EduCraft — Asisten Ajar AI IPAS SD yang Dikendalikan Rulebook

> **Materi IPAS siap ajar, lolos aturan sebelum terbit.**

Tencent Cloud Hackathon Indonesia 2026 · **Challenge C — The Creator Agent**
Dibangun dengan WorkBuddy (Tencent Cloud). Tanpa framework orkestrasi, tanpa aplikasi web, tanpa
basis data.

**Bahasa:** seluruh proyek berjalan dalam Bahasa Indonesia — masukan guru, aturan, keluaran materi,
dokumentasi, dan kontrak agen. Yang tetap apa adanya hanya nilai harfiah di dalam berkas state
(`APPROVE`, `REJECT`, `PENDING`), sintaks tag (`[src:1]`, `[UNVERIFIED]`), dan nama berkas.

---

## Repo ini apa

EduCraft adalah **empat kontrak agen plus satu lapisan pengetahuan**. Itu pilihan yang disengaja:
juri bisa membuka empat berkas Markdown dan membaca setiap aturan yang ditaati agen, alih-alih
menyimpulkan perilakunya dari kode.

Satu dokumen sumber yang disetujui masuk. Satu paket ajar utuh keluar — RPP, pre-test dan post-test
dengan kunci jawaban, garis besar slide, artikel siswa, brief infografis, dan kuis HTML yang bisa
dimainkan. Tidak ada yang dirilis sebelum agen Reviewer independen memeriksa setiap kalimat terhadap
rulebook tertulis **dan** manusia menyetujuinya.

Produknya bukan teks yang dihasilkan. **Produknya adalah gerbangnya.**

### Aturan siapa ini

Ide, rujukan kurikulum, dan substansi rulebook berasal dari **Don Jimat Akbar**, guru IPAS SD yang masih
aktif mengajar. Ia yang menetapkan apa yang tidak akan pernah diletakkan guru di depan kelas — tanpa
klaim kesehatan permanen, tanpa menakut-nakuti, tanpa klaim halal tanpa sertifikat. Pekerjaan tim
adalah memformalkan penilaian itu menjadi predikat yang bisa diperiksa mesin, dan membangun pipeline
yang menegakkannya.

Karena itulah `rulebook_ipas.md`, bukan kodenya, adalah artefak yang bisa diadopsi sekolah: tim
kurikulum bisa menyunting aturan tanpa menyentuh pipeline.

---

## Pipeline

```
Brief guru (sumber disetujui + kode CP)
    │
    ▼
Orchestrator ── menulis 00_run_config.md, menambahkan ke audit log
    │
    ├─► Planner ──────────► outline per format, dipetakan ke kode CP, celah ditandai
    │                            │
    ├─► Writer ───────────► draf v1, setiap kalimat faktual bertag [src:#]
    │        ▲                   │
    │        │                   ▼
    │        │            Reviewer ──► APPROVE | REJECT + findings[]
    │        │                   │        (ID aturan + kutipan teks + alasan + saran)
    │        └──── REJECT ◄──────┤  iteration += 1
    │                            │  bila iteration == 3 dan masih REJECT → HALT, eskalasi
    │                            ▼
    │                        APPROVE
    ▼                            ▼
Gerbang approval manusia ──► Format Rendering (WAJIB)
                             Materi_Guru .md → RPP .docx → Slide .pptx → Kuis .html
                                        │
                                        ▼
                             paket siap pakai dirilis (+ audit log)
```

**Keluaran akhir bukan draf.** Draf Markdown yang bertag `[src:#]` adalah bahan kerja internal;
ia tidak pernah diserahkan ke guru. Sebuah run baru dianggap selesai setelah empat artefak siap
pakai ada dan lulus checklist: `Materi_Guru_*.md`, `RPP_*.docx`, `Slide_*.pptx`, `quiz_*.html`.
`.md` dibangun lebih dulu sebagai lapisan konten teresolusi, dan ketiga format lain diturunkan
darinya — sehingga satu angka tidak bisa berbeda antar berkas (FR-09).

Tiga sifat ditegakkan oleh kontrak, bukan oleh harapan:

| Sifat | Mekanisme |
|-------|-----------|
| Grounding | Writer hanya boleh memakai fakta yang ada di sumber; jalan keluarnya token literal `[UNVERIFIED]` |
| Pemisahan kewenangan | Reviewer punya **veto** tetapi tidak bisa menulis ulang; Writer punya **tulis ulang** tetapi tidak bisa menyetujui |
| Tanpa penerbitan mandiri | Penerbitan adalah langkah terpisah yang bergerbang manusia. Agen tidak punya jalur ke keluaran yang melewati gerbang |

---

## Peta repo

| Path | Isinya |
|------|--------|
| `05_Bukti_Proses/skills_package/` | **Kodenya**: empat kontrak `SKILL.md` + aset pengetahuan |
| `05_Bukti_Proses/skills_package/edu-reviewer/assets/rulebook_ipas.md` | **Rulebook** R001–R012 (v2.0) |
| `02_Sumber/` | Dua PDF resmi kementerian yang menjadi bahan lapisan pengetahuan, plus hasil ekstraksi teksnya. Inventaris dan pengecualian: `02_Sumber/README.md` |
| `08_Referensi/` | Lapisan pengetahuan: source material, CP, daftar konteks aktual, rulebook |
| `03_Hasil/edu_output/` | Folder run `-001` (Energi Alternatif): `00_run_config.md`, `audit_log.md`, dan `01_lesson_plan.md` |
| `03_Hasil/materi_ajar/` | Salinan artefak run `-001` untuk bundel (draf yang diperbaiki + kuis HTML). **Bukan run tersendiri** — tidak punya `00_run_config.md` sendiri |
| `03_Hasil/edu_output_wujud_zat/` | Keluaran run `-002` (Perubahan Wujud Zat) + tiga PDF siap cetak |
| `03_Hasil/edu_output_tata_surya/` | Keluaran run `-003` (Tata Surya), satu-satunya run dengan konvensi sitasi kelas |
| `03_Hasil/edu_output_wujud_zat_faseC/` | Keluaran run `-004` (Wujud Zat Fase C, pemantapan lintas fase) |
| `03_Hasil/edu_output_energi_alternatif*/` | Enam folder untuk run `-005` sampai `-010` (Energi Alternatif: RPP, kuis, slide, dua poster, uji prompt injection) — masing-masing punya `00_run_config.md` dan `grounding_report.md` |
| `03_Hasil/audit/` | **Kedua** laporan review — yang REJECT dan yang APPROVE |
| `06_Submission/panduan/` | Cara mendemokan: panduan guru + testimoni, dan runbook Demo Day (anggaran 8 menit, tangga fallback, penunjuk bukti untuk Q&A) |
| `04_Diskusi/test_cases_matrix.md` | Suite 23 kasus, termasuk delapan yang kritis, dan tabel cakupan per aturan yang jujur |
| `06_Submission/` | Bundel submission: deskripsi, lembar akuntabilitas, hasil uji, arsitektur, deck |
| `06_Submission/architecture_diagram.png` | Diagram komponen dan batas kepercayaan |
| `07_Dokumentasi/` | Dokumen rekayasa: arsitektur, workflow, batas skill, spesifikasi rulebook, rencana uji, ketertelusuran kebutuhan, daftar celah |
| `tools/check_grounding.py` | Pemeriksaan R001 deterministik — me-resolve setiap tag terhadap lapisan pengetahuan, keluar non-nol bila gagal. Hanya memeriksa draf; metadata run dilewati dan disebutkan namanya di laporan |
| `tools/install_skills.py` | Menyalin empat folder skill ke tempat WorkBuddy membacanya, lalu memverifikasi jumlahnya 4. Python, jadi jalan sama di Linux, macOS, dan Windows |
| `tools/doctor.py` | Tujuh pemeriksaan pra-terbang pada clone baru — Python, kontrak, skill terpasang, lapisan pengetahuan, checksum salinan, grounding di sebelas folder run, konvensi sitasi. Kode yang sama di semua OS |
| `tools/check_capture.py` | Memeriksa berkas screenshot sebelum submit: mana yang belum ada, mana yang di bawah 1366 px, mana yang bukan PNG, mana yang tidak terdaftar di tracker. Daftar berkasnya dibaca dari `INDEX.md`, bukan dari daftar kedua yang bisa melenceng |
| `tools/capture.py` | Menangkap layar di Windows: menyetel DPI-awareness lebih dulu (tanpa itu layar 1366 px terekam 1093 px pada skala 125 %), menyimpan langsung dengan nama final, dan menolak menimpa bukti yang sudah ada. Menggantikan `gnome-screenshot` yang ditulis untuk mesin Linux |
| `tools/capture_session.py` | Menjalankan sesi tangkap enam berkas wajib berurutan: nama berkas, prompt yang dipaste, dan syarat isi frame dipegang skrip, sehingga tidak ada salah nama atau salah folder. Memanggil `capture.py`, bukan menyalin logikanya. Setelah tiap tangkapan gambar dibuka dan frame-nya **wajib dikonfirmasi**; jawaban `n` memindahkan berkas ke `_karantina/` — `check_capture.py` tidak bisa membaca isi gambar, jadi konfirmasi manusia itulah yang menutup celahnya. `--list` untuk rencana, `--only TC-13` untuk satu berkas |
| `tools/render_evidence.py` | Merender berkas hasil run (outline Planner, draf bertag, vonis Reviewer, audit log) menjadi PNG 1600 px untuk bukti submission. Setiap halaman membawa banner "berkas hasil run · dirender" — ia bukti artefak, bukan tangkapan UI |
| `06_Submission/video_kit/concat_video.py` | Menormalkan tiga rekaman, menyambung dengan dua kartu judul, meratakan suara ke −16 LUFS, dan menolak hasil di luar durasi 5:00–8:00 |

---

## Rulebook (R001–R012, v2.0)

| Aturan | Yang dijaga |
|--------|-------------|
| R001 | Fakta apa pun tanpa tag `[src:#]` yang bisa di-resolve |
| R002 | Menakut-nakuti dan pembingkaian katastrofik |
| R003 | Bahasa yang tidak sesuai untuk usia ~10–12 tahun |
| R004 | Penyimpangan dari *Capaian Pembelajaran* |
| R005 | Konten yang hanya memuat bahaya, tanpa mitigasi atau peran siswa |
| R006 | Klaim kesehatan tanpa dasar — efek permanen, kesembuhan, khasiat absolut |
| R007 | Mempromosikan atau menormalkan praktik berbahaya |
| R008 | Nada yang tidak hangat, edukatif, dan memberdayakan |
| R009 | Bahasa Indonesia tidak baku, atau narasi tanpa ajakan bertindak positif |
| R010 | Diksi yang menstigma atau menyalahkan murid atau kelompok |
| R011 | Klaim dunia nyata tanpa URL resmi, bertanggal, dan bisa ditelusuri |
| R012 | Klaim komersial, khasiat produk, superlatif, atau halal tanpa sertifikat — `N/A` untuk materi yang murni edukatif |

Rulebook yang bisa disunting tim kurikulum tanpa menyentuh kode itulah yang membuat adopsi
institusional realistis, bukan teoretis. Ini juga trade-off yang jujur: aturan di dalam prompt
bersaing untuk ruang konteks, dan rulebook yang sangat panjang akan menurunkan kepatuhan. Lihat
`06_Submission/05_Architecture.md` §4 untuk empat trade-off yang kami pertahankan beserta biaya
masing-masing.

---

## Jejak bukti — termasuk kegagalannya

**Run `EDU-ORCH-20261026-001`** (Energi Alternatif, Fase C, CP C4 + B5)

| Langkah | Berkas |
|---------|--------|
| Konfigurasi run | `03_Hasil/edu_output/00_run_config.md` |
| Audit log | `03_Hasil/audit/audit_log_edu_orchestrator.md` |
| **REJECT** 29 Okt (R001, R011, R004) | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-29.md` |
| Remediasi: source material sungguhan dibuat | `08_Referensi/source_material_energi.md` |
| Remediasi: URL resmi bertanggal | `08_Referensi/konteks_aktual.md` |
| **APPROVE** 30 Okt | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-30_REVISI.md` |

Pada 29 Oktober agen Reviewer **menolak keluaran kami sendiri**: draf ditandai terhadap berkas
capaian pembelajaran alih-alih sumber yang memuat fakta, dan dua klaim "dunia nyata" tidak punya
dokumen yang bisa diverifikasi di belakangnya. Kami mengirim laporan penolakan itu. Kami tidak
menghapusnya, dan tidak menambal draf diam-diam.

**Run `EDU-ORCH-20261030-002`** (Perubahan Wujud Zat, Fase C)

Reviewer Pass 1 mengembalikan **REJECT dengan 5 temuan Mayor**, semuanya R001: klaim tentang susunan
partikel dan ciri tiap wujud zat tidak ada di sumber. Writer menghapusnya dan mengganti pembingkaian
"lebih rapat/lebih longgar" dengan pasangan arah yang eksplisit. Pass 2: APPROVE di iterasi 2 dari 3.
Guru menyetujui pada 30 Oktober 2026 pukul 17:19, yang membuka gerbang publikasi — setelah itu dua
paket cetak terpisah dibuat agar kunci jawaban tidak pernah ikut dalam buku siswa. Jejak lengkap:
`03_Hasil/edu_output_wujud_zat/audit_log.md`.

Urutan itu — **tolak, diagnosis, perbaiki, review ulang** — adalah bukti penggunaannya. Screenshot
dari jalur yang mulus justru membuktikan lebih sedikit.

**Run `EDU-ORCH-20261104-004`** (Perubahan Wujud Zat untuk Fase C) — bukti bahwa agen berhenti ketika
kurikulumnya tidak cocok. Topik perubahan wujud zat ada di Fase B, bukan Fase C; alih-alih mengarang
butir CP yang tidak ada, agen menandai run sebagai **pemantapan lintas fase** dengan `PERLU KONFIRMASI
GURU` di tiga butir terbuka. Pass 1: REJECT (3 Major, 3 Minor). Pass 2: APPROVE — berhenti di
`AWAITING_APPROVAL` dengan publikasi terkunci, dan tetap berhenti sampai guru memutuskan. Guru
memutuskan 5 Nov 2026 16:13: status naik ke `APPROVED_FOR_USE`, **publikasi tetap `LOCKED`**. Jejak:
`03_Hasil/edu_output_wujud_zat_faseC/audit_log.md` §8 dan §12.

---

## Status pengujian (dinyatakan apa adanya)

| Hasil | Jumlah |
|-------|--------|
| `PASS` — dibuktikan artefak, tangkapan, atau render di repo ini | 15 |
| `BY DESIGN` — ditegakkan di `SKILL.md`, bukti langsung belum diambil | 6 |
| `BELUM` — belum pernah dieksekusi, diungkap | 1 |
| `TO RUN` — belum dijalankan, diungkap | 1 |

**Kami tidak mengklaim 23/23.** Tabel lengkap, termasuk kasus kritis dan kegagalan yang diungkap:
`06_Submission/04_Test_Results.md`.

Satu kasus bisa diperiksa mesin dari ujung ke ujung, dan itulah yang paling penting:

```bash
python3 tools/check_grounding.py --run 03_Hasil/materi_ajar \
    --knowledge 08_Referensi --out 03_Hasil/materi_ajar/grounding_report.md
```

| Folder | Run | Tag diperiksa | Dangling | Pelanggaran kelas | Vonis |
|--------|-----|-------------:|---------:|------------------:|-------|
| `materi_ajar` | `-001` Energi | 121 | 0 | 0 | **PASS** |
| `edu_output` | `-001` Energi (draf produksi) | 121 | 0 | 0 | **PASS** |
| `edu_output_wujud_zat` | `-002` Wujud Zat, sebelum perbaikan | 89 | 0 | 84 | **FAIL** — defek D1 |
| `edu_output_wujud_zat` | `-002` Wujud Zat, sesudah perbaikan | 115 | 0 | 0 | **PASS** |
| `edu_output_wujud_zat_faseC` | `-004` Wujud Zat Fase C | 212 | 0 | 0 | **PASS** |
| `edu_output_tata_surya` | `-003` Tata Surya | 109 | 0 | 0 | **PASS** |
| `edu_output_energi_alternatif` | `-005` Energi Alternatif, dieskalasi | 269 | 0 | 0 | **PASS** |
| `edu_output_energi_alternatif_faseC` | `-006` Energi Alternatif Fase C | 134 | 0 | 0 | **PASS** |
| `edu_output_energi_alternatif_faseC_007` | `-007` RPP + kuis + slide | 199 | 0 | 0 | **PASS** |
| `edu_output_energi_alternatif_faseC_008` | `-008` poster promosi | 44 | 0 | 0 | **PASS** |
| `edu_output_energi_alternatif_faseC_009_versi_bersih` | `-009` poster versi bersih | 22 | 0 | 0 | **PASS** |
| `edu_output_energi_alternatif_faseC_010` | `-010` uji prompt injection | 271 | 0 | 0 | **PASS** |
| **Total per run** | **sepuluh run** | **1.496** | **0** | **0** | |

> Run `-001` diperiksa di **dua folder** karena keduanya memuat artefaknya: `materi_ajar` (draf markdown
> terkoreksi) dan `edu_output` (folder produksi berisi `.docx`/`.pptx`/`.html` serta draf kerja).
> Keduanya lulus dengan angka identik, **121 tag**, sehingga run `-001` dihitung **sekali** pada total.
> Sebelum 5 November 2026 draf di `edu_output` masih memakai tag kurikulum untuk fakta dan gagal dengan
> 73 pelanggaran kelas; perbaikannya tercatat di `03_Hasil/edu_output/audit_log.md` §7.4.

> Run `-003` memakai konvensi penulisan sumber yang berbeda sejak 5 November 2026: RPP dan slide
> menyebut nama sumber dalam kata, kuis tanpa rujukan, dan tag mesin dipindahkan ke
> `05_Jejak_Sumber.md`. Angka 109 adalah tag di lampiran itu, bukan di badan dokumen. Konvensinya
> diperiksa terpisah oleh `tools/check_sitasi.py`.

---

## Jalankan sendiri

Ditulis untuk guru di laptopnya, bukan untuk developer. Dua perintah, satu restart, lalu satu
pemeriksaan kesehatan. **Dua perintah yang sama berlaku di Linux, macOS, dan Windows** — semua skrip
di `tools/` berbahasa Python, karena tim ini memakai Linux (Mint) dan Windows, dan skrip bash adalah
program berbeda di masing-masing.

```bash
git clone https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026.git
cd educraft-hackathon-workbuddy-2026
```

Lalu pasang, dari akar repo:

| | Linux / macOS | Windows (cmd atau PowerShell) |
|---|---|---|
| Pasang skill | `python3 tools/install_skills.py` | `python tools\install_skills.py` |
| Pemeriksaan kesehatan | `python3 tools/doctor.py` | `python tools\doctor.py` |

Kalau `python` tidak ada di PATH pada Windows, pakai launcher: `py tools\install_skills.py`.

Pemasang menyalin `edu-orchestrator`, `edu-planner`, `edu-writer`, dan `edu-reviewer` dari
`05_Bukti_Proses/skills_package/` ke `~/.workbuddy-ai/skills/` (di Windows,
`C:\Users\<anda>\.workbuddy-ai\skills`), lalu menghitungnya kembali untuk memastikan empat yang tiba.
**Tidak ada yang dikompilasi dan tidak ada package manager yang terlibat** — skill adalah folder
berisi `SKILL.md`, dan "memasang" artinya meletakkan folder itu di tempat agen membacanya. Tambahkan
`--dry-run` untuk melihat rencananya tanpa menulis apa pun.

Lalu **restart WorkBuddy**. Daftar skill dibaca saat sesi dibuka, jadi sesi yang sedang berjalan tidak
akan melihat folder baru. Buka chat baru, pastikan `edu-orchestrator` dikenali, lalu verifikasi sisa
clone dengan `doctor.py` (tabel di atas).

Ia menjalankan tujuh pemeriksaan dan keluar non-nol bila ada yang gagal, sehingga clone yang rusak
mengatakan *di mana* rusaknya:

| # | Pemeriksaan | Arti bila FAIL |
|---|-------------|----------------|
| 1 | Python 3.6+ | pemeriksaan grounding tidak bisa jalan |
| 2 | empat kontrak ada di clone | clone tidak lengkap |
| 3 | empat skill `edu-*` terpasang | jalankan `install_skills.py`, lalu restart |
| 4 | rulebook, CP, daftar konteks aktual, semua lembar sumber | lapisan pengetahuan hilang |
| 5 | salinan rulebook dan tiap lembar sumber berbagi satu SHA-256 | ada salinan yang menyimpang — Reviewer akan menilai dengan aturan yang berbeda dari yang ditulis Writer |
| 6 | pemeriksaan grounding di sebelas folder run | ada draf yang tidak lagi menunjuk sumbernya |
| 7 | konvensi sitasi pada dokumen yang dibaca guru | run `-003` satu-satunya yang memakai konvensi sitasi kelas; run lain masih bertag sebaris |

Clone yang sehat mencetak `19 passed / 0 failed / 0 warning` dan keluar dengan kode 0. Diukur di
mesin Windows 7 November 2026. Pemeriksaan #7 hanya dijalankan pada run yang memang memakai konvensi
kelas (`03_Hasil/edu_output_tata_surya`), jadi tidak ada `SKIP` yang perlu dihitung sebagai warning.

### Run pertama

Tempel ini ke chat baru:

> Gunakan `edu-orchestrator`. Topik: Perubahan Wujud Zat. Fase C (kelas V–VI).
> Kode CP: CP-B.1.1.4 dan CP-C.2.2. Format: RPP, artikel, kuis.
> Sumber: `assets/source_material_wujud_zat.md`.

Harapkan urutan ini, tidak kurang:

```
Plan → Draft → Review → (REJECT → remediasi, maks 3) → APPROVE → BERHENTI di gerbang approval
```

Run harus berakhir di `publish_status: PENDING`. **Kalau ia menerbitkan sendiri, pemasangannya
salah** — gerbangnya adalah produknya, dan itu hal pertama yang harus diverifikasi.

### Kalau ada yang gagal

| Gejala | Penyebab | Perbaikan |
|--------|----------|-----------|
| `doctor.py` bilang `0 of 4 installed` | skill masuk ke tempat yang tidak dibaca agen | arahkan kedua skrip ke folder sebenarnya: `--dest <path>`, atau set `WORKBUDDY_SKILLS_DIR` |
| `could not replace ...` | ada berkas yang terbuka di editor, atau agen masih berjalan (umum di Windows) | tutup lalu ulangi |
| `python: command not found` (Windows) | Python belum terpasang, atau tidak ada di PATH | coba `py tools\doctor.py`; kalau tidak bisa, pasang Python 3 dan centang *Add to PATH* |
| `python3: command not found` (Linux/macOS) | Python 3 belum ada | `sudo apt install python3` — pemeriksaan grounding adalah inti proyek ini, jadi `doctor.py` tidak akan lulus tanpa itu |
| Skill tetap tidak dikenali setelah pemasangan | sesi belum di-restart | tutup WorkBuddy sepenuhnya, buka lagi, chat baru |
| `ffmpeg: command not found` (Windows) | terminal atau sesi itu lahir sebelum PATH diperbarui — PATH dibaca sekali saat proses dibuat | buka terminal baru. Kalau tetap gagal, periksa apakah folder `bin` paket ffmpeg ada di PATH pengguna, lalu tambahkan — lihat `06_Submission/13_Demo_Video_Runbook.md` §2.1 |

**Khusus Windows.** `cmd`, PowerShell, dan Git Bash semuanya bisa — tidak ada skrip bash yang perlu
dijalankan. Pakai garis miring terbalik (`tools\doctor.py`) atau garis miring biasa; keduanya
diterima. Kalau konsol mencetak kode warna sebagai teks, tambahkan `--no-color`.

**Line ending.** `.gitattributes` mengunci `*.py` dan `*.md` ke LF serta menandai PDF dan hasil
ekstraksi teks sebagai binary, sehingga clone Windows dengan `core.autocrlf=true` tidak menulis ulang
repo dan tidak menampilkan diff seluruh berkas setelah pull.

**Yang dibutuhkan:** WorkBuddy (atau runtime agen apa pun yang membaca folder `SKILL.md`) dan
Python 3.6+. Tanpa API key miliknya sendiri, tanpa langkah build, tanpa basis data.

---

## Keterbatasan yang diketahui (dinyatakan, bukan disembunyikan)

- **Satu Reviewer, bukan pasangan yang saling menyerang.** Titik buta sistematis di Reviewer adalah
  titik buta sistematis di produk. Mitigasi: setiap vonis wajib mengutip teks dan menyebut aturan,
  sehingga manusia bisa mengaudit auditnya. Ini cara kami menangkap kegagalan R001 kami sendiri.
- **Grounding butuh dua pemeriksaan, dan kami baru punya satu.** Atribusi ("apakah kalimat ini
  membawa tag?") ditegakkan; resolusi ("apakah tag menunjuk sumber yang benar-benar mengatakan ini?")
  belum. Celah itulah yang menghasilkan penolakan 29 Oktober. Tag bukan sitasi.
- **Run `-002` awalnya berpijak pada entri topik, bukan lembar fakta — sudah diperbaiki.** Klaimnya
  mengutip `[src:B4]`, nama topik kurikulum di `cp_ipas.md`. Pemeriksaan deterministik menemukan 84
  pelanggaran kelas; `source_material_wujud_zat.md` khusus dibuat dari Panduan IPAS resmi (hlm. 26–27)
  dan setiap artefak ditandai ulang ke `[src:W1]`–`[src:W11]`. Isi materi tidak diubah. Dua entri
  (`[src:W10]`, `[src:W11]`) adalah **turunan tim** — pemetaan arah dan contoh sehari-hari yang tidak
  dinyatakan panduan resmi — ditandai demikian dan menunggu validasi guru.
- **Grounding ketat menghasilkan materi tipis.** Sumber tipis menghasilkan paket tipis, dan agen akan
  tampak kurang mengesankan daripada chatbot umum pada topik yang sama. Kami mengoptimalkan untuk mode
  kegagalan yang merusak kepercayaan.
- **Animatik belum bersuara.** `07_video_animatik.html` berdurasi 4:45 dengan subtitle; narasi belum
  direkam.
- **Satu bahasa: Bahasa Indonesia.** Ini keputusan cakupan, bukan cacat — sasarannya guru IPAS SD
  Indonesia, dan bahasa keluaran kini diwajibkan oleh kontrak Writer dan Reviewer. Versi bahasa lain
  ada di roadmap; TC-17 (konsistensi lintas bahasa) tercatat `TO RUN`.
- **Screenshot kasus kritis belum diambil.** Dilacak di
  `05_Bukti_Proses/evidence_bundle/03_screenshots/INDEX.md`.

---

## Lisensi dan data

- **Kode, kontrak, dan dokumentasi:** MIT — lihat `LICENSE`. Ini mencakup pipeline, keempat berkas
  `SKILL.md`, pemeriksa, dan setiap dokumen di repo ini.
- **Atribusi:** substansi rulebook adalah penilaian profesional Don Jimat Akbar, yang diformalkan tim.
  Lisensi MIT mencakup implementasi repo ini, bukan kepengarangannya.
- **Dua dokumen resmi kementerian diedarkan ulang tanpa perubahan** —
  `Final Panduan Mata Pelajaran IPAS_03_10_2025_Revisi 4.pdf` dan
  `Permendikdasmen-no-13-tahun-2025.pdf` — bersama teks polos hasil ekstraksinya. Keduanya ada di sini
  karena pemeriksaan grounding tidak bermakna tanpa teks yang menjadi pembandingnya: seorang reviewer
  harus bisa membuka halaman asal sebuah klaim. **Syarat penggunaannya bukan milik kami untuk
  dilisensikan ulang.** Lihat `THIRD_PARTY_NOTICES.md`; salah satunya akan dihapus bila diminta.
- **Yang *tidak* diedarkan ulang:** enam dokumen RPP yang diunduh dari `centralpendidikan.com`, satu
  panduan penilaian komersial, satu ekspor WhatsApp, dan handbook panitia. Alasan per berkas di
  `02_Sumber/README.md`.
- **Source material:** run `-001` (`source_material_energi.md`) adalah mock, ditulis untuk hackathon
  ini, dan menyatakan begitu di header-nya sendiri. Run `-002` (`source_material_wujud_zat.md`)
  **dikutip dari Panduan IPAS resmi hlm. 26–27**, dengan nomor halaman, karena data mock adalah defek
  aslinya. Klaim dunia nyata membawa URL resmi dan tanggal akses di `konteks_aktual.md`.
- **Data siswa:** tabel skor memakai ID peserta yang sudah dianonimkan. Tidak ada data siswa nyata.

---

*Disiapkan untuk submission Tencent Cloud Hackathon Indonesia 2026. Setiap klaim di README ini
tertaut ke sebuah berkas di dalam repositori.*
