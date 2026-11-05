---
title: AK(3) next visible fourth-lift boundary
description: Exact reduced-length cell classification and support-unbounded exclusion of the next inequivalent visible fourth lift.
---

# AK(3) next visible fourth-lift boundary

For the fixed prefix

\[
G_2,\quad H,\quad
K_{0,+}=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]

exact free lifts are ordered by the sum of the freely reduced lengths
of their two images.  Normalized four-update cells are compared under

\[
(G_2,H,K_{0,+},L)\mapsto
(PG_2R^{-1},QHR^{-1},SK_{0,+}R^{-1},TLR^{-1}),
\qquad P,Q,S,T,R\in B_2.
\]

This classification reuses the independently accepted arbitrary-\(L\)
Fox--Magnus response, inner-lift covariance, adjacent-shear exclusion,
and complete \(L=(ab,b)\) cell exclusion without rebuilding them.

There are eight exact lifts of total length two and \(64\) of total
length three.  Literal inverse words and both inverse compositions are
checked for every lift.  The resulting five normalized cell keys
consist of the signed-permutation cell, the reviewed \(L=(ab,b)\)
cell, two reviewed adjacent-shear sign cells, and one new
length-three cell represented by

\[
\lambda=(a^{-1}b,b^{-1}),\qquad
\lambda^{-1}=(b^{-1}a^{-1},b^{-1}),\qquad
L=\begin{pmatrix}-1&1\\0&-1\end{pmatrix}.
\]

This cell is genuinely visible.  Exact collection from the original
AK(3) words retains four unrestricted Laurent families
\(h,r,g,w\); in component pattern \((1,1,1,1)\), for example,
\([gw^*]R_1=t-1\ne0\) at a primitive seventh root.  Every one of the
sixteen component patterns has a nonzero fourth-family coefficient.

The complete \(S_2\) fiber has axes

\[
U_2U_3x_+ +y_+-T^{-1}w_+=-T^{-2},
\qquad x_-=T^{-2}.
\]

The free axes have augmentations

\[
z_\pm(1)=\mu,\quad w_\pm(1)=\nu,\quad
x_+(1)=1,\quad y_-(1)=-7+\nu,
\]

and all four \((A-1)(B-1)\)-Laurent kernels are arbitrary.  In
particular,

\[
x=A^2+(B-1)h
\]

for arbitrary finite Laurent \(h\).

At \((A,B)=(\zeta_3^{-1},\zeta_3)\), all sixteen second residuals are
identical and every coefficient involving \(r,g,w\) vanishes:

\[
R_2=C+ah-a^*h^*+Dh^*h,
\]

where

\[
C=\frac{-7-14\zeta_3}{3},\qquad
a=\frac{5+\zeta_3}{3},\qquad
D=-1-2\zeta_3.
\]

The exact identity

\[
(a^*-Dh)^*(a^*-Dh)=-\frac{14}{3}-DR_2(h)
\]

precludes \(R_2(h)=0\) for every complex \(h\), hence for every finite
integral Laurent support.  The six relation-cycle columns have zero
reduced outer augmentation by the arbitrary-\(L\) insertion and
suffix identities, and terminal powers act by nonzero units.

Therefore this complete cell has no lift to \(S_3\).  This is a
support-unbounded exclusion of one new cell, not an
Andrews--Curtis counterexample; other inequivalent fourth bases and
\(C1187\) remain open.

The exact proof and rerunnable certificates are in
[`THEOREM.md`](../../../../../research/experiments/ak3-next-visible-fourth-lift/THEOREM.md).
