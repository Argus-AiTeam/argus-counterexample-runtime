---
title: Endpoint-notch two-bank cycle-quotient boundary
description: The minimal incidence six-cycle has exact half-loss, but arbitrarily small nonzero quotient perturbations of the vanishing two-bank kernel have threshold-energy ratio tending to one.
---

# Endpoint-notch two-bank cycle-quotient boundary

On the bipartite incidence graph with left vertices \((v,z-uv)\), right
vertices \((u,z)\), and lattice labels as edges, the full two-bank space is
\[
{\cal B}=\{F_v(z-uv)+H_u(z)\}.
\]
The Heisenberg-dilated standard six-cycle has unsigned incidence rank five.
Its local quotient by \({\cal B}\) is therefore one-dimensional, generated
by the alternating edge vector.

For every depth \(m\geq4\), an isolated rational alternating residual on
any sufficiently interior translate is complete-pair one-Lipschitz and
satisfies the exact complete-frame comparison
\[
{\cal R}^{\rm th}_m(g_m)=\frac12{\cal E}_m(g_m)>0.
\]
The factor \(1/2\) pairs every supported point's outgoing slot, whose
threshold remainder is zero, with an incoming slot of the same exact
profile denominator, whose remainder equals its original energy.

This local half-loss is not a quotient invariant. Let \(b_m\) be the
reviewed period-three two-bank scalar with
\({\cal R}^{\rm th}_m(b_m)={\cal E}_m(b_m)\to0\). With the explicit
rational lower bound
\[
L_m=\frac1{92160K_mh_m^4(5m+80)}
\]
and \(f_m=b_m+L_m^2g_m\), every \(f_m\) is complete-pair one-Lipschitz and
has nonzero six-cycle quotient, while
\[
\frac{{\cal R}^{\rm th}_m(f_m)}{{\cal E}_m(f_m)}
\geq\frac{1-7L_m}{1+3L_m}\longrightarrow1.
\]
Its energy still tends to zero.

Thus neither nonzero quotient amplitude nor the isolated-cycle
calculation supplies a uniform strict loss. The unresolved theorem must
be amplitude-sensitive and global: it must compare quotient size with
the original profile-weighted energy while handling overlapping and
longer incidence cycles. The opposite rational positive-energy branch
also remains open.

The proof, exact replay, and typed nullspace record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/two_bank_cycle_quotient/`.
