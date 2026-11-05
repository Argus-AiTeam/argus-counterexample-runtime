---
title: Explicit negative-mutation graph calibration
description: Machine-readable O'Brien mutation circles, exact two-change replays, and bounded linear and extension-field screening.
---

# Explicit negative-mutation graph calibration

## Marked graph source

`research/obrien_negative_mutation_graph_source.json` records two closed
oriented PD graphs, the crossings inside a Conway circle, the four boundary
darts in cyclic order, and the half-turn axis. The verifier derives the
endpoint directions from the graph and reconnects boundary dart \(i\) to
dart \(i+2\). It does not take a target Seifert matrix or expected rank as
input.

For the graph labelled \(13a2720\), the inside crossings are
\(0,\ldots,6\), the cyclic boundary darts are
\[
(0,3),(2,0),(4,1),(6,2),
\]
and their directions are in, in, out, out. The perpendicular half-turn
therefore reverses all four directions and is a negative mutation. The
derived diagram has a link-extending complement isometry to \(13a2727\).
Both graph-derived Alexander presentations have cokernel dimension three
over \(\mathbb F_3\) at \(t=2\).

For the graph labelled \(13n2937\), the inside crossings are
\[
0,1,2,8,9,11,12,
\]
the boundary darts are
\[
(0,2),(11,0),(8,1),(1,3),
\]
and their directions are out, in, in, out. This is again a negative
perpendicular half-turn. The derived diagram has a link-extending
complement isometry to \(13n2955\). At \(t=2,3\) over \(\mathbb F_5\),
the source fibre has dimension two and the mutant fibre has dimension one.

O'Brien identifies these as negative mutant pairs in Killian Michael
O'Brien, *Seifert's algorithm, Chatelet bases and the Alexander ideals of
classical knots* (Durham PhD thesis, 2002), Section 5.3.1, printed
pp. 102-104, Figures 5.5-5.6.

## Exact two-change replay

In the \(13n2937\) source PD, switching zero-based crossings 1 and 6
reduces to the empty unknot diagram through eight RI/RII moves. The same
indices in the graph-derived mutant do the same. Each move records the
eliminated crossing labels and remaining crossing count in
`research/obrien_negative_mutation_graph_result.json`.

Thus the second pair has two-change upper bounds on both sides, not a
counterexample. The source-side mod-5 dimension two gives \(u\ge2\);
the mutation-\(u=1\) theorem and the mutant's nonzero Alexander module
exclude values 1 and 0 on the other side, so both values are exactly two.
The first pair instead has the required dimension-three lower bound on
both sides and supplies no two-change low side. These two explicit pairs
separate the two desired features rather than combining them.

## Bounded forward screens

Two forward screens found no candidate:

- A deterministic search generated 6,000 two-change diagrams from explicit
  unknot diagrams, tested 94,400 four-edge Conway circles whose crossing
  subsets are connected on both sides and 37,366 distinct negative mutants,
  and reached maximum tested fibre dimension two.
- From the pinned KnotInfo CSV row set, 7,021 thirteen-crossing knots with
  a listed upper bound at most two yielded 44,153 visible four-edge Conway
  circles with connected crossing subsets on both sides, 25,756 negative
  half-turns, and 15,046 distinct mutants. Across every linear
  specialization over primes \(3,5,7,11\), the maximum mutant fibre
  dimension was two.
- A separate extension-field pass tested every monic irreducible polynomial
  of degrees two and three over \(\mathbb F_2\) and \(\mathbb F_3\), for 14
  exact field presentations. Of the 7,021 low knots, 5,104 had an active
  fibre in this list. Their visible circles produced 22,455 negative
  half-turns and 13,207 distinct mutants; the maximum mutant fibre
  dimension was again two.

The exact parameters and counts are in
`research/relative_conway_forward_search.json` and
`research/negative_mutant_13_upper_two_scan.json`, while the exact extension
fields, counts, and result are in
`research/negative_mutant_13_upper_two_extension_scan.json`. These are
finite negative experiments. They do not exclude hidden Conway circles,
alternate diagrams, extension fields outside the recorded list, larger
diagrams, or lower bounds from other invariants.

The two exact low knots from O'Brien pair 2 were also searched through
changed diagrams. Three thousand 30-step trials produced 43 distinct
diagrams and 182 distinct mutants for \(13n2955\), and 34 diagrams and
154 mutants for \(13n2937\). A separate 3,000-trial run using the
100-step scale of Spherogram's `many_diagrams` produced 45 diagrams and
199 mutants for \(13n2937\). Every tested mod-5 fibre again had dimension
at most two. Randomized triangulation-to-link recovery exceeded its
1,200-second bound without returning a result; that timeout is a
non-conclusion, not another negative search result.

The earlier forced-cancellation plat family is excluded for a stronger
reason. Its local marked changes commute with both implemented word-level
half-turns: after the changes, the mutated left word freely reduces to
either \(\sigma_1^{-1}\) or \(\sigma_3^{-1}\), the right word reduces to
\(\sigma_3^{-1}\), and the resulting two-crossing closure is removed by
one RII move. Thus every mutant in that entire parameterized family also
has a two-change upper bound. The proof is in
`research/local_tangle_mutation_obstruction.md`; enlarging that finite
search cannot reach the required lower bound.

## Independent arithmetic replay

The pair-one mutant's \(12\times12\) graph-derived matrix over
\(\mathbb F_3\) was sent to Jacobian operation
`prime_field.matrix.rank.compute`. Under server 0.14.0 and protocol
2025-11-25 it returned rank 9 in 1 ms, hence cokernel dimension three.
The exact payload and full typed response, including the absence of a
structured error or timeout, are in
`research/jacobian-obrien-graph-rank-input.json` and
`research/jacobian-obrien-graph-rank-raw.json`; normalized adapter status
is in `research/jacobian-obrien-graph-rank-result.json`.

The extension-field implementation was separately calibrated on the
pair-one mutant at
\(\mathbb F_4=\mathbb F_2[x]/(x^2+x+1)\), \(t=x\). Restricting its
\(12\times12\) matrix to the ordered \(\mathbb F_2\)-basis \((1,x)\)
gives a \(24\times24\) matrix. The same Jacobian operation returned rank
22, hence extension-field rank 11 and cokernel dimension one, matching the
local field calculation. The exact payload, typed response, server and
protocol versions, and zero-error adapter status are in the three
`research/jacobian-obrien-gf4-regular-rank-*` files. This checks one exact
calibration matrix, not all 13,207 mutants.

No candidate is emitted.
