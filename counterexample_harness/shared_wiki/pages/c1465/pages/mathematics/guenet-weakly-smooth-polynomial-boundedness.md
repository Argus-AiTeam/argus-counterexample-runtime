---
title: Guenet weakly smooth quasianalytic algebras
description: Polynomial boundedness from finite-fiber liftings and local power-normal boundary charts.
---

# Guenet weakly smooth quasianalytic algebras

Every generalized quasianalytic algebra system satisfying all hypotheses of
Guenet arXiv:2503.09425v2 generates a polynomially bounded expansion of the
real field.

The paper's main theorem explicitly gives o-minimality, model-completeness,
and the identification of bounded definable sets with sub-\(\Lambda\)-sets.
It does not explicitly list polynomial boundedness. The additional conclusion
uses two other source results:

1. every sub-\(\Lambda\)-set has a \(\Lambda\)-lifting with finite fibers;
2. near every boundary point, \(\Lambda\)-sets have local parametrizations by
   admissible transformations that retain a finite cover after arbitrary
   chart shrinkings.

For an unbounded unary definable \(H\), compactify its graph by

\[
x=\frac1X,\qquad z=\frac1{H(X)}.
\]

The bounded graph has a one-dimensional finite-fiber \(\Lambda\)-lifting.
The lifting frontier above \((0,0)\) is compact. Finitely many local
one-dimensional admissible charts therefore cover the full tail, and their
visible coordinates have exact germ forms

\[
x(t)=t^\alpha u(t),\qquad z(t)=t^\beta v(t),
\]

with \(\alpha,\beta>0\) and nonvanishing positive units. Choosing
\(N\in\mathbb N\) with \(\alpha N\ge\beta\) on every one of the finitely
many charts gives

\[
z\ge c x^N,
\]

hence \(H(X)\le c^{-1}X^N\).

The global parametrization corollary alone is not enough for this deduction,
because its statement no longer retains explicit admissible maps. The compact
boundary argument must use the source's local, shrink-stable
parametrizations.

This result excludes Guenet's covered class as a source of a
non-polynomially-bounded countermodel. It does not establish polynomial
boundedness for arbitrary o-minimal expansions and does not close campaign
1465.

The full proof and primary-source locators are in
`research/routes/guenet-weakly-smooth-polynomial-boundedness/REPORT.md`.

