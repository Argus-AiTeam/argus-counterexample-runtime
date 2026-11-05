---
title: Li v2 pairwise-affine dual transfer
description: Li's bounded-cost certificate controls static reciprocal endpoint gaps, while an exact all-length constant-two family refutes a uniform superlinear multiplier-cost transfer.
---

# Li v2 pairwise-affine dual transfer

Li's `arXiv:2606.17955v2` Lemma 3.3 proves, for every external
\(n\), a pointwise upper bound on the static extremum

\[
\mathcal M(n)=
\sup_A\sum_{a\in A}\frac1{n-a},
\]

where \(A\subset[1,n)\) is pairwise coprime. Its finite prime-divisor
charges have bounded total cost, while uncharged elements remain in the
rough residual \(\mathcal U(n)\). The paper controls that residual in mean
and almost everywhere; its all-\(n\) Proposition 5.1 is still an upper bound
for the same reciprocal-distance functional.

At an affine-row endpoint the source-legal map is

\[
n=x_j,\qquad A_j=\{x_i:i<j\},\qquad
W_j=\sum_{i<j}\frac1{x_j-x_i}.
\]

This map does not contain the shifted-Jacobsthal state
\(\alpha_j=x_j^{-1}\pmod{\operatorname{rad}\prod_{i<j}x_i}\), the next
multiplier \(m_j\), or the child factorization. It therefore gives no
dependent-shift amortization.

The exact obstruction holds at every length. Set

\[
N_L=\prod_{d<L}(2^d-1),\qquad x_i=2^iN_L+1.
\]

Then all \(x_i\) are pairwise coprime, every multiplier is \(2\), and

\[
\frac1L\sum_{i<L-1}\log m_i\to\log2.
\]

Nevertheless, at every endpoint,

\[
W_j\le\frac{j}{2^{j-1}N_L},\qquad
\sum_{j<L}W_j<\frac4{N_L}.
\]

Thus the complete collection of static quantities controlled by Li is tiny
while multiplier cost remains linear. The same construction has
\(N_L\ge2^{(L-1)(L-2)/2}\), so it is not a fixed-base counterexample.
Only the direct superlinear-cost transfer is excluded; universal affine-row
and prime-chain exclusion remain open.

The all-length construction is mechanically certified by Lean theorem
`LiV2AffineDual.universal_constant_two_certificate` in
`research/li_v2_pairwise_affine_dual/lean/Main.lean`. It quantifies over every
natural \(L\ge2\) and every valid index pair, proves both endpoint-weight
bounds by an exact finite identity, and has no finite replay cap. The claim
ledger records it as `closed_kernel`; independent statement-fidelity review is
still required. The older length-80 Python replay remains only an ancillary
source, payload, and concrete-value regression check.
