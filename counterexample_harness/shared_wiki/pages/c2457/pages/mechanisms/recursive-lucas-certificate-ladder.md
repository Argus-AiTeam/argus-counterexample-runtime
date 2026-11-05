---
title: Recursive Lucas-certificate ladder
description: Lucas composition exposes a prescribed affine cyclotomic-factor selector; a least-certificate rule gives exact finite edges but no search-free all-height update or linear cost theorem.
---

# Recursive Lucas-certificate ladder

For an odd prime \(q\), write \(m=2k\) and
\[
N=2kq-1.
\]
The BLS Theorem 15 size condition is exactly \(k\le2q-2\).

For the Lucas sequence \(V_n(P,Q)\), composition gives
\[
V_{kq}(P,Q)
=V_q(V_k(P,Q),Q^k)
=V_k(P,Q)H_q(V_k(P,Q),Q^k)
\]
when \(q\) is odd. Hence, under
\(\gcd(N,V_k)=1\), the first BLS congruence is equivalent to
\[
2kq-1\mid H_q(V_k,Q^k).
\]
This is a prescribed affine-factor condition, not an automatic consequence
of the Lucas identity.

The fixed state \((P,Q,D)=(1,3,-11)\) has a checked exact-class ancestry
\[
5\to29\to173\to2767.
\]
Starting from the explicit exact-class-4 base \(2767\), the least complete
certificate success in the BLS size window occurs at
\[
k=88,\qquad
486991=176\cdot2767-1.
\]
The output is prime of exact class \(5\); the multiplier factors as
\(176=2^4\cdot11\), with \(11\) of exact class \(1\).

This is finite interface evidence only. Defining \(k\) as the least complete
BLS success selects a prime through its certificate. No search-free formula
for \(k\), all-height totality theorem, or bound
\(\sum_{i<L}\log(2k_i)=O(L)\) is known from this mechanism. Therefore it
does not establish a fixed-exponential exact-class family or negate Erdos
divergence.
