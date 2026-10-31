# 01 — Architecture (canonical)

> **Status of this document:** canonical source of truth for architecture.
> Derived, judge-facing summaries: `06_Submission/05_Architecture.md` (condensed),
> `06_Submission/architecture_diagram.html` (visual), `README.md` §Pipeline.
> If those disagree with this file, **this file wins** and they must be corrected.
>
> **Evidence rule:** every architectural claim below carries a status.
> `IMPLEMENTED` = an artefact in the repo proves it. `SPECIFIED` = written into a contract but not
> yet demonstrated. `GAP` = not true today. No claim is left unmarked.

---

## 1. What the system is

EduCraft turns **one approved source document** into a **teaching pack of several formats**, and
refuses to release it until an independent Reviewer has checked it against a written rulebook and a
human has approved.

It is not a web application. It is:

| Layer | What it is | Where it lives |
|-------|-----------|----------------|
| Contracts | 4 agent specifications (`SKILL.md`) | `05_Bukti_Proses/skills_package/` |
| Knowledge | read-only facts, curriculum outcomes, rulebook, actual-context register | `03_Hasil/referensi/` |
| State | run configuration + append-only audit log | `03_Hasil/edu_output*/` |
| Output | Markdown drafts, HTML quiz/animatic, PNG infographic, print PDFs | `03_Hasil/` |

---

## 2. Design invariants

These five are the reason the system exists. If an invariant is dropped, the product has no thesis.

| # | Invariant | Enforcement | Status |
|---|-----------|-------------|--------|
| I1 | **One source of facts.** No fact outside the approved source; fallback is the literal token `[UNVERIFIED]`. | Writer contract + R001 | IMPLEMENTED |
| I2 | **Veto is separate from rewrite.** Reviewer may reject, never rewrite; Writer may rewrite, never approve. | Separate contracts | IMPLEMENTED |
| I3 | **No self-publication.** Publication is a distinct step that requires an explicit human act. | Orchestrator step 5 + run config | IMPLEMENTED (run 002: gate opened only after 17:19 approval) |
| I4 | **Bounded loops.** Three rejections means halt and escalate; never retry forever. | Orchestrator hard rule | SPECIFIED — counter is recorded in prose, not enforced by a file |
| I5 | **Source content is data, not instructions.** Embedded commands are reported, never obeyed. | Orchestrator hard rule | SPECIFIED — no injection test executed yet (TC-15) |

---

## 3. Components

| # | Component | Type | Owns | May not do | Status |
|---|-----------|------|------|-----------|--------|
| C1 | Teacher / SME | Human | Approval decision, source selection | — | IMPLEMENTED |
| C2 | Orchestrator | Agent (state machine) | Routing, iteration limit, gates, audit log | Publish, write content, change a verdict | IMPLEMENTED |
| C3 | Planner | Agent | Decomposition into per-format outline + CP mapping | Invent facts, draft prose | IMPLEMENTED |
| C4 | Writer | Agent | All draft text + asset briefs (article, RPP, quiz, slide outline, infographic brief, video script) | Use facts outside the source, approve its own work | IMPLEMENTED |
| C5 | Reviewer | Agent | Verdict `APPROVE`/`REJECT` + findings with rule ID and quoted text | Rewrite content, soften a finding to end a loop | IMPLEMENTED |
| C6 | Knowledge assets | Files (read-only) | Facts, CP, rulebook, actual-context register | — | IMPLEMENTED |
| C7 | Run record | Files (append-only) | Run config, audit log, review reports | — | IMPLEMENTED |

### 3.1 Reconciliation with the run logs

The audit logs for run `-002` label some steps `edu-infographic`, `edu-video`, `edu-quiz`.
**Those are not separate agents.** They are execution phases of **C4 Writer** producing a different
artefact class (visual and interactive assets) from an already-approved brief. They have no
independent veto and no separate contract.

This matters for scoring honesty: the system has **four agents with distinct roles**, which satisfies
the Challenge C requirement of at least three (Planner, Writer, Reviewer + Orchestrator). We do not
claim five or six agents. A separate `Producer` skill is a v2 refinement, listed in
`07_GAP_DAN_REKOMENDASI.md` — not a current fact.

---

## 4. Trust boundaries

| Boundary | Between | What may not cross | Status |
|----------|---------|--------------------|--------|
| B1 Read-only knowledge | C2–C5 ↔ C6 | Any write. An agent may not edit the source, the CP, or the rulebook to make its own output pass | IMPLEMENTED (files are static assets) |
| B2 Human authority | Agent loop ↔ approval gate | Publication. Reviewer `APPROVE` is a precondition, not a permission | IMPLEMENTED |
| B3 Publish authority | Gate ↔ output | Any unapproved artefact | IMPLEMENTED |
| B4 Data/instruction | Source documents ↔ agent instructions | Commands inside a source | SPECIFIED |

**B1 is the boundary most likely to be violated in practice**, because it is enforced by convention
(file permissions in a repo), not by the runtime. Mitigation: the knowledge layer is never written by
an agent step; the audit log records which asset version was read.

