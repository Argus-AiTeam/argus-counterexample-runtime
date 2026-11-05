---
title: Endpoint-notch horizontal-checkerboard transport boundary
description: A nonzero dyadic horizontal pushforward is routed at vanishing normalized cost by a cross-scale right-horizontal flow.
---

# Endpoint-notch horizontal-checkerboard transport boundary

For the profile-balanced six-cycle, the scale-adapted field
\[
\beta_{m,j}(U,V,\lambda)
=(-1)^{\lfloor U/(2r_j)\rfloor+\lfloor V/r_j\rfloor}
\]
has exact matched-scale collection
\[
4A_j(u)B_j(v).
\]
Its complete-core horizontal pushforward is nonzero and equals
\[
-\frac{8(2L_m^2+1)}{\sqrt{H_m(r_j^2)}}A_j(u)B_j(v).
\]
The collected vector is genuinely supported at every scale, is nonzero on
more than \(1/(45\cdot2^{42})\) of all frame occurrences, annihilates both
complete banks, and satisfies
\[
\|y_m\|_2^2>2K_m^2|I_m|Q_m.
\]

This does not yield a positive complete-transport gap. Grouping at most
\(m\) consecutive scales, one exact flow along right \(a^{2^a}\) edges
uses orthogonality of the transverse Rademacher factors and costs
\(O(\sqrt m\,Q_m)\) per block. Exact central, horizontal, inclusive-root,
carrier, and top-scale corrections give
\[
\operatorname{TC}_m(d_m)
<Q_m\left[
4288\sqrt m\left\lceil\frac{K_m-11}{m}\right\rceil
+85000m+100\right].
\]
Consequently
\(\Gamma_m(y_m)/\|y_m\|_2\to0\).

This excludes only the preregistered horizontal-checkerboard field. It does
not prove decay for arbitrary scale-dependent fields or settle the
unrestricted endpoint-notch transport gap. The proof, exact replay, and
typed finite min-cost-flow audit are under
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_gap/horizontal_checkerboard_transport/`.
