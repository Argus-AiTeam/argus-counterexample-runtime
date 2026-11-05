---
title: "Yang exact-level convolution admission"
description: "The growing convolution sum, modulus scale, and balanced well-factorability contracts in arXiv:2608.13299v1 do not admit the fixed-band exact-level graph slice."
---

# Yang exact-level convolution admission

For the lower-flow target

\[
\sum_{q\in E_r}\frac1{(q-1)^2}
\sum_{\substack{2\mid m\\m\leq B}}
\mathbf1_{\mathbb P}(mq-1)\geq\delta M_r,
\]

the variables \(q,m,p=mq-1\) are respectively the parent, multiplier, and
genuine prime child.

Yang's Theorem 1.1 uses different objects: a modulus \(s\), a prime \(t\),
and a full convolution sum over \(l\asymp x^\nu\), with
\(\varepsilon<\nu\). Its modulus weight must be well-factorable at level
\(Q=x^{\mathcal L(\nu)-\varepsilon}\), and
\(\mathcal L(\nu)<1\) throughout every nonvacuous range.

| Map | Exact graph identification | First contract failure |
|---|---|---|
| Parent as modulus | \(s=q,\ t=p,\ l=1,\ a=-1\) | \(l=1\) requires the absent endpoint \(\nu=0\). Growing representatives such as \(l=q-1\) leave the target on an unselected diagonal inside the full \(l,s\)-sum. |
| Child as modulus | \(s=p,\ t=q,\ l=m,\ a=1\) | The fixed band \(m\leq B\) again requires \(\nu=0\). Representatives \(l\equiv m\pmod p\) no longer select the original multiplier. |

At either modulus-independent localization, excluding the unwanted
congruence lifts forces the modulus to have size comparable with \(x\),
outside the legal \(x^{\mathcal L(\nu)-\varepsilon}\) range. Enlarging
\(x\) admits many lifts and does not recover the genuine \(k=1\) edge.

There is also an exact weight obstruction. In the balanced split
\(Q_1=Q_2=\sqrt Q\), a prime \(z>\sqrt Q\) has no factor pair supported in
both ranges. Hence every well-factorable sequence of level \(Q\) satisfies
\(\lambda_z=0\) at such a prime. The natural exact-level coefficient
\((q-1)^{-2}\mathbf1_{E_r}(q)\) therefore cannot be inserted at the direct
isolating scale. Yang's upper-bound linear-sieve weights are admissible,
but they neither select nor minorize exact-level prime mass.

The theorem remains a signed ambient discrepancy estimate. It supplies no
positive main term comparable with \(M_r\), no error absorption relative to
that sparse mass, and no fixed \(B,\delta,R\). This retires only the direct
Yang specialization; the bounded-multiplier correlation and the
unconditional Erdős target remain open.

The version-fixed source, complete proof, and exact replay are in
`research/yang_exact_level_convolution_admission/`.
