# 06 — Ketertelusuran persyaratan

> **Tujuan:** menjawab, untuk setiap persyaratan yang ditulis panitia, satu pertanyaan: *di mana
> buktinya?* Setiap baris punya status. `READY` = artefaknya ada dan disitir. `PARTIAL` = artefaknya
> ada tetapi belum lengkap. `GAP` = belum terpenuhi. `UNVERIFIED` = kami bersandar pada klaim yang
> tidak bisa dibuktikan dari repo ini.

---

## A. Item submission (handbook §7)

| # | Item | Status | Artefak | Bukti substansi |
|---|------|--------|---------|-----------------|
| 1 | Judul proyek | READY | `06_Submission/01_Title_Blurb.md` | — |
| 2 | Blurb singkat, <10 kata | READY | sama | 8 kata, dihitung di dalam berkas |
| 3 | Deskripsi proyek (4 bagian) | READY | `02_Project_Description.md` | 4 bagian ada; §3.3 mencakup desain prompt sesuai ketentuan |
| 4 | Lembar akuntabilitas, 1 halaman | READY | `03_Accountability_Sheet.md` | Memuat tabel per run: `-001` disetujui 4 Nov 14:49 lalu diserahkan ke guru, `-002` disetujui 30 Okt 17:19 lalu dicetak, `-003`/`-004` `PENDING`. **Setiap pernyataan menyebut run-nya** (G2 ditutup 31 Okt) |
| 5 | Hasil uji + screenshot | **PARTIAL** | `04_Test_Results.md` | Tabel ada (9 PASS / 12 BY DESIGN / 2 TO RUN, 23 kasus). **0 screenshot tertangkap.** Handbook mewajibkannya |
| 6 | Diagram arsitektur | READY | `05_Architecture.md`, `architecture_diagram.png` (2720×3000), `.html` | Komponen, 4 batas kepercayaan, 4 trade-off |
| 7 | Video demo 5–8 menit | **GAP** | `07_Demo_Video_Script.md` (7:40) + `13_Demo_Video_Runbook.md` | Baru skrip dan runbook; belum ada berkas video |
| 8 | Product sharing | READY | `06_Product_Sharing.md` | Nilai spesifik WorkBuddy, insight |
| 9 | Kode sumber / workflow | READY | `github.com/otnamhcar/educraft-hackathon-workbuddy-2026` | Publik, MIT, 119 berkas ter-track; empat kontrak + aset pengetahuan |
| 10 | Sampul 16:9 | READY | `cover_image_380x216.png`, `1280x720.png` | Dimensi benar |
| 11 | Tautan proyek (bonus) | GAP | — | Belum ada URL langsung. Opsional. |

**Hitungan: 8 READY · 1 PARTIAL · 2 GAP (satu di antaranya bonus).**

---

## B. Keharusan Challenge C (handbook §5)

| Persyaratan | Dipenuhi di mana | Bukti | Status |
|-------------|------------------|-------|--------|
| ≥3 agen dengan peran terdefinisi (Planner, Writer, Reviewer) | `01_ARSITEKTUR.md` §3 | 4 berkas `SKILL.md` | READY |
| ≥2 platform/format dari satu sumber | `03_Hasil/materi_ajar/`, `03_Hasil/edu_output_wujud_zat/` | 5 dokumen + kuis interaktif | READY |
| Reviewer menilai setiap draf terhadap aturan terdokumentasi | `rulebook_ipas.md` v2.0 | 2 laporan review dengan vonis per aturan | READY |
| Penolakan dibenarkan dengan menyitir aturan yang dilanggar | `05_review.md` PASS 1 | 7 temuan, masing-masing dengan ID aturan + kutipan | READY |
| Writer meremediasi dan menyerahkan ulang; ≥1 siklus penuh | run `-001` dan `-002` | REJECT → remediasi → APPROVE di kedua run | READY |
| Maksimal 3 iterasi, lalu eskalasi | `02_WORKFLOW.md` §4 | Perilaku: 2 dari 3 terpakai. **Penegakan: GAP** (penghitung berupa prosa) | PARTIAL |
| Persetujuan manusia sebelum penerbitan | `audit_log.md` §3.7 | Persetujuan 30 Okt 17:19, bernama, dikutip | READY |
| Menyimpan pertukaran antar-agen + riwayat revisi | `audit_log*.md`, kedua laporan review | Laporan yang ditolak tetap disimpan, tidak dihapus | READY — log `-001` kini memuat rekaman v1→v2 di §7 (D2 ditutup 31 Okt) |

---

## C. Dimensi penilaian (handbook §10, 10 × 10 = 100)

