---
title: D81 three-step norm escape boundary
description: Exact equality at n=5 refuting strict three-step norm growth for the reviewed D81 orbit.
---

For the reviewed seed in
\[
K=\mathbf Q(\theta),\qquad \theta^3-3\theta+1=0,\qquad
\theta\in(1/3,1/2),
\]
the exact homogeneous first-coordinate norms begin
\[
1,1,-1,-1,3,-8,-24,-3021,-8.
\]
All intervening standard Jacobi--Perron floors are certified by strict
rational-algebraic inequalities, and every displayed homogeneous state has
coefficient determinant \(28\).

The first four required comparisons hold:
\[
3>1,\qquad8>1,\qquad24>1,\qquad3021>3.
\]
At the next index,
\[
x_5=-58+142\theta+72\theta^2,\qquad
x_8=-142+354\theta+158\theta^2=x_5-x_6,
\]
and exact multiplication-matrix norms give
\[
|N(x_8)|=8=|N(x_5)|.
\]
Thus \(|N(x_{n+3})|>|N(x_n)|\) is false, with first failure \(n=5\).

The separate periodic-tail lemma remains valid: a periodic inverse branch
block is primitive and unimodular, so Perron cone contraction makes
\(s_{n+p}\) proportional to \(s_n\).  The proportionality factor is a
lattice unit of field norm one, hence
\(|N(x_{n+p})|=|N(x_n)|\) on the tail.  The failed three-step growth
proposition therefore closes this mechanism without proving periodicity or
producing a campaign counterexample.
