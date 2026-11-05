---
title: AK(3) projective Magnus-length boundary
description: Exact scalar-depth collapse and one-AC3 obstruction for Nagao/Bass-Serre lengths of the two-row Fox cocycle.
---

For a pair \(X=(x_1,x_2)\), let \(J_k(X)\) be its two-row Fox matrix over
\(\mathbb Z[S_k]\).  Any scalar polynomial or Laurent specialization of
this matrix sends \(S_k\) to an abelian unit group, so it factors through
\(S_k^{\mathrm{ab}}\cong\mathbb Z^2\).  Consequently every Magnus layer
has the same specialized matrix:

\[
[J_{k,\rho}(X)]=[J_{\mathrm{ab},\rho}(X)].
\]

The corresponding endpoint recurrence is constant in the derived depth.
For the normalized AK(3) pair under \(A,B\mapsto t\), the determinant is
\(t^{-1}-1+t\), while the standard pair has matrix \(I_2\); the former is
not a Laurent unit, so it is not an element of the Laurent \(PGL_2\) group
on which an amalgam word length is defined.

The complete AC3 row transport is nevertheless invertible.  With
\(v=(A-1,B-1)^T\), \(V=\mathcal D(h)\), and
\(\eta=\operatorname{ab}(h)\),

\[
C_h=\eta^{-1}(I_2+vV),\qquad
\det C_h=\eta^{-1},\qquad C_hv=v.
\]

This acts only on the conjugated tuple row, not on the full two-row matrix.
For

\[
c=[a,b],\quad h_n=c^{a^n},\quad
(a,b)\longmapsto(a,b^{h_n}),
\]

the common specialization \(A,B\mapsto t\) gives

\[
q_n=t^{-n}(t-1)^2,\qquad
C_n=\begin{pmatrix}1-q_n&q_n\\-q_n&1+q_n\end{pmatrix}.
\]

With \(P=\left(\begin{smallmatrix}1&0\\1&1\end{smallmatrix}\right)\),
\[
P^{-1}C_nP=
\begin{pmatrix}1&q_n\\0&1\end{pmatrix}.
\]
The full two-row matrix has \(t\)-adic elementary-divisor valuations
\((-n,0)\), so even after enlarging to the fraction-field tree its
base-vertex length jumps by \(n\) in this one AC3 edge.
The transport \(C_n\) has elementary-divisor valuations \((-n,n)\), hence
its base-vertex displacement is \(2n\).  Serre's
adjacent-stabilizer amalgam for
\(\operatorname{SL}_2(\mathbb Q[t,t^{-1}])\) then forces Bass--Serre
syllable length at least \(n\).  This is one legal AC3 edge for every
\(n\).

On the polynomial subfamily \(q_n^+=t^n(t-1)^2\), the isolated transport
has constant Nagao reduced length three, but the full two-row matrix has
determinant \(1+q_n^+\), a nonunit, and therefore still lies outside
\(\operatorname{PGL}_2(\mathbb Q[t])\).

Thus this scalar projective Magnus mechanism cannot simultaneously supply
a globally defined tuple length, a universal elementary-move bound, and a
derived-depth-divergent endpoint gap.  This is only a boundary for that
route; elementary-AC distance divergence and C1187 remain open.

Primary tree/amalgam source: Jean-Pierre Serre, *Arbres, amalgames, SL2*,
Astérisque 46 (1977), Chapter I, Section 1.2, Theorem 1, and Chapter II,
Sections 1.1, 1.4, and 1.6.  The exact theorem, free-word replay, typed
Jacobian matrix multiplication, and archived source are in
`research/experiments/ak3-projective-magnus-length/`.
