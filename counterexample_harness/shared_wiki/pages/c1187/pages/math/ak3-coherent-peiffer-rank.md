---
title: AK(3) coherent Peiffer--Fox rank boundary
description: Exact inverse-system compatibility dichotomy and a common-character one-AC3 obstruction to weighted layer flattenings.
---

For \(S_d=F_2/F_2^{(d)}\), let

\[
R_k=\mathbb Z[S_k],\qquad
T_k=R_k^2,\qquad
C_k(X)=T_k/
\bigl(R_k\mathcal D_k(x_1)+R_k\mathcal D_k(x_2)\bigr).
\]

Fox naturality makes these cokernels an inverse system. Signed AC1 scales a
row by a unit, and both signed AC2 moves are invertible row additions. After
these Nielsen changes are quotiented out, conjugating \(x_i\) by \(h\)
adds the one compatible Peiffer--Fox displacement

\[
(g_i-1)\mathcal D_k(h)
\]

at every layer.

This coherence does not produce a growing endpoint rank. A finite compatible
system through layer \(d-1\) is determined by its top coordinate, and its
coherent cokernel remains a quotient of a two-generated module.

The failure can be seen at one exact character shared by the endpoint and
the counterfamily:

\[
\mathbb Z[A^{\pm1},B^{\pm1}]\longrightarrow\mathbb F_{11},
\qquad A\mapsto3,\quad B\mapsto6.
\]

At this character, the standard Fox matrix has rank two, while the
five-move normalized AK(3) matrix is

\[
\begin{pmatrix}2&4\\5&10\end{pmatrix}
\]

and has rank one. Thus the coherent normalized AK(3) cokernel has dimension
one for every \(d\). If the layers are instead flattened independently, its
unweighted dimension is \(d-1\).

That growth is not Lipschitz under AC3. With \(c=[a,b]\) and
\(m_q=1+11q\),

\[
(a,b)\longmapsto(a,b^{c^{m_q}})
\]

is one AC3 move, and its evaluated Fox matrix is

\[
\begin{pmatrix}1&0\\8&0\end{pmatrix}.
\]

It too has cokernel dimension one at every layer. Hence the same one edge
changes the independent-layer dimension by \(d-1\). More generally, if
layer \(k\) is assigned any nonnegative multiplicity \(w_{d,k}\), both the
normalized AK(3) endpoint gap and this one-edge jump equal
\(W_d=\sum_k w_{d,k}\).

The arbitrary-Laurent family

\[
h_\tau=\prod_{p,q}
\left([a,b]^{a^{-p}b^{-q}}\right)^{n_{p,q}}
\]

realizes the full principal term
\(1+(A-1)(B-1)\tau\) in one AC3 move. Both signed product moves on
\((a,b^{[a,b]^m})\) preserve the row module exactly, so this boundary is an
AC3 coherence/flattening obstruction rather than the earlier signed-AC2
failure of cyclic coinvariant norms.

The exact theorem, finite-field replay, and Jacobian typed rank check are in
`research/experiments/ak3-coherent-peiffer-rank/`. This exhausts only the
coherent Fox-row cokernel and fixed-character weighted-flattening mechanism;
elementary-AC distance divergence remains open.
