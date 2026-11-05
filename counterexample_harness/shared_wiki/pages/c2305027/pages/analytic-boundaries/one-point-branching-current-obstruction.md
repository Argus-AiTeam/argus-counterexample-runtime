---
title: One-point obstruction for conserved branching currents
description: Exact geometric limit of parent-equals-children contour flows on four-ary planar neck trees.
---

# One-point obstruction for conserved branching currents

An exact raw-contour identity with one incoming and four outgoing circular
necks makes the incoming circle the outer boundary of a planar five-holed
cell. The four child disks are therefore nested inside the parent disk.

Suppose level \(k\) contains \(4^k\) pairwise disjoint disks with radii in
\([a4^{-k},b4^{-k}]\), and all level centers converge uniformly to one
point. If \(d_k\) is the diameter of the level-\(k\) centers, nesting gives

\[
d_k\leq2b4^{-k}.
\]

Packing the \(4^k\) disks into a disk of radius \(d_k+b4^{-k}\) gives

\[
d_k\geq a2^{-k}-b4^{-k}.
\]

Hence \(a2^k\leq3b\) for every \(k\), which is impossible. This obstruction
is independent of periodicity and survives exact aperiodic perturbations.

The abstract current mechanism is not defective. On a finite nested tree,
the radii \(s_k=s_0 4^{-k}\) give constant total contour norm per level,
and Laurent-coefficient cocycles yield the exact lower bound
\(q_N\geq N/2\). The infinite nested model has a Cantor end set, not one
accumulation point. Thus the exhausted boundary is the simultaneous
one-point/nested-current class; nonnested branching covers and Cantor-end
domains are not covered.

The proof and exact replay are in
`research/routes/branching-residue-current/`.
