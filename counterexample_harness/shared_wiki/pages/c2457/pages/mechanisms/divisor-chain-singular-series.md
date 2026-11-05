---
title: Divisor-chain singular-series normalization
description: Good-prime shift equivalence, exact first-multiplier fibers, and the universal prime-2 obstruction to direct Kuperberg averaging.
---

# Divisor-chain singular-series normalization

For an even multiplier word, write

\[
P_i(n)=A_i n-B_i,\qquad
A_i=m_iA_{i-1},\quad B_i=m_iB_{i-1}+1,
\]

and let \(A=A_{K-1}\). The integral divisor-chain shifts

\[
H_i=\frac{AB_i}{A_i}
\]

satisfy

\[
\frac{A}{A_i}P_i(n)=An-H_i,\qquad
H_i-H_{i-1}=\frac{A}{A_i}.
\]

For every prime \(p\nmid A\), multiplication by \(A^{-1}\) shows that
the affine tuple and the shift set have equal local root counts. This
equivalence does not extend to primes dividing \(A\).

Every even word has affine root count one modulo 2: \(P_0(n)=n\), while
all later forms are constant 1 modulo 2. In contrast, all normalized
shifts except the last are even and the last shift is odd. The shift set
therefore occupies both classes modulo 2, so its standard singular
series is zero. The affine modulo-2 factor is \(2^{K-1}\).

The all-two word is primitive and affine-admissible at every height. At
odd \(p\), its root count is
\(\min(K,\operatorname{ord}_p(2))\leq p-1\). Thus the prime-2 mismatch
persists on a genuine admissible all-height subfamily, not only on words
already excluded by a local obstruction.

The normalized shift set determines \(m_2,\ldots,m_{K-1}\), but not
\(m_1\). If \(D=\prod_{i=2}^{K-1}m_i\), then under
\(Ar<C^r\) the exact first-multiplier fiber has size

\[
\left\lfloor\frac{C^r-1}{2Dr}\right\rfloor.
\]

Any future average over normalized shift sets must retain this
multiplicity and the exact endpoint floor
\(\lfloor(C^r+B)/A\rfloor\).

The recurrence also does not guarantee primitivity. If
\(\gcd(A_i,B_i)>1\), then \(P_i(n)\) is a proper composite multiple for
every \(n\geq2\), so such words are removed exactly before applying a
prime-tuple estimate.

## Source support boundary

Kuperberg `arXiv:2210.09775v2`, Theorem 1.2, bounds sums of the full
standard shift singular series with no relative restriction on set size
and shift height. It cannot directly dominate these affine singular
series because every normalized even-word term is zero at \(p=2\).

Theorem 1.8 concerns additive prime shifts and requires moment order
\(o((\log x)^{1/4})\). A divisor-chain suffix has \(K\) proportional to
the height \(r\), while its available start scale has
\(\log x=O_C(r)\). The source range therefore fails, and the scaled
values \((A/A_i)P_i(n)\) are composite multiples rather than additive
prime shifts.

This rules out only the direct Kuperberg normalization transfer. An
independently proved odd-prime-only weighted average is not excluded,
and the universal fixed-\(C\) prime-chain zero count remains open.
