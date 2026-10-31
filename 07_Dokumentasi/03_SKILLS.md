# 03 — Skills and role boundaries (canonical)

> **Purpose:** prove that no two agents own the same decision. A role is defined by three things:
> what it must produce, what it may never do, and what it is allowed to read.

---

## 1. Role map

| Skill | Role | One-sentence mandate | Reads | Writes |
|-------|------|----------------------|-------|--------|
| `edu-orchestrator` | State machine | Holds state, routes work, enforces limits and gates | run config, all artefacts | run config status fields, audit log, grounding report |
| `edu-planner` | Decomposer | Turns one topic into a per-format outline mapped to CP codes | source, CP | `00_plan.md` |
| `edu-writer` | Drafter | Produces every text and asset artefact, strictly from the source | plan, source, findings | drafts, briefs, rendered assets |
| `edu-reviewer` | Gate | Returns `APPROVE`/`REJECT` with rule ID and quoted text | drafts, rulebook, source | `05_review.md` |

Four skills. Not five, not six. The audit-log labels `edu-infographic`, `edu-video`, `edu-quiz` are
**phases inside `edu-writer`** (asset rendering), not separate agents — they hold no veto.

---

## 2. Non-overlap proof (RACI)

`R` = does the work · `A` = accountable for the decision · `C` = consulted · `I` = informed.
**Every row has exactly one `R`.** If a row ever has two, the design has drifted.

| Artefact | Orchestrator | Planner | Writer | Reviewer | Human |
|----------|:---:|:---:|:---:|:---:|:---:|
| Run configuration | **R** | I | I | I | A |
| Content plan / outline | I | **R** | I | C | A |
| Draft text (all formats) | I | I | **R** | C | A |
| Asset brief (infographic, video) | I | I | **R** | C | A |
| Rendered asset (PNG, HTML, PDF) | I | I | **R** | C | A |
| Grounding report | **R** | I | I | C | I |
| Review verdict | I | I | C | **R** | A |
| Audit log | **R** | I | I | I | I |
| Approval record | I | I | I | I | **R** |

Two separations carry the whole design:

- **Veto ≠ rewrite.** Reviewer holds `R` on the verdict and nothing else. Writer holds `R` on content
  and no verdict. An agent that can grade and fix its own work will eventually grade itself generously.
- **Route ≠ decide.** Orchestrator decides *when* a gate runs, never *what* the verdict is.

---

## 3. Contract schemas

### 3.1 Planner output

```json
{
  "topic": "string",
  "phase": "Fase B | Fase C",
  "formats": ["lesson_plan", "quiz", "slide_outline", "short_article", "infographic", "short_video"],
  "curriculum_refs": ["CP-B.1.1.4", "CP-C.2.2"],
  "outline": { "format_name": ["point 1", "point 2"] },
  "gaps": ["PERLU KONFIRMASI GURU: ..."]
}
```
`gaps` is mandatory. An empty array is a claim that nothing is missing, and must be true.

### 3.2 Writer output (per artefact)

```markdown
<!-- front-matter -->
format: short_article | lesson_plan | quiz | slide_outline | infographic_brief | video_script
word_count: 400
sources_used: [src:1, src:3, src:CA1]

<!-- body: every factual sentence carries a tag -->
```

Tag rules: fact → `[src:n]`; curriculum → `[src:CP]`/`[src:B4]`; real world → `[src:CA n]`;
unknown → `[UNVERIFIED]` **plus** a `PERLU KONFIRMASI GURU` note. A curriculum tag may never carry a
fact.

### 3.3 Reviewer output

See `01_ARSITEKTUR.md` §5.2. Additional constraints:

- `findings[]` may not be empty when `status = REJECT`.
- Every finding needs `rule`, `quote`, `reason`, `suggestion`. A finding without a quote is invalid.
- The Reviewer may not propose a full rewrite; `suggestion` is a direction, not replacement prose.

---

## 4. "May never" list (the actual guardrails)

| Role | May never |
|------|-----------|
| Orchestrator | Publish; write or edit content; change a verdict; exceed 3 iterations; edit the rulebook or source |
| Planner | Introduce a fact not in the source; draft prose; approve anything |
| Writer | Use a fact outside the source; approve its own draft; publish; edit the rulebook; drop a finding without addressing it |
| Reviewer | Rewrite content; approve on a rule that is not in the rulebook; end a loop by softening a finding |

---

## 5. Overlaps that exist today (and the fix)

| Overlap | Why it is a problem | Fix | Status |
|---------|---------------------|-----|--------|
| Rulebook shipped 2× (orchestrator + reviewer assets) | Two copies can drift; then "which rules applied?" has no answer | Keep one canonical file, generate copies, verify by checksum | Canonical: `03_Hasil/referensi/rulebook_ipas.md`. Copies are byte-identical today (verified). Add a checksum check to CI/manual pre-submit. |
| Format list differs by document | Contracts say 3 formats; submission claims 5 + quiz | Single list lives in `01_ARSITEKTUR.md` §3 and Planner schema; contracts updated to match | **GAP** — `edu-orchestrator/SKILL.md` and `edu-writer/SKILL.md` still say three formats |
| "Run of record" ambiguous | Two runs, different statuses | Always name the run ID; `02_WORKFLOW.md` §7 defines each run's purpose | **GAP** in `03_Accountability_Sheet.md` and `04_Test_Results.md` |
| Architecture described in 4 places | Drift | `01_ARSITEKTUR.md` is canonical; others are derived and must not add claims | Documented in `00_INDEX.md` |

---

## 6. Install layout

```
skills_package/
├── edu-orchestrator/
│   ├── SKILL.md
│   └── assets/   rulebook · cp_ipas · konteks_aktual · source_material_ipas · source_material_energi
├── edu-planner/
│   ├── SKILL.md
│   └── assets/   cp_ipas
├── edu-writer/
│   ├── SKILL.md
│   └── assets/   source_material_ipas · source_material_energi
└── edu-reviewer/
    ├── SKILL.md
    └── assets/   rulebook · cp_ipas · konteks_aktual · source_material_ipas · source_material_energi
```

Each skill is self-contained: assets are **copies**, never cross-folder references, so a skill
installs alone. The cost is duplication; the control is a checksum check before submission.
