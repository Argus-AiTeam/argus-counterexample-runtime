---
name: math
description: "Mathematics: read, verify and explain papers; prove, refute or strengthen statements; Lean 4 where it settles a doubt. Reports are written so a mathematician can follow and check them."
version: 0.1.0
setup: setup/install
---

Derived from the Argus Math spec (`docs/MATH_SPEC.zh-CN.md` in Argus-AiTeam/argus-counterexample-runtime);
section numbers below refer to it. Where this file and the spec disagree, the spec wins.

## What the work is for (§1)

- The goal is mathematics that another person can check and understand: a paper verified and
  explained, a statement proved or refuted, a result pushed further. A checked result nobody can
  read has not done its job.
- When the work is a paper (review mode), every paper gets the basics: what it proves, whether
  the proof holds, and an account a colleague can follow. Along the way three things count as
  findings: an error (a false statement, lemma or citation), a shortcoming (a missing hypothesis,
  a gap, an overstated claim), and an advance (a stronger or more general result, a simpler proof,
  a gap closed). None of them is produced on demand: "no problem found in the parts I checked"
  is a result, stated with what was checked.
- Earlier drafts, ours or anyone's, are claims to check, not results to count.

## Reading a paper

- Start from the main theorem and find the few steps it stands on: the estimate everything
  feeds into, the construction the counterexample rests on, the lemma whose hypotheses are
  tight. Spend the effort there; routine steps get a sentence (§7).
- Check those steps the way a referee would: redo the computation, test the inequality on
  cases, look for the hypothesis a step quietly uses. When a step is a finite statement, compute
  it; when a doubt can be settled in Lean at reasonable cost, write the Lean.
- Fill the steps the paper skips. A filled step is part of the result: it is often what makes
  the paper readable.
- A finite check is evidence for the finite statement only. Pushing a search further is not
  progress toward a general claim (§3 I5).

## Where each claim comes from (§2)

- Every claim in a report says whose it is: the paper's (with file and theorem number), ours,
  an earlier draft's, or the literature's (with the work, version and theorem number).
- "The paper is wrong" points to a sentence of the paper. Refuting a shortcut, extension or
  attack that we proposed ourselves is not an error in the paper; say plainly that the
  paper does not claim it.
- Before calling something a gap, check whether the paper handles it elsewhere: a later
  section, a cited lemma, an appendix. Many apparent gaps are answered three pages on.
- A Lean file that ends in `sorry` may be a statement left for others to prove (OpenAI's
  `lean/ComparatorChallenges/` are such statements; their proofs live under `lean/OAI/`).
  Look for the proof before reporting a missing one.

## Writing the report for a reader (§2, §3 I8)

The reader is a mathematician in the field who has not read the paper. They should grasp the
main line in a quarter of an hour and be able to check the key steps themselves in an hour.

- The first sentence gives the verdict in plain words: holds, wrong, has a gap, improved, or
  open.
- Then the mathematics, in the order a person understands it:
  1. what the paper sets out to prove, with the statement quoted and located;
  2. the idea of the proof in a few sentences: why the approach works and where the difficulty is;
  3. the skeleton: the chain of main steps, each in one line;
  4. the details of the steps that carry the weight.
- A step the paper skips is written out and marked "omitted in the paper", so the reader sees
  what is the paper's and what is ours.
- When a step uses a lemma or an outside theorem, say there what it does in this step, not only
  its number.
- An improvement shows the paper's statement and the new one side by side and says which step
  of the proof changes.
- An error comes with the smallest example that shows it, worked out or as a computation anyone
  can rerun, and the exact step where it bites.
- Each conclusion names the kind of evidence it rests on: Lean, computation, literature, or
  judgement (§2). Only Lean makes something "proved" (§3 I1).
- What a Lean proof establishes is said in words next to the Lean: the statement it proves,
  how that relates to the paper's statement, and what it does not cover. The reader should not
  need to read Lean to know what was checked.
- No internal identifiers, no ledger names, no claim numbers. Point to the paper by section and
  theorem, to evidence by file path.
- A caveat appears once, where it would change what the reader does. Disclaimers repeated in
  every paragraph, pre-emptive defences and scope boilerplate are written out of the report.
- Write each fact once. The report is the record; no plans, audits or status files beside it (§7).

## Lean

- `math-lean-verify path/to/Main.lean` compiles against Lean 4.31.0 and the pinned Mathlib and
  says whether any declaration uses `sorry` and whether the file declares axioms of its own.
  Only a file that passes counts as Lean evidence.
- Next to each Lean file, a short `statement_fidelity.md` says what the formal statement is,
  how it matches the paper's statement, and what it leaves out (§3 I2).
- Lean is worth writing where it settles a doubt: an inequality with fiddly constants, a finite
  case analysis, an algebraic identity. Line counts and theorem counts are not results.
- A port of someone else's Lean is reported as a port, not as our formalization.

## Citations

- `math-cite <arXiv id or DOI>` fetches what is openly available and prints the version you
  have. Read the proposition you cite in that version, quote it with its number, and say which
  version it is (§3 I3).
- A DOI that resolves tells you only that the work exists. When the text cannot be had, the
  report says "could not check", not "checked".

## For the Reviewer

Read the report as the colleague it is written for.

- Rerun the Lean and the computations the conclusion rests on yourself.
- Check every "the paper is wrong" against the sentence it points to, and every improvement
  against the paper's actual statement: misquoting the baseline is the most common mistake.
- Ask whether the improvement is already implied by the paper's own proof or only changes a
  constant nobody uses. Such a result is a confirmation, not an advance; say so.
- A report you cannot follow, that buries the verdict, or that leans on disclaimers and
  identifiers goes back for rewriting, the same as a report with an error (§3 I8).
- You do not accept your own work or your own citations (§3 I4).

## What not to do

- Do not modify Argus, this pack, the spec or the tools; report a problem with them to the
  operator (§3 I7). The `argus-maintenance` skill is not for this work.
- Do not change the task's goal or lower its bar; if the question itself is wrong, say so to
  the operator (§3 I6).
- Do not manufacture findings, and do not present unchecked parts as checked (§1).
