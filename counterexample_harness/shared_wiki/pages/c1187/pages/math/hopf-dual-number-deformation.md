---
title: Restricted-Heisenberg dual-number deformation boundary
description: Exact vanishing of the AK(3) endpoint derivative for every rank-eight deformation over F2[epsilon]/(epsilon^2) above the reviewed restricted-Heisenberg special fiber.
---

Let \(R=\mathbb F_2[\epsilon]/(\epsilon^2)\), and fix the reviewed
restricted-Heisenberg Hopf algebra \(H_0\) with PBW basis

\[
(1,x,y,xy,z,xz,yz,xyz).
\]

Every Hopf structure on a free rank-eight \(R\)-module reducing to \(H_0\)
is, after an isomorphism fixing closed categorical scalars, represented by
1104 binary first-order coefficients: 512 for multiplication, 512 for
coproduct, 64 for the antipode, and eight each for the integral and
cointegral. Because \(\epsilon^2=0\), the complete Hopf, integral,
cointegral, and normalization conditions are exactly linear over
\(\mathbb F_2\), not merely necessary tangent conditions.

The resulting system has rank 1051 and nullity 53. Two independent exact
implementations of Bobtcheva's presentation morphism--a direct primal
integral contraction and a dual coordinate-algebra word-map
contraction--both give

\[
\overline\Omega_H(\operatorname{AK}(3))
=1
=\overline\Omega_H(\langle a,b\mid a,b\rangle)
\]

for every point of that deformation space.

The decisive certificate is smaller than the full solve. The
\(\epsilon\)-coefficient of the direct endpoint difference has eight
structure terms and is exactly the XOR of nine coordinate equations from
unitality, the coproduct of the unit, counitality, coassociativity, and the
left antipode identity. It therefore vanishes on every admissible
deformation.

This exhausts only dual-number deformations whose special fiber is the
reviewed rank-eight restricted-Heisenberg object. It does not rule out Hopf
objects over \(R\) with another special fiber and does not decide ordinary
Andrews--Curtis equivalence. The proof and exact replay are in
`research/experiments/hopf-dual-number-deformation/`.
