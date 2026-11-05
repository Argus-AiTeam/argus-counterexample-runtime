---
title: Endpoint-notch profile-balanced root-primitive boundary
description: Exact finite-root summation by parts forces the profile-balanced period-three transport gap below 11/m.
---

# Endpoint-notch profile-balanced root-primitive boundary

Inverse profile weights remove the largest-scale domination of the
unweighted matched-dilation flow. For every \(m\geq8\), the resulting
noncentral coefficient vector uses every allowed dyadic scale, is nonzero
on a fixed positive fraction of occurrences at at least \(K_m/2\) scales,
and has overall support density greater than
\[
\frac1{45\cdot2^{43}}.
\]
Its exact demand annihilates every actual bank label, so the
full-bank-visible transport cost is zero.

This stronger candidate still has a vanishing complete support gap. Its
period-three root chirp has the bounded primitive
\[
G=(1/2,0,-1/2),\qquad
\chi_3(n)=G(n)-G(n-1).
\]
Exact summation by parts along each finite horizontal root line, including
both endpoint terms and both translated demand families, gives
\[
\operatorname{TC}_m(A_m^{\mathsf T}y_m)<4000mQ_m.
\]
Exact collision collection and genuine word-ball counts give
\[
\|y_m\|_2>\frac38K_m\sqrt{|I_m|Q_m}.
\]
Consequently,
\[
\frac{\Gamma_m(y_m)}{\|y_m\|_2}
<\frac{32}{3m}<\frac{11}{m}.
\]

This excludes only the profile-balanced period-three root chirp. It does
not cover coefficient fields with quantitatively long horizontal
primitives, arbitrary noncentral corrective flows, or the universal
transport-gap dichotomy.

The theorem, exact replay, and campaign validation are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_gap/`.
