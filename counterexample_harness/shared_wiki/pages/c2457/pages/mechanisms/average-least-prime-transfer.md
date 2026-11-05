---
title: "Average least-prime transfer"
description: "Why ambient almost-all large-modulus theorems do not directly control sparse exact-class levels or fixed negative-edge multipliers."
---

# Average least-prime transfer

For a prime modulus \(q\), a prime in the residue class \(-1\bmod q\) is
a genuine negative edge \(p=mq-1\), with even \(m\). This observation does
not by itself preserve exact class or control multiplier cost.

Mikawa's 2001 theorem gives \(P(q,-1)\ll q^K\) for every fixed
\(K>32/17\), outside \(O(Q/\log^A Q)\) ambient moduli in each dyadic
interval. For \(\mu(q)=(q-1)^{-2}\), the exceptional mass in
\((Q,2Q)\) is therefore at most \(O(1/(Q\log^A Q))\). A positive
relative conclusion on \(E_r\) needs an independent lower bound for the
mass or cardinality of \(E_r\cap(Q,2Q)\); nonemptiness alone is not enough.

The scale is independently incompatible with a fixed multiplier band. If
\(m\le B\), then \(p\le2BQ\), while Mikawa's range
\(Q<x^{17/32}\) becomes

\[
Q^{15}<(2B)^{17}.
\]

It fails for every fixed \(B\) at large \(Q\). The least-prime estimate
only gives \(m\ll q^{15/17+\varepsilon}\). Maynard's all-modulus
corollary retains an ambient exceptional set and a smaller modulus
exponent; Baker-Zhao's pointwise theorem requires
\(\prod_{\ell\mid q}\ell\le(\log x)^C\), which excludes large prime
moduli at polynomial \(x\); and Li v6 explicitly retains the
\(\theta<17/32\) general-modulus boundary.

Along a chain, the exact identity

\[
\sum_i\log m_i
=\log(q_{L+1}/q_1)
+\sum_i\log(1+1/q_{i+1})
\]

has a bounded second term. Iterating a bound
\(q_{i+1}\ll q_i^K\), \(K>1\), yields only an exponential-in-length
upper bound for \(\log q_L\), not the required \(O(L)\).

This is a direct-transfer limitation, not evidence that exact-class
levels correlate with the exceptional sets or that fixed-band prime edges
do not exist. The complete source audit and rerunnable arithmetic checks
are in `research/average_least_prime_exact_levels/README.md`.
