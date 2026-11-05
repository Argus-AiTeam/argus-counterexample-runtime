---
title: Negative-mutation algebraic feasibility
description: Exact genus-three O'Brien block, corrected integral crossing covectors, and a low-side two-change existence lift, but no mutation-compatible diagram.
---

# Negative-mutation algebraic feasibility

## Initial module-gap block

An integral genus-three O'Brien block was first found for which
transposing the internal \(B\)-block changes the specialized
Alexander-module dimension. Writing the two matrices as \(C\) and
\(C^-\), both satisfy
\[
\det(C-C^T)=\det(C^--(C^-)^T)=1
\]
and
\[
\det(tC-C^T)=\det(tC^--(C^-)^T)
=-(3t-4)^3(4t-3)^3.
\]
In the ordered partition \(A,b_0,B\), the \(A\)-\(B\) blocks vanish, the
\(b_0\)-\(B\) coupling is symmetric, and \(C^-\) is obtained by
transposing exactly the \(2\times2\) block \(B\).

At the maximal ideal \((5,t-2)\), the ranks of the two \(6\times6\)
presentations are
\[
\operatorname{rank}_{\mathbb F_5}(2C-C^T)=4,\qquad
\operatorname{rank}_{\mathbb F_5}(2C^--(C^-)^T)=3.
\]
Thus the mutant-side presentation has a three-dimensional cokernel and
needs at least three Alexander-module generators. The latter rank was
also reproduced by Jacobian operation
`prime_field.matrix.rank.compute` under server 0.14.0 and protocol
`2025-11-25`.

## Exact coordinate convention

A broader search then produced explicit integral data
\[
C=T+vv^T-ww^T,
\]
where
\[
v=(-34,-13,32,24,1,0)^T,\qquad
w=(-49,10,10,38,0,1)^T.
\]
The earlier values \(-1,-2\) were only representatives modulo \(5\), not
the integral coordinates in the JSON. If the two free coordinates are
\(a,b\), exact isotropy is
\[
976+10a-32b=0.
\]
The chosen solution is \(a=24,b=38\). Substitution of \(-1,-2\) gives
the nonzero integral pairing \(1030\), so those residues cannot describe
the required disjoint integral crossing data.

Both exact vectors are primitive, their rows \(4,5\) minor is one, and
they span a primitive isotropic rank-two covector lattice. Here
\(T=P^TEP\), \(P\) is the listed integral symplectic basis change, and
\(E\) is obtained from the empty Seifert matrix by three directed
elementary enlargements.

## What the lift now proves

The directed enlargements can be realized by adding three tubes to the
standard spanning disk without changing its boundary unknot. The basis
change \(P\) gives \(T\) on that same surface. The primitive isotropic
covectors are represented by two disjoint proper arcs on the surface;
their bicollar crossing disks change the Seifert matrix by \(+vv^T\) and
\(-ww^T\). Thus there exists a knot with Seifert matrix \(C\) which is
changed to the actual unknot by those two crossing changes. The proof and
coordinate derivation are in
`research/two_change_low_side_geometric_lift.md`.

This new \(C\) again has O'Brien block form. Its \(B\)-block transpose
\(C^-\) has the same Alexander determinant as \(C\), while at
\((5,t-2)\) their presentation ranks are four and three. The exact
integer reconstruction is in
`research/two_change_negative_mutation_lift.json`; the rank-three
mutant specialization was also reproduced on that exact matrix by
Jacobian operation `prime_field.matrix.rank.compute`.

This is still not a mutant-knot candidate. O'Brien's calculation assumes
a Seifert surface already in standard position relative to a Conway ball;
the numerical block form is not a converse realization theorem. No
mechanically recoverable disk-band diagram has yet put that Conway ball
in the same embedding as the two crossing disks, and no PD/DT or
Reidemeister replay exists. Moreover, both exact crossing covectors have
nonzero \(A\)- and \(B\)-parts. A crossing disk wholly inside the Conway
ball would have zero \(A\)-part, while one wholly outside would have zero
\(B\)-part. Thus both disks in any compatible realization must cross the
Conway sphere; the missing geometry cannot be supplied by placing the
two changes independently on its two sides. Consequently no unequal
unknotting numbers are claimed.

Two narrower searches preceding the successful algebraic lift were
negative:

1. A deterministic \(10^8\)-iteration search through sparse symplectic
   transvection walks in the fixed three-hyperbolic-pair congruence
   orbit found no lift.
2. An exhaustive mod-5 search of all \(5^9\) normalized forms obtained
   by three direct elementary enlargements, with \(195{,}312{,}500\)
   two-crossing lifts, found no lift.

These computations exclude only the stated finite parameterizations.
Allowing a direct-enlargement seed and a symplectic transvection walk
produced the lift above at deterministic iteration 112,619; it does
not by itself settle the remaining geometric realization.

The exact matrices and checks are in
`research/negative_mutation_algebraic_template.json` and
`research/verify_negative_mutation_algebraic_template.py`. The bounded
search definitions and results are in
`research/two_change_seifert_template_searches.json`; the stronger
lift is checked by
`research/verify_two_change_negative_mutation_lift.py`.
