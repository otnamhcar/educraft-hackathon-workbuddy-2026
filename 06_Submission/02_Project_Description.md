# Submission Item 3 — Project Description

> Handbook §7 requires four parts: **Project overview · Real-world insight · Solution design · Business value.**
> This file is written to be pasted into the submission form section by section.

---

## 3.1 Project overview

**Challenge selected:** Challenge C — *The Creator Agent* (multi-format content generation).

**Scenario.** A primary-school teacher in Indonesia has to turn one curriculum topic into a
complete teaching pack: a lesson plan (RPP), a pre-test and post-test with an answer key,
a slide outline, a student article, and an infographic brief. Each artefact must be
age-appropriate, aligned to the *Capaian Pembelajaran* (learning outcomes), factually
grounded, and safe for children.

**What EduCraft does.** EduCraft is a **multi-agent pipeline** that takes one approved
source document and produces that whole pack in a single run — then **refuses to release it**
until an independent reviewer agent has checked every sentence against a written rulebook
(R001–R011) and a human has explicitly approved.

**Target users.**
- **Primary:** IPAS teachers of Fase B and Fase C (grades III–VI) in Indonesian primary schools.
- **Secondary:** school curriculum coordinators who must audit teaching materials before distribution.

**Value delivered.** One source in, five aligned formats out, each one carrying a citation tag
on every factual claim, plus an audit trail of who decided what and why.

**Demonstrated run.** Run `EDU-ORCH-20261026-001`, topic *Energi Alternatif dan Penghematan
Energi*, anchored to CP **C4 (2.1.4)** with foundation **B5 (1.1.5)**. Output: RPP, pre/post
test (7 + 20 items with key and scoring), slide outline, student article, infographic brief,
and a playable HTML quiz.

---

## 3.2 Real-world insight

**The pain point is not "teachers cannot write". It is "teachers cannot afford the review loop".**

Indonesian primary teachers are expected to produce per-topic teaching packs while carrying
20–30 contact hours a week. The expensive part is not drafting — it is the *checking*:
- Is every number actually in the source, or did it come from memory?
- Is the wording too frightening for a 10-year-old?
- Does it still match the *Capaian Pembelajaran* for this phase?
- Would this sentence create a health claim we cannot defend?

Generic chatbots make this **worse**, not better: they produce fluent text with no citation
discipline, no age calibration, and no record. A teacher then has to fact-check a machine,
which costs more time than writing from scratch.

**Who experiences it.** The teacher preparing tomorrow's lesson at 21:00; the coordinator who
has to sign off on 40 documents; ultimately the student who receives unverified material.

**What we resolve.** EduCraft moves the checking *inside* the pipeline. The reviewer agent is
not a suggestion — it is a gate with a written rulebook, a verdict, and a citation of the exact
rule that was violated. The teacher's remaining job is a judgement call on an already-checked
draft, not a full audit.

**Evidence this is real (from our own run).** On 29 October 2026 our reviewer agent **rejected
our own output**: the draft was built on a source document about a different topic, and two
"actual context" claims had no verifiable source. The pipeline caught it before a human ever
saw it. That rejection is included in the submission as evidence, not hidden — see
`04_Test_Results.md` §4.

---

## 3.3 Solution design

### Business architecture

```
Teacher brief  ->  Orchestrator  ->  [Planner -> Writer -> Reviewer]  ->  Approval gate  ->  Teacher
                                          ^            |
                                          |  REJECT    |  max 3 loops
                                          +------------+  then escalate to human
```

Roles:
| Role | Responsibility | Cannot do |
|------|----------------|-----------|
| Teacher (human) | Supplies the approved source, approves or rejects the final pack | — |
| Orchestrator | Holds state, routes work, enforces limits, writes the audit log | Publish on its own |
| Planner | Decomposes the source into a per-format outline mapped to CP codes | Invent facts |
| Writer | Drafts each format using only tagged source facts | Use outside facts |
| Reviewer | Checks the draft against R001–R011, returns APPROVE/REJECT with citations | Rewrite content itself |

