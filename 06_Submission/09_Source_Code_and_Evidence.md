# Submission Item 9 — Source Code & Evidence of Use

> Handbook §7 (REQUIRED): *"A public code repository, or your exported WorkBuddy workflow with
> evidence of use."*

**Status: DONE — published at https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026**
(public, MIT, 31 October 2026).

---

## 1. What the code actually is

EduCraft is not a web app. It is a **set of agent contracts plus a knowledge layer**, which is the
correct artefact for this challenge: a judge can read every rule the agent obeys.

```
05_Bukti_Proses/
├── skills_package/
│   ├── README.md
│   ├── edu-orchestrator/
│   │   ├── SKILL.md                     # state machine, limits, approval gate, escalation
│   │   └── assets/
│   │       ├── rulebook_ipas.md         # R001–R012
│   │       ├── cp_ipas.md
│   │       ├── konteks_aktual.md
│   │       ├── source_material_ipas.md
│   │       └── source_material_energi.md
│   ├── edu-planner/
│   │   ├── SKILL.md                     # decomposition contract
│   │   └── assets/cp_ipas.md
│   ├── edu-writer/
│   │   ├── SKILL.md                     # drafting contract, tagging discipline
│   │   └── assets/
│   │       ├── source_material_ipas.md
│   │       └── source_material_energi.md
│   └── edu-reviewer/
│       ├── SKILL.md                     # verdict contract, must cite rule + quote text
│       └── assets/
│           ├── rulebook_ipas.md
│           ├── cp_ipas.md
│           ├── konteks_aktual.md
│           ├── source_material_ipas.md
│           └── source_material_energi.md
└── evidence_bundle/                     # run trail, screenshot slots, audit copies
```

The published repository mirrors this bundle, with `README.md` as the front page:
https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026

**Note on the duplicated rulebook:** the rulebook ships inside both `edu-orchestrator/assets/` and
`edu-reviewer/assets/` so that each skill is self-contained when installed. The two copies are
byte-identical (verified by checksum); if they ever diverge, the Reviewer's copy governs.

## 2. Evidence of use (the run trail)

A judge can reconstruct the entire run of record `EDU-ORCH-20261026-001` from these files, in this order:

| Step | File | What it proves |
|------|------|----------------|
| 1 | `03_Hasil/edu_output/00_run_config.md` | Topic, CP codes, source, approver, publish status |
| 2 | `03_Hasil/audit/audit_log_edu_orchestrator.md` | Planner → Writer → Reviewer steps, revision history |
| 3 | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-29.md` | The **REJECT** (R001, R011, R004) |
| 4 | `03_Hasil/referensi/source_material_energi.md` | Source created in response to the rejection |
| 5 | `03_Hasil/referensi/konteks_aktual.md` | CA1/CA6 with official URLs and access dates |
| 6 | `03_Hasil/materi_ajar/` | The five corrected drafts + interactive HTML quiz |
| 7 | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-30_REVISI.md` | The **APPROVE** after remediation |

That sequence — reject, diagnose, fix, re-review — is the evidence of use. A static screenshot of a
happy path would prove less.

## 3. How to reproduce

1. Install the four skills from `05_Bukti_Proses/skills_package/` into your agent runtime
   (see `01_Dokumen/CARA_IMPORT_SKILL.md`).
2. Place `source_material_energi.md`, `cp_ipas.md`, `konteks_aktual.md` and `rulebook_ipas.md`
   where the orchestrator expects them (`assets/` of each skill).
3. Invoke the orchestrator with: topic, grade band (Fase C), and the CP codes C4 + B5.
4. Expect: `Plan → Draft → Review → (REJECT → remediate ≤3) → APPROVE → STOP at approval gate`.
5. The run must end at `publish_status: PENDING`. If it publishes on its own, the install is wrong.

No build step, no dependencies, no API keys required to read the contracts.

## 4. What is still missing (action required before submit)

| Gap | Why it matters | Status |
|-----|----------------|--------|
| **Public repository** | Handbook accepts either a public repo *or* an exported workflow with evidence. | ✅ **DONE** — https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026 (public, MIT). Option (a) chosen. |
| **Screenshots** | Required by §7 for test results | ⏳ Capture per `04_Test_Results.md` §3; store in `05_Bukti_Proses/evidence_bundle/03_screenshots/` |
| **Demo video** | Required, 5–8 min | ⏳ Script is ready: `07_Demo_Video_Script.md` |
| **Human approval** | Ethical gate, not a formality | ✅ Run `-002` approved by teacher 30 Oct 2026 17:19; run `-001` still PENDING |

## 5. Licence and data note

- **Code/contracts:** intended for open publication with the submission (MIT or CC-BY-4.0 — choose
  one and state it in the repo README).
- **Source material:** `source_material_energi.md` is a **mock/illustrative** document written for
  this hackathon. The handbook permits mock data (§10: *"Mock data is acceptable"*). Real-world
  claims are the exception: those cite official URLs in `konteks_aktual.md`.
- **Student data:** the score table uses anonymised participant IDs. No real student data is included.
- **Third-party curriculum documents** in `02_Sumber/` are **not** redistributed in the public repo —
  they are reference material only. The repo should link to the official sources instead.
