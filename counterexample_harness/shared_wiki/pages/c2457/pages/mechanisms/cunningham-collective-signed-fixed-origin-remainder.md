---
title: Cunningham collective signed fixed-origin remainder
description: Exact variational identity equating the globally signed Selberg quadratic minimum with the unresolved partial-root survivor count.
---

On every exact complete CRT branch, retain the fixed-origin count
\[
A_b(q)=N_b\frac{\rho(q)}q+r_b(q)
\]
with its signed discrepancy \(r_b(q)\). Allow every nonempty branch its own
real Selberg weights \(\lambda_{b,d}\), normalized by
\(\lambda_{b,1}=1\), and its own legal divisor level. Before any triangle
inequality, Heath-Brown's Selberg square gives
\[
\begin{aligned}
U_{\rm total}
&=\sum_b\sum_{n\in J_b}
 \left(\sum_d\lambda_{b,d}V_b(n,d)\right)^2\\
&=\sum_bN_bQ_b+\sum_b{\cal R}_b.
\end{aligned}
\]
The second expression retains the actual signs after complete branch
aggregation; no termwise, progressionwise, branchwise, or final absolute
value is used.

Every point avoiding all selected partial roots has inner sum
\(\lambda_{b,1}=1\), so every legal quadratic is at least the exact survivor
count \(R_{\rm surv}\). At full divisor level,
\(\lambda_{b,d}=\mu(d)\) gives
\[
\sum_{d\mid P}\mu(d)V_b(n,d)
=\prod_{p\in H_b(n)}(1-1)
={\bf1}_{H_b(n)=\varnothing}.
\]
Therefore
\[
\min U_{\rm total}=R_{\rm surv}.
\]
This includes arbitrary short branches, empty and singleton branches, lcm
collisions, and the final truncated band.

The signed remainder can genuinely cancel the density main. An exact
four-branch replay has
\[
\sum_bN_bQ_b=\frac{70009}{24750},\qquad
\sum_b{\cal R}_b=-\frac{57103}{22000},\qquad
U_{\rm total}=\frac{839}{3600}.
\]
The reviewed \(h=4\) final-band example has exact value zero. These are finite
algebra checks only: in both cases the selected local survivor count is
already zero.

For the full cutoff using every odd \(p\leq Y\), \(R_{\rm surv}\) is the open
rough branch-cover count. Thus global signed Selberg optimization is exactly
equivalent to that unresolved count; it is not a separate asymptotic
estimate, a zero-count theorem, a survivor construction, or a Problem 1055
counterexample.
