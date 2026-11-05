---
title: Endpoint-notch asymmetric horizontal zero-kernel boundary
description: An asymmetric soft-threshold passes the complete six-cycle and 772-flow gates, but monotone translate packing forces the entire product-contraction class to have vanishing energy.
---

# Endpoint-notch asymmetric horizontal zero-kernel boundary

Let
\[
f_m(X(u,v,z))=a_m\Theta_m(z-\phi_m(u)\psi_m(v)),
\]
where \(a_m\Theta_m\) is monotone and \(\phi_m,\psi_m\) are fixed-zero,
sign-preserving, nondecreasing one-Lipschitz contractions. They may be
different, rational piecewise-linear, and depend on the depth.

For every genuine frame occurrence, the left and matched
right-horizontal argument shifts have opposite signs. Thus
\[
d_eq_e\leq0
\]
for both generators, every scale, every boundary and zero slice, and every
repeated occurrence.

A monotone translate-packing lemma controls the full class. On each actual
central slice, intervals of length at most \(T=2^j|q|\) whose origins
differ by integers overlap at most \(T+1\) times. Complete-pair
one-Lipschitzness bounds their total variation by the block diameter.
Using the exact endpoint-notch profile floor and all genuine slice
multiplicities gives
\[
{\cal E}_m(f_m)
\leq566231040\,\frac{m^{3/2}}{K_m}
<\frac{2^{32}}{\sqrt m}\longrightarrow0.
\]
This exhausts the full monotone product-contraction zero-kernel class,
including depth-dependent rational clamps and thresholds.

The finite mechanism is nevertheless genuine. With
\[
\phi(u)=u,\qquad
\psi(v)=\operatorname{sign}(v)\max\{|v|-1,0\},
\]
\[
f_m(X(u,v,z))=\frac1{48}{\bf1}_{\{z-u\psi(v)\geq1\}},
\]
the complete-pair constraint holds, label swap is broken, and the reviewed
six-cycle has alternating value \(1/48\). The exact 772-occurrence flow has
zero divergence at every off-cycle vertex and proves positive full-bank
residual at every depth. The all-depth estimate above shows why this valid
\(B_4\) selector still cannot provide a uniform positive energy floor.

The proof and complete replay, including every supported off-cycle value,
generator, scale, profile weight, boundary margin, and occurrence
multiplicity, are under
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/asymmetric_horizontal_zero_kernel/`.
