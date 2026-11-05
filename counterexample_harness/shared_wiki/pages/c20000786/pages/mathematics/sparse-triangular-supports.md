---
title: Sparse triangular Cartier-Manin supports
description: Exact structural boundary for the reviewed 45 degree-five and degree-six sparse supports.
---

For a support \(T\), let \(a=\min T\) and
\(d=\gcd\{e-a:e\in T\}\). Writing \(f(x)=x^a g(x^d)\) shows that an eventual
Cartier-Manin entry is structurally present exactly when its target exponent
is congruent to \(an\) modulo \(d\). Thus the 36 supports with \(d=1\) are
eventually structurally dense.

Exactly nine supports have \(d>1\):

\[
\{0,5\},\{1,5\},\{1,3,5\},\{0,6\},\{1,6\},
\{0,2,6\},\{0,3,6\},\{0,4,6\},\{0,2,4,6\}.
\]

The four binomials have previously proved infinite all-zero prime
progressions. The other five are geometrically bielliptic: the even supports
have the two quotients \(Y^2=g(u)\) and \(V^2=u g(u)\), while
\(\{0,3,6\}\) and \(\{1,3,5\}\) have an explicit reciprocal involution.
Consequently no nonsplit survivor remains in this structural class.

The proof and exact residue tables are in
`research/TRIANGULAR_SPARSE_BOUNDARY.md`; the rerunnable 45-record
classification is `research/evidence/triangular-support-classification.json`.
