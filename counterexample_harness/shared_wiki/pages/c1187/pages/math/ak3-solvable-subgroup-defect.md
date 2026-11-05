---
title: AK(3) iterated Fox subgroup-defect boundary
description: Exact one-AC3 obstruction for raw cyclic-generator and Fitting defects, and collapse of arbitrary-AC3 saturation.
---

For the \(k\)-th Magnus layer of \(S_d=F_2/F_2^{(d)}\), let

\[
L_k(X)=\mathbb Z[S_k]\mathcal D_k(x_1)
       +\mathbb Z[S_k]\mathcal D_k(x_2),
\qquad
C_k(X)=\mathbb Z[S_k]^2/L_k(X).
\]

These tuple-symmetric row modules are unchanged by AC1 and signed AC2.
They do not yield a uniformly Lipschitz iterated defect under arbitrary
AC3.

For every normally generating pair, the exponent matrix is unimodular, so
the abelian Fox determinant has augmentation \(\pm1\) and is nonzero.
Hence every Fox span needs exactly two generators at every layer. Minimum
generator number of the span itself is constant on all intermediate
vertices; the only plausible accumulated generator defect comes from the
cokernel.

More generally, every finite Laurent polynomial \(\tau\) is realized by
an explicit product \(h_\tau\) of conjugates of \(c=[a,b]\). The move

\[
(a,b)\longmapsto(a,b^{h_\tau})
\]

has abelian Fox determinant

\[
f_\tau=1+(A-1)(B-1)\tau.
\]

For every nonzero \(\tau\), this is a nonunit: specializing at \(A=1\) and
\(B=1\) would force any Laurent-unit value to be one, which would force
\(\tau=0\). The integer subfamily \(\tau=m\) gives
\(h_\tau=c^m\) and \(y_m=b^{c^m}\). Thus the move

\[
(a,b)\longmapsto(a,y_m)
\]

is one AC3 edge for every \(m\geq1\). Its abelian Fox matrix has determinant

\[
f_m=1+m(A-1)(B-1)=(m+1)-mA-mB+mAB.
\]

The cokernel \(C_k(a,y_m)\) is nonzero and cyclic at every layer, whereas
\(C_k(a,b)=0\). Therefore

\[
\sum_{k=1}^{d-1}\mu(C_k)
\]

changes by exactly \(d-1\) in one edge. More generally, a nonnegative
weighted sum has one-edge change equal to its total weight, while the
normalized AK(3) endpoint value is at most twice that total weight. A
uniform edge bound therefore forces a bounded endpoint gap. Fitting sizes
have the same obstruction: \(\|f_m\|_1=4m+1\) is unbounded already at one
layer, and a bounded nonunit indicator repeats at all \(d-1\) layers.

Quotienting away arbitrary AC3 terms does not repair the route. Exact
conjugation transport forces the two-sided ideal

\[
I_X=\sum_i\mathbb Z[S_k](g_i-1)\mathbb Z[S_k].
\]

For a normally generating pair this is the augmentation ideal. Modulo it,
the Fox rows are the exponent-sum rows, whose matrix is unimodular.
Consequently the saturated row module is all of
\(\mathbb Z[S_k]^2\), and the saturated cokernel is zero for every normally
generating pair.

Thus the precisely scoped cyclic-generator/Fitting subgroup-defect route
has an exact dichotomy: raw accumulation has no derived-length-independent
AC3 bound, while the forced two-sided AC3 saturation is identically
trivial. This does not decide whether the elementary-AC distances of
AK(3) in the free-soluble tower diverge.

The complete symbolic replay is in
`research/experiments/ak3-solvable-subgroup-defect/verify.py`; its theorem
and exact Jacobian sidecar record are beside it.
