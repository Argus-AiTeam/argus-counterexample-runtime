---
title: AK(3) least visible third-basis boundary
description: General G2,H,K,I solvability and cubic-character criterion, plus a complete first-lift obstruction for the least-height visible orbit.
---

# AK(3) least visible third-basis boundary

For

\[
K=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in
\operatorname{GL}_2(\mathbb Z),
\]

the normalized AK(3) three-update cell with successive bases
\(G_2,H,K,I\) has determinant

\[
D=\Delta+(AB^2-1)(AB^3-1)f_1
 +(B-1)(AB-1)f_2
 +(A^aB^b-1)(A^cB^d-1)f_3.
\]

An exact rank-one Fox recurrence shows that every nonlinear parameter
coefficient vanishes.  The two terminal-axis equations give a
complete unrestricted \(S_2\) fiber for every \(K\); its only gluing
condition is equality of the two axis augmentations, and its mixed
kernel is independently
\((A-1)(B-1)\mathbb Z[A^{\pm1},B^{\pm1}]\) in each parameter.

At

\[
(U,V)=(\zeta_3^{-1},\zeta_3),
\]

the third direction has value

\[
(\zeta_3^{b-a}-1)(\zeta_3^{d-c}-1).
\]

It is visible exactly when both \(b-a\) and \(d-c\) are nonzero
modulo three.  Exact height-one enumeration modulo the complete
signed-permutation cell action selects

\[
K_0=\begin{pmatrix}1&-1\\0&1\end{pmatrix}
\]

as a representative of the least visible nonassociate orbit, with
response

\[
(\zeta_3-1)^2=-3\zeta_3\ne0.
\]

The cell \(G_2,H,K_0,I\) nevertheless has no first lift to
\(S_3=F/F'''\).  Actual free Nielsen maps with these cumulative bases
compose to the identity, and original-word replay reconstructs all
three internal and both terminal relative-grade columns in all eight
component patterns.  The reduced \(2\times5\) operator has zero outer
augmentation in every one of its 80 scalar entries, so evaluation at
\(X=Y=1\) annihilates every unrestricted relation-cycle correction.
Terminal axis powers only multiply by units.

The projection of the complete \(S_2\) fiber onto its first parameter
is

\[
f_1=A^2+(B-1)h
\]

for arbitrary finite Laurent \(h\).  Exact support-unbounded
second-Fox collection shows that the second outer-augmentation
residual is identically the reviewed depth-two residual

\[
\Phi_2(h)=C+L^*h-h^*L+D\,h^*h,
\]

independent even after enlarging the other two update parameters to
arbitrary Laurent polynomials.  Its completion identity would force
a star norm to equal \(-14\) at the cubic character if the residual
vanished, contradicting nonnegativity in
\(\mathbb Z[\zeta_3]\).

Thus visibility of the determinant direction is not sufficient to
alter the obstructing relative-grade coordinate.  This conclusion is
specific to the least-height \(K_0\) orbit; other visible third bases
and longer cells remain open.

The exact derivation and replay are in
[`THEOREM.md`](../../../../../research/experiments/ak3-depth-three-visible-basis/THEOREM.md),
`s2_fiber.py`, `visible_basis_probe.py`,
`operator_cokernel.py`, and `unrestricted_residual.py`.
