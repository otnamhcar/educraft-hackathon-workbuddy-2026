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

## How to reproduce

1. Install the four skills from `05_Bukti_Proses/skills_package/` into your agent runtime.
2. Each skill is self-contained: its `assets/` folder already holds the rulebook, `cp_ipas.md`,
   `konteks_aktual.md` and both source materials. Pick the source for the topic you want to run.
3. Invoke the orchestrator with: topic, grade band (Fase B or C), and the CP codes.
4. Expect: `Plan → Draft → Review → (REJECT → remediate ≤3) → APPROVE → STOP at the approval gate`.
5. The run must end at `publish_status: PENDING`. If it publishes on its own, the install is wrong.

No build step, no dependencies, no API keys required to read the contracts.

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

- **Code and contracts:** MIT — see `LICENSE`.
- **Source material** is mock/illustrative, written for this hackathon. The handbook permits mock
  data. Real-world claims are the exception: those carry an official URL and an access date in
  `konteks_aktual.md`.
- **Student data:** score tables use anonymised participant IDs. No real student data is included.
- **Third-party curriculum documents** are *not* redistributed here. They are reference material
  only; this repository links to the official sources instead.

---

*Prepared for the Tencent Cloud Hackathon Indonesia 2026 submission. Every claim in this README is
cross-referenced to a file in the repository.*
