# EduCraft — Proyek Hackathon Tencent Cloud Indonesia 2026

> **Peta navigasi proyek, bukan dokumen submission.** Untuk isi yang dikirim ke juri, mulai dari
> `06_Submission/00_SUBMISSION_CHECKLIST.md`; untuk gambaran publik, `README.md`.
>
> **Penanda waktu.** Bagian 1–5 ditulis 29–30 Oktober 2026 sebagai catatan konsolidasi dan **sengaja
> dibiarkan apa adanya** — itu potret keadaan saat itu, bukan keadaan sekarang. Yang diperbarui
> 7 November 2026 adalah bagian 6, dan bagian 7 menjelaskan apa saja yang sudah berubah sejak 30 Oktober.
> Kalau ada selisih antara bagian lama dan bagian 7, **bagian 7 yang berlaku**.

## 1. Apa itu EduCraft?
- **Produk:** AI Teaching Assistant untuk mata pelajaran **IPAS SD** (Kurikulum Merdeka).
- **Hackathon:** Tencent Cloud Hackathon Indonesia 2026.
- **Status:** Tahap uji lapangan (field testing). **Deadline submit: 7 November 2026** (perpanjangan panitia; dikonfirmasi guru 30 Okt 2026, sebelumnya 1 Nov 2026).
- **Domain ketat:** SD–IPAS, Kurikulum Merdeka — **Fase B (kelas III–IV) & Fase C (kelas V–VI) SAJA**.
- **Engine:** Multi-agent pipeline (Orchestrator → Planner → Writer → Reviewer) dengan guardrail **rulebook R001–R011** — *sejak 31 Okt menjadi R001–R012; lihat §7*.

## 2. Struktur Proyek (self-contained)
```
EduCraft_Hackathon_2026/
├── PROJECT.md                          # Index utama (file ini)
├── .workbuddy-ai/memory/               # Memori proyek (terisolasi)
│   ├── MEMORY.md
│   ├── 2026-10-29.md
│   └── 2026-10-30.md
├── 01_Dokumen/                         # Dokumen resmi & panduan
│   ├── Tencent_Cloud_Hackathon_Indonesia_2026_Handbook.pdf
│   ├── handbook_text.txt               # Ekstraksi teks handbook
│   ├── CARA_IMPORT_SKILL.md
│   └── README_lama_workBuddy_work.md
├── 02_Sumber/                          # Sumber kurikulum resmi
│   ├── Final Panduan Mata Pelajaran IPAS_03_10_2025_Revisi 4.pdf
│   ├── Permendikdasmen-no-13-tahun-2025.pdf
│   ├── 1. Panduan Penilaian SMP - Cetakan Keempat 2017.pdf
│   ├── centralpendidikan.com 1-6. rpp 1 lembar ipa kelas 7.docx
│   ├── centralpendidikan.com RPP IPA KEL 7 SEM 1.rar
│   ├── extract_pdf.py
│   └── extracted/                      # Hasil ekstraksi .txt
├── 03_Hasil/                           # Draf final + output asli
│   ├── materi_ajar/                    # [Run Energi] RPP, kuis pre/post, slide, artikel, brief, quiz_interaktif.html
│   ├── panduan/                        # Panduan Guru, Panduan Demo/Testimoni
│   ├── referensi/                      # source_material_ipas.md, rulebook_ipas.md, cp_ipas.md, konteks_aktual.md
│   ├── audit/                          # audit_log_edu_orchestrator.md + review kepatuhan R001–R011
│   ├── edu_output/                     # [Run Energi] output asli 8 file
│   └── edu_output_wujud_zat/           # [Run Wujud Zat] 17 file — lihat §6A
├── 04_Diskusi/                         # Catatan analisis & diskusi
│   ├── analisis_hackathon.md
│   ├── dokumentasi_diskusi.md
│   ├── rencana_persiapan_kategori_C.md
│   └── test_cases_matrix.md
└── 05_Bukti_Proses/                    # Engine & bukti pipeline (untuk submission)
    ├── skills_package/                 # Kode engine agent
    ├── evidence_bundle/                # Bundel bukti proses
    ├── edu-creator-agent-skills.zip
    └── make_evidence_bundle.py
```

