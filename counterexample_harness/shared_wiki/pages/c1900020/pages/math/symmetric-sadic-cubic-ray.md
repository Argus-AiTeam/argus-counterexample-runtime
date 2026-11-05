---
title: Symmetric S-adic periodic-inflation boundary
description: Exact supertile recursion and the precise algebraicity gap for the symmetric three-letter family.
---

For

\[
\sigma_m=(0\mapsto2,\ 1\mapsto02^m,\ 2\mapsto12^m),\qquad
\tau_m=\sigma_m^3,
\]

code \(0,1\) by \(D=(p,q)\) and \(2\) by the distinct digit
\(E=(r,s)\). If \(P=N(p,q)\), \(Q=N(r,s)\), and \(U=PQ^m\), the
first coded supertiles are exactly

\[
A_1=U^{m+1},\qquad
B_1=U^{m^2+m+1},\qquad
C_1=QU^{m^2+2m}.
\]

At every later level the products obey the noncommutative recurrence

\[
\begin{aligned}
A_{n+1}&=A_nC_n^m(B_nC_n^m)^m,\\
B_{n+1}&=B_nC_n^mA_{n+1}^m,\\
C_{n+1}&=C_n(B_nC_n^m)^mA_{n+1}^m.
\end{aligned}
\]

Uniform four-step cone contraction gives one real nested ray for every
legal coding, and the Perron tie rule proves every coded digit is its true
Jacobi--Perron floor. The fixed word is not eventually periodic: its
\(E\)-frequency is

\[
\frac{\lambda^2}{1+\lambda+\lambda^2},
\qquad \lambda^3-m\lambda^2-m\lambda-1=0,
\]

which is irrational for every \(m\ge1\).

The two historical cubic recognitions are exact periodic rays of cyclic
phases of \(DE^m\). The first substitution-word deviations occur at

\[
(m+1)^2,\quad (m+1)(m^2+m+1),\quad
1+(m+1)^2(2m+1)
\]

for seeds \(0,1,2\). At \(m=4\), the latter two are exactly 105 and
226.

Requiring the periodic inflation ray to survive the nonperiodic defect
forces \(P\) and \(Q\) to preserve one normalized ray. Exact elimination
of the two eigenvector systems gives

\[
\langle p-r,\ q-s\rangle.
\]

Thus a common inflation ray exists only when \(D=E\), outside the
declared family.

This does not decide whether the actual aperiodic ray is cubic.
Cubicity only places all tail states in one three-dimensional rational
vector space; it does not make a supertile a projective return or a digit
matrix a field-multiplication operator. No applicable general
transcendence theorem for bounded primitive-substitutive
Jacobi--Perron digit pairs is currently available in the checked sources.
Accordingly, the common-inflation mechanism is exhausted, while the full
symmetric S-adic family remains open.
