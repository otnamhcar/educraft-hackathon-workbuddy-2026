# 02 — Workflow (canonical)

> **Scope:** how a run executes, in what order, who writes which file, and what a valid stop looks
> like. Architecture (components, boundaries) is in `01_ARSITEKTUR.md` — not repeated here.

---

## 1. The run in one table

| Step | Actor | Input | Artefact written (path) | Guard before advancing | On failure |
|------|-------|-------|--------------------------|------------------------|------------|
| S0 Intake | Orchestrator | teacher brief | `00_run_config.md` | Source file exists and is readable | Stop; ask for source |
| S1 Plan | Planner | source + CP | `00_plan.md` | Every format mapped to a CP code, or `PERLU KONFIRMASI GURU` | Flag gap, continue with warning |
| S2 Draft | Writer | plan + source | `01_artikel.md`, `02_*brief.md`, `03_*storyboard.md`, `04_kuis*.md` | Every factual sentence carries a tag | Emit `[UNVERIFIED]`, do not invent |
| S3 Ground | Orchestrator | drafts + source | `grounding_report.md` | 0 dangling tags, 0 class mismatches | Back to S2 with the report |
| S4 Review | Reviewer | drafts + rulebook + source | `05_review.md` | Verdict + findings with rule ID and quoted text | `REJECT` → S2, `iteration += 1` |
| S4b Limit | Orchestrator | iteration counter | audit log entry | `iteration < 3` | At 3 → S6 (escalate, do not publish) |
| S5 Approve | Human | whole pack | approval line in `00_run_config.md` | Explicit approval, name + timestamp | No approval → halt |
| S6 Release | Orchestrator | approved pack | print packs, quiz HTML, audit close | Approval recorded before any distribution | Refuse |

**Status of S3:** the checker exists (`tools/check_grounding.py`); making it a mandatory gate is a
**GAP** — the orchestrator contract does not yet require it. See `07_GAP_DAN_REKOMENDASI.md` G1.

---

## 2. States and transitions

```
S0 ──► S1 ──► S2 ──► S3 ──► S4 ──APPROVE──► S5 ──approved──► S6
                    ▲         │
                    └──REJECT─┤
                              └──iteration==3──► S6-ESCALATE (no publication)
```

| Transition | Condition | Recorded where |
|-----------|-----------|----------------|
| S2→S3 | draft complete for the requested formats | audit log §agent exchange |
| S3→S2 | ≥1 dangling or misclassified tag | `grounding_report.md` |
| S3→S4 | 0 findings | audit log |
| S4→S2 | `REJECT` | findings list + iteration increment |
| S4→S5 | `APPROVE` | verdict JSON |
| S5→S6 | explicit human approval | `approver`, `approved_at` |
| S4→S6 | third `REJECT` | escalation entry with outstanding findings |

**Terminal states:** `RELEASED` (approved and distributed) and `ESCALATED` (halted with findings).
There is no path from `S4` to `RELEASED`.

---

## 3. Artefact ledger

Every run owns exactly one folder. Nothing is written outside it except the audit log.

| File | Producer | Immutable after? | Purpose |
|------|----------|------------------|---------|
| `00_run_config.md` | Orchestrator | No (status fields only) | State of record |
| `00_plan.md` | Planner | No | Traceability to CP, declared gaps |
| `0N_*.md` drafts | Writer | Superseded, not edited in place | Versioned content |
| `05_review.md` | Reviewer | **Yes** — append new pass, never rewrite an old one | Verdict history |
| `grounding_report.md` | Orchestrator | Yes, per pass | Deterministic tag check output |
| `audit_log.md` | Orchestrator | Append-only | Who decided what, when |
| print PDFs / PNG / HTML | Writer (asset phase) | Regenerated from source HTML | Deliverables |

**Rule:** a rejected draft is never deleted or silently patched. It is superseded and the reason is
recorded. This is what makes the 29 October rejection usable as evidence.

---

## 4. Iteration semantics

- `iteration` counts **rejections**, not drafts. `iteration = 1` means one rejection has occurred.
- Increment happens **once per `REJECT` verdict**, on the whole pack, not per format.
- At `iteration == 3` the run **halts**: no fourth draft, no "one more try". The teacher receives the
  outstanding findings and two options: supply a better source, or change the brief.
- Rationale: unbounded self-correction has two endings — an infinite loop, or a model that degrades
  its own output until the reviewer relents.

**Status:** semantics are IMPLEMENTED in behaviour (run `-002` used 2 of 3). The counter is
**GAP** as a machine-readable field — it exists only as a sentence in the audit log, so it cannot be
asserted deterministically. Fix: add `iteration: <int>` to `00_run_config.md` and rewrite it at every
transition.

---

## 5. Approval protocol (what counts as evidence)

An approval is valid only if all four exist:

1. **Named human** — not "the team", not "the teacher" generically.
2. **Timestamp** — date and time with timezone.
3. **Scope** — which artefacts, and explicitly whether the answer key and any CP-gap waiver are covered.
4. **Verbatim statement** — the approving sentence, quoted.

Recorded as, e.g.:

```markdown
- Human approver: <name>, <role>
- Approved at: 2026-10-30 17:19 GMT+7
- Scope: all artefacts in this run, including Fase-B topic placement in grades V–VI,
         27 quiz items and key, final infographic
- Statement: "ok saya setujui"
```

**Run `-002` satisfies all four.** Run `-001` does not — it is still `PENDING`, and any document that
describes run `-001` as approved is wrong.

---

## 6. Escalation

| Trigger | What the human receives | What the system must not do |
|---------|--------------------------|------------------------------|
| 3rd `REJECT` | Findings list with rule IDs and quoted text; two options (better source, changed brief) | Produce a fourth draft |
| Missing source | Request naming what is missing | Invent a plausible source |
| Out-of-phase topic | `PERLU KONFIRMASI GURU` on the outline | Silently retarget the grade band |
| Unresolvable tag | The exact tag and the file it failed to resolve in | Drop the sentence quietly |

---

## 7. Two runs, two purposes (do not conflate)

| | Run `-001` Energi | Run `-002` Wujud Zat |
|---|---|---|
| Purpose | Demonstrate the reject → remediate → approve cycle | Demonstrate a complete, approved, printed pack |
| Verdict path | REJECT (29 Oct) → remediate → APPROVE (30 Oct) | REJECT (5 major) → remediate → APPROVE (iteration 2) |
| Human approval | **none — PENDING** | **yes — 30 Oct 17:19** |
| Publication | none | gate opened, print packs distributed |
| Use in submission | evidence of the loop and of failure disclosure | evidence of the gate and of a real deliverable |

Any statement about "the run of record" must say which one. Conflating them is the single easiest
inconsistency for a judge to find (see `07_GAP_DAN_REKOMENDASI.md` G2).

---

## 8. What must never happen (workflow-level)

1. A draft reaching `RELEASED` without a recorded human approval.
2. An iteration count above 3.
3. A review report edited after the fact instead of a new pass being appended.
4. A rejected artefact deleted.
5. A publish status changed by anything other than a human decision.