## 3. Verifikasi Integritas (29 Okt 2026)
Salinan diverifikasi dengan membandingkan jumlah file sumber vs tujuan — **semua cocok**:

| Material | Sumber | Salinan | Status |
|----------|--------|---------|--------|
| sumber hackton | 13 | 13 | OK |
| hasil_akhir | 12 | 12 | OK |
| edu_output | 8 | 8 | OK |
| skills_package | 10 | 10 | OK |
| evidence_bundle | 5 | 5 | OK |

Total file proyek saat konsolidasi: **61**. File asli di `workBuddy_work/` **tidak dihapus**.
> Per 30 Okt 2026 18:07 total sudah **103 file / 16 MB** (bertambah karena run materi ajar Wujud Zat + paket cetak).

## 4. Cara Pakai (agar tidak campur aduk)
1. Saat buka obrolan baru tentang EduCraft/hackathon, arahkan workspace ke folder
   folder kerja hackathon di mesin Windows (dulu `D:/…/EduCraft_Hackathon_2026/`); sejak 5 Nov juga repo git di mesin Linux.
2. Setiap sesi selesai, minta AI merangkum ke `04_Diskusi/` dan update `MEMORY.md`.
3. Jangan mulai diskusi hackathon di workspace proyek lain.

## 5. Langkah Berikutnya
- [x] Konsolidasi: material lama disalin ke `01–05_*` (proyek self-contained).
- [x] Definisikan formal **R009–R011** di rulebook (3 salinan) + selaraskan SKILL & catatan diskusi. Rulebook kini resmi R001–R011.
- [x] Verifikasi rulebook R001–R011 di draf final. **APPROVE** setelah remediasi: source material energi (`[src:1–9]`) + `konteks_aktual.md` (CA1/CA6) + koreksi 145 MWac/192 MWp. Laporan: `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-30_REVISI.md`.
- [x] Siapkan bundel submission final (bukti pipeline + audit) dari `05_Bukti_Proses/`. **SELESAI 30 Okt 2026** → lihat §6.

## 6. Bundel Submission (30 Okt 2026)
Semua 11 item wajib/opsional handbook §7 sudah disusun di `06_Submission/`.

| Item handbook | Status | File |
|---------------|--------|------|
| Project title | READY | `01_Title_Blurb.md` |
| Short blurb (<10 kata) | READY | `01_Title_Blurb.md` (8 kata, EN + ID) |
| Project description (4 bagian) | READY | `02_Project_Description.md` |
| Accountability sheet (1 halaman) | READY | `03_Accountability_Sheet.md` |
| Test results + screenshot | PARTIAL | `04_Test_Results.md` — tabel 20 TC siap, **screenshot belum** |
| Architecture diagram | READY | `architecture_diagram.png` (2720×3000) + `.html` + `05_Architecture.md` |
| Demo video 5–8 menit | TODO | skrip siap: `07_Demo_Video_Script.md` (7:20) |
| Product sharing | READY | `06_Product_Sharing.md` |
| Source code / workflow | READY | Repo publik (MIT): `github.com/otnamhcar/educraft-hackathon-workbuddy-2026` — 88 file, push 31 Okt 2026 |
| Cover image 16:9 | READY | `cover_image_380x216.png`, `cover_image_1280x720.png` |
| Project link (bonus) | TODO | opsional |

**Tambahan:** `EduCraft_Deck.pptx` (11 slide, tema cover) untuk Demo Day · `10_Submission_Form_CopyPaste.txt` (teks siap tempel) · `00_SUBMISSION_CHECKLIST.md` (kendali akhir) · `11_Screenshot_Capture_Runbook.md` (runbook 4 sesi capture) · `12_Capture_Prompts.txt` (prompt siap-tempel).

