---
title: Depth-shifted Laakso orbit-submetry boundary
description: Exact quotient lifting, Fourier alignment defect, and a depth-two non-interval quotient ball.
---

The full arm-swap group acts isometrically on every unchanged
depth-shifted Laakso diffusion metric.  Its orbits are exactly the
horizontal fibers, and the orbit map is a submetry.

If every orbit-quotient radius-\(R\) ball has at most \(M\) points mutually
farther than \(R/16\), the reviewed scalar model on each fiber transports
any full-space strict \(R/2\)-packing into at most \(M\) fibers with at
most \(60\) points each.  Hence the full doubling constant is at most
\(60M\); the proposed quotient value \(M=257\), if proved, would give
\(N=15420\).

Writing \(A_{m,h,j}\) for the reviewed fiber shell energies and
\(a_j(h)=\sqrt{A_{m,h,j}}\), the exact orbit metric satisfies
\[
(d_m^Q(h,k))^2=(d_m^H(h,k))^2+\|a(h)-a(k)\|_2^2+2\Delta_{hk},
\]
where \(\Delta_{hk}\ge0\) is the defect of using one arm alignment across
all ancestry shells.  This gives an unconditional vector lower bound, but
the available within-fiber \(1/5\) contraction controls only shell norms
and does not bound \(\Delta_{hk}\).

Orbit balls are not order intervals.  At depth two, with
\(R^2=8/125\), the exact quotient ball centered at coordinate \(0\)
contains coordinate \(12\) but excludes the intermediate coordinate
\(10\):
\[
d_2^Q(0,10)^2>13/200>8/125>63/1000>d_2^Q(0,12)^2.
\]
Therefore a four-adic interval-cover proof based on radial monotonicity is
invalid.  This is a boundary of the current fibration implementation, not
a non-doubling result for the unchanged family.
