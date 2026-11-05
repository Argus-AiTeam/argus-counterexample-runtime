---
title: Length-two U(sl3) boundary on the AK family in Ver_7^+
description: Exact 15-dimensional transfer closure and scalar-one theorem for both F7 square classes on every AK(n).
---

# Length-two \(U(\mathfrak{sl}_3)\) boundary on the AK family

The two reviewed 63-dimensional internal enveloping Hopf objects on
Newton's \(L_3\oplus L_5\) Lie algebra, represented by the two nonzero
square classes \(t=1,3\) in \(\mathbb F_7\), both give
\[
\overline\Omega_{U_t}(\operatorname{AK}(n))=1
\qquad\text{for every }n\geq2.
\]
Their standard-presentation scalar is also one. Thus neither object
separates any member of the AK family.

The replay uses the reviewed corrected PBW tables and never rebuilds
them. A local state records a variable-block product and its
unexpanded coproduct tail, giving \(63^2=3969\) coordinates. The
paired operator \(T=A_+\otimes A_-\) acts on
\(3969^2=15{,}752{,}961\) joint coordinates, and a fixed exact boundary
functional consumes the extra negative \(b\)-letter and the complete
braid relator.

For each square class, the reachable cyclic Krylov module has exact
dimension 15 and minimal polynomial
\[
(z-1)^{15}.
\]
The verifier proves \((T-I)^{15}v_0=0\) coordinatewise and proves
independence of \(v_0,\ldots,T^{14}v_0\). It also directly checks
\(T^{49}v_0=v_0\).

Every required initial value \(q_2,\ldots,q_{16}\) is one in two exact
schedules. The transfer uses right-comb coproduct tails. The
independent schedule starts from fresh integrals, traverses the
complete braid relator right-to-left with left-comb splitting, then
contracts the complete reversed first relator
\(b^{-(n+1)}a^n\). Both schedules reproduce the already reviewed
AK(3) value, and the opposite schedule reproduces its reviewed
intermediate state counts.

The typed Jacobian run fits an order-one recurrence only to the
supplied 30-term scalar prefix and is retained solely as a cross-check.
The all-parameter result comes from the exact vector recurrence and
the independently contracted 15-value window.

The detailed theorem, replay contract, and bounded scope are in
`research/experiments/verlinde7-sl3-enveloping-ak-family/BOUNDARY.md`;
the machine-readable result is `certificate.json`. This closes only
these two Hopf objects on the AK family and does not settle C1187.