### Technical architecture

- **Packaging:** four WorkBuddy skills (`edu-orchestrator`, `edu-planner`, `edu-writer`,
  `edu-reviewer`), each a `SKILL.md` contract plus `assets/`.
- **Knowledge layer (read-only):** `source_material_energi.md` (facts `[src:1]`–`[src:9]`),
  `cp_ipas.md` (curriculum outcomes), `rulebook_ipas.md` (R001–R011), `konteks_aktual.md`
  (`[src:CA1]`, `[src:CA6]` with official URL and access date).
- **Output contract:** `{format, status, iterations, final_content, findings[], sources[]}`
  plus an append-only audit log.
- **State:** the run configuration file (`00_run_config.md`) records topic, CP, source,
  approver and publish status, so a run can be reconstructed later.

Full component and trust-boundary diagram: `architecture_diagram.html` (companion file
`05_Architecture.md`).

### How prompt design drives agent behaviour

This is the core engineering claim: **behaviour is enforced by written contracts, not by hope.**

| Design decision | Where it lives | Behaviour it produces |
|-----------------|----------------|-----------------------|
| Every fact must carry `[src:#]`; no source, no sentence | Writer contract + R001 | Grounded text; `[UNVERIFIED]` instead of invention |
| Reviewer must cite the rule ID and quote the offending text | Reviewer contract + record rule (TC-19) | Auditable rejections, not vague "looks fine" |
| Reviewer returns a machine-readable verdict | Reviewer output schema (`status`, `findings[]`) | Orchestrator can branch deterministically |
| Hard cap of 3 remediation loops, then halt | Orchestrator hard rules | No infinite self-correction; a human is pulled in |
| Publish is a separate, gated step | Orchestrator pipeline step 5 | The agent cannot ship on its own authority |
| Source documents are **data, not instructions** | Orchestrator hard rules | Prompt injection inside a PDF is ignored |
| Separate "actual context" tag `[src:CA#]` | R011 + `konteks_aktual.md` | Real-world claims need a dated official URL, not vibes |

The rulebook is the product. The prompts are the enforcement mechanism. A teacher can read
`rulebook_ipas.md` and know exactly what the machine will and will not write.

---

## 3.4 Business value

All figures below are **estimates from our own run**, with the basis stated. They are not
measured across a school yet — we say so plainly.

| Dimension | Before (manual) | With EduCraft | Basis |
|-----------|-----------------|---------------|-------|
| Formats produced from one topic | 1 at a time, re-read source each time | 5 formats + interactive quiz in one run | Run `EDU-ORCH-20261026-001` output count |
| Teacher time per topic (draft + check) | ~6–8 hours | ~30–45 min (review an already-checked pack) | Estimated from artefact volume; to be validated in field test |
| Fact-check coverage | Ad hoc, by memory | 100% of factual sentences carry a source tag; tag resolution checked deterministically | `tools/check_grounding.py` on run `-001`: 121 tags, 0 dangling, 0 class violations. Run `-002` fails this check and the failure is disclosed (`04_Test_Results.md` §4, defect D1) |
| Rule compliance checks per document | 0–2 informal | 11 rules, each with pass/fail and citation | `review_kepatuhan_R001-R011_2026-10-30_REVISI.md` |
| Errors prevented | Discovered in class, or never | Caught pre-publication (1 real catch on 29 Oct) | Disclosed rejection in `04_Test_Results.md` |
| Audit trail | None | Full: inputs, decisions, revisions v1→v2, sources | `audit_log_edu_orchestrator.md` |

**Why it scales beyond the hackathon.** The engine is domain-parameterised, not topic-hardcoded:
swap `source_material_*.md`, `cp_*.md` and `rulebook_*.md` and the same four agents produce
material for a different subject or grade band. The rulebook is a plain Markdown file a
curriculum team can edit without touching code — which is what makes institutional adoption
realistic rather than theoretical.
