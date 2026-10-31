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
| **G3** | 0 screenshots for 20 test cases | `05_Bukti_Proses/evidence_bundle/03_screenshots/` contains only `INDEX.md` | ≥6 captured, P0 first: TC-08, TC-10, TC-14, TC-15, TC-18 (+TC-02) | Test results item becomes READY; critical evidence 1/6 → 5/6; lifts Technical Execution and Responsible AI |
| **G4** | No demo video | `06_Submission/` has a script, no media file | 5:00–8:00 video, 3 accountability stops, audio intelligible | Demo & Storytelling 3 → 8 (10 points) |
| ~~**G5**~~ | ~~Deadline claim unverified~~ | **CLOSED 31 Oct** — `01_Dokumen/BUKTI_KOMITE_2026-10-31.md` §2: committee extended the deadline to **7 Nov 2026** | Done. Internal target: submit **5 Nov** | Unblocked all P0 work |

---

## P1 — inconsistency that undermines credibility

| ID | Gap | Evidence | Definition of done |
|----|-----|----------|--------------------|
| **G6** | Contracts list 3 formats; submission claims 5 + quiz | `edu-orchestrator/SKILL.md`, `edu-writer/SKILL.md` vs `02_Project_Description.md` | Format list defined once (`01_ARSITEKTUR.md` §3) and copied into both contracts |
| **G7** | Loop counter is prose, not a field | `02_WORKFLOW.md` §4; audit logs say "2/3" with no machine-readable field | `iteration: <int>` in `00_run_config.md`, rewritten at every transition; TC-13 demonstrable |
| **G8** | `-001` audit log contradicts its own rejection | `audit_log_edu_orchestrator.md` §3.4 "no rejection" vs the 29 Oct REJECT report | Append the rejection and v1→v2 history; never rewrite existing entries |
| **G9** | Rulebook copies could drift | Two asset copies + canonical | Checksum check script + pre-submit step (documented in `04_RULEBOOK.md` §1); today identical |
| **G10** | R012 is declared but not exercised | `04_RULEBOOK.md` §2 | One test case using a halal claim, or a `tools/check_claims.py`; either makes it demonstrable |

---

## P2 — raises the ceiling, not required

| ID | Gap | Why it matters | Effort |
|----|-----|----------------|--------|
| **G11** | Animatic has no audio, no MP4 | UX & Accessibility; a silent "video" looks unfinished | Record narration, render to MP4 |
| **G12** | No live project link (bonus) | Bonus points; also a 90-second demo surface | Publish the quiz + animatic as a static page |
| **G13** | No bilingual output (TC-17) | Bonus in Challenge C | One EN version + cross-language fact check |
| **G14** | No adversarial second Reviewer | Stated limitation; roadmap item | Only if time remains after P0 |
| **G15** | Surprise test never rehearsed | 90 seconds is unforgiving | Two timed dry runs with an unseen case |

---

## Schedule — 31 October to 5 November (submit date)

Deadline is confirmed **7 November 2026** (`BUKTI_KOMITE_2026-10-31.md` §2). Internal target is
**5 November**, leaving two days for upload failures and form problems.

| Day | Work | Why this order |
|-----|------|----------------|
| **31 Oct** | ✅ **DONE** — G1 (fact sheet, re-tag, grounding PASS, correction memo); G5 closed (deadline verified); U1–U3 resolved | It was the only P0 item that changes the product's truthfulness; everything else is presentation |
| **1 Nov** | G3 — capture the 5 critical screenshots (TC-08, 10, 14, 15, 18) + TC-02 | Critical evidence 1/6 → 5/6; unblocks the Responsible AI cap |
| **2 Nov** | G4 — record the 5–8 min video from the existing script | Largest single dimension gain (3 → 8) |
| **3 Nov** | G6–G8 — contract format list, iteration field, `-001` audit log append | Removes contradictions a judge can find by reading |
| **4 Nov** | G10 + G15 — one R012 test case, two timed surprise-test rehearsals | Demo Day readiness; cheap |
| **5 Nov** | Final reconciliation: test counts, checksums, links, ZIP, submit + screenshot the confirmation | The mechanical points that are free |

If any day slips, drop in this order: G10 → G8 → G6. Never drop G1 or G3.

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
