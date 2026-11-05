---
title: "Exact-level hyperbolic lower flow"
description: "Duplicate normalization is an identity, and its square-summable cofactor tail reduces every uniform all-cofactor lower bound to the open fixed-band prime correlation."
---

# Exact-level hyperbolic lower flow

Give the terminal primes \(2,3\) height zero.  For \(r\ge2\), let
\(\mathcal A_r\) contain the positive integers whose nonterminal prime divisors
have exact class at most \(r\), with \(2,3\) always permitted, and let

\[
d_r(p)=\#\{q\in E_r:q\mid p+1\}.
\]

The genuine class-compatible edges are exactly

\[
(q,m),\qquad q\in E_r,\quad m\in\mathcal A_r,\quad 2\mid m,\quad mq-1
\text{ prime}.
\]

Each \(p\in E_{r+1}\) has exactly \(d_r(p)\) such representations.  Hence,
with \(\mu(p)=(p-1)^{-2}\),

\[
\sum_{q,m}\frac{\mu(mq-1)}{d_r(mq-1)}=M_{r+1}.
\]

If \(T_r(B)\) restricts this sum to \(m\le B\), then

\[
0\le M_{r+1}-T_r(B)\le\frac{M_r}{B}.
\]

Indeed, \(mq-2\ge m(q-1)\), and
\(\sum_{m>B}m^{-2}\le1/B\).  Thus a proposed bound
\(M_{r+1}\ge\rho M_r\) forces

\[
T_r(B)\ge\frac{\rho}{2}M_r
\quad\text{for every integer }B\ge2/\rho.
\]

This in turn forces the existing bounded-multiplier prime correlation with
\(\delta=\rho/2\).  Conversely, the independently reviewed fixed-band
transfer gives

\[
M_{r+1}\ge
\frac{16\delta}{25B^2\lfloor B/2\rfloor}M_r
\]

once the finitely many prime factors of the band are class-compatible.
Therefore the existence of a uniform all-cofactor hyperbolic lower flow is
quantitatively equivalent to the still-open fixed-band correlation.

The compatible cofactor set itself is infinite because it contains every
\(2^a3^b\) with \(a\ge1\), while dropping the prime indicator yields only the
upper bound \(M_{r+1}\le(\pi^2/24)M_r\).  Neither fact supplies a lower flow.

The all-cofactor route is retired only as an independent escape from that
gate.  The reduction neither proves nor refutes the correlation, positive
exponential level mass, or the Problem 1055 counterexample target.  The full
proof and the bounded non-asymptotic Jacobian record are in
`research/exact_level_hyperbolic_lower_flow/`.
