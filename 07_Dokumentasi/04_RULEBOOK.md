# 04 — Rulebook specification (canonical pointer)

> **The rulebook itself lives at** `03_Hasil/referensi/rulebook_ipas.md` (v2.0).
> This file does not repeat the rules — it specifies how the rulebook is governed, how each rule is
> enforced, and what evidence exists for that enforcement. Duplicating the rule text here would
> create a second source of truth, which is the exact failure mode this documentation set exists to
> remove.

---

## 1. Governance

| Property | Rule |
|----------|------|
| Canonical file | `03_Hasil/referensi/rulebook_ipas.md` |
| Copies | `skills_package/edu-orchestrator/assets/`, `skills_package/edu-reviewer/assets/` |
| Copy integrity | Byte-identical; verified by checksum before every submission |
| Change control | Human edit only. An agent may propose a rule, never enact one |
| Versioning | `vMAJOR.MINOR` + changelog table at the top of the file |
| Backward compatibility | A change that loosens a rule requires re-review of every artefact that passed under the old rule |

**Checksum evidence (31 Oct 2026, v2.0):**

```
9fe6336872159a65  03_Hasil/referensi/rulebook_ipas.md
9fe6336872159a65  05_Bukti_Proses/skills_package/edu-orchestrator/assets/rulebook_ipas.md
9fe6336872159a65  05_Bukti_Proses/skills_package/edu-reviewer/assets/rulebook_ipas.md
```

Re-run with:
```bash
sha256sum 03_Hasil/referensi/rulebook_ipas.md \
          05_Bukti_Proses/skills_package/*/assets/rulebook_ipas.md
```

---

## 2. Rule set and enforcement status

| Rule | Guards against | Enforcement | Evidence that it works |
|------|----------------|-------------|------------------------|
| R001 | Unresolvable or misclassified citation | Prompt + **deterministic tool** | `tools/check_grounding.py`; run `-001` 121 tags → PASS; run `-002` 115 tags → PASS after the D1 fix (it was 84 class violations before, which is what found the defect) |
| R002 | Fear-mongering | Prompt only | Reviewer finding F-? — quoted rejection in `05_review.md`; live screenshot **TO RUN** |
| R003 | Age-inappropriate language | Prompt only | Rule present; live capture **TO RUN** |
| R004 | Curriculum drift | Prompt + human sign-off | Run `-002` flagged `PERLU KONFIRMASI GURU`, teacher approved 30 Oct 17:19 |
| R005 | Harm-only content | Prompt only | Run `-001` re-review: R005 PASS with student-action section |
| R006 | Health claims | Prompt only | **TO RUN** (TC-08/09, critical) |
| R007 | Harmful promotion | Prompt only | **TO RUN** (TC-10, critical) |
| R008 | Tone | Prompt only | Infographic render loop rejected 2 iterations on clarity (audit log §3.6) |
| R009 | Language + CTA | Prompt only | CTA present in article/slide/brief; manual check |
| R010 | Stigmatising wording | Prompt only | Rule present; no failing example captured |
| R011 | Unsourced real-world claim | Prompt + URL requirement | The 29 Oct rejection (F-02) — two CA claims had no document |
| R012 | Commercial / halal claim | Prompt only | **NEW in v2.0; never exercised.** Applicability for IPAS material: `N/A` with justification |

**Honest summary:** one rule (R001) has deterministic enforcement. The other eleven are enforced by
prompt and audited by a human reading quoted findings. That is the actual state; do not describe it
as an automated policy engine.

---

## 3. What changed in v2.0 and why

| Change | Reason | Risk if not done |
|--------|--------|------------------|
| R003 keyed to the phase in `00_run_config.md` instead of "kelas 5–6" | The project serves Fase B (III–IV) **and** Fase C (V–VI). A rule that only names grades 5–6 cannot judge a Fase B artefact | A Fase B pack would be judged against the wrong age band |
| R005/R006/R007 lost their hardcoded `[src:6]`/`[src:7]`/`[src:8]` pointers | Those numbers belong to one particular source file. Swap the source and the rules point at the wrong sections — which contradicts the claim that the engine is domain-parameterised | "Swap the source and it works" would be false |
| R004 lost its topic list | Same reason: the rule named one topic's themes | A new topic would technically violate R004 |
| R012 added | Handbook Challenge C names *advertising and halal* as review criteria. Without a rule, the Reviewer has no basis to reject a commercial or halal claim | A judge's test case on a halal claim would pass unchecked — a visible hole |
| §0 tag taxonomy added | The 29 Oct and run `-002` defects both came from a curriculum tag standing in for a fact tag | The rule said "must cite a source" but never defined what counts as one |
| §0b N/A rule added | "Silently skipped" and "assessed as not applicable" look identical in a report | A judge cannot tell whether a rule was applied |

**Backward compatibility:** no rule was loosened. Every verdict issued under v1.1 remains valid
without re-review. R012 is recorded as `N/A` for both existing runs because neither contains a
commercial, efficacy, testimonial or halal claim — verified by search, see
`03_Hasil/audit/addendum_R012_2026-10-31.md`.

---

## 4. How to add a rule (procedure)

1. State the harm the rule prevents, in one sentence.
2. Write the rule as a **testable predicate**: what must be true in the text for it to pass.
3. Add one calibration example that should `REJECT` and one that should `APPROVE`.
4. Bump the version and record it in the changelog.
5. Sync both asset copies; verify checksums.
6. If the rule is stricter than before, re-review every artefact that passed under the old version.
7. Add at least one test case to `05_TEST_PLAN.md` so the rule is demonstrable, not just declared.

A rule that has no test case is a wish. A rule that has no calibration example is ambiguous.

---

## 5. Known limitation

The rulebook is only as good as its author. A missing rule is a missing check, and the Reviewer
cannot reject what the rulebook does not forbid. This is why R012 exists: it was missing, and the
handbook names it explicitly. The same argument applies to whatever is still missing.
