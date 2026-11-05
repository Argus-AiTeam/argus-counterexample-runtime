---
title: Torsion-translated Gaussian CM denominator parity
description: A nonzero rational two-torsion translate gives exact reduction order 2q at a primitive prime, but the source-faithful full denominator ideal has only even valuations and cannot force an inert output by quadratic-character parity.
---

# Torsion-translated Gaussian CM denominator parity

On
\[
E:y^2=x^3-25x,\qquad P=(25/4,75/8),
\]
fix any rule taking prime indices to one of the three nonzero rational
two-torsion points. If a good prime \(p\) is primitive for the translated
term \(B_q(P,T)\), then
\[
[q]\widetilde P=\widetilde T.
\]
For odd prime \(q\), primitiveness excludes reduction order \(2\), so
\(\widetilde P\) has exact order \(2q\). An inert output therefore satisfies
\[
p\equiv3\pmod4,\qquad q\mid p+1.
\]
Translation supplies the desired conditional negative edge.

It does not supply the inert prime. Verzobio defines \(B_q(P,T)\) as the
full denominator ideal of \(x([q]P+T)\). Whenever \(v_p(x)=a<0\), the curve
equation gives
\[
2v_p(y)=3a,
\]
so \(a\) is even. Hence every exponent in the full denominator ideal is
even. Any primitive part formed by deleting prime supports while retaining
source exponents is a square, and its \((-1)\)-character is \(+1\), not
\(-1\). This remains true for all three rational two-torsion choices.

`arXiv:2010.10175v2` proves ordinary primitive-divisor existence for all but
finitely many terms of a fixed torsion translate, but gives no output
Frobenius class, explicit onset, or selected-prime size. The effective
theorem in `arXiv:2001.02987v3` applies to the unshifted scalar denominator
of \(x(nP)\); its constant bounds the index, not an individual primitive
prime.

Thus the full-denominator odd-valuation mechanism is unavailable. This does
not rule out inert primitive primes occurring with even source exponent or
a new theorem for a separately defined square-root denominator. It supplies
neither \(p\leq Aq\) nor recursive fixed-exponential closure.
