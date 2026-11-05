---
title: Pisot unit-scaled unipotent frame boundary
description: Complete all-orientation obstruction for canonical rank-one and full-Jordan moving frames.
---

Fix the reviewed field
\[
K=\mathbf Q(\epsilon),\qquad
\epsilon^3-11\epsilon^2+10\epsilon-1=0,
\]
the ordered vector \(v=(\epsilon^2,\epsilon,1)^t\), and
\[
C=\begin{pmatrix}11&-10&1\\1&0&0\\0&1&0\end{pmatrix},
\qquad Cv=\epsilon v.
\]
For \(s_m=U^m v\) and
\[
B_m=U^mC^{m+1}U^{-(m+1)},
\]
all twelve canonical coordinate orientations are exactly obstructed.

Among the six rank-one frames \(I+E_{ij}\), only \(ij=12,13\) remain
in the normalized range for arbitrarily large \(m\).  Among the six
full-Jordan frames \(I+E_{ij}+E_{jk}\), only \(ijk=123,132\) do so.
The other eight orientations eventually have their second or third
coordinate exceed the first; a common exact threshold is \(m=91\).

Let
\[
q_{-2}=1,\quad q_{-1}=q_0=0,\quad q_1=1,\qquad
q_{r+1}=11q_r-10q_{r-1}+q_{r-2}.
\]
Then \(q_r\geq0\) and \(q_r>q_{r-1}\) for \(r\geq1\).  With
\(n=m+1\), the four surviving orientations have the respective
negative entries
\[
\begin{array}{c|c}
12&(B_m)_{22}=q_{n-2}-10q_{n-1}-nq_n\\
13&(B_m)_{23}=q_{n-1}-nq_n\\
123&(B_m)_{32}=q_n-(n+11)q_{n-1}\\
132&(B_m)_{23}=q_{n-1}-nq_n.
\end{array}
\]
The \(123\) expression is negative for \(n\geq2\); the other three are
negative for \(n\geq1\).

Every standard inverse Jacobi--Perron matrix
\[
N(a,b)=\begin{pmatrix}b&0&1\\1&0&0\\a&1&0\end{pmatrix}
\]
is nonnegative.  Therefore none of these \(B_m\) can have a standard
inverse-branch factorization, even before internal suffix floors are
tested.  All states still preserve the same lattice because
\(\det U=\det B_m=1\).  This exhausts precisely the canonical
rank-one/full-Jordan unit-scaled moving-frame class and does not
produce a counterexample.
