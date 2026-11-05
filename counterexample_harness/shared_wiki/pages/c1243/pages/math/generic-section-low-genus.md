---
title: Low-genus residual covers of generic first-congrua sections
description: Global Tan bound and exact classification of every S=nP+mQ+T whose normalized residual I-cover has genus at most two.
---

# Low-genus residual covers of generic sections

For the certified first-congrua elliptic quotient

\[
E(\mathbb Q(a))=\mathbb ZP+\mathbb ZQ+E[2],
\]

write \(S=nP+mQ+T\) and let \(t_S(a)\) be its quartic parameter.  Adjoining
a root of

\[
I(S)=1-\delta(t_S)+\delta(a)
\]

gives an algebraic point on the relatively minimal genus-5 first-congrua
fibration.  If the normalized residual cover has genus \(q\le2\), Tan's
normalized discriminant satisfies \(d\le1\).  With 14 possible singular
fibers, his non-semistable inequality gives

\[
h_K(S)<9(1+3\cdot14)=387.
\]

The resolved divisor formula

\[
h_K(S)=2\deg(t_S)+4-r(S),\qquad 0\le r(S)\le2,
\]

therefore gives \(\deg(t_S)\le192\).  The exact coordinate-height comparison
and the saturated Mordell-Weil lattice lower bound then give

\[
n^2+m^2\le1277.
\]

This disk contains 4,009 free pairs and 16,036 torsion translates.  Exact
good-reduction branch sieves at \(p=101,103\), followed by reconstruction
over \(\mathbb Q(a)\), leave exactly

\[
(n,m)\in\{(0,0),(0,1),(1,0),(1,1)\},\qquad T\in E[2].
\]

All 16 covers split and have genus zero.  The eight sections with
\((n,m)=(0,1)\) or \((1,0)\) have simultaneous generic \(I,F,D\) lifts but
satisfy \(x=0\).  The other eight satisfy \(x+y=0\).  Thus the entire
genus-at-most-two generic-section family is collision-degenerate.  This
classification does not cover higher-genus section covers, higher-degree
multisections, or isolated points on the full surface.

The rerunnable certificate is
`research/r2-generic-section-low-genus-multisections/evidence/exhaustion-validation.json`.
