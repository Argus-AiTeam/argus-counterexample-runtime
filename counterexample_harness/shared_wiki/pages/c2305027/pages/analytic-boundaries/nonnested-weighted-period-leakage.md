---
title: Nonnested weighted-period leakage
description: Uniform rational splitting and adjoint leakage on the explicit critical four-ary one-point packing.
---

# Nonnested weighted-period leakage

There is an exact nonnested one-point packing with \(4^k\) holes of
radius

\[
s_k=2^{-2k-8}
\]

on a \(2^k\)-by-\(2^k\) rational grid near \(2^{-k}\). All disks enlarged
to radius \(3s_k\) are pairwise disjoint, while

\[
4^ks_k=\frac1{256}.
\]

Thus the total contour scale is critical even though the packing is
nonnested.

For controlled holomorphic contour moments and their normalized
absolutely summable principal parts, every depth-\(N\) tree cocycle has
the explicit path primitive

\[
b_v=-\sum_{w\preceq v}a_w
\]

with

\[
q_N(a)\leq\frac{355}{348}.
\]

The constant is independent of depth and moment order. Nonnesting also
lets each principal part act as a rational pole probe for its own
contour. Consequently every weighted period system obeys

\[
\left|\sum_w\Lambda_w(a_w)\right|
\leq4\mathcal D_N(\Lambda).
\]

The symmetric critical vector has pairing \(N\), but total adjoint defect
at least \(N+1/4\). Exact balance forces all weights to vanish.

If these principal parts are the complete transition cocycle of local
two-generator Bezout rows bounded by \(M\), the same primitive produces a
global row bounded by \(M+355/348\). This exhausts the declared weighted
Wiener/principal-part class, not arbitrary bounded analytic cocycles on
nonnested covers.

The proof and exact replay are in
`research/routes/nonnested-weighted-period-dual/`.
