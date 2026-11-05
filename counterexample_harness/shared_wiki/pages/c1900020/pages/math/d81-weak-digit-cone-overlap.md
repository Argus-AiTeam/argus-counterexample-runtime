---
title: D81 arbitrary-word first-overlap boundary
description: Every normalized true D81 word is covered; determinant matches exist, but all 8,900 matching pairs fail integral basis reconstruction modulo 473.
---

For
\[
K=\mathbb Q(\theta),\qquad \theta^3-3\theta+1=0,\qquad
\Xi_k=\theta^{2^{k+1}}(1+\theta^{2^k}),
\]
the first three power-basis rows are
\[
(-1,3,1),\quad(1,-7,12),\quad(115,-444,325),
\]
with determinant \(473\). Exact root-sign arithmetic gives
\[
\left\lfloor\Xi_0/\Xi_1\right\rfloor=9,\qquad
\left\lfloor\Xi_1/\Xi_2\right\rfloor=75.
\]

Every true normalized inverse digit is
\[
N(a,b)=\begin{pmatrix}b&0&1\\1&0&0\\a&1&0\end{pmatrix}
\]
with \(0\le a<b\), or \(a=b\ge1\) on a terminal suffix satisfying
\(y<z\). Hence all true words lie in the unconditional weak superset
\(b\ge1,\ 0\le a\le b\).

A cutoff-free endpoint traversal of this superset has exactly 896 words
at the first boundary and 595,384 at the second. The shifted-continuant
state retains the projected inverse rows, so equal first rows are not
silently merged. The resulting 37 forward signatures and 4,687 inverse
signatures give the complete first-overlap determinant reachability set
without materializing all 533,464,064 word pairs.

Unlike the D49 boundary, both target determinants \(-473\) and \(473\)
are reachable. They occur in 31 signature cells containing exactly
8,900 word pairs. Full matrix replay computes
\[
A_2=R^{-1}V=\frac{\operatorname{adj}(R)V}{\det R}
\]
for every pair. In every case
\((\operatorname{adj}(R)V)_{1,0}\not\equiv0\pmod{473}\), so none gives
\(A_2\in GL_3(\mathbb Z)\). There is therefore no normalized integral
first overlap and no suffix-floor survivor for this D81 scalar
recurrence.

This is an arbitrary-true-word obstruction, stronger than the earlier
fixed one-, two-, and three-digit substitution obstructions. It produces
no Jacobi--Perron counterexample and does not exclude another scalar
recurrence. The reviewed fresh-prime implication remains conditional and
is not activated.
