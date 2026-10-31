# Submission Checklist — Tencent Cloud Hackathon Indonesia 2026

**Project:** EduCraft · **Challenge:** C — The Creator Agent
**Deadline:** 7 November 2026 — committee message 27/10/2026 21:23, quoted in
`01_Dokumen/BUKTI_KOMITE_2026-10-31.md` §2 · **Internal submit target: 5 November 2026** · **Prepared:** 30 October 2026
**Form:** https://forms.gle/y1aHBH4BsrytXDxdA

Legend: `READY` = artefact exists in this bundle · `TODO` = must be done by the team · `BLOCKED` = waiting on someone else

---

## 1. The 11 required items

| # | Item (handbook §7) | Req. | Status | File / action |
|---|--------------------|------|--------|---------------|
| 1 | Project title | REQUIRED | **READY** | `01_Title_Blurb.md` |
| 2 | Short blurb, under 10 words | REQUIRED | **READY** | `01_Title_Blurb.md` (8 words, EN + ID) |
| 3 | Project description (4 parts) | REQUIRED | **READY** | `02_Project_Description.md` |
| 4 | Accountability sheet (one page) | REQUIRED | **READY** | `03_Accountability_Sheet.md` |
| 5 | Test results **with screenshots** | REQUIRED | **PARTIAL** | Table ready in `04_Test_Results.md`; **screenshots still TODO** (§3 below) |
| 6 | Architecture diagram | REQUIRED | **READY** | `architecture_diagram.png` (2720×3000) + `.html` + `05_Architecture.md` |
| 7 | Demo video, 5–8 min | REQUIRED | **TODO** | Script `07_Demo_Video_Script.md` (7:20) + production runbook `13_Demo_Video_Runbook.md`. 7 of 10 scenes recordable now; 3 need the agent live |
| 8 | Product sharing | REQUIRED | **READY** | `06_Product_Sharing.md` |
| 9 | Source code / exported workflow | REQUIRED | **READY** | Public repo (MIT): https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026 — 100+ files |
| 10 | Cover image (optional, 16:9) | OPTIONAL | **READY** | `cover_image_380x216.png` + `cover_image_1280x720.png` |
| 11 | Project link (bonus) | BONUS | **TODO** | Optional live demo URL |

**Score: 8 ready · 1 partial · 2 todo.** The remaining partial is test evidence — the one judges
weigh heaviest — so do not submit on the strength of the document count.

---

## 2. Ready to paste

`10_Submission_Form_CopyPaste.txt` — plain-text blocks for every form field, in order.
Open it next to the form and paste section by section. Do not reformat.

---

## 3. Screenshots — what to capture (P0 first)

> **Cara mengambilnya:** ikuti `11_Screenshot_Capture_Runbook.md` — 4 sesi run, ± 2 jam 45 menit,
> dengan prompt siap-tempel di `12_Capture_Prompts.txt`. Jangan menjalankan pipeline 20 kali;
> satu sesi menghasilkan beberapa screenshot sekaligus.
> Pelacak hasil: `05_Bukti_Proses/evidence_bundle/03_screenshots/INDEX.md`.

Save to `05_Bukti_Proses/evidence_bundle/03_screenshots/`, name as shown.

| Priority | Case | Filename | What must be visible in frame |
|----------|------|----------|-------------------------------|
| P0 | TC-08 | `TC-08_reject-R006.png` | The `REJECT` verdict, rule `R006`, the quoted sentence |
| P0 | TC-10 | `TC-10_reject-R007.png` | Refusal to write burning instructions, rule cited |
| P0 | TC-14 | `TC-14_approval-gate.png` | `publish_status: PENDING` after an APPROVE |
| P0 | TC-15 | `TC-15_injection-ignored.png` | Embedded instruction ignored + user notified |
| P0 | TC-18 | `TC-18_image-text-check.png` | Validation of text on a generated image |
| P1 | TC-02 | `TC-02_unverified-token.png` | `[UNVERIFIED]` emitted instead of a guess |
| P1 | TC-12 | `TC-12_loop-v1-v2.png` | v1 rejected → v2 approved, same screen |
| P1 | TC-13 | `TC-13_escalation-3.png` | Iteration counter at 3, halt message |
| P1 | TC-21 | `TC-21a_reject-R012.png`, `TC-21b_rules_na-R012.png` | `REJECT` naming R012 and all three sub-clauses (efficacy, halal without certificate, superlative); then `rules_na: R012` **with a reason** on clean material |
| P2 | TC-06, TC-09, TC-11, TC-17 | — | As available |

**Rule for all screenshots:** the rule ID and the quoted text must both be readable at 100% zoom
on a 1080p laptop. If a judge has to squint, it does not count.

