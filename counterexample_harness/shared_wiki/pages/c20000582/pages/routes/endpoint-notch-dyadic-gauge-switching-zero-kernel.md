---
title: Endpoint-notch dyadic gauge-switching zero-kernel boundary
description: The r=1,2 modular constraints force two-gauge behavior in the inner diamond, while every boundary switch has total normalized energy O(1/K_m).
---

# Endpoint-notch dyadic gauge-switching zero-kernel boundary

Let \(N_m=2^{L_m}\) be arbitrary and consider
\[
f_m(X(u,v,z))=G_m([z-F_m(u,v)]_{N_m}),
\]
where \(G_m\) may be any rational nonmonotone profile. Suppose every
genuine dyadic frame occurrence satisfies
\[
F_m(u+r,v)-F_m(u,v)\in\{0,rv\},\qquad
F_m(u,v+r)-F_m(u,v)\in\{0,ur\}
\pmod {N_m}.
\]
One matched increment then vanishes on every occurrence, so the corrected
loss is exactly zero.

The unit- and two-step constraints classify the cocycle on the complete
inner horizontal diamond
\[
D_h=\{(u,v):|u|+|v|\leq h\}.
\]
Adjacent unit selectors must agree unless their transverse label is zero
modulo \(N_m\), in which case both candidate increments already coincide.
Compatibility with the axes and the line \(u=1\) therefore gives
\[
\boxed{F_m(u,v)=C+cuv\pmod {N_m}\quad((u,v)\in D_h),\qquad c\in\{0,1\}.}
\]
This uses no division modulo \(N_m\), so labels with large 2-adic
valuation create no exception.

At \(m=4\), the complete horizontal frame has 462350
generator-scale classes. The reviewed six-cycle and all 772 occurrences
of its exact flow lie strictly inside \(D_{128}\). For \(c=0\), every
profile is a right-bank \(z\)-potential; for \(c=1\), it is a left-bank
\(z-uv\)-potential. Hence the alternating cycle value and full-flow
pairing are zero for every period and profile. The required nonzero
finite selector on that support is therefore impossible.

Larger-scale choices can differ only when their forward horizontal
endpoint leaves \(D_h\). At fixed \((u,v)\), fewer than \(2h^2\) central
labels occur in \(B_W(e,h)\). Summing the escaping boundary strips over
both generators and all dyadic scales gives fewer than \(12h^4\)
occurrences. The reviewed lower bound \(|I_m|\geq h^4/2^{13}\) makes
their normalized contribution less than \(49152/K_m\).

On every nonescaping occurrence the two-gauge classification localizes
the reviewed label-swap estimate. Consequently the entire modular class
satisfies
\[
\boxed{
{\cal E}_m(f_m)
\leq\frac{221184}{2^{K_m}}
+\frac{509607936}{\sqrt m}
+\frac{49152}{K_m}
\longrightarrow0.}
\]
This covers every depth-dependent power-of-two period, compatible
cocycle, and rational profile; it is not unrestricted scalar
concentration.

Separately, replacing \(uv\) by an arbitrary nonproduct real height does
not defeat translated-interval packing while a single monotone profile
is retained: on every genuine central slice,
\[
\sum_z|d_e|\leq(r|q|+1)\operatorname{osc}G_m.
\]

The proof and exact replay, including the complete \(B_4\) horizontal
enumeration, all flow occurrences and off-cycle symbolic values, rigorous
profile weights, boundary counts, and typed Jacobian records, are under
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/dyadic_gauge_switching_zero_kernel/`.
