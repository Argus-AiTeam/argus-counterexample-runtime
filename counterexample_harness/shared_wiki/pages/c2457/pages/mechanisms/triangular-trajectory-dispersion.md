---
title: Triangular trajectory dispersion
description: Explicit complete-history count and exact unit-diagonal obstruction for uncentered one-copy factor dispersion.
---

For fixed \(C\geq1\) and height \(r\), every exact-anchor structural history
of length at most \(r\) and endpoint at most \(C^r\) lies in an envelope of
size
\[
9rC^{2r}
\cdot\bigl(\lfloor\log_2(C^r+1)\rfloor+1\bigr)
\cdot\bigl(\lfloor\log_3(C^r+1)\rfloor+1\bigr),
\]
where \(A_C=1+\log_2(2C)\) and \(B_C=1+\log_3(2C)\) give the pure
exponential bound
\[
9A_CB_C(8C^2)^r.
\]
This includes every multiplier word and endpoint case but contains no
primality saving.

The uncentered one-copy factor dispersion has an exact arbitrary-height
obstruction. At \(C=12\), for every \(r\geq4\) and
\(1\leq k\leq\lfloor r/2\rfloor-1\), take
\[
q_1=5,\qquad m_1=5\cdot6^{2k},\qquad
m_2=\cdots=m_{r-1}=2.
\]
These histories are structurally admissible, have endpoint below \(12^r\),
and have earliest composite
\[
q_2=(5\cdot6^k-1)(5\cdot6^k+1).
\]
The selected balanced factor pairs form a partial permutation matrix
\(A_r\), so
\[
A_rA_r^{\mathsf T}=I,\qquad
\|A_r\|_{2\to2}=1,\qquad
\|A_r\|_{\mathrm{HS}}^2=\lfloor r/2\rfloor-1.
\]
The all-ones bilinear count saturates Cauchy--Schwarz on this matrix.
Splitting the multiplier words gives singleton norm-one blocks; merging them
leaves the same full diagonal. Iterated multilinear Cauchy--Schwarz also
retains one unit full-diagonal term per atom.

Therefore a mechanism that represents each first-composite history once,
applies Cauchy--Schwarz or \(TT^\ast\), and adds nonnegative block envelopes
cannot produce an additive error below one. This does not rule out exact
removal of the algebraic family or a centered arithmetic dispersion theorem
that evaluates off-diagonal cancellation before nonnegative bounding.
