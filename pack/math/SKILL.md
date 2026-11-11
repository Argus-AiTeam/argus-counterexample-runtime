---
name: math
description: "Mathematics: read, explain and verify papers; prove, refute or strengthen statements; Lean 4 where it settles a doubt. Everything is written so a mathematician can follow and check it."
version: 0.8.2
setup: setup/install
---

Derived from the Argus Math spec (`docs/MATH_SPEC.zh-CN.md` in Argus-AiTeam/argus-counterexample-runtime);
section numbers below refer to it. Where this file and the spec disagree, the spec wins.

## What the work is for (§1)

- The goal is mathematics another person can understand and check. Two things count equally:
  making a paper easier to understand, and proving something that matters. A checked result
  nobody can read has not done its job.
- When the work is someone else's paper (review mode), every paper gets a reader's guide and a
  verdict in three parts: improvements, errors and shortcomings, and what was verified (below).
- Checking is not the end. Going past the paper is planned work with a task of its own (see
  "For the Planner"), and everyone checking a step also asks whether it could be sharper.
  Nothing is produced on demand: when the push gets nowhere, say what was tried.
- Earlier drafts, ours or anyone's, are claims to check, not results to count.

## Going past the paper (§2)

- **Where to look**: a constant the paper leaves unnamed or never optimizes, a hypothesis the
  proof does not use in full, a step whose loss looks wasteful, a special case that generalizes,
  an argument that could be shorter.
- **Compute first, then prove.** Search numerically for the best constant, enumerate small
  cases, look for the extremal or the breaking example, and let what you see suggest the stronger
  statement. Then prove it, or report it as a conjecture with the data. Python first; C++ or
  PARI/GP (`gp`) when Python is too slow, and the machine has many cores, so a search can run in
  parallel; `math-ops` for exact finite operations. An experiment is not a result.
- **A complete small result beats a conditional large one.** A sharp constant with the example
  that attains it, or a lemma with a counterexample at its boundary, is an improvement in full.
  A larger extension that leans on other steps of the paper is still worth reporting, marked
  conditional, naming exactly what it rests on.
- **Along the way**: whoever checks a step and sees it can be tightened computes it there and
  then and hands it to the report's "Improvements".

## Pin down the statement first (§2)

- Write the exact statement at the top of the report before any other work: the objects and
  their domains, the order of quantifiers, normalizations and conventions (which norm, whether 0
  is a natural number, up to which equivalence, which asymptotic regime). Most wrong
  conclusions start from a statement read slightly differently.
- A statement that fails only under a literal misreading or a transcription slip is a scope
  correction, not a refutation; report it as one.

## Reading a paper (§2, I3)

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

The verdict follows in its own section, in three parts, always in this order:

1. **Improvements**: each beside the paper's statement, saying which step changes, and whether
   its key step was checked independently (Lean, computation, or a second person by hand) or is
   only plausible on reading.
2. **Errors and shortcomings**: false statements, lemmas or citations; missing hypotheses, gaps,
   overstated claims. Each points to the sentence of the paper and comes with the smallest
   example.
3. **Verified**: what holds, which parts were checked and how.

A part with nothing in it says "none" and what was looked at. The claims table closes the verdict.

## The report is the record (§2)

The report is the one place where the proof stands: its structure, and what each step rests on.
Nothing else keeps a second copy, so nothing can disagree with it. While the work goes on, the
report is the draft being written; read it before you start, and change it when the proof
changes. In review mode the report is the reader's guide followed by the verdict.

- **The statement** at the top, pinned down as above, quoted, with where it comes from.
- **The skeleton**: the main steps in order, and which lemmas each uses.
- **The claims table** closes the verdict: one row per claim, with four columns, Claim | Source
  | Basis | Evidence. Source is the paper (with its location), ours, an earlier draft, or the
  literature. Basis is one of: proved in Lean; checked by computation; checked by hand;
  conditional on a cited result (name it); open; refuted. Evidence is a file path. "Proved in
  Lean" needs a file that passes `math-lean-verify` (§3 I1). `math-claims` reads these tables
  back. When a definition changes, the claims stated with it are checked again.
