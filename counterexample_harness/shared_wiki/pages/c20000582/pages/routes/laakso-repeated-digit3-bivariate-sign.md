---
title: Repeated-digit-3 bivariate margin-resolvent boundary
description: Exact schedule-complete formal resolvent, fixed-dimensional profile-rank exclusion, and a positive phase-five completion.
---

For the canonical repeated-digit-3 contacts, let
\[
N_j=2\cdot18^j,\qquad m=k+r+2,
\]
and let \(F_k\) include `accumulated_direct` and all four ordered root
channels.  With \(T(H)=6g(H\circ\zeta)\), the complete margin is
\[
M_{k,r}=6^{k+2}\sum_{j=0}^{m}
96^{j-m}[z^{N_j}]T^rF_k.
\]

The sparse-clock transform
\[
\mathscr K_tH=\sum_{j\ge0}[z^{N_j}]Ht^j
\]
gives the exact identity
\[
\sum_{k\ge1,r\ge0}M_{k,r}X^kY^r
=\operatorname{CT}_t
\frac{36t^{-2}}{1-t/96}\,
\mathbf1^{\mathsf T}\mathscr K_t
\mathbf Z(6X/t,Y/t),
\]
where
\[
\mathbf Z(x,y)=
(I-y\mathbf T)^{-1}\sum_{k\ge1}x^k\mathbf f_k.
\]
This is a coefficientwise regular, infinite-dimensional formal operator
resolvent.  It retains every scheduled clock and provenance channel, but
it is not an ordinary rational bivariate generating function and confers
no sign.

The reviewed phase-\(m\) profile rank is exactly \(m-2\).  Therefore no
fixed finite-dimensional linear realization can faithfully contain all
complete phase-aligned profiles.  The separately reviewed distinct-degree
old-gate tower also excludes fixed-dimensional state-independent
polynomial-test pullbacks.  Neither result rules out a scalar rational
generating function, a nonlinear quotient, or a phase-dependent state.

The exact first-clock normalization is
\[
M_{k,r}=16^{-m}\sum_{j=0}^m96^jb_{k,r,j},
\]
with \(b_{k,0,0}=107/36\) and \(b_{k,r,0}=32/9\) for \(r\ge1\).
The available absolute tail estimate scales as \(3^{-m}\), not
\(16^{-m}\), so it cannot absorb this reserve uniformly.

The previously missing phase-five cell has the rigorous outward value
\[
M_{2,1}
=[4.6759977251225280967\cdot10^{-5}
\mathbin{+/-}2.85\cdot10^{-25}]>0
\]
at old-scaled contact \((980,972,988)\).  Thus all phase-five cells are
positive, but this finite diagonal does not decide the family.  No exact
negative contact and no all-\((k,r)\) nonnegativity theorem is known.
