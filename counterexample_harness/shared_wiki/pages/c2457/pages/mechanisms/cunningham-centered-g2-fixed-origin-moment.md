---
title: Fixed-origin G-squared moment boundaries
description: The centered CRT high-modulus L1 tail has factorial-scale mass, while Nair's favorable Euler product lacks uniform diagonal constants; equation (45) remains open.
---

# Fixed-origin G-squared moment boundaries

For
\[
 G^2(n)=\prod_{p\in{\cal P}_h(z_h)}
 \left(1-\frac34{\bf1}_{R_{p,h}}(n)\right),\qquad
 A_h=\prod_p\left(1-\frac{3h}{4p}\right),
\]
the normalized centered expansion is
\[
 \frac{G^2(n)}{A_h}
 =
 \sum_{D\subseteq{\cal P}_h}
 (-1)^{|D|}
 \prod_{p\in D}
 \frac{3/4}{1-3h/(4p)}
 \left({\bf1}_{R_{p,h}}(n)-\frac hp\right).
\]
This identity retains the target origin and every selected root hit.

The complete-period \(L^1\) activity of a prime is
\[
 \theta_p=
 2\frac{3/4}{1-3h/(4p)}
 \frac hp\left(1-\frac hp\right).
\]
For selected \(p\ge2h\),
\[
 \frac34\frac hp\leq\theta_p\leq\frac35,\qquad
 \frac{\theta_p}{1+\theta_p}\geq\frac{15}{32}\frac hp.
\]
Using the reviewed reciprocal-prime estimate, an activity-weighted support
contains \(\asymp h\log h\) such primes. Any support with product at most
\(M=X_h(C)-(\lceil h/2\rceil-1)\) contains only
\(O_C(h/\log h)\) primes at least \(2h\). Chebyshev's inequality therefore
gives
\[
 \frac{{\cal V}_{h,\leq M}}{{\cal V}_h}
 =O_C\!\left(\frac1{h\log h}\right),\qquad
 \log{\cal V}_{h,>M}
 \geq\left(\frac{15}{32}+o(1)\right)h\log h.
\]
Thus a moduluswise complete-period \(L^1\) closure of the high-modulus tail
has a factorial-scale loss. Exact signed resummation avoids that loss but
returns \(G^2/A_h\) minus the low-modulus block pointwise, so it supplies no
new fixed-origin estimate by itself.

There is also an exact primary-source near match. Define
\[
 P_h(T)=\prod_{j=1}^h(2^jT+1)
\]
and a multiplicative function taking \(1/4\) on selected prime powers and
\(1\) elsewhere. Its value at \(P_h(n)\) is exactly \(G^2(n)\). In Nair's
1992 short-interval theorem, every selected explicit Euler factor obeys
\[
 (1-h/p)e^{h/(4p)}\leq1-\frac{3h}{4p},
\]
and every unselected factor is at most one. The displayed source product is
therefore at most \(A_h\).

The source is fixed-degree, however. Its range constant and implied constant
may depend on the degree and discriminantal factor, and its norm condition
contains
\[
 \|P_h\|\geq2^{h(h+1)/2}
\]
while \(X_h(C)=\exp(\Theta_C(h))\). No published diagonal dependence from
that theorem yields \(\log E_C(h)=o(h\log h)\).

Both statements are route boundaries, not a refutation of the true moment.
Equation (45), the target RMS estimate, and the multiplier-two zero count
remain open. A continuation must introduce a genuinely new fixed-origin
signed estimate or another source with explicit growing-degree constants.