**Bukti screenshot:** folder sesi + pelacak sudah disiapkan di `05_Bukti_Proses/evidence_bundle/03_screenshots/` (`S1_golden_path`, `S2_refusal_cycle`, `S3_escalation`, `S4_extras`, `INDEX.md`).

**Bundle ZIP:** `EduCraft_Submission_Bundle_2026-10-30.zip` (60 entri, 2,76 MB) — berisi `06_Submission/`, `03_Hasil/`, `skills_package/`, `PROJECT.md`. ⚠️ Dibuat 16:14; **belum memuat** `03_Hasil/edu_output_wujud_zat/` (§6A).

**Yang masih harus dikerjakan manusia:**
1. Screenshot 5 test case P0 (TC-08, 10, 14, 15, 18) → `05_Bukti_Proses/evidence_bundle/03_screenshots/`. Ikuti `11_Screenshot_Capture_Runbook.md`.
2. Rekam demo video sesuai skrip.
3. ~~Publikasikan repo~~ — **selesai 31 Okt 2026**: `github.com/otnamhcar/educraft-hackathon-workbuddy-2026` (publik, MIT).
4. **Dua lapis persetujuan yang harus dibedakan:** (a) *materi ajar* Wujud Zat sudah disetujui guru 30 Okt 2026 17:19 → lihat §6A; (b) *bundel submission* belum final — masih menunggu screenshot, video, dan repo.

## 6A. Paket Materi Ajar — Perubahan Wujud Zat (30 Okt 2026)

Run `EDU-ORCH-20261030-002` · Topik **Perubahan Wujud Zat** · Sasaran **Fase C (V–VI)**, status *pemantapan lintas fase* (CP-B.1.1.4 + CP-C.2.2).
Folder: `03_Hasil/edu_output_wujud_zat/` (17 file).

| File | Isi | Status |
|------|-----|--------|
| `00_plan.md` | Outline Planner + traceability CP + gap yang ditandai | ✅ |
| `01_artikel.md` | Artikel 400 kata, 6 bagian | ✅ APPROVE |
| `02_infographic_brief.md` | Brief infografis 6 blok | ✅ APPROVE |
| `03_infografis_wujud_zat.png` | Infografis 1080×1350 (+ `.html` sumber) | ✅ APPROVE |
| `03_video_storyboard.md` | Storyboard 6 adegan + naskah 4:45 | ✅ APPROVE |
| `04_kuis_prepost.md` | 27 butir + kunci + pedoman skor | ✅ APPROVE |
| `05_review.md` | 2 pass review R001–R011 + review lembar kerja | ✅ |
| `06_quiz_interaktif.html` | Kuis digital | ✅ |
| `07_video_animatik.html` | Animatik 6 adegan, 4:45 | ⚠️ belum bersuara |
| `08_Paket_Siswa_Cetak.pdf` | Paket siswa 7 hlm (tanpa kunci) | ✅ DISETUJUI |
| `09_Paket_Guru_Cetak.pdf` | Paket guru 4 hlm (kunci + tabel skor) | ✅ DISETUJUI |
| `10_Lembar_Kerja_Pengamatan.pdf` | Lembar kerja es–air 3 hlm | ✅ APPROVE |
| `audit_log.md` | Audit run (Planner→Writer→Reviewer, approval) | ✅ |

**Status uji:** versi siswa dinyatakan OK oleh guru (30 Okt 2026); versi guru **belum diuji lapangan** (rencana 31 Okt 2026).
**Catatan integritas:** tidak ada angka suhu di seluruh paket — sumber tidak memuat titik lebur/didih.

## 7. Di Mana Semua File Tersimpan (peta lokasi)

