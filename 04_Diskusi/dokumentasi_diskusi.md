# Dokumentasi Diskusi — Persiapan Hackathon Tencent Cloud Indonesia 2026 (Kategori C)

> **Dokumen ini** merangkum seluruh diskusi persiapan tim untuk lomba *AI CAN DO IT — Tencent Cloud Hackathon Indonesia 2026*, difokuskan pada **Kategori C (The Creator Agent)**.
> Tujuannya sebagai arsip tim dan pelengkap dokumentasi resmi.

---

## Metadata
| Field | Isi |
|-------|-----|
| Tanggal diskusi | 21 Oktober 2026 (GMT+7) |
| Peserta | Tim edukator (pendidik + guru) & Asisten AI (peran: Senior AI Engineer — spesialisasi Agent Orchestration) |
| Sumber utama | `Tencent_Cloud_Hackathon_Indonesia_2026_Handbook.pdf` (19 halaman) |
| Status | **Checkpoint** — sedang dievaluasi tim; belum masuk tahap build |

---

## 1. Ringkasan Eksekutif
Tim edukator memutuskan mengikuti **Kategori C — The Creator Agent**, membangun sistem agen AI (Planner → Writer → Reviewer) yang menghasilkan konten edukasi multi-format dengan guardrail kepatuhan yang ketat. Topik yang diusulkan & disetujui sementara: **IPAS (SD 5–6) — Dampak Kebakaran Hutan di Kalimantan**. Prinsip desain utama: **content-agnostic** (sistem menerima source + rulebook apa pun, karena test case resmi di kickoff menggunakan dataset bersama).

---

## 2. Kronologi Diskusi

### 2.1 Klarifikasi Event (Awal)
- **Pertanyaan awal:** Apakah asisten mengetahui event "teensen hackathon" dengan WorkBuddy?
- **Hasil:** Tidak ditemukan event bernama "teensen" secara spesifik. Yang terindeks: WorkBuddy adalah workstation AI kantor dari Tencent, dengan kampanye *back-to-school* 2026 (hingga 31 Okt 2026).
- **Tindakan:** User melampirkan handbook resmi → diskusi berlanjut ke analisis teknis.

### 2.2 Analisis Handbook (Teknis + 3 Kategori)
- Ekstraksi PDF (19 hlm) via `pdfplumber` → `handbook_text.txt` → dianalisis.
- **Temuan inti:**
  - Lomba: bangun **Agentic AI Solution** pakai WorkBuddy; **"No deep coding required"**; fokus = desain agen yang *accountable*.
  - **5 Aturan Akuntabilitas** (berlaku semua kategori): (1) Shows sources, (2) Stays within permissions, (3) Asks before acting, (4) Admits limits, (5) Keeps a record.
  - Landasan hukum: **PP 33/2026** (eff. 16 Jan 2027) mewajibkan DPIA saat AI proses data pribadi.
  - **Testing:** ~20 test case/kategori + **live surprise test 90 detik** di Demo Day. 1 *critical failure* → Responsible AI di-cap 5/10.
  - **Timeline:** Kick-off 15 Okt · Training 15 Okt–1 Nov · **Deadline 1 Nov** · Finalis 10 Nov · **Demo Day 27 Nov 2026**.
  - **Penilaian:** 10 dimensi × 10 = 100; satu prize pool; hadiah s.d. USD 1.200 + credit.
- **3 Kategori (dikaji):**
  - **A — Workplace Brain:** asisten pengetahuan RAG + access control (HR/ops/public).
  - **B — Office Agent:** dekomposisi request → approval gate (admin/finance/founder).
  - **C — Creator Agent:** tim ≥3 agen pembuat konten + rule-based guardrails (marketer/creator/educator). → **Dipilih.**

### 2.3 Pemilihan Kategori C + Rencana Persiapan
- **Alasan pilih C:** latar edukator sangat cocok; skenario *Learning Content* paling natural.
- Disusun `rencana_persiapan_kategori_C.md`: arsitektur orchestration, pemetaan WorkBuddy (Custom Skills/Automation/Memory), prompt per agen, test matrix, submission plan, sprint timeline, risk register.

### 2.4 Usulan & Evaluasi Topik IPAS
- **Usulan user:** Mapel IPAS dengan tema kebakaran hutan Kalimantan (alam, ekonomi, kesehatan).
- **Verdict asisten:** **Masuk akal & kuat.** Alasan: pas skenario Learning Content; memberi lapangan uji kaya untuk Reviewer (klaim berlebihan ~ analog aturan BPOM); relevan nasional.
- **Refinement diberikan:**
  - Kelola cakupan (3 sub-topik → 1 modul via Planner).
  - Source material harus *grounded* & tersitasi (KLHK/BMKG/BPS/Kemenkes).
  - Rulebook domain (no unverified stats, no fear-mongering, age-appropriate SD, curriculum alignment, balanced/solutif, health-claim caution).
  - **Catatan teknis penting:** test case kickoff pakai dataset bersama → rancang **content-agnostic**.

