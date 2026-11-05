---
title: Primitive mu_8-Prym at p=167
description: Exact supersingular good reduction that disqualifies the fixed cyclic-cover candidate.
---

For

\[
C_8:y^8=x(x-1)(x-3),\qquad
C_4:z^4=x(x-1)(x-3),
\]

the connected kernel of
\(\operatorname{Jac}(C_8)\to\operatorname{Jac}(C_4)\) has dimension
\(7-3=4\) and good reduction outside \(\{2,3\}\). In denominator-character
notation, its primitive Hodge dimensions for \(j=1,3,5,7\) are
\((0,1,1,2)\).

At \(p=167=8\cdot20+7\), both proposed Cartier coefficients vanish:

\[
[x^{62}]((x-1)(x-3))^{104}
=[x^{104}]((x-1)(x-3))^{62}=0\pmod {167}.
\]

Complete power-map enumeration over \(\mathbf F_{167^2}\) gives

\[
\#C_4(\mathbf F_{167^2})=28828,\qquad
\#C_8(\mathbf F_{167^2})=30164.
\]

Thus the Prym power sum is \(s_2=-1336=-8\cdot167\). Weil extremality forces
every Frobenius root \(\alpha\) to satisfy \(\alpha^2=-167\), so

\[
P_{A,167}(T)=(T^2+167)^4.
\]

All eight slopes are \(1/2\). This is an exact supersingular good prime, so it
disqualifies this fixed candidate but does not settle the campaign target for
other abelian varieties. The proof and rerunnable arithmetic are in
`research/MU8_PRIMITIVE_PRYM.md` and
`research/certificates/mu8_primitive_prym/verify_p167.py`.
