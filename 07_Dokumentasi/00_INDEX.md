# 00 — Documentation index

> **What this folder is:** the engineering documentation set for EduCraft. It exists so that no
> question about the system has two different answers in two different files.
>
> **What it is not:** submission copy. Judge-facing documents live in `06_Submission/` and are
> *derived* from here.

---

## 1. Reading order

| Reader | Read in this order | Time |
|--------|--------------------|------|
| Judge / reviewer | `06_Submission/02_Project_Description.md` → `05_Architecture.md` → `03_Accountability_Sheet.md` → `04_Test_Results.md` → `06_TRACEABILITY.md` §A–C | 15 min |
| Teammate joining today | `01_ARSITEKTUR.md` → `02_WORKFLOW.md` → `03_SKILLS.md` → `05_TEST_PLAN.md` → `07_GAP_DAN_REKOMENDASI.md` | 40 min |
| Future maintainer | This index → `04_RULEBOOK.md` → `01_ARSITEKTUR.md` §5 (data contracts) → `tools/check_grounding.py` | 30 min |

---

## 2. Source of truth

One canonical file per topic. Everything else is derived and **must not add claims**.

| Topic | Canonical | Derived (do not edit as if primary) |
|-------|-----------|--------------------------------------|
| Architecture | `07_Dokumentasi/01_ARSITEKTUR.md` | `06_Submission/05_Architecture.md`, `architecture_diagram.html`, `README.md` §Pipeline |
| Workflow / state machine | `02_WORKFLOW.md` | `edu-orchestrator/SKILL.md` (runtime contract), `02_Project_Description.md` §3.3 |
| Rules | `03_Hasil/referensi/rulebook_ipas.md` (v2.0) | `skills_package/*/assets/rulebook_ipas.md` (byte-identical copies) |
| Skill boundaries | `03_SKILLS.md` | the four `SKILL.md` files |
| Tests | `05_TEST_PLAN.md` | `04_Diskusi/test_cases_matrix.md` (legacy), `04_Test_Results.md` (results), `03_screenshots/INDEX.md` (capture tracker) |
| Requirements coverage | `06_TRACEABILITY.md` | `06_Submission/00_SUBMISSION_CHECKLIST.md` |
| Known gaps | `07_GAP_DAN_REKOMENDASI.md` | — |

**Why this matters:** before today, architecture was described in four places and the rulebook in
three, with different wording. That is how the "four agents vs five formats" inconsistency survived
for days.

---

## 3. The document set

| File | Answers the question |
|------|----------------------|
| `01_ARSITEKTUR.md` | What are the parts, what may each one do, where are the trust boundaries, what are the data contracts? |
| `02_WORKFLOW.md` | In what order does a run execute, what file is written at each step, when does it stop? |
| `03_SKILLS.md` | Which role owns which decision, and how do we prove no two roles overlap? |
| `04_RULEBOOK.md` | How are the rules governed, versioned, enforced — and which ones actually have evidence? |
| `05_TEST_PLAN.md` | What exactly is tested, with what parameter, against what pass criterion, proved by which file? |
| `06_TRACEABILITY.md` | For every handbook requirement and judging dimension, where is the proof? |
| `07_GAP_DAN_REKOMENDASI.md` | What is missing, in what order do we fix it, and what does done look like? |

Supporting machinery: `tools/check_grounding.py` — deterministic R001 check; writes
`grounding_report.md` per run and exits non-zero on failure.

---

## 4. Snapshot — 31 October 2026

| Item | State |
|------|-------|
| Submission items | 7 READY · 1 PARTIAL · 2 GAP · 1 bonus GAP |
| Test suite | 20 cases defined with parameters; **0 screenshots captured** |
| Deterministic checks | R001 — PASS on run `-001` (121 tags), FAIL on run `-002` (84 class violations) |
| Rulebook | v2.0, three copies, checksum verified |
| Public repo | `github.com/otnamhcar/educraft-hackathon-workbuddy-2026`, MIT, 88 files |
| Open defects | D1 (run `-002` grounding), D2 (`-001` audit log) |
| Where the score is lost | Not design — capture. Screenshots (0) and video (none) hold down three dimensions |

---

## 5. Rules of the house

1. **No claim without an artefact.** If a file cannot prove it, the sentence says "designed to" or
   does not exist.
2. **One canonical file per topic.** A derived document that contradicts its canonical source is a
   bug in the derived document.
3. **Status vocabulary is fixed:** `READY` / `PARTIAL` / `GAP` / `UNVERIFIED` for documents;
   `PASS` / `BY DESIGN` / `TO RUN` / `FAIL` for tests.
4. **Name the run.** Never "the run of record" without an ID and a status.
5. **Disclose defects in the same place they are found.** A defect mentioned only in conversation
   does not exist for a judge.

---

## 6. Change log

| Date | Change |
|------|--------|
| 31 Oct 2026 | Documentation set created; rulebook v2.0 (parameterised + R012); `check_grounding.py` shipped; grounding reports generated for both runs; R012 addendum written; defects D1/D2 logged |
