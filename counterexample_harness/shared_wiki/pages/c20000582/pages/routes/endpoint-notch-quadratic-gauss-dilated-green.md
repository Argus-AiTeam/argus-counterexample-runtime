---
title: Endpoint-notch quadratic Gauss-phase dilated Green boundary
description: The collected growing-period quadratic chirp has exact fibre telescoping and uniformly vanishing physical energy despite its nonzero raw periodic mean.
---

# Endpoint-notch quadratic Gauss-phase dilated Green boundary

For
\[
P_m=2^{\lceil\log_2(K_m^2)\rceil},\qquad t_m=P_m+1,
\]
retain the genuine full-lattice root box and the \(t_m\)-dilated alternating
six-cycle, and weight each root by
\[
\gamma_{m,\zeta}(X(U,V,C))
=\operatorname{Re}\!\left(
\zeta\exp(2\pi i(U^2+V^2)/P_m)\right),\qquad \zeta\ne0.
\]
The exact six-indicator collection has a positive-density interior source,
zero total mass, and both bank cancellations.

The raw quadratic chirp has true coordinate period \(P_m/2\), not \(P_m\),
and its complete \(P_m\)-square mean is
\(-2P_m\operatorname{Im}\zeta\). No periodic mean is subtracted. Instead,
the six-cycle collection telescopes on every genuine horizontal fibre:
every incomplete collected sum has modulus at most \(8|\zeta|\). Below
the period, every dyadic level-set cut is counted by all four endpoint
roles; at and above the period, only explicitly counted horizontal,
central-shear, and box-exit incidences remain.

After the exact full-profile Green solve, complete-pair normalization, and
McShane extension,
\[
{\cal V}_m(f_{m,\zeta})\le
\min\left\{1,\,
2E_m^\star+\frac{147456}{h_m}
+\frac{339738624}{\lfloor\sqrt m\rfloor}\right\},
\]
where
\[
E_m^\star=
\frac{3072}{125}\frac{(m+1)\sqrt m}{K_m}
\,12\left(1+(P_m/2)^{-(1-1/m)}\right)
\left(16+23500t_ms_m^{-1/m}\right).
\]
This bound tends to zero uniformly over every nonzero \(\zeta\). It
exhausts this growing-period quadratic Gauss-phase class only; it does not
prove unrestricted scalar concentration and does not produce the campaign
counterexample.

The theorem, exact replay, and typed Jacobian record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/quadratic_gauss_dilated_green/`.
