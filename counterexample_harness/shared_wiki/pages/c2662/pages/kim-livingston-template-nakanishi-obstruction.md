---
title: Kim-Livingston template Nakanishi obstruction
description: Uniform mod-3 Alexander-module obstruction ruling out a two-crossing low side in the published mutation family.
---

# Kim-Livingston template Nakanishi obstruction

For the Kim-Livingston Figure 1 knot \(K_J\), the Seifert matrix is
\[
A=\begin{pmatrix}0&2\\1&0\end{pmatrix},
\]
independently of the infection knot \(J\).  Put
\[
L_J=K_J\#-K_J^r,\qquad S_J=K_J\#-K_J.
\]
Their published family pairs
\[
H_{n,J}=nL_J
\quad\text{and}\quad
M_{n,m,J}=mL_J\#(n-m)S_J,\qquad0\le m<n.
\]
The pair is related by the Kearton half-turn on the aggregate
\((n-m)K_J\) connected-sum tangle.

At the maximal ideal \((3,t+1)\) of
\(\mathbb Z[t,t^{-1}]\), the Alexander presentation
\[
tA-A^T=
\begin{pmatrix}0&2t-1\\t-2&0\end{pmatrix}
\]
becomes zero.  Every high or low diagram contains exactly \(2n\) such
two-dimensional blocks, including their \(-A\) or \(-A^T\) transforms.
The specialized Alexander module therefore has dimension \(4n\).
Because the displayed Seifert presentation already has \(4n\)
generators, both Nakanishi indices are exactly \(4n\).

Ito's bound gives
\[
4n=m(M_{n,m,J})\le u_q(M_{n,m,J})\le u(M_{n,m,J}).
\]
For the mission value \(n=3\), every low-four-genus side has
\(u\ge12\), for every \(J\).  This includes all \(J\) satisfying the
Kim-Livingston Casson-Gordon condition \(s_7(J)>18\), which gives
\(g_4(3L_J)=3\).  Hence the published template cannot supply a
two-crossing low side; this says nothing about mutation templates with a
different Seifert matrix.

The full proof, exact source vector figures, mutation coordinates, and
replayable computation are in
`campaigns/2662/research/kim-livingston-nakanishi-obstruction.md`.