---

## 4. Code publication — ✅ DONE (Option A)

**Public GitHub repo:** https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026
MIT licence · 118 tracked files · HEAD `b56104f`, pushed 31 October 2026.

Published contents: `README.md` (front page, including a **"Run it yourself"** path written for a
teacher rather than a developer), `05_Bukti_Proses/skills_package/` (four contracts + full knowledge
assets), `03_Hasil/` (both runs, both review reports), `06_Submission/`,
`04_Diskusi/test_cases_matrix.md`, `tools/` (grounding check, `install_skills.py`, `doctor.py` — all Python, all cross-OS),
`LICENSE`, `THIRD_PARTY_NOTICES.md`.

**Also published: the two official ministry PDFs** the knowledge layer is built from — *Panduan Mata
Pelajaran IPAS* (Revisi 4) and *Permendikdasmen 13/2025* — plus their text extractions, in
`02_Sumber/`. Reason: the grounding check is only verifiable if a reader can open the page a claim
came from. They sit outside the MIT licence and are carved out in `THIRD_PARTY_NOTICES.md`.

Deliberately **not** published, with a reason per file in `02_Sumber/README.md`: six
`centralpendidikan.com` RPP worksheets, the SMP assessment guide, a WhatsApp export, the organiser's
handbook, `.workbuddy-ai/` and working notes. Enforced by `.gitignore` in the repo root.

**Verified 31 October 2026:** a fresh `git clone` of `main` installs the four skills and passes
`tools/doctor.py` — `8 passed / 0 failed / 0 warning`, exit 0.

Remaining housekeeping: re-run the push after any further edit, so the repo and the bundle match.

---

## 5. Ethics gate (do not skip)

| Check | Status |
|-------|--------|
| Run `-002` reviewed and approved by a teacher | **HOLDS for `-002`** — approver named, timestamped 30 Oct 2026 17:19 GMT+7, scope recorded in `03_Hasil/edu_output_wujud_zat/00_run_config.md` |
| Run `-001` reviewed by a teacher | **TODO** — still `PENDING`; it is never described as approved anywhere in this bundle |
| Approval record carries all four protocol parts | **PARTIAL for `-002`** — named human ✓, timestamp ✓, scope ✓, **verbatim statement ✗**. Either quote the approver's exact sentence into the run config, or state in the submission that the record has three of four parts |
| Nothing described as "published" or "live" in the submission | **HOLDS** — `-002` gate opened for *limited distribution only*; `-001` says `PENDING` |
| Student data anonymised | **HOLDS** |
| Mock data disclosed as mock | **HOLDS** — stated in `09_Source_Code_and_Evidence.md` §5 |

The handbook caps Responsible AI & Ethics at 5/10 if an agent publishes without approval. The
submission currently claims no publication — keep it that way until a human signs.

---

## 6. Pre-flight (30 minutes before submitting)

- [ ] All 11 items pasted; blurb re-counted and still under 10 words
- [ ] Architecture PNG opens at full size and is legible
- [ ] Cover image is 16:9, 380×216 present
- [ ] Video plays start to finish; runtime 5:00–8:00; audio intelligible
- [ ] Video shows at least one refusal **or** approval wait (we show three)
- [ ] Every file link in the form resolves for someone outside the team
- [ ] No file path contains a local drive letter (judges cannot open `D:/...`)
- [ ] Rejection report is included, not quietly dropped
- [ ] **Named teacher has agreed to be named** — Pak Arief appears in the repo, the
      description, the accountability sheet and the video. Confirm in writing before submitting
- [ ] Video contains the build-approach reflection and names the teacher (handbook §7 requires it)
- [ ] Team names and contact on the end card match the registration
- [ ] Submit, then screenshot the confirmation page

---

## 7. File map of this bundle

```
06_Submission/
├── 00_SUBMISSION_CHECKLIST.md        <- this file
├── 01_Title_Blurb.md                 <- items 1-2
├── 02_Project_Description.md         <- item 3
├── 03_Accountability_Sheet.md        <- item 4
├── 04_Test_Results.md                <- item 5 (table)
├── 05_Architecture.md                <- item 6 (text)
├── architecture_diagram.html         <- item 6 (interactive)
├── architecture_diagram.png          <- item 6 (upload this)
├── 06_Product_Sharing.md             <- item 8
├── 07_Demo_Video_Script.md           <- item 7 (script)
├── 09_Source_Code_and_Evidence.md    <- item 9
├── 10_Submission_Form_CopyPaste.txt  <- paste-ready form text
├── cover_image.svg                   <- item 10 (source)
├── cover_image_1280x720.png          <- item 10 (deck/social)
└── cover_image_380x216.png           <- item 10 (form upload)
```
