# EduCraft — Rule-Governed AI Teaching Assistant for Primary Science (IPAS)

> **Teacher-ready IPAS lesson kits, rule-checked before they publish.**

Tencent Cloud Hackathon Indonesia 2026 · **Challenge C — The Creator Agent**
Built with WorkBuddy (Tencent Cloud). No orchestration framework, no web app, no database.

---

## What this repository is

EduCraft is **four agent contracts plus a knowledge layer**. That is the deliberate choice: a judge
can open four Markdown files and read every rule the agent obeys, instead of inferring behaviour
from code.

One approved source document goes in. A complete teaching pack comes out — lesson plan (RPP),
pre-test and post-test with answer key, slide outline, student article, infographic brief, and a
playable HTML quiz. Nothing is released until an independent Reviewer agent has checked every
sentence against a written rulebook **and** a human has approved.

The product is not the generated text. **The product is the gate.**

### Whose rules these are

The idea, the curriculum references and the substance of the rulebook came from **Pak Arief**,
a practising IPAS primary-school teacher. He set what a teacher will never put in front of
a class — no permanent health claims, no fear-mongering, no halal claim without a certificate. The
team's work was to formalise that judgement into predicates a machine can check, and to build the
pipeline that enforces them.

This is why `rulebook_ipas.md`, not the code, is the artefact a school could adopt: a curriculum
team can edit the rules without touching the pipeline.

---

## Pipeline

```
Teacher brief (approved source + CP codes)
    │
    ▼
Orchestrator ── writes 00_run_config.md, appends to the audit log
    │
    ├─► Planner ──────────► outline per format, mapped to CP codes, gaps flagged
    │                            │
    ├─► Writer ───────────► draft v1, every factual sentence tagged [src:#]
    │        ▲                   │
    │        │                   ▼
    │        │            Reviewer ──► APPROVE | REJECT + findings[]
    │        │                   │        (rule ID + quoted text + reason + fix)
    │        └──── REJECT ◄──────┤  iteration += 1
    │                            │  if iteration == 3 and still REJECT → HALT, escalate
    │                            ▼
    │                        APPROVE
    ▼                            ▼
Human approval gate ──────► pack released  (+ audit log)
```

Three properties are enforced by contract, not by hope:

| Property | Mechanism |
|----------|-----------|
| Grounding | Writer may use only facts present in the source; the fallback is the literal token `[UNVERIFIED]` |
| Separation of powers | The Reviewer has **veto** but cannot rewrite; the Writer has **rewrite** but cannot approve |
| No self-publication | Publishing is a separate, human-gated step. The agent has no path to output that bypasses the gate |

---

## Repository map

| Path | What is in it |
|------|---------------|
| `05_Bukti_Proses/skills_package/` | **The code**: four `SKILL.md` contracts + knowledge assets |
| `05_Bukti_Proses/skills_package/edu-reviewer/assets/rulebook_ipas.md` | **The rulebook** R001–R012 (v2.0) |
| `02_Sumber/` | The two official ministry PDFs the knowledge layer is built from, plus the extracted plain text. Inventory and exclusions: `02_Sumber/README.md` |
| `03_Hasil/referensi/` | Knowledge layer: source material, CP, actual-context register, rulebook |
| `03_Hasil/materi_ajar/` | Run `-001` output (Energi Alternatif), corrected drafts + HTML quiz |
| `03_Hasil/edu_output_wujud_zat/` | Run `-002` output (Perubahan Wujud Zat) + three print-ready PDFs |
| `03_Hasil/audit/` | **Both** review reports — the REJECT and the APPROVE |
| `03_Hasil/panduan/` | How to demo it: teacher walkthrough + testimonial guide, and the Demo Day runbook (8-minute budget, fallback ladder, Q&A evidence pointers) |
| `04_Diskusi/test_cases_matrix.md` | The 20-case suite, including which six are critical |
| `06_Submission/` | Submission bundle: description, accountability sheet, test results, architecture, deck |
| `06_Submission/architecture_diagram.png` | Component and trust-boundary diagram |
| `07_Dokumentasi/` | Engineering docs: architecture, workflow, skill boundaries, rulebook spec, test plan, requirements traceability, gap register |
| `tools/check_grounding.py` | Deterministic R001 check — resolves every tag against the knowledge layer, exits non-zero on failure. Checks drafts only; run metadata is skipped and named in the report |
| `tools/install_skills.py` | Copies the four skill folders where WorkBuddy looks for them, then verifies the count is 4. Python, so it runs unchanged on Linux, macOS and Windows |
| `tools/doctor.py` | Six pre-flight checks on a fresh clone — Python, contracts, installed skills, knowledge layer, copy checksums, grounding on both runs. Same code on every OS |