Kolom angka adalah **sinyal triase untuk tim, bukan klaim skor**. Kolom ini ada untuk menunjukkan
dimensi mana yang tertahan oleh artefak yang belum ada, bukan oleh kelemahan desain. Hanya kolom
"dasar" yang boleh dikutip.

| Dimensi | Yang diminta handbook | Bukti terkuat kita | Titik terlemah | Perkiraan kini → mungkin | Dasar perkiraan |
|---------|-----------------------|--------------------|----------------|--------------------------|-----------------|
| Impact & Relevance | Masalah nyata, nilai yang berarti | Kerangka lingkar tinjauan guru; paket disetujui dan dicetak | Belum ada pengukuran penghematan waktu; baru satu guru | 7 → 8 | Masalahnya nyata dan spesifik; klaim nilai masih perkiraan |
| Human-Centered Design | Dirancang di sekitar pengguna dan kebutuhan nyata | Paket siswa (tanpa kunci) dan guru (dengan kunci) terpisah; aturan R003 terkalibrasi usia | Belum ada uji kegunaan oleh siswa | 8 → 8 | Artefak menunjukkan pemikiran pengguna; belum ada bukti uji pengguna |
| AI Interaction | Benar-benar agentic, bukan sekali jalan | 4 agen, 2 siklus tolak→remediasi nyata, gerbang | Penghitung perulangan tidak ditegakkan mesin | 8 → 8 | Dua run independen dengan jalur vonis berbeda |
| Technical Execution | Prototipe berfungsi + kinerja terhadap kasus uji | Cek grounding deterministik lulus di kedua run (121 / 115 tag) | 0 screenshot; 11 kasus BY DESIGN | 5 → 8 | Prototipe berjalan; bukti uji belum lengkap |
| Feasibility | Realistis, bisa diskalakan melewati hackathon | Tanpa infrastruktur, aturan berupa Markdown, keluaran bisa dicetak | Satu domain mata pelajaran | 7 → 8 | Biaya adopsi hampir nol untuk sebuah sekolah |
| Demo & Storytelling | Seberapa efektif dipresentasikan | Skrip 7:40 dengan tiga titik akuntabilitas | Belum ada video | 3 → 8 | Belum ada yang direkam |
| Innovation & Creativity | Orisinalitas pendekatan | "Tag bukanlah sitasi" + gerbang resolusi | Insight terdokumentasi, gerbangnya belum wajib | 7 → 8 | Insight ini memang jarang di demo RAG |
| UX & Accessibility | Kegunaan dan aksesibilitas | Paket cetak, kuis HTML satu berkas, huruf besar | Tanpa audio, tanpa cek pembaca layar, hanya Bahasa Indonesia | 6 → 7 | Terpakai, belum aksesibel |
| Responsible AI & Ethics | Sumber, izin, persetujuan, batas, rekaman | Lembar akuntabilitas, 4 batas, kegagalan diungkap, D1 diperbaiki terbuka | Bukti kritis 1 dari 7 | 6 → 9 | Desain kuat, bukti tipis |
| Overall Quality | Apakah juri akan memercayainya di organisasinya | Log cacat jujur; cek yang bisa direproduksi | Inkonsistensi antar dokumen (sedang diperbaiki) | 7 → 8 | Kepercayaan datang dari pengungkapan, dan itu ada |

**Di mana nilainya hilang hari ini bukan di desain, melainkan di bukti tangkap:** tiga dimensi
(Technical Execution, Demo & Storytelling, Responsible AI) tertahan oleh screenshot dan video yang
belum ada, bukan oleh kemampuan yang belum ada. Itu mekanis untuk diperbaiki dan merupakan poin
termurah yang tersedia.

---

## D. Persyaratan data & pengujian (handbook §6)

| Persyaratan | Status | Catatan |
|-------------|--------|---------|
| ~20 kasus uji dengan perilaku yang diharapkan | READY | `05_TEST_PLAN.md` (23 kasus, parameter bernama; R001–R012 semuanya terpetakan) |
| Jalankan dan serahkan hasil beserta screenshot | GAP | 0 screenshot |
| Sertakan kegagalan | READY | Dua cacat tercatat (D1, D2); penolakan 29 Okt disimpan |
| Ungkapkan, jangan sembunyikan | READY | Laporan penolakan disertakan; log cacat ditambahkan |
| Bangun di atas dataset bersama | **SELESAI — dikeringankan** | Panitia membebaskan dataset bersama dan kasus ujinya (`BUKTI_KOMITE` §3). Domain sendiri diperbolehkan |
| Uji kejutan 90 detik secara langsung | PARTIAL | Protokolnya tertulis (`05_TEST_PLAN.md` §7); belum pernah dilatih |

