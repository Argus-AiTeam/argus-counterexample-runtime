---
title: Endpoint-notch threshold-period matching boundary
description: Complete common-threshold periods can carry positive profile incidence while the threshold remainder equals the original energy termwise.
---

# Endpoint-notch threshold-period matching boundary

For the frozen non-star frame, the reviewed common-threshold decomposition
is
\[
\mathcal E_m(f)\leq9\mathsf A_m+\mathcal R_m^{\rm th}(f),
\qquad \mathsf A_m\to0.
\]
Complete-period matching alone cannot make the remaining term a strict
fraction of the original energy.

For every \(m\geq128\), define the rational complete-pair one-Lipschitz
scalar
\[
G_m(X(u,v,z))=
\begin{cases}
1/48,&z-uv\equiv0\pmod3,\\
-1/96,&z-uv\not\equiv0\pmod3.
\end{cases}
\]
On every \(a\)-slot the right-horizontal increment is zero. Thus, whenever
the original increment is active, the central and original threshold
intervals coincide and
\[
\mathcal R_{m,e}^{\rm th}(G_m)=\mathcal E_{m,e}(G_m).
\]
Every \(b\)-frame increment vanishes, so globally
\[
\mathcal R_m^{\rm th}(G_m)=\mathcal E_m(G_m)>0.
\]

This is not a finite-boundary artifact. A genuine box in \(I_m\) splits
into complete period-three central families, and all but
\(26+10\lceil\log_2m\rceil\) scales carry normalized profile incidence at
least
\[
\frac{1}{1080\cdot2^{25}}.
\]
Nevertheless \(G_m\) is a two-bank scalar, so the reviewed two-bank theorem
gives
\[
\mathcal E_m(G_m)=\mathcal R_m^{\rm th}(G_m)
\leq
\frac{1990656}{h_m}
+\frac{4586471424}{\lfloor\sqrt m\rfloor}
\longrightarrow0.
\]

Therefore a valid contraction must split off the entire vanishing two-bank
kernel and obtain strict loss only from genuinely cross-bank cycle energy.
Positive profile incidence and complete periods, without amplitude-sensitive
cross-bank information, are insufficient. This boundary does not refute a
contraction with a vanishing additive term and does not provide a
positive-energy scalar.

The all-depth proof and exact replay are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/direct_threshold_period_matching/`.