| Lokasi | Isi | Path absolut |
|--------|-----|--------------|
| **1. Proyek (utama)** | Semua deliverable: dokumen, hasil, bukti, submission, ZIP | folder kerja hackathon di mesin Windows (dulu `D:/…/EduCraft_Hackathon_2026/`); sejak 5 Nov juga repo git di mesin Linux |
| **2. Memori proyek** | Konteks jangka panjang + log harian proyek ini | `EduCraft_Hackathon_2026/.workbuddy-ai/memory/` (`MEMORY.md`, `2026-10-29.md`, `2026-10-30.md`) |
| **3. Memori workspace** | Log sesi obrolan lama (workspace 2026-10-29) | di mesin Windows; **tidak ikut repo** — sejak 5 Nov memori proyek ada di repo ini, `.workbuddy-ai/memory/` |
| **4. Transkrip obrolan mentah** | Log lengkap percakapan (JSONL, ditulis otomatis) | folder proyek WorkBuddy di mesin Windows — **tidak disertakan di repo**, isinya percakapan pribadi |
| **5. Material asli (arsip)** | Sumber lama 9 folder sesi + `sumber hackton/` + `hasil_akhir/` — **tidak dipindah/dihapus** | folder `workBuddy_work/` di mesin Windows |
| **6. Handbook asli** | PDF handbook dari panitia | di mesin Windows; **tidak ikut repo** — handbook panitia tidak untuk dipublikasikan ulang (`.gitignore` menutupnya) |

**Aturan:** kalau mulai obrolan baru tentang hackathon, buka workspace di **lokasi 1**. Jangan mulai dari `workBuddy_work/` — di sana tidak ada memori proyek, jadi konteks akan tercampur lagi seperti sebelumnya.

**Status ukuran (30 Okt 2026, 18:07):** **103 file · 16 MB**. ZIP submission terakhir: `EduCraft_Submission_Bundle_2026-10-30.zip` (60 file, 2,76 MB) — ⚠️ **dibuat 16:14, belum memuat paket Wujud Zat (§6A)**. Perlu dibuat ulang sebelum diunggah.

---

## 8. Keadaan 7 November 2026 — yang berubah sejak §1–§7 ditulis

Bagian di atas adalah potret 29–30 Oktober. Ini selisihnya, dan **selisih inilah yang berlaku**:

| Hal | 30 Okt (ditulis di §1–§7) | 7 Nov (keadaan sebenarnya) |
|---|---|---|
| Rulebook | R001–R011 | **R001–R012 v2.0** — R012 (klaim komersial/halal) ditambahkan 31 Okt |
| Jumlah run | 4 | **11 run** tercatat; `doctor.py` memeriksa semuanya |
| Folder hasil | `03_Hasil/materi_ajar`, `edu_output`, `edu_output_wujud_zat`, `edu_output_tata_surya` | bertambah `edu_output_wujud_zat_faseC`, `edu_output_energi_alternatif*` (`-007`…`-010`) |
| Screenshot | belum ada yang diambil | **12 wajib lengkap**, `check_capture.py` 20/0/2, semuanya lolos cek mata |
| Video demo | belum mulai | skrip 7:55 + naskah narasi 3 take + `subtitle.srt` + `concat_video.py` + `attach_narration.py`; **rekaman belum disambung** |
| Pemeriksa | `doctor.py` 11 checks | **19 passed / 0 failed / 0 warning** |
| Nama guru | tertulis apa adanya | **nama samaran**; identitas asli tidak ditampilkan, dan itu dinyatakan di artefak publik |
| Lokasi kerja | satu folder di mesin Windows | repo git di Linux Mint + mesin Windows untuk rekaman; semua path `D:/`/`C:/` di §7 sudah tidak relevan dan sengaja dibiarkan sebagai arsip |
| Status submission | 8 dari 11 item | **9 siap · 1 finalisasi di luar repo (video) · 1 draf lokal (demo_site)** |

Untuk status per item, **jangan** pakai §5 di atas — pakai `06_Submission/00_SUBMISSION_CHECKLIST.md`.
Untuk peta dokumentasi, `07_Dokumentasi/00_INDEX.md`.

**Catatan soal repo publik.** Dokumen ini disertakan di repo karena ia memperlihatkan cara kerja tim,
bukan karena ia akurat sebagai rujukan mutakhir. Bagian §4–§5 adalah riwayat; mengubahnya agar "terlihat
benar" akan menghapus justru hal yang membuatnya berguna.
