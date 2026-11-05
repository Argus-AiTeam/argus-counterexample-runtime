---
title: Depth-shifted Laakso recursive lineage payment holdout
description: Exact failure of the frozen stationary-image birth-and-aging kernel on the first depth-increase holdout.
---

The reviewed lineage-typed terminal payment table closes the roots and the
first reachable \(w=1,j=0\) case, but its entries are indexed by terminal
lineage rather than generated recursively. To test whether that local lemma
propagates, freeze a five-coordinate packet state containing the two root-to-
packet and three direct-debt payment channels. Birth vectors come from the
reviewed root and current-packet payments. A sparse rational aging matrix maps
the inner birth vector to the reviewed age-one payment vector and fixes that
image.

The support, image, and stationarity normalization uniquely determines all 25
matrix entries. A typed Jacobian rational linear solve returns `UNIQUE`, and
the exact verifier reconstructs all six reviewed training source cases,
payment matrices, residuals, conservation equations, and reflections.

On the blind \(w=11,j=0,\nu=3\) holdout, the frozen recurrence assigns the
same payment state to the age-one and age-two digit-one packets. Four donors
then have exact negative residuals:

\[
\begin{aligned}
-9/100&<r_{\mathrm{direct.D}(b1,a1)}<-2/25,\\
-1/20&<r_{\mathrm{direct.D}(b1,a2)}<-1/25,\\
-1/25&<r_{\mathrm{root.D}(a3)}<-3/100,\\
-7/100&<r_{\mathrm{root.S}(a3)}<-3/50.
\end{aligned}
\]

The reflected \(w=22,j=3\) case has the same four intervals with digit two.
All payments are nonnegative, all conservation equations hold, and both
source and payment data reflect exactly, so this is a genuine exact failure
of the frozen kernel.

The complete scheduled margin remains positive, strictly between \(10^{-6}\)
and \(2\cdot10^{-6}\). Hence no metric counterexample is obtained. The result
retires only this stationary-image continuation of the valid local lemma; it
does not exhaust finite birth-and-aging kernels and does not decide the
all-depth \(q=3/5\) assertion.
