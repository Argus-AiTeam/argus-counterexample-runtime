---
title: MSV A61 residual boundary
description: Split-prime supersingularity criterion and the exact limitation of the mod-(1+sqrt(3)) representation.
---

For the Mascot--Sijsling--Voight Prym surface \(A/\mathbf Q(\sqrt{61})\),
the coefficient field of the newform \(61.2.b.a\) is
\[
L=\mathbf Q(\alpha),\qquad \alpha^4+8\alpha^2+13=0.
\]
The element \(r=\alpha^2+4\) satisfies \(r^2=3\).  The quadratic inner twist
acts by \(\alpha\mapsto-\alpha\), so at every rational prime split in
\(\mathbf Q(\sqrt{61})\), the Hecke coefficient lies in
\(\mathbf Z[r]=\mathbf Z[\sqrt3]\).

For every split \(p\ge5\) and either \(v\mid p\),
\[
P_v(T)=\operatorname N_{\mathbf Q(\sqrt3)/\mathbf Q}
       (T^2-a_pT+p),
\qquad
A_v\text{ supersingular}\iff a_p=0.
\]
The reverse implication follows from the unramified integral valuation and
the weight-two Weil bound: supersingularity forces
\(a_p\in p\mathbf Z[\sqrt3]\), while both real embeddings have absolute
value at most \(2\sqrt p\), forcing \(a_p=0\).

The residual representation at \((1+\sqrt3)\) is surjective onto
\(\operatorname{GL}_2(\mathbf F_2)\), but four of that group's six elements
have trace zero.  It therefore proves nonvanishing only for residual
trace-one primes.  It cannot decide the remaining exact equalities:
\[
a_{19}=3-\sqrt3\ne0,\qquad
a_{19}\equiv0\pmod{1+\sqrt3}
\]
is an explicit false positive.  Thus this structure reduces a global
nonsupersingularity certificate to an unresolved Hecke-coefficient
nonvanishing condition; it does not prove or refute the fixed candidate.

The full proof boundary and exact PARI-backed replay are
`research/MSV_A61_INNER_TWIST_BOUNDARY.md` and
`research/certificates/msv_a61/verify.py`.
