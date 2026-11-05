---
title: Reverse cyclotomic search boundary
description: Exact production-graph facts and the finite-inversion limit of cycle-first-reverse-v1.
---

# Reverse cyclotomic search boundary

For an odd perfect candidate

\[
N=\prod_{i=0}^{9}q_i^{a_i},\qquad
\prod_i\sigma(q_i^{a_i})=2\prod_iq_i^{a_i},
\]

orient a production edge from rank \(i\) to rank \(j\) when
\(q_j\mid\sigma(q_i^{a_i})\). Since
\(\sigma(q_j^{a_j})\equiv1\pmod{q_j}\), self-production is impossible.
Taking \(q_j\)-adic valuations of the exact perfectness identity shows that
the total valuation supplied by other components is exactly \(a_j>0\).
Every vertex therefore has an incoming edge from another vertex, so the
ten-vertex graph contains a directed cycle of length 2 through 10. There are
1,112,073 normalized labeled directed cycle templates in that range.

For exponents 2 and 4, the production relations are
\(\Phi_3(p)=p^2+p+1\) and
\(\Phi_5(p)=p^4+p^3+p^2+p+1\). Target 3 is exceptional for exponent 2:

\[
3\mid\Phi_3(p)\quad\Longleftrightarrow\quad p\equiv1\pmod3.
\]

This inverse prime family is unbounded. An elementary Euclid argument proves
it: if \(S\) were the complete finite set of primes congruent to 1 modulo 3,
let \(A=3\prod_{s\in S}s\) and take a prime divisor \(q\) of
\(A^2+A+1\). Then \(q\ne3\), \(A\) has order 3 modulo \(q\), hence
\(q\equiv1\pmod3\), while \(A^2+A+1\equiv1\pmod s\) for every \(s\in S\).
Thus \(q\notin S\), a contradiction.

The exact rational abundancy bound used in this campaign bounds the next
ordered prime after its complete prefix is assigned. The unbounded inverse
family therefore cannot be enumerated before an arbitrary producer rank's
intervening prefix is known. It does **not** follow that cycle-first synthesis
fails: the edge is optional at that stage and can remain a deferred obligation
until both endpoints have finite prefix bounds. The earlier
`cycle-first-reverse-v1` obstruction exhausted zero signatures and does not
rule out this deferred construction.

`cycle-first-reverse-v2` freezes the complete cycle-template family first,
represents unresolved edges compactly, assigns ranks under exact prefix bounds,
and enforces each edge when both endpoints become known. Exact sigma
factorization simultaneously maintains each target's valuation budget. When
nine of the ten tuple primes are already fixed, a new next prime would fill the
last available slot; its sigma value can then be synthesized exactly from
products of the nine known primes within their remaining valuation budgets,
rather than scanning an arbitrary numeric range.

The pinned factor operation independently certifies the representative edge
\(31\to3\) through \(\Phi_3(31)=993=3\cdot331\).

The completed immutable replay processed 7,836,201 exact prefixes across all
4,660 new signatures. Its factor cache contains exactly 13,158
`integer.factor.certified_compute` COMPLETE outputs with checked Pratt
certificates; 3,578 were reused from the reviewed boundary and 9,580 were new.
Every cache entry was consumed, no input exceeded 29 digits, and no UNKNOWN or
adapter error occurred. Combining this result with the reviewed 360 signatures
exhausts exactly 5,020 exponent assignments:

- exactly ten distinct odd primes;
- special exponent 1;
- every nonspecial exponent in \(\{2,4\}\);
- at least two exponent-4 components.

No odd-perfect witness occurs in that class. This is a bounded negative result,
not a nonexistence proof for odd perfect numbers.
