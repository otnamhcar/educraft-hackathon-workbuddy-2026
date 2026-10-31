# 06 — Requirements traceability

> **Purpose:** answer, for every requirement the committee wrote, one question: *where is the proof?*
> Every row has a status. `READY` = artefact exists and is cited. `PARTIAL` = artefact exists but
> incomplete. `GAP` = not satisfied. `UNVERIFIED` = we rely on a claim we cannot prove from this repo.

---

## A. Submission items (handbook §7)

| # | Item | Status | Artefact | Evidence of substance |
|---|------|--------|----------|-----------------------|
| 1 | Project title | READY | `06_Submission/01_Title_Blurb.md` | — |
| 2 | Short blurb, <10 words | READY | same | 8 words, counted in the file |
| 3 | Project description (4 parts) | READY | `02_Project_Description.md` | 4 sections present; §3.3 covers prompt design as required |
| 4 | Accountability sheet, 1 page | PARTIAL | `03_Accountability_Sheet.md` | Says run `-001` is `PENDING` / not published. **True for `-001`, false as a statement about the project** — run `-002` was approved and printed. Must name the run. |
| 5 | Test results + screenshots | **GAP** | `04_Test_Results.md` | Table exists (7 PASS / 11 BY DESIGN / 2 TO RUN). **0 screenshots captured.** Handbook requires them. |
| 6 | Architecture diagram | READY | `05_Architecture.md`, `architecture_diagram.png` (2720×3000), `.html` | Components, 3 trust boundaries, 4 trade-offs |
| 7 | Demo video 5–8 min | **GAP** | `07_Demo_Video_Script.md` (7:20) | Script only; no video file exists |
| 8 | Product sharing | READY | `06_Product_Sharing.md` | WorkBuddy-specific value, insights |
| 9 | Source code / workflow | READY | `github.com/otnamhcar/educraft-hackathon-workbuddy-2026` | Public, MIT, 88 files; four contracts + knowledge assets |
| 10 | Cover 16:9 | READY | `cover_image_380x216.png`, `1280x720.png` | Correct dimensions |
| 11 | Project link (bonus) | GAP | — | No live URL. Optional. |

**Count: 7 READY · 1 PARTIAL · 2 GAP · 1 bonus GAP.**

---

## B. Challenge C must-haves (handbook §5)

| Requirement | Where satisfied | Evidence | Status |
|-------------|-----------------|----------|--------|
| ≥3 agents with defined roles (Planner, Writer, Reviewer) | `01_ARSITEKTUR.md` §3 | 4 `SKILL.md` files | READY |
| ≥2 platforms/formats from one source | `03_Hasil/materi_ajar/` | 5 documents + interactive quiz | READY |
| Reviewer evaluates every draft against documented rules | `rulebook_ipas.md` v2.0 | 2 review reports with per-rule verdicts | READY |
| Rejection justified by citing the rule breached | `05_review.md` PASS 1 | 7 findings, each with rule ID + quote | READY |
| Writer remediates and resubmits; ≥1 full cycle | run `-001` and `-002` | REJECT → remediation → APPROVE in both | READY |
| Max 3 iterations, then escalate | `02_WORKFLOW.md` §4 | Behaviour: 2 of 3 used. **Enforcement: GAP** (counter is prose) | PARTIAL |
| Human approval before publication | `audit_log.md` §3.7 | Approval 30 Oct 17:19, named, quoted | READY |
| Retain inter-agent exchange + revision history | `audit_log*.md`, both review reports | Rejected report retained, not deleted | READY — `-001` log now carries the v1→v2 record in §7 (D2 closed 31 Oct) |

---

## C. Judging dimensions (handbook §10, 10 × 10 = 100)

The numeric column is a **triage signal for the team, not a score claim**. It exists to show which
dimensions are held back by a missing artefact rather than by a design weakness. Only the "basis"
column should ever be quoted.

