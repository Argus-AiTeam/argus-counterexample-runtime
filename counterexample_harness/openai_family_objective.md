# Verify and explain this family of OpenAI math papers, and account for Argus's earlier work

Governing spec: docs/MATH_SPEC.zh-CN.md in the argus-counterexample-runtime
repository (§1 mission, §2 reports, §3 I1-I8). Where this file and the spec
disagree, the spec wins.

## The task

The subject is the OpenAI manuscripts of this family, listed in the file named by
`manuscript_reference_manifest` in PRIOR_DRAFTS.json (pinned revision, TeX
sources). The work has three parts:

1. **Verify each manuscript.** Establish what it claims, then check the main theorems and the
   steps they rest on. Spend effort where a wrong step would break a main theorem.
   Whole-paper verification is not required; an explicit statement of what was
   checked and what was not is.
2. **Explain each manuscript to a human expert.** Someone in the field should understand the
   result, why it holds, and where its weight lies, without rereading the paper.
3. **Account for Argus's earlier work.** PRIOR_DRAFTS.json lists every
   artifact Argus produced on this family in earlier rounds. Review each of
   them and establish what Argus actually achieved: which results hold, which
   are reproductions of the paper, which are new, and which are wrong. This
   is a deliverable in its own right, not background reading.

Along the way, three kinds of finding matter most: an **error** in the paper
(false statement, broken step, counterexample, wrong citation), a
**deficiency** (missing hypothesis, gap, overstatement, unstated dependency),
and an **advance** (a stronger or more general result, a simpler proof, a
repaired gap). "No issue found in the checked scope" is a valid result when the
scope is stated. There is no quota: never manufacture a finding, and never
report an unchecked part as verified.

Earlier rounds were run refutation-first. Many of their "refutations" refuted
an Argus attack rather than the paper; an error in an Argus attack is not an
error in the paper. Their conclusions are claims to check, not results. Keep
the old workspace read-only; reuse what survives re-checking and cite it.

## What to write

For each manuscript, in `research/papers/<manuscript_id>/`:

- `GUIDE.md`, for a human expert:
  - First sentence: the bottom line in plain words (verified in the checked
    scope / error / gap / unresolved).
  - The main results, quoted, each with its location (file and label).
  - What is new and why it matters.
  - The proof's structure: the load-bearing steps, how they depend on each
    other, the key idea of each, and which parts are standard.
  - External results it relies on (citations checked per spec I3).
  - What was checked and how (Lean, computation, reading), and what was not.
- `verdict.json`: one entry per main theorem and load-bearing lemma with
  `status` (verified, verified_with_repair, gap, error, unresolved,
  not_checked), evidence type (spec §2), location, and a one-line reason.

Each finding in `research/findings/<id>.md`: its kind (error, deficiency,
advance), the exact passage quoted with its location, the smallest
hand-checkable example or a rerunnable computation, whether it affects a main
theorem, and attribution (the results are the paper's authors'). An advance
that is called new needs a literature check first.

For Argus's earlier work: `research/DRAFT_REVIEW_INDEX.json` groups every
listed artifact into mathematical units (and explains duplicates, supporting
files and exclusions); each unit gets `research/draft_reviews/<unit>/report.md`
and `verdict.json` stating the exact claim, its scope, and one classification:
`confirmed_original` (holds and is not in the paper), `confirmed_reproduction`
(holds, restates or re-proves the paper), `refutes_argus_attack` (an Argus
attack shown wrong), `invalid` (the old argument fails), `unresolved` (a
concrete open obligation). `research/OLD_ROUND_REVIEW.md` summarises them.
Work already written in these files under the earlier contract stays valid;
continue it rather than redo it.

`research/FAMILY_REPORT.md`: one page for a human expert — each paper's bottom
line, how the papers depend on each other, the findings ranked by
importance, and what Argus's earlier work actually achieved (by classification
above).

Write for the reader (spec I8): plain words, each point once, the reader's
question answered first.

## Spend tokens on mathematics (spec §7)

Settle what is already known once, at the start, in the ledger, so workers do
not repeat the same search. Reuse checked results and earlier Argus work that
survives re-checking instead of redoing it. Check the steps a main theorem
depends on, not every routine line. Do not enlarge finite checks for their own
sake. Write no process documents; write each point once.

## Finishing

The family's research result uses `novelty_status=not_applicable`; an
advance's novelty is recorded in its finding. Run
`python -m argus_skill.verticals.math.check` before final review and clear
what it lists. The native independent Reviewer accepts the family when every
manuscript has its GUIDE.md and verdict.json, every earlier Argus artifact is
covered by the draft review, every finding carries its evidence, and
FAMILY_REPORT.md is complete. Engineer cannot self-accept.

This campaign does not repair or redeploy Argus. If the framework blocks
completion, stop and report the exact diagnostic and events.jsonl line.