---

## E. Daftar klaim yang belum terverifikasi

Apa pun di daftar ini tidak boleh dinyatakan sebagai fakta di submission sampai artefaknya ada.

| ID | Klaim yang kami sandari | Status | Bukti |
|----|-------------------------|--------|-------|
| U1 | Tenggat submission **7 Nov 2026** | **SELESAI** | `01_Dokumen/BUKTI_KOMITE_2026-10-31.md` §2 — pesan panitia 27/10/2026 21:23: "diperpanjang hingga 7 November 2026 (dari jadwal awal 1 November)". Handbook hlm. 13 sudah digantikan |
| U2 | Kasus uji dari peserta diperbolehkan | **SELESAI** | berkas sama §3 — 21/10/2026 09:53: "Untuk dataset dan test case dibebaskan … gunakan data atau skenario mandiri"; ditegaskan lagi 28/10/2026 13:41 |
| U3 | Memakai domain sendiri alih-alih dataset bersama dapat diterima | **SELESAI** | berkas sama §3 — dataset secara eksplisit bisa diringankan. Tidak ada penyimpangan yang perlu diperdebatkan |
| U4 | Run `-001` punya persetujuan guru | VERIFIED | `03_Hasil/edu_output/00_run_config.md`: `APPROVED — Don Jimat Akbar (4 Nov 2026 14:49 GMT+7)`, dikonfirmasi `audit_log.md` §3.7 |
| U5 | "Uji lapangan" sudah terjadi | BERLEBIH — tetapi ko-desain justru KURANG diklaim | Satu guru, satu sesi tinjauan, satu set cetak; bukan uji kelas di seluruh sekolah. Tulis **"ko-desain dan tinjauan bersama satu guru"**. Klaim yang benar dan justru lebih kuat: guru itu yang menyusun substansi rulebook dan memasok referensinya (`04_Diskusi/rencana_persiapan_kategori_C.md` §167 menempatkannya sebagai otoritas domain untuk kedua berkas). Jangan mengklaim uji coba sekolah |
| U6 | Mesin ini berparameter domain | PARTIAL | Benar sejak rulebook v2.0 (tidak ada nomor tag keras), tetapi belum pernah didemonstrasikan pada mata pelajaran kedua |
| U7 | Bagaimana video demo harus diserahkan (berkas, tautan, atau unggahan platform) | **BELUM DIKETAHUI — dicatat 8 Nov 2026** | Handbook §7 (baris 534–643 `01_Dokumen/handbook_text.txt`) menyebut durasi dan isi, tetapi **tidak satu kalimat pun** tentang media penyerahan: tidak ada Google Drive, ZIP, atau penamaan folder. Satu-satunya tautan adalah formulir `forms.gle/y1aHBH4BsrytXDxdA`, dan Google Forms tidak menerima unggahan berkas. Karena itu bentuk serah yang dipakai = **tautan**: unggah `06_Submission/narasi/EduCraft_Demo_narasi_bakar.mp4`, lalu uji tautannya di jendela privat. Pemetaan item mana yang butuh URL ada di `06_Submission/00_SUBMISSION_CHECKLIST.md` §2. Kalau panitia kemudian mengirim instruksi unggah, perbarui baris ini |

---

## F. Klaim yang harus berhenti kita buat

| Klaim di dokumen saat ini | Mengapa harus berubah |
|---------------------------|-----------------------|
| "100% kalimat faktual membawa tag sumber" (`02_Project_Description.md` §3.4) | Sudah dikoreksi: atribusi dan resolusi kini dinyatakan terpisah, dan keduanya lulus di kedua run setelah D1 diperbaiki. Jangan kembali ke klaim satu angka |
| "Run yang jadi acuan adalah `-001`" | Ada dua run dengan status berbeda. Selalu sebut run dan statusnya |
| "Belum ada yang diterbitkan" (`03_Accountability_Sheet.md` §3) | Benar untuk `-003` dan `-004`. `-001` diserahkan ke guru dalam format siap pakai dan paket cetak `-002` didistribusikan terbatas — keduanya setelah persetujuan, tidak ada yang ke publik |
| "Lima format dalam satu run" | Benar hanya untuk `-001` (5 dokumen + 1 kuis interaktif). Kontrak kini memuat enam format dengan aturan "subset apa pun, minimal dua" — sebutkan run dan subset yang benar-benar diminta |
| "Aturan R001–R012 semuanya sudah diuji" | Salah. Tujuh kasus punya bukti artefak, sebelas `BY DESIGN`, tiga `TO RUN`. Lihat `04_Test_Results.md` |
