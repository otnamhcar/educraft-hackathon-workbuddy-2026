# Submission Item 8 — Product Sharing

> Handbook §7 (REQUIRED): *"Where WorkBuddy added value in your build, plus your key insights
> and learnings."*

---

## 0. Where this came from

The idea, the source references and the substance of the rules came from **don Jimat Akbar**, a
practising IPAS primary-school teacher. He is not a persona in a slide: he is the person who said
which claims he would never put in front of a class, and who supplied the curriculum material the
pipeline draws from.

Our role was the other half: turn his judgement into predicates a machine can check, and build the
pipeline that enforces them. Everything below is about that half — the engineering — and it only
makes sense against the first half. **A rulebook written by engineers is a guess about pedagogy.**

---

## 1. Where WorkBuddy added value

### 1.1 Skills as the unit of engineering
The single most useful idea in this build: **a skill is a contract, not a prompt.** Each of the
four agents is a `SKILL.md` with a declared role, declared inputs, a pipeline, and a list of
hard rules it may not break. That changed the nature of the work — we stopped tuning paragraphs
and started writing specifications that a reviewer could hold the agent to.

Practical effect: when the reviewer rejected our output on 29 October, the fix was a **contract
change** (add R011, require a dated URL), not a lucky re-prompt. The fix survived the next run
because it was written down.

### 1.2 Multi-agent orchestration without a framework
No LangChain, no orchestration library. The Orchestrator skill *is* the state machine: it holds
the iteration counter, routes to Planner/Writer/Reviewer, and stops at three. For a four-agent
pipeline this was the right call — every hand-off is a readable file, and a judge can trace the
whole run by opening four Markdown files.

### 1.3 File-system-as-state
`00_run_config.md` plus an append-only audit log gave us reproducibility for free. When we needed
to explain *why* the draft changed between v1 and v2, the answer was already on disk. No database,
no tracing UI, no reconstruction from memory.

### 1.4 Project isolation for a messy build
The build spanned nine separate working sessions over two weeks. Consolidating into one project
folder with its own memory meant the agent stopped re-litigating decisions we had already made —
and, more importantly, the *rejected* artefacts stayed next to the accepted ones instead of
disappearing into an old chat.

### 1.5 Where it did not help
Being honest: long-context consistency across five output formats was still manual. The agent
would happily fix a fact in the RPP and leave the same fact stale in the slide outline. We caught
it with a grep for the old string (`145 MWp`) rather than with agent reasoning. **Cross-document
consistency needs its own gate; we do not have one yet.**

---

## 2. Key insights

### Insight 1 — Grounding has two halves, and everyone only builds one
Attribution: *does this sentence carry a citation?* Resolution: *does that citation point at a
source that actually says this?* Our first version only had attribution, and it passed its own
review while being wrong. A tag is not a citation. **This is the single most transferable lesson
from the build**, and it applies to every RAG demo that shows you a little `[1]` superscript.

### Insight 2 — A rulebook is a product artefact, not documentation
The teacher gave us the rules as judgement, not as specification: *"do not tell a child that smoke
damage is permanent"*, *"do not frighten them into caring"*, *"do not claim a product is halal
without a certificate"*. We wrote the first version down as R001–R008 and moved on.

Then the audit log started citing R009–R011, which existed nowhere. The reviewer was enforcing rules
that had been agreed in conversation but never written. **The gap was not invention — it was
transcription.** Rules that live in a person's head, or in a chat, cannot be audited, and a reviewer
citing a rule you cannot open is indistinguishable from a reviewer making one up.

Writing them down formally, with a predicate and a worked example each, was not paperwork. It was
the difference between a guardrail and a vibe — and it is also what let the teacher check our
transcription of his own judgement.

### Insight 3 — The reviewer must not be able to fix
Separating veto from rewrite keeps the reviewer honest. The moment a reviewer can also edit, it
starts approving its own edits.

### Insight 4 — "Refuse and escalate" is a feature judges can see
The most persuasive thirty seconds of any demo is the agent stopping. Ours stops for three
different reasons — missing source, rule violation, and awaiting approval — and each stop is
recorded. Designing for the stop, not just the output, is what makes the thing trustworthy.

### Insight 5 — Disclosing the failure made the story stronger
We were tempted to ship only the clean re-review. Including the rejection, the diagnosis and the
fix is what turns "an agent that writes lesson plans" into "an agent with a working quality
process". The handbook explicitly rewards this; more importantly, it is true.

---

## 3. What we would tell the next team

1. **Write the rulebook before the prompt.** If you cannot state the rules in sentences a teacher
   would sign, you do not have a product — you have a demo.
2. **Make the reviewer cite.** A verdict without a quoted line is unfalsifiable.
3. **Cap the loop.** Pick a number, write it into the contract, escalate when you hit it.
4. **Test your own output adversarially, early.** Our rejection arrived on day 3 and cost a day.
   The same rejection on submission day would have cost the submission.
5. **Keep the rejected version.** It is the most credible artefact you own.

---

## 4. Tooling notes

| Need | What we used | Note |
|------|--------------|------|
| Agent contracts | WorkBuddy skills (`SKILL.md` + `assets/`) | Versionable, diffable, no framework |
| Knowledge layer | Markdown files with tag discipline | Grep-able; a human can audit it |
| Interactive artefact | Single-file HTML quiz | No build step, opens offline |
| Documentation | Markdown → this bundle | Everything text, everything reviewable |
| Verification | `grep` for stale strings, file-count reconciliation | Cheap, caught real errors |