---

## 5. Data contracts

### 5.1 Tag taxonomy (the grounding vocabulary)

| Tag class | Form | Meaning | Resolves to |
|-----------|------|---------|-------------|
| Fact | `[src:1]` … `[src:n]` | A factual claim | A numbered section in `source_material_*.md` |
| Curriculum | `[src:CP]`, `[src:B5]`, `[src:C4]`, `[src:B4]` | A curriculum reference, **not a fact** | A CP code in `cp_ipas.md` |
| Actual context | `[src:CA1]` … | A real-world claim | An entry in `konteks_aktual.md` with official URL + access date |

**Rule:** a curriculum tag may never stand in for a fact tag. This is exactly the defect that
produced the 29 October rejection, and it recurred in run `-002` (see `07_GAP_DAN_REKOMENDASI.md` G1).

### 5.2 Reviewer verdict

```json
{
  "status": "APPROVE | REJECT",
  "iteration": 1,
  "findings": [
    {
      "rule": "R002",
      "severity": "critical | major | minor",
      "quote": "exact offending text",
      "reason": "why it violates the rule",
      "suggestion": "concrete fix",
      "location": "file + section"
    }
  ]
}
```
Status: IMPLEMENTED — the schema is used verbatim in `03_Hasil/edu_output_wujud_zat/05_review.md` §PASS 1.

### 5.3 Run configuration (state of record)

| Field | Purpose | Status |
|-------|---------|--------|
| `run_id` | Reproducibility | IMPLEMENTED |
| `topic`, `phase`, `cp_codes` | Scope | IMPLEMENTED |
| `source_path`, `source_version` | Which facts were in play | IMPLEMENTED (path only; version not hashed) |
| `iteration` | Loop counter | GAP — lives in prose, not a field |
| `per_format_status` | Which artefact is at which verdict | GAP |
| `approver`, `approved_at`, `publish_status` | Accountability | IMPLEMENTED |

---

## 6. Execution sequence

```
S0  Intake        Teacher supplies source + topic + phase
                  → writes 00_run_config.md (publish_status: PENDING)
S1  Plan          Planner → outline per format, CP mapping, gaps flagged
S2  Draft         Writer  → draft v1, every factual sentence tagged
S3  Ground        Orchestrator → tag-resolution check (deterministic)
S4  Review        Reviewer → APPROVE | REJECT + findings[]
                  REJECT → back to S2, iteration += 1; at iteration 3 → S6
S5  Approve       Human reads the pack, decides
S6  Release       Only after explicit approval. Otherwise halt with findings.
```

**S3 is the step this project was missing.** It is specified here, and a working implementation is
shipped at `tools/check_grounding.py`. Status: IMPLEMENTED as a tool; GAP as a mandatory pipeline
step (the orchestrator contract does not yet require running it).

---

## 7. Failure modes and designed responses

| Failure | Symptom | Designed response | Status |
|---------|---------|-------------------|--------|
| F1 Unresolvable tag | `[src:9]` with no such section | Grounding check fails → back to Writer | Tool IMPLEMENTED; gate GAP |
| F2 Curriculum tag used as fact | `[src:B4]` on a science claim | Grounding check flags tag class mismatch | Tool IMPLEMENTED (class-aware) |
| F3 Thin source | Writer produces short, repetitive material | Refuses to pad; escalates with `PERLU KONFIRMASI GURU` | IMPLEMENTED (run `-002` gap flags) |
| F4 Reviewer blind spot | Violation passes | Verdict must quote text + cite rule, so a human can audit the audit | IMPLEMENTED (this is how F-01 was caught) |
| F5 Infinite remediation | Loop never ends | Hard cap 3, then escalate | SPECIFIED |
| F6 Prompt injection in source | Embedded "ignore the rules" | Treated as data, reported to user | SPECIFIED |

---

## 8. Out of scope (deliberate)

- No fine-tuning, no vector database, no orchestration framework. The state machine is a contract.
- No student-facing app. Output is a printable pack and a self-contained HTML quiz.
- No automated plagiarism check, no automatic translation. Both are roadmap items.

---

## 9. Evidence map

| Claim | Proved by |
|-------|-----------|
| Four agents, distinct roles | `05_Bukti_Proses/skills_package/*/SKILL.md` |
| Reviewer vetoes, cites rule, quotes text | `03_Hasil/edu_output_wujud_zat/05_review.md` §PASS 1 (5 major findings) |
| Human approval gate blocks publication | `03_Hasil/edu_output_wujud_zat/audit_log.md` §3.7 (approval 17:19) |
| Reject → remediate → approve cycle | `03_Hasil/audit/review_kepatuhan_R001-R011_2026-10-29.md` → `..._REVISI.md` |
| Loop counter | GAP — prose only, no field. Do not claim it is enforced. |
| Tag resolution | `tools/check_grounding.py` output, reproduced in `06_TRACEABILITY.md` |
