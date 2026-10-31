# 07 — Gap register and recommendations

> Ordered by **score impact per hour**, not by elegance. Each item states the gap, the evidence that
> it is real, the definition of done, and what it unlocks.
> Nothing here is a guess about what judges want: each maps to a requirement or dimension quoted in
> `06_TRACEABILITY.md`.

---

## P0 — blocks the submission or caps the score

| ID | Gap | Evidence it is real | Definition of done | Unlocks |
|----|-----|---------------------|--------------------|---------|
| ~~**G1**~~ | ~~Run `-002` grounds 84 of 89 tags on a curriculum entry~~ | **CLOSED 31 Oct** — `03_Hasil/edu_output_wujud_zat/grounding_report.md`: 115 tags, 0 dangling, 0 violations | Done. Content unchanged; `[src:W10]`/`[src:W11]` are team-derived and await teacher validation (`11_Memo_Koreksi_Tag_2026-10-31.md`) | TC-01 honesty on both runs; the core product claim |
| **G2** | Two runs, contradictory status statements | `03_Accountability_Sheet.md` says "NOT PUBLISHED"; `edu_output_wujud_zat/audit_log.md` says the gate opened | Every document names the run and its status; accountability sheet has a per-run table | Removes a self-contradiction a judge can find in 2 minutes |
| **G3** | 0 screenshots for 21 test cases | `05_Bukti_Proses/evidence_bundle/03_screenshots/` contains only `INDEX.md`. **Blockers found 31 Oct:** (a) **CLEARED** — no `edu-*` skill was installed, so every capture session would have failed at step one; the four skills are now installed via `tools/install_skills.py` and `doctor.py` check 3 passes on the default path; (b) the runbook's capture instructions were Windows-only (`Win + Shift + S`) on a Linux machine | ≥6 captured, P0 first: TC-08, TC-10, TC-14, TC-15, TC-18 (+TC-02). Runbook §1.0 now opens with the install check and §1.4 with the `gnome-screenshot` commands verified present on this machine | Test results item becomes READY; critical evidence 1/7 → 5/7; lifts Technical Execution and Responsible AI |
| **G4** | No demo video | `06_Submission/` has a script, no media file. **31 Oct:** there was also no production runbook — no tooling, no recording order, no export spec, no verification step | **Runbook DONE 31 Oct** — `06_Submission/13_Demo_Video_Runbook.md`. It maps each of the 10 scenes to what it needs: **7 are recordable now**, 3 need the agent live. Remaining: the recording itself | Demo & Storytelling 3 → 8 (10 points) |
| ~~**G5**~~ | ~~Deadline claim unverified~~ | **CLOSED 31 Oct** — `01_Dokumen/BUKTI_KOMITE_2026-10-31.md` §2: committee extended the deadline to **7 Nov 2026** | Done. Internal target: submit **5 Nov** | Unblocked all P0 work |

---

## P1 — inconsistency that undermines credibility

| ID | Gap | Evidence | Definition of done |
|----|-----|----------|--------------------|
| ~~**G6**~~ | ~~Contracts list 3 formats; submission claims 5 + quiz~~ | **CLOSED 31 Oct** — `edu-orchestrator` and `edu-writer` were already on the canonical six; `edu-planner` was not: its description, task list and JSON schema all said three formats, so a four-format run like `-002` could not be planned from the contract | Done. `edu-planner/SKILL.md` now carries the canonical six-format list, the "any subset, at least two" rule, and an updated schema |
| ~~**G7**~~ | ~~Loop counter is prose, not a field~~ | **CLOSED 31 Oct** — `Iteration` row added to `edu_output/00_run_config.md`; `edu_output_wujud_zat/00_run_config.md` created (it did not exist at all) | Done. Both runs record `iteration: 1` of 3. Honest caveat kept in `02_WORKFLOW.md` §4: **recorded, not enforced** |
| ~~**G8**~~ | ~~`-001` audit log contradicts its own rejection~~ | **CLOSED 31 Oct** — §7 appended to `audit_log_edu_orchestrator.md`: the 29 Oct REJECT, the remediation, the 30 Oct APPROVE, and the corrected iteration count. §3.3/§3.4 left intact with a forward pointer | Done. Nothing was rewritten; the log stays append-only |
| ~~**G9**~~ | ~~Rulebook copies could drift~~ | **CLOSED 31 Oct** — `tools/doctor.py` check 5 hashes every copy and fails on any difference; today they share one checksum (`9fe63368…`). The same check covers the `source_material_wujud_zat.md` copies, which were re-synced after a header correction. The script is Python, so the check runs identically on Windows | Done. Drift is now detected on every clone, not by a manual pre-submit step |
| **G10** | R012 is declared but not exercised | `04_RULEBOOK.md` §2. **31 Oct:** found the deeper cause — `edu-reviewer/SKILL.md` listed R001–R011 and its "special checks" covered only R002/R003/R006, so the agent enforcing the rulebook was never told R012 existed | **Contract half DONE 31 Oct**: Reviewer now names R001–R012, carries an explicit R012 check, and must return `rules_na` with a reason (a rule with no verdict = unchecked). **Still open**: no live run has exercised R012. Test case **TC-21** was written on 31 Oct (`test_cases_matrix.md` §K): a branded efficacy + superlative + halal claim that must be REJECTed with all three sub-clauses named, plus a clean-material pass that must return `rules_na: R012` with a reason. Status stays `TO RUN` until it is executed and captured |