---

## The rulebook (R001–R012, v2.0)

| Rule | Guards against |
|------|----------------|
| R001 | Any fact without a resolvable `[src:#]` tag |
| R002 | Fear-mongering and catastrophic framing |
| R003 | Language inappropriate for ages ~10–12 |
| R004 | Drift from the *Capaian Pembelajaran* (learning outcomes) |
| R005 | Content that lists only harm, with no mitigation or student role |
| R006 | Unsupported health claims — permanent effects, cures, absolute efficacy |
| R007 | Promoting or normalising harmful practice |
| R008 | Tone that is not warm, educative and empowering |
| R009 | Non-standard Indonesian, or a narrative with no positive call to action |
| R010 | Wording that stigmatises or blames students or groups |
| R011 | A real-world claim without a dated, official, traceable URL |
| R012 | Commercial, product-efficacy, superlative or halal claims without a certificate — `N/A` for purely educational material |

A rulebook a curriculum team can edit without touching code is what makes institutional adoption
realistic rather than theoretical. It is also the honest trade-off: rules in the prompt compete for
context, and a very long rulebook would degrade adherence. See
`06_Submission/05_Architecture.md` §4 for the four trade-offs we would defend and the cost of each.

---

## Evidence trail — including the failure

**Run `EDU-ORCH-20261026-001`** (Energi Alternatif, Fase C, CP C4 + B5)

| Step | File |
|------|------|
| Run config | `03_Hasil/edu_output/00_run_config.md` |
| Audit log | `03_Hasil/audit/audit_log_edu_orchestrator.md` |
| **REJECT** 29 Oct (R001, R011, R004) | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-29.md` |
| Remediation: real source material created | `03_Hasil/referensi/source_material_energi.md` |
| Remediation: dated official URLs | `03_Hasil/referensi/konteks_aktual.md` |
| **APPROVE** 30 Oct | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-30_REVISI.md` |

On 29 October the Reviewer agent **rejected our own output**: the drafts were tagged against the
curriculum-outcomes file rather than a fact-bearing source, and two "real world" claims had no
verifiable document behind them. We shipped the rejection report. We did not delete it, and we did
not quietly patch the drafts.

**Run `EDU-ORCH-20261030-002`** (Perubahan Wujud Zat, Fase C)

Reviewer Pass 1 returned **REJECT with 5 Major findings**, all R001: claims about particle
arrangement and the characteristics of each state of matter were not in the source. The Writer
removed them and replaced "denser/looser" framing with explicit direction pairs. Pass 2: APPROVE at
iteration 2 of 3. The teacher approved on 30 October 2026 at 17:19, which opened the publication
gate — after which two separate print packs were produced so that the answer key never travels with
the student booklet. Full trail: `03_Hasil/edu_output_wujud_zat/audit_log.md`.

That sequence — **reject, diagnose, fix, re-review** — is the evidence of use. A screenshot of a
happy path would prove less.

---

## Test status (stated plainly)

| Result | Count |
|--------|-------|
| `PASS` — backed by an artefact in this repo | 7 |
| `BY DESIGN` — enforced in a `SKILL.md`, screenshot not yet captured | 11 |
| `TO RUN` — not executed, disclosed | 2 |

**We are not claiming 20/20.** Full table, including the critical cases and the disclosed failure:
`06_Submission/04_Test_Results.md`.

One case is machine-checkable end to end, and it is the one that matters most:

```bash
python3 tools/check_grounding.py --run 03_Hasil/materi_ajar \
    --knowledge 03_Hasil/referensi --out 03_Hasil/materi_ajar/grounding_report.md
```

| Run | Tags checked | Dangling | Class violations | Verdict |
|-----|-------------:|---------:|-----------------:|---------|
| `-001` Energi | 121 | 0 | 0 | **PASS** |
| `-002` Wujud Zat, before fix | 89 | 0 | 84 | **FAIL** — defect D1 |
| `-002` Wujud Zat, after fix | 115 | 0 | 0 | **PASS** |

---

## Run it yourself

Written for a teacher on a laptop, not for a developer. Two commands, one restart, then a health
check. **The same two commands work on Linux, macOS and Windows** — every script in `tools/` is
Python, because this team runs Linux (Mint) and Windows and a bash script is a different program on
each.

```bash
git clone https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026.git
cd educraft-hackathon-workbuddy-2026
```

Then install, from the repository root:

| | Linux / macOS | Windows (cmd or PowerShell) |
|---|---|---|
| Install the skills | `python3 tools/install_skills.py` | `python tools\install_skills.py` |
| Health check | `python3 tools/doctor.py` | `python tools\doctor.py` |

If `python` is not on your PATH on Windows, use the launcher: `py tools\install_skills.py`.

The installer copies `edu-orchestrator`, `edu-planner`, `edu-writer` and `edu-reviewer` from
`05_Bukti_Proses/skills_package/` into `~/.workbuddy-ai/skills/` (on Windows,
`C:\Users\<you>\.workbuddy-ai\skills`), then counts them back to confirm four arrived.
**Nothing is compiled and no package manager is involved** — a skill is a folder containing
`SKILL.md`, and "installing" it means putting that folder where the agent looks. Add `--dry-run` to
see the plan without writing anything.

Then **restart WorkBuddy**. The skill list is read when a session opens, so a session that is
already running will not see the new folders. Open a new chat, check that `edu-orchestrator` is
recognised, then verify the rest of the clone with `doctor.py` (table above).

It runs six checks and exits non-zero if any fails, so a broken clone says *where* it is broken:

| # | Check | What a FAIL means |
|---|-------|-------------------|
| 1 | Python 3.6+ | the grounding check cannot run |
| 2 | four contracts in the clone | the clone is incomplete |
| 3 | four `edu-*` skills installed | run `install_skills.py`, then restart |
| 4 | rulebook, CP, actual-context register, both source sheets | the knowledge layer is missing |
| 5 | rulebook and wujud-zat source copies share one SHA-256 each | a copy has drifted — the Reviewer would judge against different rules than the Writer wrote to |
| 6 | grounding check on both runs | a draft no longer resolves against its sources |

A healthy clone prints `8 passed / 0 failed / 0 warning` and exits 0.

### First run

Paste this into the new chat:

> Use `edu-orchestrator`. Topic: Perubahan Wujud Zat. Fase C (grades V–VI).
> CP codes: CP-B.1.1.4 and CP-C.2.2. Formats: lesson plan, article, quiz.
> Source: `assets/source_material_wujud_zat.md`.

Expect this sequence, and nothing shorter:

```
Plan → Draft → Review → (REJECT → remediate, max 3) → APPROVE → STOP at the approval gate
```

The run must end at `publish_status: PENDING`. **If it publishes on its own, the install is wrong** —
the gate is the product, and it is the first thing to verify.

### If something fails

| Symptom | Cause | Fix |
|---------|-------|-----|
| `doctor.py` says `0 of 4 installed` | skills went somewhere the agent does not read | point both scripts at the real folder: `--dest <path>`, or set `WORKBUDDY_SKILLS_DIR` |
| `could not replace ...` | a file is open in an editor, or the agent is still running (common on Windows) | close it and retry |
| `python: command not found` (Windows) | Python not installed, or not on PATH | try `py tools\doctor.py`; otherwise install Python 3 and tick *Add to PATH* |
| `python3: command not found` (Linux/macOS) | Python 3 missing | `sudo apt install python3` — the grounding check is the point of the project, so `doctor.py` will not pass without it |
| Skills still not recognised after install | session not restarted | quit WorkBuddy fully, reopen, new chat |

