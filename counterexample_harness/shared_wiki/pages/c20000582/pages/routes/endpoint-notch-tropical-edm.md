---
title: Endpoint-notch tropical EDM rank boundary
description: Uniform rank-four lift for all finite monomial-logarithmic cross-distance valuations, including exact leading cancellations.
---

# Endpoint-notch tropical EDM rank boundary

Let \(R_m=2^{m(m+1)/2}\).  For any finite row and column schedules whose
Heisenberg coordinates are finite sums of \(cR_m^a m^b\), with rational
\(a\) and integer \(b\), the exact endpoint-notch profiles preserve primary
\(R_m\)-degree on genuine word-ball displacements.  If
\[
A_{ij}=(u'_j-u_i)^2+(v'_j-v_i)^2
\]
and
\[
W_{ij}=w'_j-w_i+2u_iv'_j-2v_iu'_j,
\]
then the squared cross-distance valuation is exactly
\[
V_{ij}=\max\{\nu(A_{ij}),\nu(W_{ij})\}.
\]
This remains true after arbitrary exact leading cancellations inside either
expression.

Adjoin one degree-zero transcendental \(\zeta\).  The matrix
\[
M_{ij}=A_{ij}+\zeta W_{ij}
\]
has entry valuation \(V_{ij}\) and the exact factorization
\[
M_{ij}=
\begin{bmatrix}u_i^2+v_i^2-\zeta w_i&1&u_i&v_i\end{bmatrix}
\begin{bmatrix}
1\\
(u'_j)^2+(v'_j)^2+\zeta w'_j\\
-2u'_j+2\zeta v'_j\\
-2v'_j-2\zeta u'_j
\end{bmatrix}.
\]
Hence every such valuation matrix has max-tropical rank at most four; a
unique dominant permutation is impossible from order five onward.

**Scope.** This rules out arbitrary-order tropical determinant dominance
for the complete frozen finite monomial-logarithmic coordinate class.  The
lift is not a PSD Euclidean distance matrix and does not embed the complete
endpoint-notch word balls.  Non-monomial-logarithmic schedules and the
finite-Hilbert-block objective remain open.

