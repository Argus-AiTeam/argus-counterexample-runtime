---
title: A5-relative Alexander coinvariant boundary
description: Exact 19-kernel Schreier exhaustion and four-loop integral collapse of every global affine coinvariant.
---

For every epimorphism
\(\pi:F(a,b)\twoheadrightarrow A_5\), let
\[
M=\ker(\pi)/[\ker(\pi),\ker(\pi)],\qquad
G_\pi=F/[\ker(\pi),\ker(\pi)].
\]
A prefix-closed 60-sheet Schreier section gives
\(M\cong\mathbb Z^{61}\).  The exact normal form
\((u,q)=k\tau(q)\) has multiplication
\[
(u,q)(v,t)=(u+\rho_qv+c(q,t),qt),
\]
so all AC1--AC3 moves are affine on the rank-122 pair fiber.

There are 2280 ordered generating pairs in \(A_5\).  They split into 19
free \(S_5=\operatorname{Aut}(A_5)\) orbits, hence 19 kernel classes.
Direct replay builds the Schreier basis, all 60 action matrices, the
extension cocycle, arbitrary-kernel conjugation coefficients, and both
AK(3) endpoint evaluations for every class.

The universal global affine coinvariant already collapses at the base
vertex \((1,g)\), where \(g\) is a 3-cycle.  Put \(R=\rho_g\) and
\(N=I+R+R^2\).  Four AC loops contribute the relation images
\[
0\oplus RM,\quad 2M\oplus0,\quad (R-I)M\oplus0,\quad NM\oplus0.
\]
The second copy dies because \(R\) is invertible, and the first dies by the
exact integral identity
\[
I=N-(R-I)(R+2I)-2I.
\]
All 122 Smith factors are therefore 1.  The finite \(A_5\) AC graph on
normally generating pairs is directly connected, so every endpoint
difference transports into this zero quotient.

This rules out only globally affine, abelian-valued invariants obtained
from the first \(A_5\) relation module.  It is not a complete affine-orbit
certificate and does not prove AK(3) AC-equivalent to the basis.
The proof and exact replay are in
`research/experiments/a5-relative-alexander-separator/`.

