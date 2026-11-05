---
title: Cera Lucas rank-density negative edge
description: Exact Fibonacci sign density gives iterable negative edges, but fixed-d density has no cofactor-height or uniform cost control.
---

# Cera Lucas rank-density negative edge

For the Fibonacci sequence, Cera da Conceicao's rank-divisibility density
specializes at every odd prime \(q\ne5\) to

\[
\delta_F^-(q)
=\operatorname{dens}\left\{
p:q\mid\rho_F(p),\ \left(\frac5p\right)=-1
\right\}
=\frac{q}{2(q^2-1)}.
\]

The density is positive. For every prime in this negative component,
\(\rho_F(p)\mid p+1\), so

\[
p+1=mq,\qquad m\in2\mathbb Z_{\ge1},\qquad p>q.
\]

The child is again a negative-symbol prime. Recursive choice from \(q=7\)
therefore gives an unconditional infinite increasing chain with exact-class
height increasing at least once per edge.

This is a qualitative construction, not a fixed-exponential one. The printed
finite-\(x\) asymptotic counts the unsplit fixed-\(d\) set and starts at
\(x>\exp(Bd^{40})\). The negative component is assigned a Dirichlet density
without a separate error term or least-prime cutoff. More importantly, the
source does not stratify by the cofactor \(m=(p+1)/q\), the exact classes of
its prime factors, or the height gain

\[
h(p)-h(q)
=1+\max\left(
0,\max_{\substack{s\mid m\\s\ {\rm prime}\\s\ge5}}h(s)-h(q)
\right).
\]

For every finite block, multiplier costs and height gains telescope to

\[
\sum\log m
=\log\frac{q_{\rm end}}{q_{\rm start}}
 \sum\log\left(1+\frac1q\right),
\qquad
\sum\Delta h=h(q_{\rm end})-h(q_{\rm start}).
\]

Thus grouping edges cannot replace the missing endpoint
size-versus-height theorem. Even optimistically granting a selected-child
bound of shape \(\exp(O(q^{40}))\) does not yield a uniform ratio: the
abstract recurrence \(x_{n+1}=2x_n^2-1\) has the same edge and unit-gain
identities, eventually lies below every such envelope, and has multiplier
cost tending to infinity on every tail block. Its labels are not asserted
prime; it is only an insufficiency model for the retained inequalities.

The Cera v3 specialization is therefore exhausted as a route to a fixed
exponential exact-class family. A sign-specific uniform least-prime theorem
or a joint cofactor/exact-height distribution would be genuinely new input.
