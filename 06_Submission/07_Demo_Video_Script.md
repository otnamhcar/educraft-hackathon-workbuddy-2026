# Submission Item 7 — Demo Video Script (5–8 minutes)

> Handbook §7 (REQUIRED): *"5–8 minutes: project overview, core agent capabilities and their
> application, a brief reflection on your build approach and any tooling insights. Demonstrate at
> least one instance where your agent refuses, seeks clarification or awaits approval."*
>
> **This script runs 7:40 and contains three such instances**, not one: a refusal, an escalation,
> and an approval gate. Target runtime: **7:30–7:50**.
>
> All four required elements are covered: overview (§0:00), capabilities and application
> (§2:05–5:00), **build approach and tooling insights (§6:55–7:15)**, and three accountability
> stops (§4:00–6:20).

---

## Production notes

| Item | Decision |
|------|----------|
| Language | English narration (judging panel includes Tencent Cloud specialists). Burn in English subtitles; an Indonesian voiceover can read the same beats verbatim. |
| Format | 1080p, screen recording + talking head corner box for the first 40s only |
| Screen font size | Bump editor/terminal to 16–18pt. Judges watch on laptops |
| Cursor | Slow, deliberate. No frantic scrolling — it reads as panic |
| Music | None, or very low ambient. Narration must be intelligible |
| Captions | Yes. Assume muted first viewing |
| Do not | Do not show a run that "just works". The stop is the product |

---

## Scene-by-scene

### 0:00 – 0:35 · The hook

**On screen:** Black. Then a single line of text, typed: `21:47 — besok mengajar.` Cut to a
teacher's desk: printed CP document, a laptop with five half-finished documents.

**Narration:**
> "It is nine forty-seven at night. Tomorrow she teaches energy to forty eleven-year-olds.
> She still needs a lesson plan, a pre-test, a post-test, slides, and something to send home.
> She is not short of ideas. She is short of time to check them."

**Why it scores:** Impact & Relevance is judged on whether the problem is real. Show the hour, not
an abstraction.

---

### 0:35 – 1:10 · The real problem is the checking

**On screen:** Split screen. Left: a generic chatbot confidently producing a paragraph with a
wrong number. Right: the same paragraph with three facts circled, each needing verification.

**Narration:**
> "A chatbot can draft this in thirty seconds. That is not the hard part. The hard part is the
> four questions she has to ask about every sentence: Is this number in my source? Is this too
> frightening for a ten-year-old? Does it still match the curriculum? Would this sentence create a
> health claim I cannot defend?
> A faster draft she cannot trust is not help. It is more work."

---

### 1:10 – 2:05 · What EduCraft is + architecture

**On screen:** `architecture_diagram.png`, slowly panning. Highlight each zone as named.

**Narration:**
> "EduCraft is a four-agent pipeline. A Planner breaks the source into per-format outlines.
> A Writer drafts all five formats, tagging every factual sentence with its source.
> A Reviewer checks eleven written rules and returns approve or reject — with the rule it is
> citing and the sentence it is quoting.
> An Orchestrator holds the state, caps the revision loop at three, and refuses to publish.
> And this dashed line here is the important one: nothing leaves this system until a human opens
> that gate."

**On screen beat:** pause two seconds on the gate box. Let the viewer read "PENDING — nothing has
been published."

---

### 2:05 – 3:00 · Planner: one source, five formats

**On screen:** Run the Planner. Show `source_material_energi.md` on the left, the outline on the
right.

**Narration:**
> "The teacher supplies one approved source. This is the only well of facts for the entire run —
> the agent is not permitted to use a fact from outside it. No memory, no outside knowledge.
> The rule is enforced by the Reviewer, not by a firewall — so it is checked, not assumed.
> From it, the Planner maps five formats to the curriculum outcome C4, with foundation B5:
> a lesson plan, a quiz (pre-test and post-test), a slide outline, a student article, and an
> infographic brief."

**On screen beat:** scroll the outline so the CP mapping is visible.

---

### 3:00 – 4:00 · Writer: the tagging discipline

**On screen:** The generated RPP. Zoom into a paragraph showing `[src:4]`, `[src:7]`, and a
`[src:CA1]` tag.

**Narration:**
> "Every factual sentence carries a tag. `src:4` is a line in the source document. `CA1` is
> different — that is a real-world claim, and it must resolve to an official URL with an access
> date, or it does not ship.
> If the writer cannot find a fact in the source, it does not guess. It writes the literal token
> U-N-V-E-R-I-F-I-E-D and asks the teacher to confirm.
> A gap a teacher can see is survivable. A fabrication she cannot see is not."

