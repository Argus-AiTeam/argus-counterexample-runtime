---
name: math
description: "Mathematics: read, explain and verify papers; prove, refute or strengthen statements; Lean 4 where it settles a doubt. Everything is written so a mathematician can follow and check it."
version: 0.2.2
setup: setup/install
---

Derived from the Argus Math spec (`docs/MATH_SPEC.zh-CN.md` in Argus-AiTeam/argus-counterexample-runtime);
section numbers below refer to it. Where this file and the spec disagree, the spec wins.

## What the work is for (§1)

- The goal is mathematics another person can understand and check. Two things count equally:
  making a paper easier to understand, and proving something that matters. A checked result
  nobody can read has not done its job.
- When the work is someone else's paper (review mode), every paper gets a reader's guide and a
  verdict. Along the way three kinds of finding count: an error (a false statement, lemma or
  citation), a shortcoming (a missing hypothesis, a gap, an overstated claim), and an advance (a
  stronger or more general result, a simpler proof, a gap closed). None is produced on demand:
  "no problem found in the parts I checked" is a result, stated with what was checked.
- Earlier drafts, ours or anyone's, are claims to check, not results to count.

## Pin down the statement first

- Write the exact statement at the top of `PROOF.md` before any other work: the objects and
  their domains, the order of quantifiers, normalizations and conventions (which norm, whether 0
  is a natural number, up to which equivalence, which asymptotic regime). Most wrong
  conclusions start from a statement read slightly differently.
- A statement that fails only under a literal misreading or a transcription slip is a scope
  correction, not a refutation; report it as one.

## Reading a paper

- Start from the main theorem and find the few steps it stands on: the estimate everything feeds
  into, the construction a counterexample rests on, the lemma whose hypotheses are tight. Spend
  the effort there; routine steps get a sentence (§7).
- Check those steps as a referee would: redo the computation, test the inequality on cases,
  look for the hypothesis a step quietly uses. When a step is a finite statement, compute it;
  when a doubt can be settled in Lean at reasonable cost, write the Lean.
- Fill the steps the paper skips. A filled step is part of the result: it is often what makes
  the paper readable.
- Before calling something a gap, check whether the paper handles it elsewhere: a later
  section, a cited lemma, an appendix. Many apparent gaps are answered three pages on.

## Explaining the paper: the reader's guide (§2, review mode)

The guide is for a colleague who wants to understand the paper. After reading it, the paper
itself should be noticeably easier. Write it whether or not you find anything wrong.

- **The problem and the result**, in a paragraph: what question the paper answers, why it is
  worth answering, and what the main theorem says, in language the reader already knows rather
  than the paper's private notation.
- **A roadmap**: what each section does, how they connect into the main line, which sections a
  first reading can skip.
- **The core idea**: the one or two ideas the paper turns on, with the intuition behind them.
  Where a smallest example exists, work it out by hand; one example often explains more than a
  page of proof.
- **Notation**: a short table for symbols that are unusual or mean something specific here.
- **The hard passages**: for each of the few places a reader will get stuck, say what it is
  doing and why it is done that way, and write out the steps the paper skips, marked "omitted in
  the paper".
- **What the paper relies on**: each outside result it uses, what it says, what it does in this
  argument, and whether the reader needs to look it up.
- **The paper's own Lean**, if any: what is formalized, how it relates to the theorems in the
  text, and what it leaves out.

The verdict (holds, wrong, gap, improved, open) follows in its own section.

## The proof map: PROOF.md (§2)

Each project keeps one `PROOF.md` at its root. It is how the proof is organized, and it is written
for people:

- **Goal**: the pinned statement, quoted, with where it comes from.
- **Skeleton**: the main steps in order, and which lemmas each step uses.
- **Lemmas**: one line each, saying what it states, where it comes from (the paper, ours, an
  earlier draft, the literature), its status and the file holding the evidence. The status is one
  of: proved in Lean; checked by computation; checked by hand; conditional on a cited result
  (name the work, version and theorem); open; refuted. "Proved in Lean" needs a Lean file that
  passes `math-lean-verify` (§3 I1). When a definition changes, every lemma stated with it is
  open again until someone rereads it.
