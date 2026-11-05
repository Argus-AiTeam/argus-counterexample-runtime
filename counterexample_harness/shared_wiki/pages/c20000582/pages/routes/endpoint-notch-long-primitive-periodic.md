---
title: Endpoint-notch long-primitive periodic boundary
description: A period-comparable primitive with protected collision density still has vanishing transport by scale-wise direct/primitive routing.
---

# Endpoint-notch long-primitive periodic boundary

For every \(m\geq31\), set
\[
q_m=2^{\lfloor\log_2(m+1)\rfloor}-1,\qquad
P_m=\operatorname{lcm}(3,q_m),
\]
and use the rational zero-mean field
\[
f_m(n)=\chi_3(n)+\frac18\psi_{q_m}(n),
\]
where \(\psi_q\) is zero at residue zero, \(+1\) on the first half of
the nonzero residues, and \(-1\) on the second half. It satisfies
\[
\frac m2\leq P_m\leq3m,\qquad
\frac{P_m}{96}\leq\|F_m\|_\infty<\frac{P_m}{8}
\]
for its discrete primitive \(F_m\).

The period-three component protects the reviewed collision table from
the long-wave perturbation: every previously nonzero cell retains
magnitude at least \(3/4\). Consequently the profile-balanced
six-cycle vector is nonzero on more than \(1/(45\cdot2^{43})\) of all
frame occurrences and on more than half the scales, while its demand
still annihilates every actual bank label.

Long primitive growth is nevertheless insufficient. Direct cycle
routing costs less than \(9Q_m/2\) per scale, and primitive routing is
geometrically cheap after \(16\lceil\log_2m\rceil\) scales. Taking the
cheaper route at each scale gives
\[
\frac{\Gamma_m(y_m)}{\|y_m\|_2}
<
\frac{96\lceil\log_2m\rceil+32}{125m^2}
+\frac{2m}{125(2L_m+1)}
\longrightarrow0.
\]

This excludes only the explicit \(\chi_3+\psi_{q_m}/8\) field.
Arbitrary long-primitive root fields and the unrestricted
full-transport dichotomy remain open. The theorem and exact replay are
under
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_gap/long_primitive_periodic/`.