### 2.5 Pembaruan Rencana + Artefak
- `rencana_persiapan_kategori_C.md` diperbarui: kunci topik IPAS, prinsip content-agnostic, pemetaan WorkBuddy ke file source/rulebook.
- Artefak baru:
  - `source_material_ipas.md` — 8 blok fakta ber-tag `[src:1]…[src:8]` (mock/ilustratif).
  - `rulebook_ipas.md` — R001–R011 rujukan Reviewer + contoh penerapan.

### 2.6 Checkpoint
- User menunda untuk evaluasi tim; meminta dokumentasi diskusi ini.

---

## 3. Keputusan yang Telah Dikunci (Locked)
| # | Keputusan | Catatan |
|---|-----------|---------|
| 1 | Ikut **Kategori C — The Creator Agent** | Cocok latar edukator |
| 2 | Skenario **Learning Content** | 1 topik → lesson plan + quiz + slide outline |
| 3 | Topik: **IPAS (SD 5–6) — Karhutla Kalimantan** | Alam, ekonomi, kesehatan |
| 4 | Arsitektur: **Orchestrator + Planner/Writer/Reviewer** | Loop max 3 → eskalasi manusia |
| 5 | **Human approval** wajib sebelum publish | Akuntabilitas #3 |
| 6 | Prinsip **content-agnostic** | Test case kickoff = dataset bersama |
| 7 | Artfak `source_material_ipas.md` & `rulebook_ipas.md` | Siap dimasukkan WorkBuddy |

---

## 4. Hal Kritis yang Perlu Diingat (Rubrik)
- **Critical failure** (klaim terlarang / eksekusi tanpa izin) → **Responsible AI & Ethics cap 5/10**. Desain HITL & Reviewer = prioritas.
- **Demo video 5–8 mnt** wajib tunjukkan ≥1 siklus *reject→remediate→approve* + ≥1 *escalate ke manusia*.
- Juri menghargai **agent design / orchestration / responsible AI**, bukan production-grade engineering. Mock data diperbolehkan.
- Source code bisa berupa **exported WorkBuddy workflow + bukti pemakaian**.

---

## 5. Item Terbuka / Tindak Lanjut
- [ ] Tim validasi & lengkapi `source_material_ipas.md` (opsi: data resmi KLHK/BMKG/BPS/Kemenkes).
- [ ] Guru/SME finalisasi `rulebook_ipas.md` (terutama R004 curriculum alignment).
- [ ] Draft prompt final Planner/Writer/Reviewer.
- [ ] Simulasi alur (proof of concept) — jalankan Planner→Writer→Reviewer.
- [ ] F2 Build di WorkBuddy (Custom Skills + Automation).
- [ ] Penyusunan 20 test case + screenshot.
- [ ] Penyiapan deliverables (accountability sheet, architecture diagram, demo video).

---

## 6. Daftar Artefak / Dokumen yang Dihasilkan
| File | Isi |
|------|-----|
| `analisis_hackathon.md` | Analisis teknis handbook + bedah 3 kategori |
| `rencana_persiapan_kategori_C.md` | Rencana persiapan lengkap Kategori C (updated dgn topik IPAS) |
| `source_material_ipas.md` | Product sheet / sumber fakta tunggal (8 blok, tag `[src:#]`) |
| `rulebook_ipas.md` | Aturan domain R001–R011 rujukan Reviewer |
| `handbook_text.txt` | Hasil ekstraksi teks PDF (arsip) |
| `dokumentasi_diskusi.md` | **Dokumen ini** |

---

## 7. Catatan untuk Tim
- Semua file berada di folder kerja lomba: `D:\DataSheet\Ai_Skill\workBuddy_work\2026-10-21-13-47-45\`
- Angka dalam `source_material_ipas.md` bersifat **ilustratif/mock** (sesuai izin mock data handbook) — bukan data resmi; dapat diganti dengan data resmi bila diinginkan.
- Diskusi dilanjutkan setelah evaluasi tim; titik sambung berikutnya: **F1 finalisasi** atau **simulasi alur**.

---
*Dokumentasi dibuat 21 Okt 2026 sebagai checkpoint diskusi. Akan diperbarui seiring progres tim.*
