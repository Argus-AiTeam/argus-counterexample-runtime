---
title: Restricted-Heisenberg F2 determinant boundary
description: Exact collapse of the eight-dimensional restricted-Heisenberg scalar to the mod-2 exponent determinant in rank two.
---

For the normalized restricted-Heisenberg Hopf algebra

\[
H=\mathbb F_2\langle a,b,c\rangle/
(a^2,b^2,c^2,ba-ab-c,[c,a],[c,b]),
\]

with primitive generators, integral \(abc\), and top-coefficient
cointegral, Bobtcheva's scalar of any closed two-generator, two-relator
presentation \(P\) is

\[
\overline\Omega_H(P)=\det(E_P)\pmod2,
\]

where \(E_P\) is the integer exponent-sum matrix.

The reason is a degree filtration. Two inserted integrals have total PBW
degree six, and the two cointegrals can survive only in total degree six.
Every noncommutative Heisenberg correction has lower degree, so only the
commutative square-zero associated graded algebra contributes. Each of the
three primitive atom species then contributes one copy of
\(\det(E_P)\), giving \(\det(E_P)^3=\det(E_P)\) over \(\mathbb F_2\).

Consequently this invariant is one on every rank-two balanced presentation
with unimodular exponent matrix, including every

\[
\operatorname{MS}(n,w)=
\langle x,y\mid x^{-1}y^n x=y^{n+1},\ x=w\rangle
\]

with \(n>0\) and \(\exp_x(w)=0\). It cannot separate any such presentation
from the standard one. This is a boundary for this specific Hopf object,
not a statement about other nonsemisimple Hopf algebras or ordinary
Andrews--Curtis equivalence.

The proof and deterministic exact replay are in
`research/experiments/hopf-heisenberg-ms-family/`.
