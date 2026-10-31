# Submission Checklist — Tencent Cloud Hackathon Indonesia 2026

**Project:** EduCraft · **Challenge:** C — The Creator Agent
**Deadline:** 7 November 2026 (perpanjangan dari panitia, info guru 30 Okt 2026) · **Prepared:** 30 October 2026
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
| 7 | Demo video, 5–8 min | REQUIRED | **TODO** | Script ready: `07_Demo_Video_Script.md` (7:20) |
| 8 | Product sharing | REQUIRED | **READY** | `06_Product_Sharing.md` |
| 9 | Source code / exported workflow | REQUIRED | **PARTIAL** | Package ready in `05_Bukti_Proses/`; **repo or export still TODO** (§4) |
| 10 | Cover image (optional, 16:9) | OPTIONAL | **READY** | `cover_image_380x216.png` + `cover_image_1280x720.png` |
| 11 | Project link (bonus) | BONUS | **TODO** | Optional live demo URL |

**Score: 7 ready · 2 partial · 2 todo.** The two partials are the two the judges weigh heaviest
(test evidence and code), so do not submit on the strength of the document count.

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
| P2 | TC-06, TC-09, TC-11, TC-17 | — | As available |

**Rule for all screenshots:** the rule ID and the quoted text must both be readable at 100% zoom
on a 1080p laptop. If a judge has to squint, it does not count.

---

## 4. Code publication — pick one

**Option A (stronger).** Public GitHub repo:
1. `git init` inside `05_Bukti_Proses/skills_package/`
2. Add a README built from `05_Architecture.md` §1 + `09_Source_Code_and_Evidence.md` §1–2
3. Add `LICENSE` (MIT) and a note that `02_Sumber/` documents are **not** redistributed
4. Push, set public, paste the URL into the form

**Option B (acceptable).** Export the WorkBuddy workflow and submit the evidence bundle as-is,
stating explicitly: *"Exported WorkBuddy workflow with evidence of use; see run trail in
09_Source_Code_and_Evidence.md §2."*

Do **not** upload third-party curriculum PDFs to a public repo. They are reference material only.

---

## 5. Ethics gate (do not skip)

| Check | Status |
|-------|--------|
| Teacher/SME has reviewed the 5 drafts and the answer key | **TODO** |
| Approval recorded (name + date) in `00_run_config.md` | **TODO** |
| Nothing described as "published" or "live" in the submission | **HOLDS** — run config says PENDING |
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
