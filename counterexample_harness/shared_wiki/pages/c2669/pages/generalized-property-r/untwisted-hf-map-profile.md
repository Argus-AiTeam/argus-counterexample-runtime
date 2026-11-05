---
title: Untwisted Heegaard Floer map profile of R-link traces
description: Universal map profile and the Hopf-stable unit collapse for exact GST L3.
---

# Untwisted Heegaard Floer map profile

Let \(W_L:S^3\to\#^n(S^1\times S^2)\) be the punctured trace of a
zero-framed \(n\)-component R-link.  Every outgoing Spin\(^c\) structure
extends uniquely because
\[
H^2(W_L;\mathbb Z)\xrightarrow{\cong}
H^2(\#^n(S^1\times S^2);\mathbb Z).
\]

In the unique torsion outgoing structure, the \(H_1\)-action forces every
untwisted cobordism map into the exterior-degree-zero tower.  Absolute
grading and composition with the standard \(n\) 3-handles force its
coefficient to be a unit.  Hence the maps on
\(\widehat{HF},HF^-,HF^+,HF^\infty\) agree with the unlink maps, up to the
intrinsic sign over \(\mathbb Z\), under every outgoing boundary
identification.

For a nonzero label \(a\in\mathbb Z^n\), put
\[
d=\gcd(a_1,\ldots,a_n),\qquad
A_d=\mathbb Z[U,U^{-1}]/(U^d-1).
\]
Then \(\widehat{HF}\) and \(HF^+\) vanish, while
\[
HF^-\cong HF^\infty
\cong A_d\otimes\Lambda^*a^\perp.
\]
The common \(H_1\)-annihilator is the cyclic line \(A_d\otimes1\), and
the two surviving maps have the form
\[
F^\infty_{W_L,\mathfrak s_a}=m_{L,a}U^j q_a^\infty,
\qquad
F^-_{W_L,\mathfrak s_a}=m_{L,a}U^j q_a^-,
\]
where \(q_a^\infty\) is the Laurent-polynomial quotient and \(q_a^-\)
is its restriction to \(\mathbb Z[U]\).  Only the integer multiplier is
undetermined.  Their common image ideal
\[
I_{L,a}=m_{L,a}A_d\otimes1
\]
is preserved by every ordinary handle slide, after transporting the
Spin\(^c\) label.  Boundary mapping classes change the displayed
generator only by a unit.

For the one-component unlink and \(d>0\), use a genus-one triple with a
horizontal curve, a transverse meridian, and a sufficiently wound
horizontal translate.  In the fixed outgoing structure
\(\mathfrak t_d\), the target has the pair \(x_d^\pm\).  The planar lift
contains exactly one correctly ordered positive Maslov-zero triangle:
its lift is embedded, its projected domain is nonnegative and misses
the basepoint, it lands at \(x_d^-\), and it has signed count \(\pm1\).
All same-output classes are \(\psi_d+kQ_d\), where
\(Q_d=\phi_d^{\mathrm{in}}-\phi_d^{\mathrm{out}}\) has Maslov index
zero and basepoint multiplicity \(-d\).  Positive \(k\) is excluded at
the basepoint; negative \(k\) is excluded by a positive
far-winding coefficient of \(Q_d\) outside the small triangle.  Every
class landing at \(x_d^+\) has index \(-1\).  Thus there is no second
same-summand term or cancellation, including for the cheapest case
\(d=1\).  Together with
\[
\partial x_d^+=(1-U^d)x_d^-,\qquad \partial x_d^-=0,
\]
this gives the maps \(\pm U^j q_d^\infty\) and
\(\pm U^j q_d^-\).

Connected-summing with torsion genus-one factors gives the result for
\((d,0,\ldots,0)\).  A \(GL(n,\mathbb Z)\) basis change, realized by
component permutations, orientation changes, and handle slides, carries
an arbitrary \(a\) to that label.  Naturality therefore gives
\(m_{U_n,a}=\pm1\) for every \(a\ne0\), so the unlink image is the full
annihilator line.

This fixed-summand count is not Proposition 9.7 or Lemma 9.10 of the
Ozsvath--Szabo properties paper.  Those results concern the total
plus-theory surgery map summed over Spin\(^c\) structures and show only
that it is chain-homotopic to a map in a short exact sequence, with
leading term \(\iota\).  They do not remove lower terms in a fixed
non-torsion summand.

A proper ideal would be a global handle-slide obstruction for an R-link
whose trace is not already known to be diffeomorphic to the unlink trace.
It cannot occur for the GST family \(L_{n,k}\).  Proposition 10.1 and the
paragraph applying it to \(L_{n,k}\) in
Gompf--Scharlemann--Thompson, *Fibered knots and potential counterexamples
to the Property 2R and Slice-Ribbon Conjectures*, DOI
`10.2140/gt.2010.14.2305`, give
\[
L_{n,k}\cup H\sim L_{0,k}\cup H,
\]
where \(H\) is one canceling Hopf 1/2-handle pair and \(L_{0,k}\) is
handle-slide trivial.  Adding \(H\), sliding the 2-handles, and canceling
\(H\) are changes of handle decomposition of the same compact trace.
After puncturing the untouched 0-handle, they give a cobordism
diffeomorphism
\[
W_{L_{n,k}}\cong W_{U_2}
\]
fixing the incoming \(S^3\), with some induced outgoing boundary
diffeomorphism.

Fixed-Spin\(^c\) cobordism-map invariance transports every GST trace map
to an unlink map.  The outgoing diffeomorphism acts on labels by
\(GL(2,\mathbb Z)\), preserving nonzero labels and divisibility.  Therefore
\[
m_{L_{n,k},a}=\pm1,\qquad
I_{L_{n,k},a}=A_d\otimes1
\]
for every \(a\ne0\).  In particular, for the exact Cycle-14 ordered
`[V,Q]` code and \(a=(1,0)\), the differential retains the relation
\(\partial x^+=(1-U)x^-\), the unlink map has its sole term at
basepoint multiplicity zero, and
\[
m_{L_3,(1,0)}=\pm1,\qquad m_{L_3,(1,0)}\bmod2=1.
\]
The isolated finite input replay is in
`research/floer_invariants/cycle14_primitive_map/`.  It does not derive this
coefficient: every integer multiple of the displayed target cycle would pass
the same chain-map consistency test.  Its report therefore excludes the
Cycle-14 multiplier from mechanical evidence.  Separate negative controls
reject a direct-count certificate that declares non-strong admissibility,
unchecked periodic domains, or a coefficient supplied only as metadata.

The ledger retires the former misattribution to
Freedman--Gompf--Morrison--Walker, arXiv:`0906.5177v1`, whose source contains
neither Proposition 10.1 nor the \(L_{n,k}\) application.  Independent
Reviewer attribution of the corrected GST proposition remains required.

This retires the untwisted non-torsion trace-map separator for GST \(L_3\),
not the general map profile for arbitrary R-links.  It also does not turn
weak Property R into an unstabilized slide sequence: the equality follows
because the Floer map is an invariant of the trace cobordism.  Twisted or
filtered theories, graph or cocore decorations not determined by the bare
cobordism, involutive Floer theory, instanton theory, and monopole theory
are not addressed here.

The proof and source-level caveats are in
`research/floer_invariants/untwisted-cobordism-maps.md`.
