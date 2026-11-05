---
title: AK(3) in free-soluble quotients
description: Exact support and limitation boundary for quotient-distance and quotient-invariant attacks.
---

For \(S_d=F_2/F_2^{(d)}\), use the symmetric signed elementary-AC metric in
which inversion, multiplication by either sign of the other component, and
conjugation by an arbitrary group element each have unit cost.

For the AK(3) pair and the standard basis, the distances \(D_d\) satisfy

\[
D_1=5,\qquad 5\leq D_d\leq D_{d+1}<\infty.
\]

The lower value is an exact exhaustive calculation in \(\mathbb Z^2\), and
monotonicity follows because every AC path projects through a quotient map.
Guyot's Proposition 1.2 proves that the endpoint pairs are AC-equivalent in
every soluble quotient. Therefore no invariant under all AC moves in a single
\(S_d\) can separate them.

Guyot's rank-two construction also gives a uniform coarse bound
\(d_M\leq10\) in the \(M\)-metric. This does **not** bound elementary-AC
distance: a single \(M\)-move may require an unbounded number of conjugate
factors when expanded into elementary moves.

The elementary distances may still grow with \(d\); no divergent lower bound
or uniform elementary upper bound is known here. Hence free-soluble quotients
support only a metric-complexity attack, not an orbit-separating invariant
attack, and \(M\)-recalcitrance is too coarse for that metric attack.

The later mod-three certificate proves
\(\lambda_d\geq6d-8\) for the middle multiplier in Guyot's literal
fixed-component conversion. This still does not globalize to arbitrary
elementary paths. At the same collar \((p,q_0)\), one AC3 move
\(q_0\mapsto q_0^{p^m}\) has multiplier of exact fixed-\(p\) conjugate width
\(2m\) in every \(S_d\), \(d\geq2\). More sharply, conjugating by
\[
H_m=\prod_{j=0}^{3m-1}p^{b^{2j}}
\]
produces a one-edge multiplier whose minimum fixed-\(p\) width is \(6m\)
and whose forced shifts are the full interval \(0,\ldots,6m-1\), with
\(2m\) cells in each residue class modulo three. Thus fixed-component width,
shift span, and residue-support counts have no uniform AC3 step bound.

In the first normal relation module, the collar displacement itself satisfies
\[
[w_1]=(2-B-B^2)e=(1-B)(2+B)e
 =[q_0^{-1}q_0^{\,p^2p^b}],
\]
so quotienting by AC3 holonomy erases the endpoint class at that level.
This is not a one-move construction in the free-soluble tower: exact Magnus
coordinates show that \(q_0\) and \(q_1\) are not conjugate already in
\(S_2\), because the required \(B=1\) Fox-polynomial identity would equate
a five-term polynomial with a monomial shift of a three-term polynomial.

The natural residual Peiffer refinement is also exactly obstructed.  Put
\[
\eta=q_0^{-1}q_0^{\,p^2p^b},\qquad R=w_1\eta^{-1}.
\]
After the one legal AC3 move \(q_0\mapsto q_0^{p^2p^b}=q_0\eta\), the
remaining right multiplier is \(R^\eta=\eta^{-1}w_1\).  A conjugated signed
\(p\)-holonomy \(([p,g]^\epsilon)^t\) is exactly two conjugates of
\(p^{\pm1}\) and has a literal alternating AC3/signed-AC2 compiler that
restores \(p\).  Since \(\eta\) itself is six such conjugates, a correction
using \(C\) holonomies would imply
\[
\lambda_d(w_1)\leq6+2C.
\]
The reviewed \(\lambda_d\geq6d-8\) therefore forces
\[
C\geq3d-7\qquad(d\geq3).
\]
Thus the one-\(h_0\) residual Peiffer-cell mechanism is not uniform, even
when all conjugating words depend on \(d\).  This says nothing about paths
using further arbitrary AC3 moves on \(q\) or signed AC2 moves that mix \(q\)
into \(p\).

No arbitrary-path lower bound or derived-length-independent elementary path
is currently obtained.

Primary source: Luc Guyot, *On Andrews-Curtis conjectures for soluble groups*,
arXiv:1612.06912v2, Propositions 1.2 and 2.2.
