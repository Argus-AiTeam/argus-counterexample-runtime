---
title: Length-two U(sl3) boundary in Ver_7^+
description: Exact PBW Hopf structures and scalar-one AK(3) boundary for both F7 forms.
---

# Length-two \(U(\mathfrak{sl}_3)\) boundary in
\(\operatorname{Ver}_7^+\)

Newton's length-two internal Lie algebra has carrier \(L_3\oplus L_5\).
Over \(\mathbb F_7\), its two nonzero square classes are represented by
the raw parameters \(t=1\) and \(t=3\).  In the campaign's reviewed
Jordan quotient basis, the four bracket channels are
\[
(L_3L_3\to L_3,\ L_3L_5\to L_5,\ L_5L_3\to L_5,\
L_5L_5\to L_3)=(1,3,5,6t).
\]
Thus the last channel is \(6\) for \(t=1\) and \(4\) for \(t=3\).
The exact matrices agree with the archived Newton brackets and satisfy
equivariance, antisymmetry, Jacobi, and categorical \(7\)-Jacobi.

For each form, PBW gives the finite carrier
\[
S(L_3\oplus L_5)\cong S(L_3)\otimes S(L_5)
=7\mathbf1+7L_3+7L_5,
\]
whose ordinary representative dimension is \(63\).  The two
multiplications each have \(40{,}918\) nonzero coefficients and differ
in \(21{,}965\) coordinates.  They share the primitive coproduct, with
\(2{,}801\) nonzero coefficients.

The first serialized tables incorrectly reused the associated-graded
degree-sign antipode on the ordered \(L_3\)-before-\(L_5\) PBW basis.
An exact diagnostic found eight nonzero quotient coordinates in each
left and right antipode convolution for both forms, so those tables
were not accepted.  The corrected antipode reverses the PBW factors,
multiplies in \(L_5\)-before-\(L_3\) order, and then applies
\((-1)^{\text{total degree}}\).  It has \(281\) nonzero coefficients
and differs from the rejected map in \(218\) coordinates for each form.

The independent replay deserializes the corrected tables rather than
rebuilding them.  It reproduces the PBW data, checks associativity on
\((L_3\oplus L_5)\otimes H\otimes H\) and extends it by degree-one
generation, verifies the primitive coproduct and bialgebra identities,
and checks every unit, counit, antipode, cocommutativity,
coassociativity, and \(C_7\)-equivariance identity.  For each form the
two-sided integral and cointegral spaces are one-dimensional, their
selected pairing is one, and the normalized maps pass both-sided
identities.

For the literal AK(3) relators
\[
x^3y^{-4},\qquad xyxy^{-1}x^{-1}y^{-1},
\]
two exact recurrences were run against the corrected antipodes.  The
first traverses occurrences left-to-right with right-comb coproduct
splitting; the second traverses right-to-left with left-comb splitting
and right-associated word multiplication.  For both \(t=1\) and
\(t=3\), the schedules agree:
\[
\overline\Omega_{U_t(L_3\oplus L_5)}(\mathrm{AK3})
=1
=\overline\Omega_{U_t(L_3\oplus L_5)}(\mathrm{standard}).
\]

Consequently neither of the two length-two internal
\(\mathfrak{sl}_3\) enveloping objects separates AK(3).  This exact
boundary covers only these two objects and this presentation.  It does
not settle the global Andrews--Curtis conjecture, other internal Lie
algebras, other Hopf objects, or other balanced presentations.

The structural certificate is
`research/experiments/verlinde7-sl3-enveloping-hopf/certificate.json`;
the endpoint certificate is
`research/experiments/verlinde7-sl3-enveloping-hopf/endpoints-certificate.json`.
The source locations are Newton, arXiv:`2608.10585v1`, Theorem
`ThmLength2`, Equation `EqnRank2`, and the following
non-algebraically-closed remark; and Etingof,
arXiv:`1603.08133v4`, Proposition `Koszulhom` and Theorems `nol2` and
`maint`.  Exact excerpts are archived for independent attribution.
