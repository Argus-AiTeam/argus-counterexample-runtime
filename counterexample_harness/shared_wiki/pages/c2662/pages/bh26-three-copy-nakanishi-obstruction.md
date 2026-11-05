---
title: BH26 three-copy Nakanishi obstruction
description: Exact mod-13 Alexander-module lower bound ruling out the proposed three-change amplification.
---

# BH26 three-copy Nakanishi obstruction

For
\[
L=(4_1\#4_1\#4_1)\#9_{10},
\]
the Alexander module specialized at
\[
(13,t^2-3t+1)\subset\mathbb Z[t,t^{-1}]
\]
has residue-field dimension four. Hence the Nakanishi index is at least
four. Ito's bound \(m(L)\le u_q(L)\le u(L)\), together with two
preliminary figure-eight unknotting changes and the published
three-change sequence, gives
\[
4\le u_q(L)\le u(L)\le5.
\]

The calculation uses exact Knot Atlas PD/DT codes for \(4_1\) and
\(9_{10}\). Their Alexander polynomials satisfy
\[
\Delta_{4_1}\doteq t^2-3t+1
\]
and
\[
t^2\Delta_{9_{10}}
=4t^4-8t^3+9t^2-8t+4
\equiv4(t-3)(t+4)(t^2-3t+1)\pmod {13}.
\]
Each of the four connected-sum factors contributes a nonzero
one-dimensional summand after specialization.

The published proof itself is a hard-coded DT sequence with changes at
zero-based indices 3 and 11 in a 15-entry list, followed by an isotopy
to a separate eight-entry list and a change at index 6. Its source
contains no parameterized extra-summand operation or persistent map of
those three sites. The exact sequence is replayed in
`research/verify_bh26_published_sequence.py`; the isometry and
simplification calls are recorded as software checks, not as a
Reidemeister certificate.

Thus no three crossing changes, and even no three proper rational
2-tangle replacements, can unknot \(L\), regardless of where they are
placed. This strictly rules out the proposed extension of the published
three-change \(4_1\#9_{10}\) construction to three copies of \(4_1\).
It does not determine \(u(L)\), does not rule out a
three-change construction for \((4_1\#4_1)\#9_{10}\), and is not a
counterexample to Kirby Problem 1.3.

The full proof and replay are in
`research/bh26-nakanishi-obstruction.md` and
`research/verify_bh26_nakanishi_obstruction.py`.