| Dimension | What the handbook asks | Our strongest evidence | Weakest point | Est. now → attainable | Basis for estimate |
|-----------|------------------------|------------------------|---------------|----------------------|--------------------|
| Impact & Relevance | Real-world problem, meaningful value | Teacher review-loop framing; approved and printed pack | No measured time saving; one teacher | 7 → 8 | Problem is real and specific; value claim is still an estimate |
| Human-Centered Design | Designed around real users and needs | Separate student (no key) / teacher (key) packs; age-calibrated rule R003 | No student usability test | 8 → 8 | Artefacts show user thinking; no user test evidence |
| AI Interaction | Genuinely agentic, not single-pass | 4 agents, 2 real reject→remediate cycles, gates | Loop counter not machine-enforced | 8 → 8 | Two independent runs with different verdict paths |
| Technical Execution | Working prototype + performance against test cases | Deterministic grounding check passes on both runs (121 / 115 tags) | 0 screenshots; 11 cases BY DESIGN | 5 → 8 | Prototype works; test evidence incomplete |
| Feasibility | Realistic, could scale beyond hackathon | No infra, Markdown rules, printable output | Single subject domain | 7 → 8 | Cost of adoption is near zero for a school |
| Demo & Storytelling | How effectively presented | 7:20 script with 3 accountability stops | No video | 3 → 8 | Nothing recorded yet |
| Innovation & Creativity | Originality of approach | "A tag is not a citation" + resolution gate | Insight is documented, gate not yet mandatory | 7 → 8 | Insight is genuinely uncommon in RAG demos |
| UX & Accessibility | Usability and accessibility | Print packs, single-file HTML quiz, large type | No audio, no screen-reader check, Indonesian only | 6 → 7 | Usable, not yet accessible |
| Responsible AI & Ethics | Sources, permissions, approval, limits, record | Accountability sheet, 4 boundaries, disclosed failure, D1 fixed in the open | Critical evidence 1 of 6 | 6 → 9 | Strong design, thin proof |
| Overall Quality | Would a judge trust it in their organisation | Honest defect log; reproducible checks | Inconsistencies between docs (being fixed) | 7 → 8 | Trust comes from disclosure, which is present |

**Where the score is lost today is not design, it is capture:** three dimensions (Technical
Execution, Demo & Storytelling, Responsible AI) are held down by missing screenshots and a missing
video, not by missing capability. Those are mechanical to fix and are the cheapest points available.

---

## D. Data & testing requirements (handbook §6)

| Requirement | Status | Note |
|-------------|--------|------|
| ~20 test cases with expected behaviour | READY | `05_TEST_PLAN.md` (20 cases, parameters named) |
| Execute and submit results with screenshots | GAP | 0 screenshots |
| Include failures | READY | Two defects logged (D1, D2); 29 Oct rejection retained |
| Disclose rather than conceal | READY | Rejection report shipped; defect log added |
| Build on the shared dataset | **RESOLVED — waived** | Committee waived the shared dataset and its test cases (`BUKTI_KOMITE` §3). Our own domain is permitted |
| Live 90-second surprise test | PARTIAL | Protocol written (`05_TEST_PLAN.md` §7); never rehearsed |

---

## E. Unverified claims register

Anything in this list must not be stated as fact in the submission until an artefact exists.

| ID | Claim we rely on | Status | Evidence |
|----|------------------|--------|----------|
| U1 | Submission deadline is **7 Nov 2026** | **RESOLVED** | `01_Dokumen/BUKTI_KOMITE_2026-10-31.md` §2 — committee message 27/10/2026 21:23: "diperpanjang hingga 7 November 2026 (dari jadwal awal 1 November)". Handbook p.13 is superseded |
| U2 | Participant-defined test cases are allowed | **RESOLVED** | same file §3 — 21/10/2026 09:53: "Untuk dataset dan test case dibebaskan … gunakan data atau skenario mandiri"; reinforced 28/10/2026 13:41 |
| U3 | Using our own domain instead of the shared dataset is acceptable | **RESOLVED** | same file §3 — the dataset is explicitly waivable. No deviation needs to be argued |
| U4 | Run `-001` has teacher approval | UNVERIFIED | `00_run_config.md` says `PENDING`. Say "pending", never "approved" |
| U5 | "Field testing" has happened | OVERSTATED | One teacher, one review session, one printed set. Say "single-teacher review" |
| U6 | The engine is domain-parameterised | PARTIAL | True since rulebook v2.0 (no hardcoded tag numbers), but never demonstrated on a second subject |

---

## F. Claims we must stop making

| Claim in current documents | Why it must change |
|----------------------------|--------------------|
| "100% of factual sentences carry a source tag" (`02_Project_Description.md` §3.4) | Already corrected: attribution and resolution are now stated separately, and both pass on both runs after D1 was fixed. Do not revert to the single-number claim |
| "The run of record is `-001`" | Two runs with different statuses. Always name the run and its status |
| "Nothing has been published" (`03_Accountability_Sheet.md` §3) | True for `-001`; run `-002` print packs were distributed after approval |
| "Five formats in one run" | True for `-001` only (5 documents + 1 interactive quiz). Contracts still list 3 formats — fix the contracts or scope the claim |
