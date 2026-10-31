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

Two commands, then a health check — the scripts are in `tools/`:

```bash
./tools/install_skills.sh     # 4 skills into ~/.workbuddy-ai/skills, count verified
# restart WorkBuddy, then:
./tools/doctor.sh             # 8 passed · 0 failed · 0 warning on a healthy clone
```

Then invoke the orchestrator with: topic, grade band (Fase C), the CP codes, and the source sheet
already sitting in each skill's `assets/`. Expect
`Plan → Draft → Review → (REJECT → remediate ≤3) → APPROVE → STOP at the approval gate`, ending at
`publish_status: PENDING`. If it publishes on its own, the install is wrong.

The `assets/` folders are already populated in the clone, so "copy the knowledge layer" is not a
step. No build, no dependencies, no API keys of its own. Full walkthrough, including the Windows
note: README → "Run it yourself".

## 4. What is still missing (action required before submit)

| Gap | Why it matters | Status |
|-----|----------------|--------|
| **Public repository** | Handbook accepts either a public repo *or* an exported workflow with evidence. | ✅ **DONE** — https://github.com/otnamhcar/educraft-hackathon-workbuddy-2026 (public, MIT). Option (a) chosen. |
| **Screenshots** | Required by §7 for test results | ⏳ Capture per `04_Test_Results.md` §3; store in `05_Bukti_Proses/evidence_bundle/03_screenshots/` |
| **Demo video** | Required, 5–8 min | ⏳ Script is ready: `07_Demo_Video_Script.md` |
| **Human approval** | Ethical gate, not a formality | ✅ Run `-002` approved by teacher 30 Oct 2026 17:19; run `-001` still PENDING |

## 5. Licence and data note

- **Code/contracts:** **MIT** — `LICENSE` at the repository root; scope spelled out in README §
  "Licence and data".
- **Source material — two different bases, stated separately:**
  - Run `-001` (`source_material_energi.md`) is a **mock/illustrative** document written for this
    hackathon. Handbook §10 permits mock data (*"Mock data is acceptable"*). Its real-world claims are
    the exception and cite official URLs in `konteks_aktual.md`.
  - Run `-002` (`source_material_wujud_zat.md`) is **quoted from the official Panduan IPAS, pp. 26–27**,
    with line references. Nine entries are quotations; two (`[src:W10]`, `[src:W11]`) are team-derived
    and labelled as such.
- **Student data:** the score table uses anonymised participant IDs. No real student data is included.
- **Third-party curriculum documents ARE redistributed**, unmodified and attributed, in `02_Sumber/`:
  the official *Panduan Mata Pelajaran IPAS* (Revisi 4) and *Permendikdasmen No. 13/2025*, plus their
  text extractions. They are excluded from the MIT licence and carved out in `THIRD_PARTY_NOTICES.md`.
  The point is verification: a reader can walk any `[src:W#]` tag back to a page of the original PDF
  instead of trusting our summary. Third-party material that is **not** ours to publish — the six
  `centralpendidikan.com` RPP worksheets and the organiser's handbook — is excluded; `02_Sumber/README.md`
  lists every exclusion with its reason.
