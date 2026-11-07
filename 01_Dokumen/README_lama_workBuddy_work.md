# EduCraft — AI Teaching Assistant IPAS SD (Kurikulum Merdeka)

> **⚠️ ARSIP — JANGAN DIPAKAI SEBAGAI RUJUKAN (ditandai 7 November 2026).**
> Dokumen ini disimpan sebagai riwayat penyusunan, bukan dokumentasi mutakhir. Isinya sudah
> kedaluwarsa di tiga hal: **rulebook kini R001–R012 v2.0** (bukan R011), **tenggat sudah tiba**
> (bukan "≤ 3 hari ke depan"), dan gambaran pipeline kini ada di `07_Dokumentasi/00_INDEX.md`.
> Rujukan yang benar: `README.md` (gambaran publik), `06_Submission/00_SUBMISSION_CHECKLIST.md`
> (status submission), `08_Referensi/rulebook_ipas.md` (aturan yang berlaku).

> **Status:** Tahap uji lapangan (field testing). Target submit ke panitia hackathon: **≤ 3 hari ke depan**.
> **Domain:** SD–IPAS, Kurikulum Merdeka — Fase B (kelas III–IV) & Fase C (kelas V–VI) ONLY.
> **Engine:** Multi-agent pipeline (Orchestrator → Planner → Writer → Reviewer) dengan guardrail rulebook R001–R011.

---

## 1. Cara Cepat Mulai (untuk tim uji lapangan)
Buka folder **`hasil_akhir/`** — ini pintu masuk utama. Isinya:
- `hasil_akhir/materi_ajar/` — draf final siap uji: RPP, kuis (pre/post + kunci), slide, artikel, brief infografis, dan `quiz_interaktif.html`.
- `hasil_akhir/panduan/` — panduan guru & panduan demo/testimoni.
- `hasil_akhir/referensi/` — sumber fakta resmi: `source_material_ipas.md`, `rulebook_ipas.md`, `cp_ipas.md`.
- `hasil_akhir/audit/` — `audit_log_edu_orchestrator.md` (jejak Planner→Writer→Reviewer).

**Coba kuis interaktif:** buka `hasil_akhir/materi_ajar/quiz_interaktif.html` di browser.

---

## 2. Peta Folder (akar `workBuddy_work`)
| Folder | Isi | Catatan |
|--------|-----|---------|
| **`hasil_akhir/`** | **Draf final + panduan + referensi + audit (SALINAN)** | Fokus utama tim. Aman, tidak menghapus sumber. |
| `2026-10-26-18-30-04/` | Sesi terakhir EduCraft (sumber asli `edu_output/`) | Asal draf final. |
| `2026-10-23-14-33-14/` | Panduan guru, panduan demo, blueprint, quiz interaktif (versi lama), audit lama | Referensi pengembangan. |
| `2026-10-21-13-47-45/` | **`skills_package/`** (engine agent), `source_material_ipas.md`, `rulebook_ipas.md`, `evidence_bundle/` | Bukti proses & kode skill. |
| `2026-10-13-14-06-17/` | Analisis kurikulum, contoh prompt, matriks test case | Dokumentasi desain. |
| `2026-10-08-09-45-47/` | Output SlideForge (mockup SVG + spec) | Aset desain. |
| `2026-10-07-08-52-20/` | (kosong/最小) | Arsip sesi. |
| `2026-10-02-06-06-40/` | `Fix_poster_revised.jpg`, `replace_qr.py` | Aset poster awal. |
| `2026-09-30-11-37-01/` | `outputs/` (sesi perdana) | Arsip sesi. |
| `sumber hackton/` | **PDF resmi**: Panduan IPAS Revisi 4 (3 Okt 2025), Permendikdasmen 13/2025 + hasil ekstraksi `.txt` | Sumber hukum & kurikulum asli. |
| `Claw/` | **Kosong (0 byte)** | Bisa diabaikan / dihapus saat finalisasi. |

> **Penting:** Folder `2026-*-*/.workbuddy-ai/` adalah data project (memori/state). **JANGAN dihapus** — diperlukan bila sesi dibuka kembali.

---

## 3. Bukti Proses untuk Submission
Panitia biasanya menuntut bukti pipeline & audit. Lokasi utama:
- `2026-10-21-13-47-45/evidence_bundle/` (workflow, hasil, screenshot, audit) — **utuh, jangan diubah**.
- `hasil_akhir/audit/audit_log_edu_orchestrator.md` — ringkasan jejak agent terbaru.
- `2026-10-23-14-33-14/audit_log.md` — catatan run sebelumnya.

---

## 4. Alur Kerja (singkat)
1. **Planner** → susun outline (RPP, kuis, slide) terikat CP.
2. **Writer** → draf narasi, semua klaim ber-tag `[src:#]`.
3. **Reviewer** → evaluasi terhadap R001–R011; REJECT bila melanggar, maks 3 iterasi lalu eskalasi.
4. **Approval Guru** → publish (belum dilakukan untuk draf terbaru — lihat status di `hasil_akhir/audit/`).
5. **Log** → audit tersimpan.

---

## 5. Catatan untuk Tim
- Semua materi berbahasa Indonesia, usia SD (8–12 tahun), tone hangat & solutif.
- Konteks aktual (PLTS Cirata, Net Sink 2030) merujuk sumber resmi ber-tag `[src:CA#]`.
- Bila menemukan fakta di luar sumber, TIDAK diubah sembarangan — rujuk guru/SME.

---
*Dokumen ini dibuat otomatis saat merapikan folder untuk berbagi tim (2026-10-27).*
