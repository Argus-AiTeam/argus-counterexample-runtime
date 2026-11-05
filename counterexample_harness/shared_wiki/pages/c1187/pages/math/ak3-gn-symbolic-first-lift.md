---
title: AK(3) symbolic G_n first-lift boundary
description: Uniform original-word four-column operator and a two-character negative-norm obstruction excluding every unrestricted G_n fiber before S3.
---

# AK(3) symbolic \(G_n\) first-lift boundary

For every integer \(n\geq2\),

\[
G_n=((1,n),(1,n+1)),\qquad
H=((0,1),(1,1)),\qquad L=I
\]

has a nonempty unrestricted \(S_2\) Laurent fiber, but no point of
that fiber lifts the alternating depth-two cell to
\(S_3=F/F'''\), in any of the four ordered component patterns.  This
exhausts the first lift of the \(G_n\) family, not other integral
orbits or longer alternating cells, and is not an
Andrews--Curtis counterexample.

## Complete operator

Let

\[
R=\mathbb Z[X^{\pm1},Y^{\pm1}],\qquad
\Lambda=R[U^{\pm1},V^{\pm1}],
\]

with \(\sigma(U,V)=(X/U,Y/V)\), and put
\(A^-=\ker(1+\sigma)=\operatorname{im}(1-\sigma)\).  Finite free
words realize every scalar in \(A^-\).

Starting from the original AK(3) relators, use the parameterized
automorphisms

\[
(ab^n,ab^{n+1}),\qquad
(a^{-1}b,a(a^{-1}b)^{1-n}),\qquad
(ba^{-1},a).
\]

Their successive exponent bases are \(G_n,H,I\), and their composite
is the identity.  The resulting word-level \(2\times4\) operator
retains both internal and both terminal relation-cycle slots.
After removing endpoint factors, its four columns are

\[
[\,P_i\ Q_j\ C_a\ C_b\,],
\]

where, with \(W_m=1+\cdots+Y^{m-1}\),

\[
\begin{aligned}
P_1&=\binom{Y^{3-n}W_{n+1}(1-XY^n)}
 {X^{-4}Y^{-n}(1-XY^n)},\\
P_2&=\binom{Y^{3-n}W_n(XY^{n+1}-1)}
 {X^{-4}Y^{-n}(XY^{n+1}-1)},\\
Q_1&=\binom{XY^3(Y-1)}{X^{-3}(Y-1)},&
Q_2&=\binom{Y^3(1-XY)}0,\\
C_a&=\binom{Y^3(1-X)}0,&
C_b&=\binom0{X^{-3}(Y-1)}.
\end{aligned}
\]

For all four patterns and every \(n\geq2\), the complete image is

\[
(X-1,Y-1)(A^-)^2.
\]

Terminal axis powers only translate errors by outer Laurent units
and disappear in the cokernel \(X=Y=1\).

## Uniform unrestricted residual

Every finite Laurent \(h\) occurs in the complete \(S_2\) fiber
through

\[
f=A^2+(B-1)h.
\]

The all-\(n\) collection is performed directly from the original
words, not inferred from the reviewed \(n=2,3\) cases.  For
\(w=a^ib^j\mathcal C(r)\), let
\(d(w)=\overline{\partial_a w}\) and let \(\eta(w)\) be the sum of
the \(S_2\) commutator coordinates in the terms of
\(\partial_a w\).  Direct Fox-prefix collection gives

\[
\eta(uv)=\eta(u)+d(v)^*r(u)+\eta(v)
-B^{-j}S_j(B)
\frac{d(v)(1,B^{-1})-d(v)^*}{A-1}.
\]

Its closed power recurrence handles \(Q^n\) and \(u^{1-n}\).  With
\(T=B^n\) and \(N=n\) kept independent until the end, substitution
of \(f=A^2+(B-1)h\) leaves exactly the four coefficients

\[
\begin{array}{c|cccc}
\text{monomial}&1&h&h^*&h^*h\\ \hline
\text{coefficient}&C_n&M_n^*&-M_n&D_n.
\end{array}
\]

Both \(h(1,B)\) coefficients cancel.  Exact conjugacy identities,
together with the complete internal and terminal cycle columns,
identify the four component patterns.  Thus the same second
cokernel coordinate is obtained in all four:

\[
\Phi_n(h)=C_n+M_n^*h-h^*M_n+D_nh^*h,
\qquad t^*=t(U^{-1},V^{-1}),
\]

where

\[
\begin{aligned}
C_n={}&e_{2,n+1}-e_{2,-2}
+e_{1,n+1}+e_{1,0}-e_{1,-1}
-\sum_{j=3}^{n+4}e_{1,-j}\\
&-4e_{0,1}-3\sum_{j=2}^{n+2}e_{0,j}
-2e_{0,n+3}-e_{0,n+4},\\
M_n={}&U^3(V^{-n-5}-V^n)
+U^2(1+V^{-1}-V^{-n-3}-V^{-n-4}-V^{-n-5})\\
&+(U+1)(V^{-n-2}-V^{-n-1}),\\
D_n={}&e_{1,n+1}-e_{1,n}-e_{0,1}\\
={}&U^{-1}V^{-n-1}(V-1)
(UV^n-1)(UV^{n+1}-1).
\end{aligned}
\]

Set

\[
z=M_n-D_nh,\qquad
\mathcal N_n=M_n^*M_n+D_nC_n.
\]

Then

\[
z^*z=\mathcal N_n-D_n\Phi_n(h).
\]

At \((U,V)=(i,\zeta_6)\), the exact value of
\(\mathcal N_n\) is negative for every \(n\bmod6\) except residue
four.  If \(n\equiv4\pmod6\), then \(n\) is even, and at
\((U,V)=(\zeta_3,-i)\) the two possible values are
\(-15+6\sqrt3\) and \(-3-4\sqrt3\), both negative.  These are exact
periodic character identities: extending the finite sums by a full
root-of-unity orbit adds zero.

If \(\Phi_n(h)=0\), evaluation on the unit torus would give

\[
\mathcal N_n(U,V)=|z(U,V)|^2\geq0,
\]

contradicting one of the two negative values.  Thus no finite Laurent
point lifts for any \(n\geq2\), without a support cutoff.

The proof and exact replays are in
[`BOUNDARY.md`](../../../../../research/experiments/ak3-gn-symbolic-first-lift/BOUNDARY.md),
`symbolic_collection.py`, `symbolic_norm.py`, and `word_replay.py`.
`symbolic-collection.json` records the independent-\((T,N)\)
coefficient table and exact coefficientwise matches to the reviewed
\(n=2,3\) certificates.
