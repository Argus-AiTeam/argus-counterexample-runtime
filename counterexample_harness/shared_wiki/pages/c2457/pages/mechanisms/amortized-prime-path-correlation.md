---
title: "Amortized prime-path correlation"
description: "The complete all-even-word von Mangoldt-squarefree identity is exact, but bounded-divisor main terms lose the moving prime diagonal or retain an indistinguishable two-prime parity contribution."
---

# Amortized prime-path correlation

For \(D=4\), an odd-start trajectory is parameterized by

\[
P_0(n)=n,\qquad P_j(n)=m_jP_{j-1}(n)-1,
\]

where \(n\ge3\) is odd, every \(m_j\) is even, and
\(P_{L-1}(n)\le4^L\).  Writing
\(P_j=A_jn-B_j\), the exact start endpoint for a word is

\[
Y_{\mathbf m,L}
=\left\lfloor\frac{4^L+B_{L-1}}{A_{L-1}}\right\rfloor.
\]

Summing over every word with \(Y_{\mathbf m,L}\ge3\) is finite and complete.
The trajectory recovers its unique word from
\(m_j=(P_j+1)/P_{j-1}\), so there is no duplicate count.

The prime-only weighted count is

\[
W_L(4)=
\sum_{\mathbf m,n}\prod_{j=0}^{L-1}
\Lambda(P_j(n))\mu^2(P_j(n)).
\]

The identities

\[
\Lambda(N)=-\sum_{d\mid N}\mu(d)\log d,
\qquad
\mu^2(N)=\sum_{e^2\mid N}\mu(e)
\]

give one exact joint divisor expansion.  They also remove every prime power
exactly.  No marginal transition estimate is multiplied.

The range obstruction is intrinsic to a bounded-divisor use of this
identity.  For a prime value \(P_j\), the only nonzero von Mangoldt term is
the moving full divisor \(d_j=P_j\), and \(e_j=1\).  A proper-divisor or
smaller cutoff therefore deletes the prime contribution itself.

Reindexing as

\[
\Lambda(N)=\sum_{d\mid N}\mu(d)\log(N/d)
\]

moves the prime contribution to \(d=1\), but exposes the parity ambiguity.
For any fixed integer cutoff \(R\ge2\), choose distinct primes \(p,q>R\).
The retained sum gives \(\log p\) at \(p\) and \(\log(pq)\) at \(pq\),
although the exact von Mangoldt values are \(\log p\) and \(0\).  Such
\(p,q\) can be constructed by the Euclid products \(M_R+1\) and \(M_Rp+1\),
and the corresponding starts lie in every sufficiently high all-two fiber
because its exact start range is \(2^{L+1}\).

There are explicit fiberwise witnesses at every \(L\ge3\).  In the all-two fiber,
\(n=15\) has endpoint at most \(4^L\) and

\[
\log3+\log5-\log15=0.
\]

The admitted start \(n=9\) has

\[
\sum_{e^2\mid9}\mu(e)=1-1=0.
\]

These identities prove cancellation in the displayed fibers only.  They do
not compare the aggregate retained sum with the aggregate absolute tail.

A separate complete-domain argument freezes all square-divisor variables
and retains exactly \(d_j\le R(L)\) at every coordinate.  Since every
endpoint is at least \(2^L+1\), every rule \(1\le R(L)\le2^L\) omits the
endpoint prime diagonal.  A nonzero retained state must then have a
squarefree composite endpoint, so its full prime weight is zero and its
omitted signed terms cancel its retained terms state by state.  Therefore

\[
\lvert M_L(R)\rvert\le E_L^{\mathrm{abs}}(R)
\]

for every \(L\) and every cutoff in that class.  The same reasoning covers
an all-coordinate proper-divisor truncation with arbitrary scalar cutoff.
It does not cover \(R(L)>2^L\), a reorganization of square-divisor
cancellation, or a full-range nonabsolute estimate.  Positivity of the
complete count for unbounded \(L\) remains open.  The identity and fiber
replay are in `research/amortized_prime_path_correlation/`; the aggregate
theorem and replay are in
`research/amortized_prime_path_aggregate_comparison/`.
