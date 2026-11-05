---
title: Endpoint-notch energy-normalized cycle-quotient boundary
description: A complete-pair controlled quotient gives an exact low-energy branch, while the weighted six-cycle crosses one quarter but the global high-quotient loss remains open.
---

# Endpoint-notch energy-normalized cycle-quotient boundary

On the complete finite incidence graph, let
\[
{\cal B}_m=\{F_v(z-uv)+H_u(z)\}
\]
be the full two-bank subspace and let \({\cal E}_m\) be the original
profile-weighted frame quadratic form with both generators, all dyadic
scales, genuine word-ball basepoints, multiplicities, and normalization
\(2K_m|I_m|\).

The scale-invariant controlled quotient-energy fraction is
\[
{\mathfrak q}_m(f)=
\frac{\min\{{\cal E}_m(f-b):b\in{\cal B}_m,\,
\operatorname{Lip}(b)\leq\operatorname{Lip}(f)\}}
{{\cal E}_m(f)}.
\]
With the preregistered threshold \(\tau_0=1/4\), the reviewed two-bank
estimate and the triangle inequality give the exact low branch
\[
{\mathfrak q}_m(f)<\frac14
\quad\Longrightarrow\quad
{\cal E}_m(f)<
4\left(\frac{1990656}{h_m}
+\frac{4586471424}{\sqrt m}\right).
\]
The bank approximation is complete-pair Lipschitz by definition; no
orthogonal projection is assumed to preserve Lipschitz constants.

For the isolated scaled six-cycle, put
\[
A_t=\sum_j\Phi_m(2^{2j},4\cdot2^jt)^{-1},
\qquad t\in\{0,3,6\}.
\]
The corrected trace weights add the two generator contributions.  The
exact diagonal coefficients are
\[
(2A_0,A_0+A_3,A_3+A_6,2A_6,A_6+A_3,A_3+A_0).
\]
The common-coordinate kernel inequality yields
\[
\frac1{13}\leq\frac{A_3}{A_0}\leq1,\qquad
\frac1{25}\leq\frac{A_6}{A_0}\leq1.
\]
Exact weighted projection onto the alternating cycle quotient then gives
\[
q_{\rm tr}\geq\frac{3325}{13189}>\frac14,
\qquad
{\cal R}^{\rm th}_m=\frac12{\cal E}_m.
\]
An exact rational optimization also gives the largest
separation-certified alternating amplitude \(1/48\).

This trace calculation is a finite branch selector, not the global
quotient theorem.  Global competitors change off-cycle frame endpoints,
and the frame seminorm does not control complete-pair Lipschitz norm:
points in the outer word-ball shell are unseen by every frame edge.  The
high-quotient estimate
\[
{\cal R}^{\rm th}_m(f)\leq(1-c){\cal E}_m(f)+\delta_m
\]
with fixed \(c>0\) and explicit \(\delta_m\to0\) remains unproved.  No
rational complete-pair one-Lipschitz family with a uniform positive
frame-energy floor is known from this route.

The proof, exact replay, and typed Jacobian records are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/energy_normalized_cycle_quotient/`.
