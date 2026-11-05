---
title: Complete Fibonacci tree potential
description: Exact path telescoping, factor multiplicities, and the missing global frontier drift estimate.
---

# Complete Fibonacci tree potential

For a reachable negative-symbol prime \(q\), the complete negative child
multiset contains \(v_p(F_q)\) copies of every prime
\(p\mid F_q\) with \((5/p)=-1\). Its total multiplicity is positive and odd.
Every retained child is primitive at index \(q\), has unique parent \(q\) by
its Fibonacci rank, and satisfies

\[
p+1=mq,\qquad m\in2\mathbb Z_{\ge1}.
\]

Parallel factor occurrences do not create distinct arithmetic continuations.

For every root-to-node path \(7=q_0\to\cdots\to q_n\),

\[
\sum_i\log\frac{q_i+1}{q_{i-1}}
=\log\frac{q_n}{7}
 +\sum_i\log\left(1+\frac1{q_i}\right),
\]

and the final sum lies strictly between zero and \(1/6\). Exact height gains
also telescope:

\[
\sum_i(h(q_i)-h(q_{i-1}))=h(q_n)-1.
\]

Therefore a path potential

\[
\sum_i(c_i-A g_i)
\]

is endpoint \(\log q_n-Ah(q_n)\) plus a uniformly bounded explicit
correction. Explicit low-potential nodes at unbounded depths are equivalent,
up to explicit constants, to a fixed-exponential endpoint family inside this
tree. The potential is a sound reformulation and extraction mechanism, not
an independent estimate.

The complete factor product gives only an upper bound on the geometric mean
of child sizes. Without a growing lower bound for negative-factor
multiplicity, it does not force a cheap child. The cofactor recurrence gives
gain at least one, but no reviewed theorem makes that gain comparable to a
large multiplier. Consequently no normalized global frontier flow currently
has a proved uniform drift bound. Any successful continuation needs a new
Fibonacci-specific theorem controlling branching, selected factor size,
cofactor height, or a genuinely collective frontier quantity.

An exact one-child integer model with multipliers \(2(n+2)^2\) satisfies the
retained edge and formal cofactor-height identities while its potential
diverges for every fixed \(A\). Its labels are not prime or Fibonacci
divisors; it establishes only that the local identities are insufficient,
not that the actual tree theorem is false.
