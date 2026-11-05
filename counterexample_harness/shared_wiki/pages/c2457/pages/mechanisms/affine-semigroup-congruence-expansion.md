---
title: "Affine-semigroup congruence expansion"
description: "Exact chain matrices and endpoint-bounded word domain, with the source-level obstruction to applying fixed special-affine or Schottky congruence expansion."
---

# Affine-semigroup congruence expansion

For a multiplier \(m\geq2\), the chain step is

\[
T_m(x)=mx-1,\qquad
H_m=\begin{pmatrix}m&-1\\0&1\end{pmatrix}.
\]

For a word \(m_1,\ldots,m_{L-1}\), define

\[
A_0=1,\ B_0=0,\qquad
A_t=m_tA_{t-1},\ B_t=m_tB_{t-1}+1.
\]

Then

\[
H_{m_t}\cdots H_{m_1}
=\begin{pmatrix}A_t&-B_t\\0&1\end{pmatrix},
\qquad q_{t+1}=A_tq_1-B_t.
\]

At endpoint cap \(X=C^L\), the complete ambient domain is

\[
\mathcal D_{C,L}
=\{(n,\boldsymbol m):n\geq2,\ m_t\geq2,\
A_{L-1}n-B_{L-1}\leq X\}.
\]

Equivalently, a word occurs exactly when
\(2A_{L-1}-B_{L-1}\leq X\), and its starts are exactly

\[
2\leq n\leq
\left\lfloor\frac{X+B_{L-1}}{A_{L-1}}\right\rfloor.
\]

The exact chain count retains the prime indicator of every one of the
\(L\) affine forms.  A local divisor row must also retain the exception
\(F_t(n)=\ell\): divisibility by \(\ell\) proves compositeness only when
the value is not the prime \(\ell\) itself.

## Source-admission boundary

Lindenstrauss--Varju, arXiv:1409.3564v2, Theorems 1--2, works on
\(\mathbb F_p^d\rtimes\mathrm{SL}_d(\mathbb F_p)\).  In the natural
one-dimensional action the linear part is \(m\), but
\(\mathrm{SL}_1(\mathbb F_p)=\{1\}\).  A determinant-compensated
two-dimensional lift for \(p\nmid m\) preserves a proper subspace and
has diagonal linear part, so the projected \(\mathrm{SL}_2\) walk has
no spectral gap.  It also omits multipliers divisible by \(p\).
The source's integral gap input uses a previously fixed finite
Zariski-dense generator set, and its constants retain dependence on
the fixed dimension.

Magee--Oh--Winter, arXiv:1601.03705v3, Theorems 1 and 11, fixes a
Schottky semigroup in \(\mathrm{SL}_2(\mathbb Z)\).  Here
\(\det H_m=m\), so the natural matrices are not in that ambient group.
They also all fix \(\infty\), which directly contradicts the paper's
Schottky interval condition: the exterior of each compact
\(J_i\subset\mathbb R\) contains \(\infty\), but it must map into a
compact interval in \(\mathbb R\).  The paper's continued-fraction
variant instead fixes a finite alphabet and uses a different Mobius
action.

Thus neither cited theorem admits the complete variable-multiplier
chain action.  Fixed-alphabet or endpoint-only mixing cannot be
substituted: it omits words or loses the simultaneous primality of the
internal prefixes.  This resolves only admission of these two source
mechanisms.  It does not settle the growing-dimensional affine-prime
correlation left open by the three-block feedback analysis, and it
does not prove universal chain exclusion.
