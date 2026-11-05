---
title: Endpoint-notch local multiplicative interval-rank boundary
description: A uniform eight-point Hilbert projection defeats every order-four interval-regular cross-distance box at D=112.
---

For any at most eight points in a real Hilbert space, consider their at most
\(\binom82=28\) unit pair directions. A spherical band of directions whose
projection onto one fixed pair direction has magnitude below \(1/112\) has
measure at most \(2/112\). The union of all forbidden bands therefore has
measure at most \(1/2\), so some line projection preserves every nonzero
distance within factors \(1/112\) and \(1\).

After scaling, every eight-point Hilbert metric has a map \(g\) to the line
with
\[
 d(z,z')\leq |g(z)-g(z')|\leq112d(z,z').
\]
For any four row points and four column points, the resulting squared
cross-distance matrix factors as
\[
 (g(x_i)-g(y_j))^2
 =
 \begin{bmatrix}g(x_i)^2&1&g(x_i)\end{bmatrix}
 \begin{bmatrix}1\\g(y_j)^2\\-2g(y_j)\end{bmatrix},
\]
so it has rank at most \(3\). Hence at \((n,D)=(1,112)\), every
order-\(n+3=4\) endpoint-notch interval box contains a singular matrix.
This covers all depths and all label choices, including families outside
the reviewed proper supports.

The result retires the proposed local interval-minor criterion. It does not
give a fixed-rank completion of the complete \(B_m\) distance matrices, so
the complete multiplicative interval rank and the endpoint-notch candidate
remain open.
