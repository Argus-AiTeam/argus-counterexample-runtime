---
title: Endpoint-notch dyadic kernel-coercivity boundary
description: The exact one-generator short-side kernels are dense two-bank modes, while every common-period fibre with subexponential central variation has vanishing complete normalized central energy; dense smooth cycle-space scalars remain unresolved.
---

# Endpoint-notch dyadic kernel-coercivity boundary

For the pure right-horizontal increments
\[
P_rG(u,v,z)=G(u+r,v,z+rv)-G(u,v,z),\qquad
Q_rG(u,v,z)=G(u,v+r,z)-G(u,v,z),
\]
the all-dyadic kernels on the complete lattice are exactly
\[
\bigcap_j\ker P_{2^j}=\{F(v,z-uv)\},\qquad
\bigcap_j\ker Q_{2^j}=\{H(u,z)\}.
\]
Their intersection consists only of constants.  Thus a one-generator
kernel need not be horizontally sparse: explicit period-three modes are
active on two thirds of the transverse slices.  Such modes are full
two-bank scalars, so the reviewed two-bank theorem still forces their
complete normalized central energy to vanish.

There is also an exact nonlinear central-variation bound.  Put
\[
K_m=\frac{m(m+1)}2-3,\qquad h_m=2^{K_m},\qquad
\sigma_m=1-\frac1m,\qquad N_m=\frac{h_m^2}{2^{62}}.
\]
If a complete-pair one-Lipschitz scalar is the restriction of an array
that is \(N_m\)-periodic in the central coordinate and has at most \(J_m\)
nonzero adjacent differences per period on every horizontal fibre, then
for \(m\ge128\)
\[
\boxed{\mathcal V_m(G)
\le2^{95}m^3J_m^2h_m^{-2\sigma_m}.}
\]
This direct estimate retains both generators, all scales, genuine
word-ball slices, repeated occurrences, exact profile denominators, and
the single \(2K_m|I_m|\) normalization.

For arbitrary fibre-dependent thresholds of trigonometric polynomials
whose frequencies are signed subset sums of
\(\{4^{q-35}:m+1\le q\le2m\}\), the number of central changes is below
\(2^{4m-67}\).  Consequently
\[
\mathcal V_m(G)<m^3\,2^{-m^2+8m-32}\longrightarrow0.
\]
Subset-sum harmonics therefore defeat a linear Sidon extraction without
meeting the positive-energy bar.

The unrestricted scalar theorem is still open.  Any positive-energy
family within the periodic-fibre framework must obey
\[
J_m^2\ge
\frac{c\,h_m^{2\sigma_m}}{2^{95}m^3},
\]
so the remaining case is an exponentially dense, smoothly varying
cycle-space scalar rather than a sparse magnetic sheet or a
bounded-complexity nonlinear correction.
