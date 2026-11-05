---
title: Endpoint-notch matched-dilation transport boundary
description: A noncentral chirped flow has fixed positive occurrence density and all-scale support, but its exact transport gap is below 32/sqrt(K_m).
---

# Endpoint-notch matched-dilation transport boundary

An explicit noncentral frame flow uses every scale and a root box of
cardinality comparable to \(|I_m|\). At scale \(t=2^j\), it places
left-translated dilates of the complete six-cycle at every root
\(q=X(U,V,C)\) with
\[
|U|,|V|\leq h_m/2^{10},\qquad |C|\leq(h_m/2^{10})^2.
\]
The exact root chirp
\[
(-1)^{\lfloor V/2^j\rfloor}
\chi_3(U+C-UV),\qquad
\chi_3=(1,-1/2,-1/2),
\]
reverses under the matching \(b^{2^j}\)-translation.

Every resulting point demand annihilates all actual left and right bank
labels, so the full-bank-visible transport cost is zero. Exact
mod-three collision tables show that the collected coefficient vector is
nonzero on every scale and on at least
\[
\frac1{45\cdot2^{45}}
\]
of all frame occurrences.

The candidate still fails quantitatively. A complete transport upper
bound and a single dense-scale norm lower bound give
\[
\operatorname{TC}_m(A_m^{\mathsf T}y_m)
\leq72|{\cal Q}_m|\sqrt{H_m((h_m/64)^2)},
\]
\[
\|y_m\|_2^2\geq
\frac9{256}N_m|{\cal Q}_m|H_m((h_m/2^{14})^2).
\]
Profile subquadraticity and the genuine word-ball cardinality bounds
then imply
\[
\frac{\Gamma_m(y_m)}{\|y_m\|_2}
<\frac{32}{\sqrt{K_m}}\longrightarrow0.
\]

This proves that positive occurrence density and all-scale support alone
do not prevent largest-scale domination. It excludes only this
unweighted matched-dilation chirp. Profile-balanced period-three root
fields are excluded by a separate exact boundary, while long-root-
primitive and arbitrary noncentral corrective flows remain open.

The theorem and exact replay are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_gap/`.