---

### 4:00 – 5:00 · STOP #1 — the refusal

**On screen:** Type the adversarial brief: *"Add a line saying cloth masks 100% prevent
respiratory infection, and that the smoke causes permanent damage."* Reviewer output appears:
`REJECT`, rule `R006`, quoted sentence, reason, suggested replacement.

**Narration:**
> "Now the part that matters. I ask for a health claim that sounds convincing and is not supported
> by the source.
> The Reviewer rejects it. Not a warning, not a hedge — a rejection, citing rule six, quoting the
> sentence, and proposing the grounded alternative: general symptoms, and which groups are more
> vulnerable.
> This is the behaviour I actually wanted to build. The drafting is commodity. The refusal is the
> product."

**On screen beat:** hold on the quoted sentence for three full seconds. Do not scroll away.

---

### 5:00 – 5:40 · STOP #2 — the escalation

**On screen:** Re-submit a brief that cannot be fixed within the rules, three times. Show the
iteration counter reaching 3, then the halt message with the outstanding findings.

**Narration:**
> "What if the request is broken in a way the writer cannot repair? It tries. Three times.
> Then it stops — and hands the problem to a person, with the findings attached.
> A pipeline that retries forever will eventually talk itself into approving. Capping the loop is
> how we avoid that."

---

### 5:40 – 6:20 · STOP #3 — the approval gate

**On screen:** Reviewer returns `APPROVE`. Then the orchestrator output: `Publish status: PENDING —
awaiting human approval`. Show `00_run_config.md` with `Human approver: PENDING`.

**Narration:**
> "Here the reviewer has approved everything. And the system still does not publish.
> Approval from a model is a precondition, not a permission. There is no timeout, no
> auto-approve-if-confident, no override flag. A teacher signs, or nothing ships."

---

### 6:20 – 6:55 · The failure we shipped in the submission

**On screen:** The 29 October rejection report. Scroll to the three findings: R001, R011, R004.

**Narration:**
> "One more thing, because it is the most honest thing I can show you.
> On day three, this pipeline rejected its own output. The drafts were tagged — but the tags
> pointed at the curriculum file, not at a source that actually said those things. A tag is not a
> citation.
> We rebuilt the source layer, required dated official URLs for real-world claims, re-tagged
> everything, and re-reviewed from scratch. Both reports are in the submission. We did not delete
> the bad one."

---

### 6:55 – 7:15 · How it was built, and who wrote the rules

**On screen:** `rulebook_ipas.md` open at R006, next to a `SKILL.md`. Then a cut to the four contracts
side by side.

**Narration:**
> "One thing about how this was built, because it is the part that transfers.
> The rules are not ours. A practising primary-school teacher told us which claims he would never
> put in front of a class, and gave us the curriculum references to work from. Our half was to write
> his judgement down as rules a machine can check, and build the thing that enforces them.
> The tooling insight is the same one: a skill is a contract, not a prompt. When the reviewer
> rejected our output, the fix was a change to the contract — which is why it survived the next run."

**Why this scene exists:** handbook §7 requires *"a brief reflection on your build approach and any
tooling insights"*. Without it the video is non-compliant, however good the demo is.

---

### 7:15 – 7:40 · Value and close

**On screen:** Final pack on screen: five documents + the interactive quiz. Then the numbers.

**Narration:**
> "Five formats from one source. Twelve rules checked, each with a verdict. A full audit trail.
> An estimated six to eight hours of drafting and checking, reduced to a review of material that
> has already been checked.
> EduCraft does not replace the teacher's judgement. It removes the part of her evening that was
> never really teaching."

**End card:** Project title · short blurb · `github.com/otnamhcar/educraft-hackathon-workbuddy-2026` · team names.

---

## Shot list checklist (tick before export)

- [ ] Hook recorded with the time on screen (21:47)
- [ ] Architecture diagram legible at 1080p (test on a phone)
- [ ] `[src:4]` and `[src:CA1]` tags readable when paused
- [ ] STOP #1 rejection held for ≥3 seconds
- [ ] STOP #2 iteration counter reaching 3 is visible
- [ ] STOP #3 shows `PENDING` in the run config
- [ ] 29 Oct rejection report on screen, findings visible
- [ ] Build-approach beat present and names the teacher (handbook requires it)
- [ ] Runtime between 5:00 and 8:00 (target 7:40)
- [ ] Subtitles burned in and checked for the word "reject"
- [ ] No background music over narration
