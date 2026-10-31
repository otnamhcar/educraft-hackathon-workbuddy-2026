# Screenshot Index — Evidence of Use

**Proyek:** EduCraft · **Run verifikasi:** `EDU-CAP-20261030-01` … `-05`
**Diisi oleh:** ______________ · **Tanggal capture:** ______________

> **Penting:** screenshot ini berasal dari **run verifikasi terpisah**, bukan dari run of record
> `EDU-ORCH-20261026-001` (yang artefaknya sudah di-APPROVE). Sebutkan hal ini di
> `06_Submission/04_Test_Results.md` §3.

---

## A. Tujuh adegan wajib (`evidence_bundle/README.md`)

| # | Adegan | File | Run ID | Waktu | Status |
|---|--------|------|--------|-------|--------|
| 1 | Planner menghasilkan outline | `S1_golden_path/S1-01_planner_outline.png` | | | |
| 2 | Writer menghasilkan draft bertag `[src:#]` | `S1_golden_path/S1-02_writer_tags.png` | | | |
| 3 | Reviewer **REJECT** + alasan rule | `S2_refusal_cycle/TC-08_reject-R006.png` | | | |
| 4 | Writer **remediate** | `S2_refusal_cycle/S2-01_remediate.png` | | | |
| 5 | Reviewer **APPROVE** | `S2_refusal_cycle/S2-02_approve.png` | | | |
| 6 | **Human approval** sebelum publish | `S1_golden_path/S1-04_approval_pending.png` | | | |
| 7 | **Escalation** ke manusia | `S3_escalation/TC-13_escalation-3.png` | | | |

---

## B. Test case (20)

Isi `Hasil` dengan `PASS` / `FAIL` / `BELUM`. Untuk `FAIL`, wajib menulis satu baris penjelasan.

| TC | Aturan | File | Hasil | Catatan |
|----|--------|------|-------|---------|
| TC-01 | R001 grounding | `S1_golden_path/S1-02_writer_tags.png` | | |
| TC-02 | R001 `[UNVERIFIED]` | `S3_escalation/TC-02_unverified.png` | | |
| TC-03 | R001 di luar cakupan | `S3_escalation/TC-03_out_of_scope.png` | | |
| TC-04 | R002 fear-mongering | `S4_extras/TC-04_reject-R002.png` | | |
| TC-05 | R002 bahasa berlebihan | `S4_extras/TC-04_reject-R002.png` (boleh sama) | | |
| TC-06 | R003 terlalu teknis | `S4_extras/TC-06_reject-R003.png` | | |
| TC-07 | R003 detail traumatis | — | | |
| TC-08 | R006 klaim permanen **(kritis)** | `S2_refusal_cycle/TC-08_reject-R006.png` | | |
| TC-09 | R006 efikasi absolut **(kritis)** | `S2_refusal_cycle/TC-08_reject-R006.png` (boleh sama) | | |
| TC-10 | R007 instruksi berbahaya **(kritis)** | `S2_refusal_cycle/TC-10_reject-R007.png` | | |
| TC-11 | R005 solutif | `S1_golden_path/S1-03_reviewer_verdict.png` | | |
| TC-12 | siklus reject→remediate→approve | `S2_refusal_cycle/TC-12a_v1_reject.png`, `TC-12b_v2_approve.png` | | |
| TC-13 | eskalasi 3 iterasi | `S3_escalation/TC-13_escalation-3.png` | | |
| TC-14 | approval gate **(kritis)** | `S1_golden_path/S1-04_approval_pending.png` | | |
| TC-15 | prompt injection **(kritis)** | `S3_escalation/TC-15_injection-ignored.png` | | |
| TC-16 | ≥2 format | `S1_golden_path/S1-06_quiz_feedback.png` | | |
| TC-17 | konsistensi ID/EN | `S4_extras/TC-17_bilingual.png` | | |
| TC-18 | validasi teks gambar **(kritis)** | `S4_extras/TC-18_image_text.png` | | |
| TC-19 | sitasi rule saat reject | `S2_refusal_cycle/TC-19_citation.png` | | |
| TC-20 | kelengkapan audit log | `S1_golden_path/S1-05_audit_log.png` | | |

---

## C. Rekapitulasi (isi setelah selesai)

| Status | Jumlah |
|--------|--------|
| PASS | |
| FAIL | |
| BELUM | |
| **Total** | **20** |

Pastikan angka ini **sama** dengan scoreboard di `06_Submission/04_Test_Results.md` §1.
Kalau beda, perbaiki dulu sebelum submit.

---

## D. Catatan kegagalan (jika ada)

| TC | Apa yang terjadi | Apa yang dilakukan | Disclose di |
|----|------------------|--------------------|-------------|
| | | | `04_Test_Results.md` §4 |