- Progress means a step's basis got stronger. Checking a finite case at a larger bound moves
  nothing (§3 I5), and ruling out one sufficient criterion does not settle the question.
- **Routes given up** go in the team wiki, not the report: what was tried, what killed it, and
  whether the idea is wrong or only unfinished. Two routes that die of the same obstruction were
  one route. Look there before trying a route.
- Settle what is already known before several people split the work, so the search is paid for
  once; the Planner splits the work into tasks and the letters carry it.

For example, the verdict section of a guide might read:

```markdown
## Verdict
The paper's bound holds, and its constant can be halved: I(sign p) ≤ 4d√n (paper: 8d√n).

**Improvements.** I(sign p) ≤ 4d√n against the paper's 8d√n. The reduction is the paper's; the
new step is a sharper coupling bound (proved in Lean), and the rest follows as in Section 5.

**Errors and shortcomings.** None found. Looked at: every step of Sections 2–5, the constants
in Section 6, the cited results the corollaries use.

**Verified.** Theorem 1 and both corollaries, by hand, step by step.

| Claim | Source | Basis | Evidence |
|---|---|---|---|
| Lemma 5.2: sensitivity reduces to an equal-marginal coupling | paper, §5 | checked by hand | — |
| E(U−V)² ≤ 4a·E\|U−c\| for every c (paper's Lemma 2.1 has 8aσ) | ours | proved in Lean | `coupling/Main.lean` |
| The constant 4 cannot be lowered | ours | checked by computation | `coupling/verify.py` |
| I(sign p) ≤ 4d√n | ours | checked by hand | — |
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

## Counterexamples and computations (§2, I5)

Computation is an ordinary move, in checking as in going further: compute examples, try the
cheap falsification before the long proof, and when a finite exact subproblem appears, look in
`math-ops find` before writing your own code. The Planner splits work this way too.

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

## Exact operations: Jacobian (§4)

`math-ops` gives the Jacobian library: about six hundred typed, bounded operations (exact
linear algebra over Z and Q, Smith and Hermite forms, lattices and abelian groups, polynomial
and number-theoretic computations, LP and SAT/SMT checks with certificates, graph invariants,
simplicial homology, and more).

- `math-ops find smith normal form` lists the operations that match; `math-ops show <id>` gives
  the exact input it takes and what it guarantees; `math-ops run <id> payload.json` runs it.
- Reach for it when a step reduces to a finite, well-typed computation that a hand calculation
  would make error-prone: a determinant over Z, an invariant factor, a feasibility certificate.
  It does not decide what the step means; you still say why this computation settles it.
- Keep the payload file next to the report and cite the command: anyone can rerun it, and it
  counts as computational evidence. Prefer an operation whose result carries a certificate
  ("certified" in its id) when the conclusion rests on it.
- A result marked approximate, incomplete, unknown or timed out settles nothing.

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
- Write each fact once. The report is the record; no plans, audits or status files beside it (§7).

## Reading costs more than writing (§7)

Most of what a project spends is what gets read into the conversation, turn after turn; what you
write costs far less. So read as a mathematician does, with a finger on the line you need:

- Find the place first (`rg` for the label, the lemma name, the symbol), then read that stretch
  of the file with a line range. Read a whole `.tex` file only when you mean to read all of it.
- When you change the report, read the section you are changing, not the whole report again.
- For a cited work, get the text first (`math-cite`, or `pdftotext` on the PDF) and search it;
  look at a page image only when the formula itself does not come through.
- What you learned once and will need again (where the key estimate sits, what a cited lemma
  says) goes in a line of the report or the wiki, so nobody pays to find it twice.

## Is it new? (§5)

- Before calling an advance new, remove everything the cited theorems already imply and say what
  remains. A parameter choice, a worked example, a certificate, a constant made explicit, or a
  direct corollary of a known theorem is a confirmation, not an advance.
- Check whether the paper's own proof already gives the "improvement": it often does.
- "No prior result found" names what was searched and when; it is not evidence of novelty.

## Lean (I1, I2)

- `math-lean-verify path/to/Main.lean` compiles against Lean 4.31.0 and the pinned Mathlib and
  says, in words, whether any declaration uses `sorry` and which axioms each theorem rests on
  beyond Lean's standard three. Only a file that passes counts as Lean evidence. Exit status 2
  means the file could not be verified here (missing module, timeout): neither a proof nor a
  failure.
- **The authors' own Lean** (OpenAI's, at the pinned commit) uses Lean 4.34.1 and another Mathlib,
  so `math-lean-verify` cannot compile it. `math-oai-verify <module> <theorem>…` builds that module
  in the OpenAI workspace exactly as written and prints the axioms of each theorem: this is the
  check that the paper's Lean proves what its scope note says. Take the module and theorem names from
  the comparator's JSON (`solution_module`). The first build of a closure takes minutes.
  `math-lean-source-closure` lists a module's import closure with pinned sources, without building.
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

## Citations (I3)

- `math-cite <arXiv id or DOI>` fetches what is openly available, prints the version you have,
  and for a DOI looks for an arXiv preprint of the same title.
- Check three things for each cited result: the source says it in the version you read; each
  of its hypotheses holds in your setting; its symbols mean here what they mean there (the same
  letter in two papers can name different objects). Applying a theorem outside its hypotheses
  is an error even when the theorem is true.
- Quote the proposition with its number and version (§3 I3). A DOI that resolves shows only that
  the work exists; when the text cannot be had, say "could not check".

## For the Planner (§2, §4, §7)

In review mode a split that has worked: one task per paper to read it and write its guide; one
for the hardest or shared module; **one to go past the paper**, whose brief names its targets
(which constant, which hypothesis, which step) and says to compute first; one to rerun the Lean
and computations by someone who did not write them; and a final independent review. When a verdict rests on a source nobody could read, try an open
substitute or a direct proof before leaving it as a condition.

When work comes back from the Reviewer, the letter that sends it back says which passages to
change and what is wrong with each, so the one fixing it reads those and not the whole report.
If the same task comes back a second time, look at the split or the route before sending it
round again: two rejections usually mean the task asks for more than one result, or the route is
wrong.

## For the Reviewer (§4, §7, I2, I4, I8)

Read the work as the colleague it is written for.

- The Lean and the computations the conclusion rests on are rerun by someone who did not write
  them. The Reviewer cannot run commands: the Planner opens that rerun as a task of its own, and
  the Reviewer checks its output and that what the report says each step rests on matches it.
- Check every "the paper is wrong" against the sentence it points to, and every improvement
  against the paper's actual statement: misquoting the baseline is the most common mistake.
- Ask whether an improvement is already implied by the paper's own proof or only changes a
  constant nobody uses; if so, it is a confirmation.
- Read the guide as someone new to the paper. A guide that does not make the paper easier, a
  report you cannot follow, a buried verdict, or text leaning on disclaimers and identifiers
  goes back for rewriting, the same as an error (§3 I8).
- When you send work back, list everything you found in one letter, each with where it is and
  what would fix it; a small fix you can state exactly, state, so the task need not reopen for it.
  On a second look, read what changed since the first and the passages it touches (§7).
- You do not accept your own work or your own citations (§3 I4).

## The tools are the team's (§4)

`math-lean-verify`, `math-cite`, `math-ops`, `math-claims`, `math-oai-verify` and
`math-lean-source-closure` live in the team's tools/ with any others the team writes. When one is wrong or missing something, fix it there, test it on a case
it got wrong, and say in a line at the top what changed; add a tool when a check recurs; remove
one nobody needs. A change to `math-lean-verify` keeps its job: a file passes only if it compiles
without `sorry` and rests on the standard axioms.

## What not to do (I6, I7, §8)

- Do not modify Argus, this pack or the spec; report a problem with them to the operator
  (§3 I7). The `argus-maintenance` skill is not for this work.
- Do not change the task's goal or lower its bar; if the question itself is wrong, say so to the
  operator (§3 I6).
- Do not manufacture findings, and do not present unchecked parts as checked (§1).