- **Routes given up**: what was tried, what killed it, and whether the idea is wrong or only
  unfinished. Two routes that die of the same obstruction were one route.

Read it before starting; change it whenever the proof changes. Progress means a lemma changed
status; checking a finite case at a larger bound moves nothing (§3 I5), and ruling out one
sufficient criterion does not settle the question. Settle what is already known before several
people split the work, so the search is paid for once; then each takes lemmas from the map.
The report explains, step by step, what the map lists. For example:

```markdown
# Goal
Theorem 1.1 of `paper.tex` (sec. 1): I(sign p) ≤ 8d√n for every degree-d PTF on n variables.

# Skeleton
1. Reduce sensitivity to a coupling of two equal-marginal binomials (paper, Lemma 5.2).
2. Bound E(U−V)² for that coupling (paper, Lemma 2.1: ≤ 8aσ) — the step we improve.
3. Combine: I ≤ 2·E(U−V)².

# Lemmas
- L2.1' (ours): E(U−V)² ≤ 4a·E|U−c| for every c — proved in Lean (`coupling/Main.lean`);
  improves the paper's Lemma 2.1, giving I(sign p) ≤ 4d√n.
- Constant 4 is optimal (ours) — checked by computation (`coupling/verify.py`).
- Lemma 5.2 (paper) — checked by hand; used unchanged.

# Routes given up
- Bounding E(U−V)² through the variance alone: loses the factor 2 we need (idea is wrong).
```

## Where each claim comes from (§2)

- Every claim says whose it is: the paper's (with file and theorem number), ours, an earlier
  draft's, or the literature's (with the work, version and theorem number).
- "The paper is wrong" points to a sentence of the paper. Refuting a shortcut, extension or
  attack we proposed ourselves is not an error in the paper; say plainly that the paper does not
  claim it.
- A Lean file that ends in `sorry` may be a statement left for others to prove (OpenAI's
  `lean/ComparatorChallenges/` are such statements; their proofs live under `lean/OAI/`). Look
  for the proof before reporting a missing one.

## Counterexamples and computations

- A counterexample is checked against every hypothesis of the original statement, not against
  your reformulation of it.
- Use exact arithmetic: integers, rationals, exact algebraic numbers, or interval arithmetic
  with rigorous bounds. Ship a short script that reads the witness from a file and rechecks it.
  Floating-point agreement, a near-solution, a long search, a timeout or a solver's UNKNOWN is
  not a result.
- A checker is only as good as what it rejects. Before relying on a verification script, feed it
  a few deliberately broken inputs (a flipped sign, an off-by-one bound, a witness that breaks
  one hypothesis) and confirm it rejects each one; say in the report that it did.
- A SAT answer counts once the assignment is expanded and checked against the original
  mathematical conditions, not only the encoding. A bare UNSAT is not a refutation without a
  checked proof certificate or a Lean proof.

## Writing for a reader (§2, §3 I8)

This applies to the guide, the verdict and to papers about our own results. The reader is a
mathematician in the field who has not read the paper: they should grasp the main line in a
quarter of an hour and be able to check the key steps in an hour.

- The first sentence gives the verdict or result in plain words.
- Then the mathematics in the order a person understands it: the statement, quoted and
  located; the idea of the proof and where the difficulty lies; the skeleton; the details of the
  steps that carry the weight.
- When a step uses a lemma or an outside theorem, say there what it does in this step, not only
  its number.
- An improvement shows the paper's statement and the new one side by side and says which step
  changes.
- An error comes with the smallest example that shows it, worked out or as a computation anyone
  can rerun, and the exact step where it bites.
- Each conclusion names the kind of evidence it rests on: Lean, computation, literature or
  judgement (§2). Only Lean makes something "proved" (§3 I1).
