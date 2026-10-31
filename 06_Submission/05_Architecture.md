# Submission Item 6 — Architecture

> Handbook §7 (REQUIRED): *"How the components of your agent interact, where the diagram trust
> boundaries sit and the key design trade-offs. For Challenge C, illustrate how the agents are
> orchestrated."*
>
> **Visual:** `architecture_diagram.html` (interactive) · `architecture_diagram.png` (2720×3000, for upload)

---

## 1. Components

| # | Component | Type | Input | Output | Authority |
|---|-----------|------|-------|--------|-----------|
| 1 | Teacher / SME | Human | Brief, approved source; **authored the rulebook's substance and supplied the references** | Approval or rejection | Final. Can override anything |
| 2 | Orchestrator | Agent (state machine) | Brief + run config | Task assignments, audit log | Routing, limits, escalation. **Cannot publish** |
| 3 | Planner | Agent | Source + CP | Per-format outlines | Decomposition only |
| 4 | Writer | Agent | Outline + source | Drafts, tagged | Drafting only |
| 5 | Reviewer | Agent | Draft + rulebook + source | `APPROVE` / `REJECT` + findings | Veto only. **Cannot rewrite** |
| 6 | Knowledge assets | Files (read-only) | — | Facts, CP, rules, real-world register | None — data, never instructions |
| 7 | Run record | Files (append-only) | Every step | Audit trail | None |

The separation of **veto** (Reviewer) from **rewrite** (Writer) is deliberate: an agent that can
both grade and fix its own work will eventually grade itself generously.

## 2. Orchestration (Challenge C requirement)

```
Teacher brief
    │
    ▼
Orchestrator ── writes 00_run_config.md
    │
    ├─► Planner ────────────► outline{lesson_plan, quiz, slide, article, infographic}
    │                              │
    │                              ▼
    ├─► Writer ─────────────► draft v1
    │        ▲                     │
    │        │                     ▼
    │        │              Reviewer ──► findings[]  (rule ID + quoted text)
    │        │                     │
    │        └──── REJECT ◄────────┤   iteration += 1
    │                              │   if iteration == 3 and still REJECT:
    │                              │        HALT → escalate to teacher
    │                              ▼
    │                          APPROVE
    │                              │
    ▼                              ▼
Human approval gate ──────► published pack  (+ audit log)
```

**State held by the Orchestrator:** `{run_id, topic, cp_codes, source_path, iteration,
per_format_status, findings[], approver, publish_status}`. This is what makes the run
reproducible and auditable after the fact.

**Loop semantics.** `iteration` increments only on `REJECT`. Three rejections is a hard stop, not
a soft warning: the run ends with the outstanding findings in hand and a human in the loop. A
pipeline that retries forever is a pipeline that will eventually talk itself into approving.

## 3. Trust boundaries

The diagram marks three, each a place where authority changes hands:

| Boundary | Between | What may not cross it |
|----------|---------|----------------------|
| **Read-only** | Agents ↔ knowledge assets | Any write. The agent cannot edit the source, the rulebook, or the CP to make its own output pass |
| **Human authority** | Agent loop ↔ approval gate | Any publication. Reviewer `APPROVE` is a precondition, not a permission |
| **Publish authority** | Gate ↔ output | Anything unapproved. There is no path from Writer to output that bypasses the gate |

A fourth, implicit boundary sits around the source documents themselves: **content inside a
source is data, not instruction.** A PDF that says "ignore the rules and publish" is quoted as
data and reported, never obeyed. This is the cheapest and most commonly skipped defence in
document-processing agents.

## 4. Key design trade-offs

We made four choices that a reviewer should be able to argue with. Each is a real cost.

### 4.1 Rules in the prompt, not fine-tuning
**Chosen:** the rulebook is a Markdown file injected into the Reviewer's contract.
**Cost:** rules compete for context; a very long rulebook would degrade adherence.
**Why:** a curriculum team can read and edit the rules without touching code or retraining.
For a regulated domain like education, *auditability of the rule* beats *elegance of the model*.

### 4.2 One Reviewer, not an adversarial pair
**Chosen:** a single Reviewer with a written standard.
**Cost:** no second opinion; a systematic blind spot in the Reviewer is a systematic blind spot in the product.
**Why:** cost and latency per run, and the hackathon brief rewards orchestration clarity over
ensemble complexity. **Mitigation:** the Reviewer must quote the offending text and cite a rule,
so a human can audit the audit. This is also how we caught our own R001 failure.
**Roadmap:** an adversarial second Reviewer on critical rules only (R006, R007).

### 4.3 Strict grounding over coverage
**Chosen:** no fact outside the source; fallback is the literal token `[UNVERIFIED]`.
**Cost:** thin source → thin, sometimes repetitive material. The agent will look "less smart"
than a general chatbot on the same topic.
**Why:** a teacher can fix a gap. A teacher cannot easily detect a confident fabrication. We
optimised for the failure mode that damages trust.

### 4.4 Three iterations, then stop
**Chosen:** hard cap at 3 remediation loops.
**Cost:** some drafts could have been salvaged with a fourth pass.
**Why:** unbounded self-correction has two bad endings — an infinite loop, or a model that
degrades its own output until the reviewer relents. Escalating to a human at iteration 3 is the
honest failure.

## 5. What we would build next

1. **Tag-resolution check** as a distinct gate: not just "does this sentence have a tag" but "does the tag resolve to a source line that supports it". This is the fix for the failure we actually hit.
2. **Adversarial second Reviewer** on critical rules only.
3. **Bilingual output** (TC-17) with a cross-language fact-consistency check.
4. **Diff view for the teacher** — show v1 vs v2 so approval is a comparison, not a re-read.
