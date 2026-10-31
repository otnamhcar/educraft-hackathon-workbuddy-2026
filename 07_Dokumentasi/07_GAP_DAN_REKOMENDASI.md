# 07 — Gap register and recommendations

> Ordered by **score impact per hour**, not by elegance. Each item states the gap, the evidence that
> it is real, the definition of done, and what it unlocks.
> Nothing here is a guess about what judges want: each maps to a requirement or dimension quoted in
> `06_TRACEABILITY.md`.

---

## P0 — blocks the submission or caps the score

| ID | Gap | Evidence it is real | Definition of done | Unlocks |
|----|-----|---------------------|--------------------|---------|
| **G1** | Run `-002` grounds 84 of 89 tags on `[src:B4]`, a curriculum topic entry, not a fact source | `03_Hasil/edu_output_wujud_zat/grounding_report.md` — FAIL | `03_Hasil/referensi/source_material_wujud_zat.md` exists with `[src:1]`–`[src:n]` facts traceable to the official Panduan IPAS (section *Proses Perubahan Wujud Zat*, `02_Sumber/extracted/panduan_ipas.txt` lines 856–870); artefacts re-tagged; `check_grounding.py` returns PASS; a correction memo covers the already-printed packs | TC-01 honesty; the core product claim; removes the easiest attack a judge can make |
| **G2** | Two runs, contradictory status statements | `03_Accountability_Sheet.md` says "NOT PUBLISHED"; `edu_output_wujud_zat/audit_log.md` says the gate opened | Every document names the run and its status; accountability sheet has a per-run table | Removes a self-contradiction a judge can find in 2 minutes |
| **G3** | 0 screenshots for 20 test cases | `05_Bukti_Proses/evidence_bundle/03_screenshots/` contains only `INDEX.md` | ≥6 captured, P0 first: TC-08, TC-10, TC-14, TC-15, TC-18 (+TC-02) | Test results item becomes READY; critical evidence 1/6 → 5/6; lifts Technical Execution and Responsible AI |
| **G4** | No demo video | `06_Submission/` has a script, no media file | 5:00–8:00 video, 3 accountability stops, audio intelligible | Demo & Storytelling 3 → 8 (10 points) |
| **G5** | Deadline claim unverified | Handbook p.13: 1 Nov. Project assumes 7 Nov | Committee notice stored in `01_Dokumen/` and cited | Determines whether P0 items are even possible. **Decide this first.** |

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

## The decision that must be made today

**G5.** The handbook says the deadline is **1 November 2026**. The project has been operating on a
7 November extension that exists only as a message from a teacher. Two futures:

| If deadline is 1 Nov | If deadline is 7 Nov |
|----------------------|----------------------|
| Submit what is READY now. Fix G2 (wording) only — it costs 20 minutes and removes a contradiction. Screenshots of TC-14 and TC-15 from existing artefacts are still possible; a video is not. | Execute P0 in order: G1 → G3 → G4 → G2. Then P1 G6–G8. Rehearse G15. |

Do not start G1 (re-tagging) before G5 is settled: if the deadline is tomorrow, re-tagging printed
material is the wrong use of the remaining hours.

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
