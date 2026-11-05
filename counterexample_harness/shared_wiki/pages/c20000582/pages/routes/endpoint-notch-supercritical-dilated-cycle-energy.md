---
title: Endpoint-notch supercritical dilated-cycle energy boundary
description: Sharp horizontal-profile cancellation gives a uniform vanishing bound for the actual physical energy of the complete three-block Green class at the first K_m-squared dilation.
---

# Endpoint-notch supercritical dilated-cycle energy boundary

Let
\[
K_m=\frac{m(m+1)}2-3,\qquad
\ell_m=\lceil\log_2(K_m^2)\rceil,\qquad
t_m=2^{\ell_m}+1.
\]
Use the \(t_m\)-dilated alternating six-cycle, every integer root in the
positive-density box
\[
|U|,|V|\leq h_m/64,\qquad |C|\leq(h_m/64)^2,
\]
and every mean-zero three-block coefficient with arbitrary block origins.
The exact collected demand is genuine, nonzero, bank-annihilating, and
has positive-density quadratic source mass for every \(m\geq7\).

The coarse critical-dilation estimate loses decay at
\(t_m\asymp K_m^2\).  The decisive replacement uses the reviewed sharp
horizontal-profile bounds.  With \(\sigma_m=1-1/m\),
\[
\sqrt{H_m(r^2)}
\geq\frac{r^{\sigma_m}}{6(m+1)},\qquad
\sqrt{H_m(t_m^2)}
\leq2\lceil\sqrt m\rceil t_m^{\sigma_m}.
\]
The exact phase-cut sum is
\[
\sum_j\min\{1,2^j/t_m\}2^{-j\sigma_m}
<(\ell_m+5)t_m^{-\sigma_m}.
\]
Thus the cycle transportation factor \(t_m^{\sigma_m}\) cancels the
Green-normalization factor exactly, uniformly over every phase member
and origin:
\[
{\cal E}_m(f)\leq
\min\left\{1,
\frac{2048\lceil\sqrt m\rceil(m+1)(\ell_m+5)}
{3K_m}\right\}.
\]

Applying the reviewed complete overlap comparison to the same
complete-pair McShane extension gives the actual physical central
functional
\[
\begin{aligned}
{\cal V}_m(f)\leq \min\bigg\{1,\,
&\frac{4096\lceil\sqrt m\rceil(m+1)(\ell_m+5)}
{3K_m}\\
&+\frac{147456}{h_m}
+\frac{339738624}{\lfloor\sqrt m\rfloor}\bigg\}
\longrightarrow0.
\end{aligned}
\]
Both generators, every dyadic scale, genuine word-ball basepoints,
repeated and boundary incidences, exact \(H_m,C_m,\Phi_m\) denominators,
and the single \(2K_m|I_m|\) normalization are retained.

This exhausts the first \(K_m^2\)-scale supercritical three-block Green
class.  It does not prove unrestricted scalar concentration, cover larger
dilations or other root waves, or construct the campaign counterexample.
The proof, exact replay, and typed rational optimization audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/supercritical_dilated_cycle_energy/`.