**Windows specifics.** `cmd`, PowerShell and Git Bash all work — there is no bash script to run. Use
backslashes (`tools\doctor.py`) or forward slashes; both are accepted. If the console prints colour
codes as text, add `--no-color`.

**Line endings.** `.gitattributes` pins `*.py` and `*.md` to LF and marks the PDFs and the extracted
text as binary, so a Windows clone with `core.autocrlf=true` does not rewrite the repository and
does not show a whole-file diff after a pull.

**What you need:** WorkBuddy (or any agent runtime that reads `SKILL.md` folders) and Python 3.6+.
No API keys of its own, no build step, no database.

---

## Known limitations (stated, not hidden)

- **One Reviewer, not an adversarial pair.** A systematic blind spot in the Reviewer is a systematic
  blind spot in the product. Mitigation: every verdict must quote the text and cite a rule, so a
  human can audit the audit. This is how we caught our own R001 failure.
- **Grounding needs two checks, and we only had one.** Attribution ("does this sentence carry a
  tag?") was enforced; resolution ("does the tag point at a source that actually says this?") was
  not. That gap is what produced the 29 October rejection. A tag is not a citation.
- **Run `-002` was originally anchored to a topic entry, not a fact sheet — fixed.** Its claims cited
  `[src:B4]`, the curriculum topic name in `cp_ipas.md`. The deterministic check found 84 class
  violations; a dedicated `source_material_wujud_zat.md` was created from the official Panduan IPAS
  (pp. 26–27) and every artefact re-tagged to `[src:W1]`–`[src:W11]`. Content was not edited. Two
  entries (`[src:W10]`, `[src:W11]`) are **team-derived** — direction mapping and everyday examples
  the official guide does not state — labelled as such and awaiting teacher validation.
- **Strict grounding produces thin material.** A thin source yields a thin pack, and the agent will
  look less impressive than a general chatbot on the same topic. We optimised for the failure mode
  that damages trust.
- **The animatic has no audio yet.** `07_video_animatik.html` runs 4:45 with subtitles; narration
  is not recorded.
- **Indonesian only.** TC-17 (bilingual consistency) is recorded as not yet run.
- **Screenshots of the critical cases are not captured yet.** Tracked in
  `05_Bukti_Proses/evidence_bundle/03_screenshots/INDEX.md`.

---

## Licence and data

- **Code, contracts and documentation:** MIT — see `LICENSE`. This covers the pipeline, the four
  `SKILL.md` files, the checker and every document in this repository.
- **Attribution:** the substance of the rulebook is Pak Arief's professional judgement, formalised by
  the team. The MIT licence covers this repository's implementation of it, not his authorship.
- **Two official Indonesian ministry documents are redistributed unmodified** —
  `Final Panduan Mata Pelajaran IPAS_03_10_2025_Revisi 4.pdf` and
  `Permendikdasmen-no-13-tahun-2025.pdf` — together with the plain text extracted from them. They are
  here because the grounding check is meaningless without the text it checks against: a reviewer
  must be able to open the page a claim came from. **Their terms are not ours to relicense.** See
  `THIRD_PARTY_NOTICES.md`; any of them will be removed on request.
- **What is *not* redistributed:** six RPP documents downloaded from `centralpendidikan.com`, a
  commercial assessment guide, a WhatsApp export and the hackathon handbook. Reasons per file in
  `02_Sumber/README.md`.
- **Source material:** run `-001` (`source_material_energi.md`) is mock, written for this hackathon,
  and says so in its own header. Run `-002` (`source_material_wujud_zat.md`) is **quoted from the
  official Panduan IPAS pp. 26–27**, with page numbers, because mock data was the original defect.
  Real-world claims carry an official URL and an access date in `konteks_aktual.md`.
- **Student data:** score tables use anonymised participant IDs. No real student data is included.

---

*Prepared for the Tencent Cloud Hackathon Indonesia 2026 submission. Every claim in this README is
cross-referenced to a file in the repository.*