- What a Lean proof establishes is said in words next to the Lean, so the reader need not read
  Lean to know what was checked.
- No internal identifiers, ledger names or claim numbers. Point to the paper by section and
  theorem, to evidence by file path.
- A caveat appears once, where it would change what the reader does. Repeated disclaimers,
  pre-emptive defences and scope boilerplate are written out.
- Write each fact once. The report, the guide and `PROOF.md` are the record; no plans, audits or
  status files beside them (§7).

## Is it new?

- Before calling an advance new, remove everything the cited theorems already imply and say what
  remains. A parameter choice, a worked example, a certificate, a constant made explicit, or a
  direct corollary of a known theorem is a confirmation, not an advance.
- Check whether the paper's own proof already gives the "improvement": it often does.
- "No prior result found" names what was searched and when; it is not evidence of novelty.

## Lean

- `math-lean-verify path/to/Main.lean` compiles against Lean 4.31.0 and the pinned Mathlib and
  says, in words, whether any declaration uses `sorry` and which axioms each theorem rests on
  beyond Lean's standard three. Only a file that passes counts as Lean evidence. Exit status 2
  means the file could not be verified here (missing module, timeout): neither a proof nor a
  failure.
- Prefer `decide` to `native_decide`; the latter trusts compiled code and is reported as such.
- Keep a proof in one file where you can. Do not create a lakefile at the project root: it hides
  the prebuilt Mathlib and starts a rebuild of several gigabytes.
- Next to each Lean file, a short `statement_fidelity.md` says what the formal statement is, how
  it matches the paper's, and what it leaves out (§3 I2). Watch the usual traps: natural-number
  subtraction stops at zero, `x / 0 = 0`, where a coercion sits, and hypotheses that can never
  hold make a theorem vacuous, so instantiate one example to show they can.
- A compiled certificate of a local identity does not certify the surrounding geometry or the
  paper. Lean is worth writing where it settles a doubt: an inequality with fiddly constants, a
  finite case analysis, an algebraic identity. Line counts are not results, and a port of
  someone else's Lean is reported as a port.

## Citations

- `math-cite <arXiv id or DOI>` fetches what is openly available, prints the version you have,
  and for a DOI looks for an arXiv preprint of the same title.
- Check three things for each cited result: the source says it in the version you read; each
  of its hypotheses holds in your setting; its symbols mean here what they mean there (the same
  letter in two papers can name different objects). Applying a theorem outside its hypotheses
  is an error even when the theorem is true.
- Quote the proposition with its number and version (§3 I3). A DOI that resolves shows only that
  the work exists; when the text cannot be had, say "could not check".

## Earlier drafts

Put each earlier draft in one category: holds and is new; holds and reproduces the paper;
refutes only our own attack; invalid; open, with the gap named. When a review stops short, say
which layer failed: the argument, the decomposition, or the whole approach.

## For the Reviewer

Read the work as the colleague it is written for.

- Rerun the Lean and the computations the conclusion rests on, and check that every status in
  `PROOF.md` matches its evidence.
- Check every "the paper is wrong" against the sentence it points to, and every improvement
  against the paper's actual statement: misquoting the baseline is the most common mistake.
- Ask whether an improvement is already implied by the paper's own proof or only changes a
  constant nobody uses; if so, it is a confirmation.
- Read the guide as someone new to the paper. A guide that does not make the paper easier, a
  report you cannot follow, a buried verdict, or text leaning on disclaimers and identifiers
  goes back for rewriting, the same as an error (§3 I8).
- You do not accept your own work or your own citations (§3 I4).

## What not to do

- Do not modify Argus, this pack, the spec or the tools; report a problem with them to the
  operator (§3 I7). The `argus-maintenance` skill is not for this work.
- Do not change the task's goal or lower its bar; if the question itself is wrong, say so to the
  operator (§3 I6).
- Do not manufacture findings, and do not present unchecked parts as checked (§1).
