---
title: Cyclic-coset certificates for P_(2,2) binomial pairs
description: Exact right-coset reduction for nonzero and zero x_0 abelianization, with degree-eleven and degree-ten common multiples.
---

# Cyclic-coset certificates for P_(2,2) binomial pairs

For
\[
a=x_0^2+x_1^2,\qquad
b=x_0x_1+x_0x_3+x_2^2
\]
over \(\mathbf F_2[F]\), left normalization by \(p=x_0^2\) gives
\[
(1+\alpha)u=cv,\qquad
\alpha=p^{-1}x_1^2,
\quad c=p^{-1}b.
\]
The image of left multiplication by \(1+\alpha\) consists exactly of the
finite sums having even coefficient parity on every right coset
\(\langle\alpha\rangle g\). The implementation canonically represents each
coset using the \(x_0\)-abelianization of \(\alpha\), which is \(-2\), and
reconstructs the unique finite lift by parity along the integer
\(\alpha\)-coordinate.

`research/ring_p22/overlap_gain/cyclic_coset_positive_d11.json` stores an
exact dependency in the canonical degree-eleven positive layer. Its 48-term
right multiplier lifts to a 96-term left multiplier, and direct infinite
normal-form reduction gives the same 144-term product on both sides of
\(au=bv\). `scripts/ring_p22_cyclic_coset.py verify` regenerates the
normalization, every coset coordinate and lift interval, and the final
group-ring equality.

The common multiple rejects all eight routing templates for this coefficient
pair, including frozen templates 105166 and 105167, because it supplies a
nonempty even-incidence family and hence an actual identity-gain closed walk
for every routing choice. It does not prove or disprove amenability of \(F\),
and finite full-rank searches preceding the degree-eleven dependency have no
independent conclusion.

The same reduction now supports a cyclic generator with zero
\(x_0\)-abelianization. For the binomial mask 144,
\[
x_1^2+x_2^2=x_1^2(1+\beta),\qquad
\beta=(x_1^2)^{-1}x_2^2=((4,4),(1,1))
\]
in reduced infinite normal form. Abelianization cannot choose a coset
representative here. Instead, the exact PL action has support component
\((1/2,31/32)\) and the half-open fundamental interval
\([3/4,15/16)\). For an element \(g\), the midpoint of
\(g^{-1}(1/2,31/32)\) is moved by the unique power of \(\beta\) into that
interval. Exact rational PL evaluation then records the representative and
integer coordinate and directly verifies reconstruction.

`research/ring_p22/overlap_gain/residual-42-144/swapped_d10_kernel.json`
stores the resulting degree-ten dependency for masks 144 and 42:
\(144L=42R\), with 62 terms in \(L\) and 32 terms in \(R\).
`research/ring_p22/overlap_gain/exact_kernel_shortcuts/42-144-d10.json`
stores the directly replayed original orientation \(42R=144L\). Its explicit
`finite_cyclic_coset_parity_dependency_swapped` mechanism checks homogeneous
degree-ten support on the 32-term left input, because that is the projected
dependency before the binomial lift. This exact common multiple applies to
every routing for masks 42 and 144; the preceding degree-five through
degree-nine full-rank layers remain bounded results only.
