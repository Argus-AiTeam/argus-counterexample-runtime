---
title: Character-split Aurifeuillian norm factors
description: Brent and Granville--Pleasants split cyclotomic polynomial values into integer or norm factors, but the factor signs do not isolate negative-Frobenius rational primes or imply a linear selected-prime bound.
---

# Character-split Aurifeuillian norm factors

For an odd prime \(q\), a predeclared integer \(m\ge1\), and \(x=qm^2\),
Brent's identities give
\[
F_q^\pm(x)=C_q(x)\pm qmD_q(x),\qquad
F_q^-(x)F_q^+(x)=\Phi_q((-1)^{(q-1)/2}x).
\]
These are genuine integer factors.  Their plus/minus labels come from a
difference of squares, not from a partition of their rational prime divisors
by Frobenius.

Indeed, if a rational prime \(p\) divides either factor, then
\(p\nmid qm\), and the signed base has exact order \(q\) modulo \(p\).
Consequently
\[
q\mid p-1,
\]
so every such prime has positive orientation.  It cannot also satisfy
\(q\mid p+1\) because \(q\) is odd.  The exact \(q=5,m=1\) specialization is
\[
\Phi_5(5)=781=(41-30)(41+30)=11\cdot71,
\]
and both \(11\) and \(71\) are \(1\bmod5\).

Granville--Pleasants classifies the substituted cyclotomic polynomials that
split into two irreducible rational factors of equal degree and explains
selected cases as norms from cyclotomic fields.  It does not state a
primitive-prime theorem, assign every prime divisor of one factor to negative
Frobenius, or bound an individual divisor by \(Aq\).

Brent's Corollary 1 compares the sizes of the two whole factors.  Comparable
whole factors on the square-root scale of an exponential cyclotomic carrier
do not force either factor to have a prime divisor of linear size; a
rational-prime factor-count theorem would be additional input.

This rules out only the direct Brent/Granville--Pleasants application.  It
does not exclude a new relative factorization theorem for reciprocal norm-one
units.  No fixed-exponential exact-class family or Erdos counterexample
follows.