---

## P2 — raises the ceiling, not required

| ID | Gap | Why it matters | Effort |
|----|-----|----------------|--------|
| **G11** | Animatic has no audio, no MP4 | UX & Accessibility; a silent "video" looks unfinished | Record narration, render to MP4 |
| **G12** | No live project link (bonus) | Bonus points; also a 90-second demo surface | Publish the quiz + animatic as a static page |
| **G13** | No bilingual output (TC-17) | Bonus in Challenge C | One EN version + cross-language fact check |
| **G14** | No adversarial second Reviewer | Stated limitation; roadmap item | Only if time remains after P0 |
| **G15** | Surprise test never rehearsed | 90 seconds is unforgiving. **31 Oct:** no Demo Day runbook existed either — the 8-minute format (presentation + 90 s test + Q&A, handbook p. 15) had no time budget, no live/recorded split and no fallback ladder | **Runbook DONE 31 Oct** — `03_Hasil/panduan/Runbook_Demo_Day.md`. **Still open:** two timed rehearsals with an unseen case, logged in its §8 |
| **G16** | Approval record has three of the four protocol parts | `03_Hasil/edu_output_wujud_zat/00_run_config.md` records the named approver and the timestamp, but the scope is a single line ("distribusi terbatas — paket cetak siswa & guru") that never says whether **the answer key** is covered, and there is **no verbatim sentence**. `07_Dokumentasi/02_WORKFLOW.md` §5 requires all four | Either quote the approver's exact sentence and name the answer key explicitly in the scope, or state in the submission that the record is 3/4. Do not describe it as "full protocol" until one of those is done |
| ~~**G17**~~ | ~~Nothing let the teacher install and verify the pipeline from a clone~~ | **CLOSED 31 Oct** — `tools/install_skills.py` + `tools/doctor.py`. A fresh `git clone` installs 4 skills and reports `8 passed / 0 failed / 0 warning`, exit 0. Rewritten in Python on 31 Oct because the team is split Linux/Windows and the bash versions were a different program on each | Done. README → "Run it yourself", with per-OS command forms and a symptom/cause/fix table |

---

## Schedule — 31 October to 5 November (submit date)

Deadline is confirmed **7 November 2026** (`BUKTI_KOMITE_2026-10-31.md` §2). Internal target is
**5 November**, leaving two days for upload failures and form problems.

| Day | Work | Why this order |
|-----|------|----------------|
| **31 Oct** | ✅ **DONE** — G1 (fact sheet, re-tag, grounding PASS, correction memo); G5 closed (deadline verified); U1–U3 resolved; **G6–G8 pulled forward and closed** (planner format list, `iteration` field + missing `-002` run config, `-001` audit addendum); **G3 unblocked** (skill-install pre-flight + Linux capture commands) | G1 was the only P0 item that changes the product's truthfulness; G6–G8 were mechanical and sat in front of G3, so doing them early buys a day of buffer for the video |
| **1 Nov** | G3 — capture the 5 critical screenshots (TC-08, 10, 14, 15, 18) + TC-02 + TC-21. Skills are **already installed** (31 Oct, `doctor.py` check 3 passes) | Critical evidence 1/7 → 5/7 (6/7 with TC-21); unblocks the Responsible AI cap |
| **2 Nov** | G4 — record the 5–8 min video from the existing script | Largest single dimension gain (3 → 8) |
| **3 Nov** | *Buffer* — G6–G8 are already done. Use the day for a second capture pass (S3/S4) or G10 | Absorbs the overrun that capture sessions always produce |
| **4 Nov** | G10 + G15 — one R012 test case, two timed rehearsals using `Runbook_Demo_Day.md` §8 | Demo Day readiness; cheap. Demo Day is 27 Nov and only applies if selected on 10 Nov, so this is the first thing to drop |
| **5 Nov** | Final reconciliation: test counts, checksums, links, ZIP, submit + screenshot the confirmation | The mechanical points that are free |

If any day slips, drop in this order: G10 → G9 → G15. Never drop G1 or G3.

---

## What "done" means for the submission

A submission is complete when all of the following are true, and each is checkable by someone who
was not in the room:

1. All 11 items have an artefact, and the form links resolve for a stranger.
2. `06_Submission/04_Test_Results.md` counts reconcile with `03_screenshots/INDEX.md`.
3. No document claims a behaviour that a file in the repo cannot demonstrate.
4. Every run mentioned is named with its status (`PENDING` / `RELEASED`).
5. The defect log is present and specific (D1, D2).
6. `check_grounding.py` has been run on the final artefacts and its output is included.
7. The rulebook checksum matches across three copies.

Items 2–7 are all mechanical. They are the cheapest points in the competition.
