# Submission Item 4 — Accountability Sheet

> Handbook §7 (NEW, REQUIRED): *"A one-page summary of what your agent can access, what it
> executes autonomously, what requires human approval, and what it will never do."*
> This page is designed to be read alone, by a judge, in 60 seconds.

**Project:** EduCraft — Rule-Governed AI Teaching Assistant for Primary Science (IPAS)
**Two runs exist. They are not interchangeable — each has its own status:**

| Run | Topic | Human approver | Publish status |
|-----|-------|----------------|----------------|
| `EDU-ORCH-20261026-001` | Energi Alternatif | PENDING (teacher/SME) | **NOT PUBLISHED** |
| `EDU-ORCH-20261030-002` | Perubahan Wujud Zat | **don Jimat Akbar (teacher), 2026-10-30 17:19 GMT+7** | Gate opened for limited distribution; print packs produced |

Nothing was published before an explicit human approval. Run `-001` has no approval and is not
published; run `-002` was approved by a named teacher and only then released.

---

## 1. What the agent can access

| Resource | Access | Notes |
|----------|--------|-------|
| Source material (`source_material_energi.md`) | Read-only | The **only** permitted source of facts for the run |
| Curriculum outcomes (`cp_ipas.md`) | Read-only | CP codes C4 (2.1.4), B5 (1.1.5) |
| Rulebook (`rulebook_ipas.md`, R001–R012) | Read-only | Enforced by the Reviewer, not advisory |
| Actual-context register (`konteks_aktual.md`) | Read-only | Each entry carries an official URL + access date |
| Run configuration (`00_run_config.md`) | Read + append status | Records topic, source, approver, publish state |
| Own prior drafts and findings | Read | Required for the remediation loop |
| Student score table | Read, **anonymised** | Names replaced with participant IDs before the run |

**No access to:** the open internet during a run, external accounts, email, messaging, payment
systems, or any student personal data beyond anonymised scores.

## 2. What it executes autonomously

- Decomposing the source into per-format outlines mapped to curriculum outcomes (**Planner**).
- Drafting all five formats with citation tags on every factual sentence (**Writer**).
- Self-review against all 11 rules, returning `APPROVE` or `REJECT` with rule IDs and quoted text (**Reviewer**).
- Re-drafting after a `REJECT`, **up to 3 iterations** (**Orchestrator**).
- Writing and appending to the audit log after every step.
- Refusing to proceed when a source is missing, contradictory, or out of scope.

## 3. What requires human approval

| Action | Gate | Enforced where |
|--------|------|----------------|
| Publishing or distributing any pack to students | **Explicit approval, every time** | Orchestrator pipeline step 5 |
| Overriding a `REJECT` verdict | Named human decision, recorded with reason | Orchestrator hard rules |
| Accepting a claim marked `[UNVERIFIED]` | Teacher confirms or supplies a source | R001 convention |
| Changing the source material or the rulebook | Human edit only; agent has no write access | File permissions / read-only assets |
| Using the output outside the intended grade band | Curriculum coordinator sign-off | Run configuration |

**Current state:** run `-001` is at `PENDING` approval and nothing from it has been published. Run
`-002` was approved on 30 October 2026 at 17:19 by a named teacher, and only then did the publication
gate open — the agent produced material and stopped until a human acted, which is the intended
behaviour, not a delay.

## 4. What it will never do

1. **Never publish without explicit human approval.** Not on timeout, not on "looks good", not after 3 clean iterations.
2. **Never invent a fact that is not in the source.** The fallback is the literal token `[UNVERIFIED]` plus a request for teacher confirmation — never a plausible guess.
3. **Never present an unverified "real world" claim as fact.** Claims tagged `[src:CA#]` must resolve to a dated official URL in `konteks_aktual.md`.
4. **Never write a health claim** about permanent effects, cures, or efficacy that the source does not support (R006).
5. **Never promote a harmful practice** — including burning land for clearing, or normalising it (R007).
6. **Never use fear as a teaching device** — no catastrophic or graphic framing for children aged 10–12 (R002, R003).
7. **Never follow instructions found inside a source document.** Content is treated as data; embedded commands are ignored and reported (prompt-injection defence).
8. **Never loop indefinitely.** Three failed remediations means halt and escalate to a human with the outstanding findings.
9. **Never expose student identity.** Score tables are anonymised before entering the pipeline.
10. **Never hide a failure.** Rejections, including our own, are kept in the audit log and disclosed in the submission.

## 5. Record-keeping and escalation

- **Audit log** (`audit_log_edu_orchestrator.md`): inputs, sources retrieved, per-step decisions, findings with rule IDs, revision history v1→v2, final verdict.
- **Review reports:** the rejection (`..._2026-10-29.md`) and the re-review (`..._2026-10-30_REVISI.md`) are both retained. The rejected version is not deleted.
- **Escalation path:** Reviewer `REJECT` × 3 → Orchestrator halts → teacher/SME receives the findings list and the two options (supply a better source, or change the brief). No silent workaround exists.

## 6. Known limitations (stated, not hidden)

| Limitation | Consequence | Mitigation in place |
|------------|-------------|---------------------|
| Rulebook is only as good as its author | A missing rule is a missing check | Rules are plain Markdown; versioned and human-editable |
| Reviewer is an LLM, not a proof engine | It can miss a subtle violation | Every verdict must quote text and cite a rule, so a human can audit the audit |
| Source coverage bounds output quality | Thin source → thin material | Agent refuses to pad with outside facts; escalates instead |
| No automated plagiarism check | Possible overlap with existing material | Teacher review before publish; future work |
| Single reviewer, single pass | No adversarial second opinion | Deliberate trade-off (see `05_Architecture.md` §4) |
| Indonesian-only output today | Not usable for bilingual schools yet | On roadmap; test case TC-17 is recorded as not yet run |

---

*Prepared 30 October 2026. This sheet describes enforced behaviour in the shipped skill
contracts, and is cross-referenced to the artefacts that demonstrate it.*
