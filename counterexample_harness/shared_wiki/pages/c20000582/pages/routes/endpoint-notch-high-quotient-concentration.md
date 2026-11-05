---
title: Endpoint-notch high-quotient concentration boundary
description: Sparse, affine, Green, nested-distance, parabolic-chirp, rectangle-charge, signed Haar-adjoint, guarded macrocell-vector, isolated subcell, adjacent-tile reuse, periodic collision, bounded carrier-state, uniform four-lift localization, variance-only cylinder comparison, and local quadratic-closure mechanisms are excluded; unrestricted scalar concentration remains open.
---

# Endpoint-notch high-quotient concentration boundary

Let \(f\) be a complete-pair one-Lipschitz scalar on the depth-\(m\)
endpoint-notch block, let \(b\) be a full two-bank potential with
\(\operatorname{Lip}_m(b)\leq L\), and put \(r=f-b\).  Count every frame
occurrence separately and define
\[
\delta_m(f,b)=
\frac{|\{(x,y)\in{\cal F}_m:r(y)\ne r(x)\}|}
     {2K_m|I_m|},
\qquad
\Omega_m(f,b)=\max r-\min r.
\]
With
\[
\epsilon_m=\frac{1990656}{h_m}
            +\frac{4586471424}{\sqrt m},
\]
the complete all-depth estimate is
\[
\boxed{
\sqrt{{\cal E}_m(f)}
\leq L\sqrt{\epsilon_m}
+\min\left\{
(1+L)\sqrt{\delta_m(f,b)},
\sqrt{\frac{150}{m}}\,\Omega_m(f,b)
\right\}.}
\]

The density term uses the complete-pair Lipschitz bound
\({\cal E}_m(r)\leq(1+L)^2\delta_m(f,b)\).  The range term uses every
exact profile denominator:
\[
\Delta_e\geq H_m(1)\geq m/150,
\qquad
{\cal E}_m(r)\leq150\Omega_m(f,b)^2/m.
\]
The reviewed full two-bank theorem supplies
\({\cal E}_m(b)\leq L^2\epsilon_m\), and the frame-energy triangle
inequality combines the two parts.

Every vertex is incident to at most \(4K_m\) frame occurrences, counting
all generator, scale, basepoint, and endpoint multiplicities.  Hence, if
\(r\) is constant outside \(S\),
\[
\delta_m(f,b)\leq\frac{2|S|}{|I_m|}.
\]
For a controlled bank,
\[
\boxed{
{\cal E}_m(f)\leq
\left(
\sqrt{\epsilon_m}+
\sqrt{\frac{8|S|}{|I_m|}}
\right)^2.}
\]
If \(S\) is covered by \(T_m\) translated six-point incidence cycles,
\[
{\cal E}_m(f)\leq
\left(
\sqrt{\epsilon_m}+
\sqrt{\frac{48T_m}{|I_m|}}
\right)^2.
\]
Thus finitely many or \(o(|I_m|)\) such defects cannot retain positive
normalized energy.

For the controlled quotient
\[
D_m(f)=\mathfrak q_m(f){\cal E}_m(f),
\]
the high branch \(\mathfrak q_m(f)\geq1/4\) forces, relative to every
controlled bank,
\[
\delta_m(f,b)\geq\frac{{\cal E}_m(f)}{16},
\qquad
\Omega_m(f,b)\geq
\sqrt{\frac{m{\cal E}_m(f)}{600}}.
\]
If the residual is constant off \(S\), then
\[
\frac{|S|}{|I_m|}\geq\frac{{\cal E}_m(f)}{32},
\]
and a union of six-point defects requires
\[
T_m\geq\frac{{\cal E}_m(f)|I_m|}{192}.
\]

This exactly retires sparse or sublinear replication of the reviewed
six-cycle as a positive-energy construction.  It does not establish
scalar concentration and does not construct a positive-energy family:
positive-density residuals with oscillation of order \(\sqrt m\) remain
open.

The theorem, exact complete-incidence replay, and typed Jacobian record
are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/`.

The additive signs above are essential.  The exact full two-bank scalar
\[
b_m(X(u,v,z))=\frac{u}{96R_m},\qquad f_m=b_m,
\]
has zero residual density and zero residual oscillation but positive
frame energy, because its \(e\mapsto a\) increment is nonzero.  It
therefore refutes the former multiplicative display exactly.

The next dense class is also settled.  Put
\[
\kappa_m=\frac{\lfloor\sqrt m\rfloor}{2^{20}},\qquad
r_{\alpha,\beta}(X(u,v,z))
=\frac{\kappa_m}{R_m^3}
\left(\alpha u(z-uv)+\beta vz\right),
\quad |\alpha|+|\beta|\leq1.
\]
Every such residual is complete-pair one-Lipschitz and
\[
{\cal E}_m(r_{\alpha,\beta})
\leq288(m+1)^2\,2^{-(m^2+39)}.
\]
Adding any controlled two-bank potential still gives a uniformly
vanishing explicit energy rate.  This is not a sparse failure:
\(r_{1/2,-1/2}\) is active on at least
\(1/(45\cdot2^{21})\) of all frame occurrences, has nonzero
circulation on at least \(1/(15\cdot2^{27})\) of rooted scale-cycle
occurrences, and its difference from every two-bank potential has
oscillation at least \(\sqrt m/(3\cdot2^{41})\).

Thus complete affine left-bank/right-bank products are exhausted even
after crossing the density and range gates.  Nonlinear dense
cycle-space interactions remain open, and no high-quotient theorem or
positive-energy scalar family follows from this class boundary.

## Exact unrestricted transport dual

The remaining problem can be stated without restricting \(f\) to a
subclass.  Let \(A_m\) be the normalized complete frame operator, with
every repeated occurrence kept as a separate coordinate.  For a
zero-sum demand \(q\), let
\[
\operatorname{TC}_m(q)=
\min_{P_m^{\mathsf T}\theta=q}
\sum_{\{x,y\}}\rho_m(x,y)|\theta_{xy}|
\]
be its exact transportation cost on the complete graph.  Let
\(\operatorname{TC}^{\mathcal B}_m(q)\) use the same objective but
require only
\[
J_m^{\mathsf T}P_m^{\mathsf T}\theta=J_m^{\mathsf T}q,
\]
where \(J_m\) retains every actual label in both controlled banks.

Finite-dimensional Fenchel duality followed by exact transportation LP
duality gives
\[
\boxed{
\sqrt{\zeta_m}=
\sup_{y\ne0}
\frac{
\operatorname{TC}_m(A_m^{\mathsf T}y)
-\operatorname{TC}^{\mathcal B}_m(A_m^{\mathsf T}y)}
{\|y\|_2}.}
\]
Only two suprema are commuted; no supremum is interchanged with the
controlled-bank minimum.  The fixed unit bank ball and the convention
\(\operatorname{Lip}(b)\leq\operatorname{Lip}(f)\) give the same
supremum by balanced convexity and scaling.

Consequently the decay branch is now exactly the all-depth congestion
inequality
\[
\operatorname{TC}_m(A_m^{\mathsf T}y)
-\operatorname{TC}^{\mathcal B}_m(A_m^{\mathsf T}y)
\leq \sqrt{g(m)}\,\|y\|_2
\quad\text{for every }y,
\qquad g(m)\to0.
\]
The canonical frame flow gives only the trivial bound with \(g(m)=1\).
No vanishing \(g(m)\) and no unbounded-depth positive-energy family is
proved, so the endpoint-notch route and the campaign objective remain
open.

The derivation, exact rational replay, and typed Jacobian min-cost-flow
record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/full_transport_dual/`.

### Optimal-selector boundary

A generic cycle-basis lifting has the wrong quantifiers.  If
\(s(y)\) is the number of nonzero frame occurrences, the canonical
complete-edge flow gives the exact bound
\[
0\leq
\operatorname{TC}_m(A_m^{\mathsf T}y)
-\operatorname{TC}^{\mathcal B}_m(A_m^{\mathsf T}y)
\leq
\sqrt{\frac{s(y)}{2K_m|I_m|}}\,\|y\|_2.
\]
Support on only \(L\) dyadic scales improves the last factor to
\(\sqrt{L/K_m}\).  Thus only dense, all-scale coefficient vectors can
obstruct decay.

On the other hand, a genuine translated six-cycle lies inside \(B_m\),
retains every left and right bank-label cancellation, and lies outside
all frame endpoints.  Hence there is no frame right inverse on the
whole bank annihilator.  More decisively, at \(y=0\) arbitrary
multiples of a genuine bank-cycle transport are relaxed-feasible but
need positive exact-demand restoration cost.  Therefore a uniform
bound cannot cover every relaxed representative.

Selecting an optimal or quantitatively near-optimal relaxed transport
does not by itself reduce the open problem.  For \(q=A_m^{\mathsf T}y\),
let \(R_m(y,\tau)\) be the least complete transport cost of the defect
left by a bank-visible demand whose cost is at most
\(\operatorname{TC}^{\mathcal B}_m(q)+\tau\|y\|_2\), and put
\[
\omega_m(\tau)=
\sup_{y\ne0}\frac{R_m(y,\tau)}{\|y\|_2}.
\]
The exact norm-quotient Pareto theorem gives
\[
R_m(y,\tau)=0
\iff
\Gamma_m(y)\le\tau\|y\|_2,
\]
\[
(\Gamma_m(y)-\tau\|y\|_2)_+\le R_m(y,\tau),
\qquad
\omega_m(\tau)=0
\iff
\tau\ge\sqrt{\zeta_m}.
\]
Consequently
\[
\sqrt{\zeta_m}
=\inf\{\tau:\omega_m(\tau)=0\},
\qquad
\sqrt{\zeta_m}\le\tau+\omega_m(\tau).
\]
Thus a vanishing near-optimal restoration rate is equivalent to the
original support-gap decay rather than a weaker intermediate theorem.

Optimality alone supplies no quantitative modulus.  In an exact
complete three-point transport family with parameter
\(\delta\downarrow0\), the support gap is \(\delta\), but the unique
optimal relaxed demand has restoration cost \(2-\delta\).  With
absolute slack \(0\le s\le\delta\), its full Pareto curve is
\[
R_\delta(s)
=(2-\delta)\left(1-\frac{s}{\delta}\right).
\]
This is a method countermodel, not an endpoint-notch witness: it gives
neither a lower bound for the endpoint \(\Gamma_m\) nor a primal
positive-energy scalar.  Endpoint-specific geometry must still bound
\(\Gamma_m\) directly, and no \(g(m)\to0\), obstruction depth, gluing
conclusion, or positive-energy family is known.

### Shared-cut scale-slice boundary

A broader nested-sheet class is also excluded.  If
\[
 f_m(X(u,v,z))=G_m(z-\Psi_m(u,v))
\]
is complete-pair one-Lipschitz, \(G_m\) is monotone, and its two exact
frame shears are bounded by
\(\Lambda_m r|v|\) and \(\Lambda_m r|u|\), then genuine-slice monotone
interval packing gives
\[
 \boxed{
 {\cal E}_m(f_m)<
 \frac{2^{29}(\Lambda_m+1)}{\sqrt m}.}
\]
The height \(\Psi_m\) is arbitrary and may be nonseparable.  Hence every
fixed natural-shear class, and every \(\Lambda_m=o(\sqrt m)\), has
vanishing energy.

Dyadic cut coherence and complete collision collection do not extend this
to arbitrary scalars.  For the reviewed critical-period complete-pair
scalar, the exact common-threshold remainder and original energy tend to
zero:
\[
 {\cal R}^{\rm th}_m\leq48\overline A_m,\qquad
 {\cal E}_m\leq27\overline A_m,
\]
but the threshold-induced adjoint, after every scale collision is collected
before absolute values, satisfies
\[
 {\mathfrak D}^{\rm th}_m
 \geq
 \frac{m}
 {270\cdot2^{59}\lceil\log_2m\rceil^2}\longrightarrow\infty.
\]
Thus an absolute collision envelope is not a vanishing profile-weighted
majorant even when all coefficients come from one nested family of common
thresholds.  A future decay proof must retain signed cancellation before
absolute values or directly control metric-weighted margins; a future
single-sheet witness must have genuinely high shear.  Neither branch is
constructed here, so the endpoint candidate and project objective remain
open.

The theorem, exact replay, and typed Jacobian record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/shared_cut_scale_slice/`.

## Signed optimal-residual normality boundary

For a complete-pair one-Lipschitz scalar \(f\), let \(b_f\) minimize
\({\cal E}_m(f-b)\) over actual full two-bank functions
\(b=F_v(z-uv)+H_u(z)\) with complete-pair Lipschitz norm at most one,
and put \(r_f=f-b_f\).  A minimizer exists after fixing one additive
constant.  Applying the convex variational inequality separately to
\(c\) and \(-c\) gives
\[
\sup_{\operatorname{Lip}(c)\leq1,\ c\in{\cal B}_m}
\left|\langle A_mr_f,A_mc\rangle\right|
=\langle A_mr_f,A_mb_f\rangle
\leq\sqrt{\epsilon_m{\cal E}_m(r_f)}.
\]
Thus \(b_f\) is already the strongest actual controlled-bank test
against its optimal residual.  The signed rectangle coefficient field
is a demand, not a bank potential.

Consequently an actual bank captures the common-threshold remainder
exactly when
\[
{\cal R}^{\rm th}_m(r_f)
\leq\langle A_mr_f,A_mb_f\rangle.
\]
If this endpoint-specific inequality held for every \(f\), then
\[
\eta_m\leq
\frac{23+3\sqrt{57}}6\,\epsilon_m
<8\epsilon_m,
\]
with the computable obstruction depth
\[
m_0(n,D)=\min\{m\geq5:8nD^2\epsilon_m<1\}.
\]

The implication cannot come from convex normality and the vanishing
bank-energy estimate alone.  An exact all-\(k\) six-point complete
metric model has controlled-bank energy, optimal residual energy, and
genuine three-value threshold remainder all equal to \(1/(2k^2)\),
while every bank correlation is zero.  This was a method countermodel,
not an endpoint-notch scalar; the later construction below settles the
endpoint-specific question itself.

Optimal subtraction also removes the reviewed critical-period
controlled-bank mode completely: its optimal residual has zero frame
increments and zero threshold remainder.  Conversely, the alternating
six-cycle's persistent layer-cake charge is not the geometric
threshold coefficient and by itself does not refute the endpoint
inequality.

The normality theorem and exact replay are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/signed_optimal_residual/`.

## Exact all-depth failure of endpoint signed capture

The endpoint-specific inequality is now refuted in its full stated
domain.  For every \(m\geq5\), put
\[
h=R_m/8,\qquad r=R_m/16.
\]
Six genuine maximum-scale \(b\)-occurrences use the basepoints
\[
\begin{array}{c|r|r|r|r}
i&g_i&u_i&v_i&z_i\\ \hline
0&-1&7&h-10&h-10\\
1& 1&8&h-9&2h-18\\
2& 1&6&h-10&0\\
3&-1&8&h-8&2h-18\\
4& 1&7&h-8&h-10\\
5&-1&6&h-9&0 .
\end{array}
\]
With \(x_i=X(u_i,v_i,z_i)\) and \(y_i=b^rx_i\), their point demand
\[
\sigma_m=\sum_i g_i(\mathbf1_{y_i}-\mathbf1_{x_i})
\]
is nonzero and satisfies \(J_m^{\mathsf T}\sigma_m=0\) exactly.  The
left-bank changes cancel in the pairs \((0,2),(1,5),(3,4)\), and the
right-bank changes cancel in \((0,4),(1,3),(2,5)\).

The genuine right-horizontal intermediates
\[
p_i=x_ib^r=X(u_i,v_i+r,z_i)
\]
lie in \(B_m\) but outside the complete frame-endpoint set.  Exact word
counting handles every endpoint class: their \(v\)-coordinate excludes
the inner ball, every left \(a\)-translate, and every \(b\)-scale at
most \(r/2\); at scale \(r\), the preimages have negative canonical
areas
\[
-5r-10,\ -4r-18,\ -6r,\ -4r-18,\ -5r-10,\ -6r
\]
too large for the zero, one, or two available detour pairs.

The frame-endpoint component is connected, so the exact gauge-fixed
Green equation
\[
L_m\phi_m=\sigma_m
\]
has a unique solution.  Summation by parts makes it orthogonal to the
unrestricted bank subspace.  Normalize its endpoint range to
\([0,1/48]\), assign each \(p_i\) the value at \(x_i\), assign the other
intermediates values in the same interval, and use the McShane
extension.  The reviewed profile bounds
\[
H_m(1),C_m(4)>1/192
\]
give \(\rho_m(x,y)>1/24\) for every distinct lattice pair, so this is a
strictly complete-pair one-Lipschitz scalar \(f_m\).

The legitimate optimal bank is \(b_{f_m}=0\).  On each of the six
displayed slots,
\[
q_i=0,\qquad z_i=d_i,\qquad \ell_i=|d_i|.
\]
Positive Green energy forces at least one \(d_i\ne0\).  Since every
other fully retained threshold summand is nonnegative,
\[
\boxed{
{\cal R}^{\rm th}_m(f_m)
\geq\frac1{2K_m|I_m|}
\sum_{i=0}^5\frac{d_i^2}{\Delta_i}>0
=\langle A_mf_m,A_mb_{f_m}\rangle.}
\]
This refutes only signed capture.  It supplies no uniform lower bound
on \({\cal E}_m(f_m)\), so \(g(m)\), scalar concentration, a finite
obstruction depth, and the project counterexample remain open.  The
proof and exact replay are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/endpoint_capture_witness/`.

## Dense multiscale Green amplification boundary

The genuine six-point bank cycle can be replicated at positive density without
preserving a positive normalized Green energy.  Put
\[
s_m=h_m/128,\qquad
{\cal Q}_m=\{X(U,V,C):U,V\in4\mathbb Z,\ |U|,|V|\leq s_m,\
C\in16\mathbb Z,\ |C|\leq s_m^2\},
\]
and use every \(b\)-scale
\[
2\leq j\leq\lfloor K_m/2\rfloor-1
\]
with arbitrary rational root-independent coefficients
\(1\leq\alpha_j\leq2\).  The resulting occurrence flow uses at least
\[
\frac1{60\cdot2^{33}}
\]
of the complete frame occurrences and at least \(1/4\) of all scales.  Its
nonzero point demand has zero total mass and annihilates both complete banks.

For the exact full-profile gauge-fixed Green solution, endpoint Lipschitz
normalization followed by McShane extension gives a complete-pair
one-Lipschitz scalar with zero as an unrestricted-bank minimizer.  Nevertheless,
\[
\boxed{
{\cal E}_m(f_{m,\alpha})
<
\frac{442368}{2^{\lfloor K_m/2\rfloor}}
\longrightarrow0.}
\]
The mechanism is exact cancellation through the translation box:
\[
\sum_{q\in{\cal Q}_m}\bigl(s(b^{2^j}q)-s(q)\bigr)
\]
is supported on
\({\cal Q}_m\triangle b^{2^j}{\cal Q}_m\), and the total relative root
boundary over the retained \(\Theta(K_m)\) scales is at most
\(256/2^{\lfloor K_m/2\rfloor}\).  A unique largest-scale source anchor and
the complete Laplacian degree and profile bounds then force the displayed
energy decay.

This exhausts the frozen lower-half-scale translation-invariant Foelner-box
class.  It does not cover coefficients varying with the translation root,
upper-scale arrays, non-Foelner arrays, or unrestricted scalar concentration.
The theorem, exact replay, and typed Laplacian audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/dense_multiscale_green_amplification/`.

## Root-dependent anti-translation Green boundary

The canonical root-dependent law
\[
\beta_j(X(U,V,C))=(-1)^{\lfloor V/2^j\rfloor}
\]
reverses sign under its own scale-matched translation:
\[
\beta_j(b^{2^j}q)=-\beta_j(q).
\]
On the unchanged root box, lower-half scales, and genuine translated
six-cycle flow, the collected root coefficient is
\[
\gamma_m(t)=-
\sum_j\beta_j(t)
\left(\mathbf1_{{\cal Q}_m}(t)
+\mathbf1_{b^{2^j}{\cal Q}_m}(t)\right).
\]
The indicator sum makes the overlap a bulk source instead of a Folner
boundary.  Exact dyadic Rademacher orthogonality on an interior product box
gives
\[
\boxed{\|\sigma_m\|_2^2\geq
\frac{K_m|I_m|}{15\cdot2^{35}}.}
\]
At the smallest genuine depth \(m=5\), complete collection before any Green
solve gives point support \(299682\), \(\ell_1\) mass \(770544\),
\(\ell_2^2=3052908\), and exact normalized ratio
\[
\frac{\|\sigma_5\|_2^2}{K_5|I_5|}
=\frac{254409}{|I_5|}.
\]
The complete scale Gram matrix is recorded in the route evidence.

Bulk source mass still does not survive complete-pair Green normalization.
All dyadic signs align at the identity, where
\(\gamma_m(e)=-2\ell_m\) for
\(\ell_m=\lfloor K_m/2\rfloor-2\).  The full root coefficient
\(\ell_1\) norm is only \(O(\sqrt{\ell_m}|{\cal Q}_m|)\).  The identity
anchor, exact complete-frame degree and profile bounds, gauge-fixed Green
equation, endpoint Lipschitz normalization, and McShane extension give
\[
\boxed{
{\cal E}_m(f_m)\leq
\frac{600}{\sqrt{\ell_m}}+
\frac{55296}{\ell_m2^{\lfloor K_m/2\rfloor}}
\longrightarrow0.}
\]

This theorem by itself exhausts the frozen \(\tau_j=0\) phase law.  The
all-phase theorem below now closes every independent integer shift of the
same square-wave law.  Upper scales, different root supports, arbitrary
root-dependent arrays, and unrestricted scalar concentration remain open.
The unshifted proof, exact complete-source replay, and typed Gram audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/root_dependent_green_amplification/`.

## All integer-shifted phases still align

The full integer-shifted family is
\[
\beta_{j,\tau}(X(U,V,C))
=(-1)^{\lfloor(V+\tau_j)/2^j\rfloor},
\qquad
2\leq j\leq\lfloor K_m/2\rfloor-1,
\]
with every \(\tau_j\in\mathbb Z\) chosen independently.  It retains exact
scale-matched anti-translation:
\[
\beta_{j,\tau}(b^{2^j}q)=-\beta_{j,\tau}(q).
\]

On the central root line \(V=4n\), put \(k=j-2\) and
\(a_k=\lfloor\tau_{k+2}/4\rfloor\).  Then
\[
b_k(n)=\beta_{k+2,\tau}(X(0,4n,0))
=(-1)^{\lfloor(n+a_k)/2^k\rfloor}.
\]
The \(k\)-th output bit is the \(k\)-th bit of \(n\) plus a carry depending
only on lower bits.  Hence
\[
n\bmod2^{\ell_m}\longmapsto(b_0(n),\ldots,b_{\ell_m-1}(n))
\]
is triangular with unit diagonal and therefore bijective for every phase
vector.  The half-open central root interval has length
\(2^{K_m-8}\), a multiple of \(2^{\ell_m}\), so it contains a complete
residue block.  Choosing the all-\(+1\) vector gives a common aligned root
\(t_\tau\in{\cal Q}_m\) with
\[
|\gamma_{m,\tau}(t_\tau)|\geq\ell_m.
\]

The same bijection makes the shifted scale rows pairwise orthogonal on the
half-open interval.  After adding the one inclusive endpoint and the
unchanged translated-box boundary,
\[
\sum_t|\gamma_{m,\tau}(t)|
<
|{\cal Q}_m|\left(
2\sqrt{2\ell_m}
+\frac{256}{2^{\lfloor K_m/2\rfloor}}\right)
\]
uniformly in \(\tau\).  The complete-frame degree and profile estimates,
exact Green equation, bank orthogonality, endpoint Lipschitz normalization,
and McShane extension then give
\[
\boxed{
{\cal E}_m(f_{m,\tau})
\leq
\frac{1200}{\sqrt{\ell_m}}
+\frac{110592}
{\ell_m2^{\lfloor K_m/2\rfloor}}
\longrightarrow0.}
\]

Thus an integer phase vector can only move the order-\(\ell_m\) aligned
root; it cannot turn this construction into a positive-energy scalar.  This
exhausts all independent integer shifts on the reviewed lower-half scales
and root box.  It does not cover upper scales, other root supports, arbitrary
root-dependent arrays, or unrestricted scalar concentration.  The proof,
exact all-phase replay, and typed shifted Gram audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/shifted_phase_alignment/`.

## Unrestricted fixed-cycle Green norm

The phase restrictions are no longer needed.  On the same root box, define
for an arbitrary real coefficient field
\[
S_m\gamma=\sum_{q\in{\cal Q}_m}\gamma(q)
\sum_{i=1}^6\varepsilon_i\mathbf1_{qp_i}.
\]
The six cycle points occupy distinct horizontal residue classes modulo four.
Consequently all translated source coordinates are disjoint and
\[
\|S_m\gamma\|_2^2=6\|\gamma\|_2^2.
\]
Each translated cycle is zero-sum and its opposite-sign equal-label pairs
annihilate both complete banks.

Let \(\phi_{m,\gamma}\) be the exact gauge-fixed solution of
\(L_m\phi=S_m\gamma\), normalize it by its complete-pair endpoint Lipschitz
seminorm, and extend by McShane.  Write \(\Xi_m\) for the supremum of the
resulting frame energy over every nonzero real \(\gamma\).

The decisive estimate is the full occurrence-weighted degree, not a
single-source peak.  The reviewed profile inequality
\[
H_m(4A)\geq2H_m(A)
\]
turns all reciprocal scale weights into a geometric series.  Since a vertex
is incident to at most four occurrences per scale,
\[
d_m(x)<\frac8{N_mH_m(1)}.
\]
Summing the local Laplacian Cauchy--Schwarz inequality over all six disjoint
source coordinates per root gives an \(\ell_2\) bound for the Green
normalization.  The cycle functional is bounded by the total length twelve
of the six explicit words.  Combining the two estimates yields
\[
\boxed{
0<\Xi_m\leq
\frac{384|{\cal Q}_m|}{N_m}
=\frac{192|{\cal Q}_m|}{K_m|I_m|}
\leq\frac{192}{K_m}\longrightarrow0.}
\]

This exhausts every support and every real nonlinear coloring on translated
copies of the fixed six-cycle over the entire reviewed root box.  It removes
all coefficient restrictions for direct cycle roots in that box.  Since the
reviewed anti-translation constructions can acquire collected cycle roots
outside the box, their separate exclusions remain necessary.  The result does
not cover scale-dilated or different cycles, roots outside the box, or
unrestricted scalar concentration.  The proof, exact \(m=5\) collection,
constant replay, and typed weighted-Laplacian audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/unrestricted_cycle_green_norm/`.

## Critical dilated-cycle three-block Green norm

The first cycle family that escapes the fixed-word-length estimate also has a
uniform negative theorem.  Put
\[
R_m=2^{\lceil\log_2K_m\rceil},\qquad t_m=R_m+1,
\]
dilate all six cycle coordinates by \(t_m\), and use every integer root in
the box
\[
|U|,|V|\leq h_m/64,\qquad |C|\leq(h_m/64)^2.
\]
For every block-origin shift, the frozen coefficient class is the full
two-dimensional mean-zero span of the cyclic translates of
\((2,-1,-1)\), evaluated at
\[
\left\lfloor\frac{U+\alpha}{t_m}\right\rfloor+
\left\lfloor\frac{V+\beta}{t_m}\right\rfloor\pmod3.
\]

This class passes the intended escape diagnostics.  Its roots have uniform
positive density; every translated cycle cancels both complete banks; its
opposite-sign transportation cost lies between
\(3\sqrt{H_m(t_m^2)}\) and \(4\sqrt{H_m(t_m^2)}\); and
\[
H_m(t_m^2)\geq K_mH_m(1).
\]
After complete collection, range-normalized members satisfy
\[
\|\sigma_m\|_\infty\leq6,\qquad
\|\sigma_m\|_2^2\geq\frac9{32}|{\cal Q}_m|,
\]
outside a relative boundary at most \(2304t_m/h_m\).

Nevertheless, complete-pair normalization forces decay.  Summing the exact
Green equation over one interior phase class turns every scale-\(2^j\)
frame contribution into a cut term.  Below \(t_m\), only a
\(2^j/t_m\) fraction crosses the cut; above \(t_m\), profile doubling makes
the reciprocal weights geometric.  Uniformly over every nonzero real phase
member and every origin shift,
\[
\boxed{
{\cal E}_m(f_{m,v,\alpha,\beta})
<\frac{4096}{\sqrt{K_m}}\longrightarrow0.}
\]
The proof uses the actual full-profile Laplacian, both generators, every
scale and basepoint, repeated occurrences, boundary endpoints, exact
complete-pair Lipschitz normalization, and McShane extension.  It does not
cover another dilation schedule, root wave, cycle, or unrestricted scalar
concentration.  The theorem, exact replay, and typed factorization audit are
in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/critical_dilated_cycle_green/`.

## Critical nested magnetic-distance cascade

The direct distance-cone cascade is now decided without reducing it to a
raw atom field. For \(m\geq512\), let
\[
S_{m,r}=B_m\cap
\{(\ell_ra,\ell_rb,16t_rn):a,b,n\in\mathbb Z\},
\quad
A_{r+1}-A_r=2^{-12}\sqrt{C_m(t_r)},
\]
on the frozen range \(30m\leq r\leq
\lfloor(K_m-j_0)/4\rfloor-4\), and set
\[
F_m(x)=\min_r\{\rho_m(x,S_{m,r})-A_r\}.
\]
The sets are nonempty and nested, and the finite minimum is
complete-pair one-Lipschitz. Adjacent and nonadjacent competition is
exactly
\[
(d_q-A_q)-(d_p-A_p)
=d_q-d_p-\sum_{i=p}^{q-1}2^{-12}\sqrt{C_m(t_i)}.
\]

The decisive count uses the actual winning branch at each point. Break
ties deterministically and let \(W_r\) be the resulting partition of
\(B_m\). For a pure-central frame pair \(p_0,p_1\),
\[
|\Delta F_m|^2\leq
\sum_r(\mathbf1_{W_r}(p_0)+\mathbf1_{W_r}(p_1))
|\Delta d_r|^2.
\]
After writing the frame scale as \(k=j_r+n\), each fixed-\(n\) endpoint
map is injective and preserves the transverse slice. Since the \(W_r\)
are disjoint, all \(\Theta(K_m)\) branch-labelled images pack into one
copy of \(B_m\), whose size is less than \(2^{29}|I_m|\). Combining
this winner packing with the reviewed one-band tube and large-slice
estimates gives
\[
\boxed{
\begin{aligned}
{\cal E}_m(F_m)\leq6\bigg[
&\frac{73728}{2^{K_m}}
+\frac{169869312}{\lfloor\sqrt m\rfloor}\\
&+2^{30}\left(
\frac{2^{14}}{m^2}
+\frac{\Lambda_m+N_m+2+3m+K_m/2^{K_m}}{K_m}
\right)\bigg]\longrightarrow0,
\end{aligned}}
\]
where
\[
\Lambda_m=\left\lceil
\log_2(2^{23}m^{13}L_m)\right\rceil+2
\]
and \(N_m\) is the least integer with
\[
2^{N_m(m-1)}\geq(2^{17}m^5)^m.
\]

This is neither the dominant-well collapse nor the common-mask Fourier
decay theorem: different subcritical branches may remain active. Their
matched-scale contributions still cannot accumulate because the winner
partition pays for every relative scale only once. The carrier weights
are not small-Lipschitz, so the earlier weighted min-plus extension
argument does not subsume this result. The proof, integer/Fraction
replay, and typed Jacobian aggregation audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/critical_nested_magnetic_distance_cascade/`.

## Critical odd-period parabolic-chirp distance

For \(m\geq512\), put
\[
P_m=2^{K_m}+1,\qquad q_m=2^{K_m-1},\qquad
\lambda_m=2^{\lceil(\log_2m)/2\rceil},
\]
\[
\tau_m(u,v,z)=z-uv-\lambda_mu^2,
\]
and let \(S_{m,0},S_{m,1}\) be the two phase fibers
\(\tau_m\equiv0,q_m\pmod{P_m}\) inside the actual finite block \(B_m\).
The signed ambient-distance scalar
\[
F_m=\frac{\rho_m(\,\cdot\,,S_{m,0})
          -\rho_m(\,\cdot\,,S_{m,1})}{2}
\]
is complete-pair one-Lipschitz. Its exact left-generator phase increments
are
\[
\tau_m(a^rX)-\tau_m(X)
=-r(v+2\lambda_mu+\lambda_mr),\qquad
\tau_m(b^rX)-\tau_m(X)=0.
\]

The essential horizontal shear does not create a positive normalized
energy floor. Every actual frame endpoint has word length at most
\(3h_m/2\). For either phase, changing only its canonical central label
by the unique centered residue in \([-h_m/2,h_m/2]\) produces a genuine
point of the corresponding finite set still inside \(B_m\). The reviewed
upper central profile therefore bounds the square of every frame
increment by \(144m h_m^{1-1/m}\), irrespective of which true nearest
point wins.

Keeping the exact denominator
\(\Phi_m(r^2,4r|t|)\), the normalized summand on every nonzero transverse
slice is at most
\[
\min\left\{1,\,
55296m^5\left(\frac{h_m}{r|t|}\right)^{1-1/m}\right\}.
\]
The genuine slice bound \(9h_m^3\), the lower bound
\(|I_m|\geq h_m^4/2^{13}\), both signs, both generators, and all
\(K_m\) scales then give
\[
\boxed{
{\cal E}_m(F_m)\leq
\min\left\{1,\,
\frac{221184}{h_m}
+\frac{147456}{K_m}
\left(3m+34+10\lceil\log_2m\rceil\right)
\right\}\longrightarrow0.}
\]
No frame occurrence or repeated incidence is deduplicated, and boundary
slices remain in the count.

This family is not covered by label-swap symmetry, the natural-shear
interval theorem, an epigraph/complement theorem, a single periodic
contact line, a one-band magnetic lattice, or a nested-winner argument.
An integral coordinate shear straightens \(\tau_m\), but it changes both
the endpoint-notch metric signatures and the frozen frame. The theorem,
exact replay, and typed polynomial-factorization audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/critical_parabolic_chirp_distance/`.

## Correlated dyadic martingale rectangle-charge boundary

The adjacent-increment martingale ledger is exact on every actual central
slice of \(I_m\).  For \(r=2^j\), the two \(a\)-children
\[
A_j(u,v,z-rv),\qquad A_j(u,v,z)
\]
have parent \(A_{j+1}(u-r,v,z-rv)\), and the \(b\)-family has the
word-isometric ledger with parent \(B_{j+1}(u,v-r,z-ru)\).  Summing the
parallelogram identity over the complete set of valid anchors gives the
exact parent coefficient
\[
\frac{S^{a}_{2r,v}}{4S^{a}_{r,v}}
\quad\hbox{or}\quad
\frac{S^{b}_{2r,u}}{4S^{b}_{r,u}},
\]
together with an explicit nonnegative multiplicity for every unmatched
child copy.  No translation-complete slice is substituted for the genuine
word ball.  The exact Mellin profile comparison
\[
\frac{C_m(2T)}{C_m(T)}<2^{1-1/m}\qquad(T>0)
\]
further shows that, after the legitimate twofold child count, the parent
term contracts by \(q_m=2^{-1-1/m}<1/2\) modulo the already reviewed
horizontal defect.  The parent weights therefore close; the centered
Haar detail is the remaining step.

The intended direct charge of the centered Haar details to the genuine
rectangle sides fails with depth-growing loss.  Put
\[
s_m=h_m/64,\qquad \kappa=1/96,
\]
and define the complete-pair one-Lipschitz magnetic sheet scalars
\[
G^a_m(X(u,v,z))
=\kappa{\bf1}_{\{v=s_m\}}
\cos\!\left(\frac{2\pi(z-s_mu)}{3s_m}\right),
\]
\[
G^b_m(X(u,v,z))
=\kappa{\bf1}_{\{u=s_m\}}
\cos\!\left(\frac{2\pi z}{3s_m}\right).
\]
For \(0\leq j\leq K_m-8\), both short sides of the corresponding
rectangles vanish identically, while every centered detail has multiplier
\(3\).  An exact interior box, all of whose vertices lie in \(I_m\), gives
\[
\frac{\text{weighted centered-detail energy}}
     {\text{energy of all long sides in its containing envelope}}
\geq
\frac{13824}{15925}(K_m-7).
\]
Thus a nonnegative bounded-overlap rectangle-side estimate cannot have a
depth-independent constant, even before word-ball boundary losses.

This is a route exclusion, not a positive-energy witness.  Actual slice
counting gives
\[
\mathcal V_m(G^a_m),\mathcal V_m(G^b_m)
\leq6144/h_m\longrightarrow0.
\]
Consequently \(\nu_m\), \(\eta_m\), finite obstruction depths, and the
project counterexample remain open.  Any continuation must exploit signed
cancellation beyond nonnegative side energy or use a materially different
correlated mechanism.  The exact theorem, replay, actual-slice incidence
ledger, and typed Haar-determinant audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/correlated_dyadic_martingale_trace/`.

## Signed Haar-adjoint collision reinforcement

Collecting the magnetic-sheet long sides before absolute values does not
repair the centered-detail estimate.  Let
\[
S_j=H_m(2^{2j})+C_m(4\cdot2^js_m),\qquad
W_m=\sum_{j=0}^{K_m-2}S_j^{-1}.
\]
After canonicalizing orientations, the complete \(a\)-family coefficient
on \(Q_{s_m}(x,0,w)\) is a four-anchor difference.  On every edge for
which those anchors are genuine, its scale-\(j\) value is exactly
\[
\frac{9\kappa}{4S_j}
\cos\!\left(\frac{2\pi(w-s_mx)}{3s_m}\right).
\]
The two values of \(2^j\bmod3\) give the same sign: the horizontal and
central translations turn the four phases into
\[
2\cos\phi-\cos(\phi-\delta_j)-\cos(\phi+\delta_j)
=3\cos\phi.
\]
Thus every scale reinforces.  The \(b\)-family is the exact word-isometric
copy.

The edge box
\[
4s_m\leq x<8s_m,\qquad 0\leq w<3s_m^2
\]
is saturated by every scale \(0\leq j\leq K_m-2\).  All possible
colliding anchors, including those outside the edge box, have horizontal
coordinate at most \(28s_m\), central coordinate or magnetic gauge below
\(19s_m^2\), and word length at most \(59s_m<h_m\).  Hence no boundary
anchor or scale is omitted.  Over its complete periods, the
post-collision cost is exactly \(3/4\) of the corresponding
pre-collision cost; there is genuine constant cancellation but no
cross-scale cancellation.

Using the complete genuine-slice bound \(N_m(s_m)\leq9h_m^3\) gives, for
both families,
\[
\mathscr J_m^\gamma
\geq\frac{\sqrt{H_m(s_m^2)}}{4096}\mathscr H_m^\gamma.
\]
With
\[
L_m=
\frac{
2^{\left\lfloor (m-1)(K_m-6)/m\right\rfloor}
}{m+1},
\]
the reviewed horizontal profile floor yields the explicit all-depth
reinforcement
\[
\boxed{
\mathscr J_m^\gamma
\geq\frac{L_m}{24576}\mathscr H_m^\gamma,
\qquad m\geq5,\qquad L_m\to\infty.}
\]
The original \(2K_m|I_m|\) normalization is retained on both sides.
Unmatched child copies and the terminal \(j=K_m-1\) layer remain outside
this centered-detail claim.

This excludes only the direct parent-child signed long-edge adjoint for
the reviewed magnetic sheets.  Since the same sheets still satisfy
\(\mathcal V_m\leq6144/h_m\to0\), this is neither scalar decay nor a
positive-energy witness.  The exact proof, replay, and typed Jacobian
four-term simplification are under
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/high_quotient_scalar_concentration/correlated_dyadic_martingale_trace/signed_collision_gate/`.

## Guarded macrocell-vector packing boundary

The full-cell magnetic system admits a stronger spatial-packing
exclusion than the global common-mask theorem.  Keep the reviewed
guarded macrocells and all \(L\geq K_m/8\) remote bands, but let every
macrocell carry an independently arbitrary complex vector across those
bands.  The vectors need not come from a finite palette and can be
staggered arbitrarily between macrocells.  If the resulting remote field
is genuinely complete-pair \(1/4\)-Lipschitz, the exact finest-carrier
McShane envelope satisfies
\[
\begin{aligned}
{\cal E}_m(F_{m,c})\leq6\bigg[
&5\left(\frac{73728}{h_m}
+\frac{169869312}{\lfloor\sqrt m\rfloor}\right)
+\frac{2^{89}m^2}
{K_m\lfloor\sqrt m\rfloor}
+\frac{25}{4K_m}\\
&+\frac{460800}{K_m}
\left(J_m+2+3m+\frac{K_m}{h_m}\right)
\bigg]\longrightarrow0,
\end{aligned}
\]
where \(J_m\) is the least integer with
\(2^{J_m(m-1)}\geq(2^{17}m^5)^m\).

The reason no macrocell-count factor appears is local.  At each
macrocell center, genuine complete-period horizontal and central probes
give the powers-of-four Sidon budget
\[
\sum_r|c_{r,\mathfrak Q}|^2
\leq2^{18}m^{3/2}.
\]
Different macrocell fields have disjoint horizontal support, and one
frame edge evaluates only the fields at its two endpoints.  Forward and
backward diagonal estimates, together with the one-extra-period Gram
bound on every genuine central slice, then sum over at most \(9h_m^2\)
horizontal labels rather than over the number of macrocells.

This theorem still does not cover independent coefficients in every
individual band cell: all guarded cells of one band inside a macrocell
share its vector entry, and the remote field is Lipschitz before
projection.  There is also an exact reuse obstruction to obtaining the
missing theorem from corrected-event counts alone.  The reviewed
full-cell scale star has \(K_m-31\) fixed-threshold high events controlled
by one self-contact, while the other query endpoints are not contacts
and all raw contact values agree.  Its normalized mass and energy vanish,
so it is not a counterexample; it shows that a global matching argument
needs a proved contact-reuse or cell-tree Carleson bound.

The exact theorem, replay, and typed maximum-matching audit are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/global_matched_contact_packing/`.

## Adjacent-level two-child contact-switch boundary

The smallest centered-grid class beyond one guarded-macrocell vector is
now classified.  At adjacent retained levels, put one parent atom in a
cell of side \(2L\) and independently weight two address-child atoms of
side \(L\) in the same guarded macrocell.  The centered grids are
staggered: address-children are defined by
\[
\left\lfloor\frac{k_\nu+1}{2}\right\rfloor=p_\nu,
\]
and only one of the four is literally contained in the parent cell.
This distinction is retained together with the half-open zero-boundary
tent.

After adding only the reviewed finest carrier, a rational amplitude
simplex makes the three-atom modulation \(1/8\)-Lipschitz.  Every
carrier well is then a unique self-contact.  On a complete parent
carrier period the parent and active child have only the distinct
frequencies \(\{\pm1,\pm4\}\).  Of the six unordered child pairs,
exactly two are one-generator center pairs on which the parent tent
switches from zero to one.

For the horizontal pair, one exact quarter-phase choice gives a genuine
left-\(a\) frame edge and its pure-central comparison with period
averages
\[
\frac12\left(A_p^2+(A_1+A_2)^2\right)>0,
\qquad
\left(1-\frac1{\sqrt2}\right)A_p^2+2A_1^2>0.
\]
All period points lie in the genuine inner word ball, and both endpoint
pairs are distinct self-contacts with nonzero raw and envelope
differences.  A frame-admissible guarded translation changes only one
Gaussian quarter phase on the horizontal edge.  Its isolated
pure-central difference is nonzero exactly when the translated parent
address satisfies \(p_2\not\equiv0\pmod8\); the two residue classes
\(p_2=0,8\pmod{16}\) are exact phase aliases.

This local existence result is not a laminate.  Uniformly over the
frozen one-tile parameter class, the complete original-frame energy is
bounded by an explicit expression tending to zero; in particular one
tile retains the \(K_m^{-1}\) scale loss.  No coefficient law achieves
fixed spatial density on a fixed fraction of all scales, and the
self-contact proof is not stable under arbitrary surrounding raw
coefficients.  Thus neither a positive-energy scalar family nor a
surrounding-field-uniform cell-tree/Carleson theorem follows.

The exact classification, replay, and typed algebraic comparison are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/subcell_contact_switch/`.

## Adjacent-tile compatibility and linear reuse

The decisive two-tile test does not produce a phase incompatibility.
For a fine parent address \(p\), adjacent coarse parent address \(P\),
and \(d=p-2P\), positive tent supports overlap exactly for
\(d\in\{-1,0,1\}^2\).  The shared middle-band slots are precisely
\(d=0\) and \(d=(-1,0)\); every such overlap is inside one genuine
guarded macrocell.  With nonzero nominal coefficients, both
pure-central differences survive exactly under
\[
\begin{array}{c|c}
d=0&P_2\not\equiv0\pmod8,\\
d=(-1,0)&\gamma_p\ne0,\quad P_2\not\equiv0\pmod4,\\
\text{otherwise}&P_2\not\equiv0\pmod8,\quad
p_2\not\equiv0\pmod8.
\end{array}
\]
Both shared cases have explicit compatible Gaussian quarter phases in
one pre-fixed coefficient field.  A strong finest carrier makes both
complete-period cores simultaneous unique self-contacts whenever the
actual merged remote field is strictly Lipschitz on the carrier.

More strongly, one origin-macrocell field has exact nonzero
distinct-self-contact switches on
\[
Q=q_*-30m-5\geq K_m/8
\]
adjacent selected scales.  All right centers coincide, and one top
center atom has a strict nonzero contribution to every pure-central
switch.  Hence the local pattern has reuse multiplicity at least
\(K_m/8\); no uniform finite contact-reuse theorem can follow from
two-tile geometry.

The same common center exposes an exact amplitude conflict.  If its
carrier restriction is \(\Lambda\)-Lipschitz, complete-period Sidon
probes give
\[
\sum_j|c_j|^2\leq2^{23}\Lambda^2m^{3/2}.
\]
Thus fixed coefficient amplitude cannot occur on a fixed fraction of
the \(K_m\) common-center levels.  The explicit compatible chain uses a
geometric coefficient schedule and has complete-frame energy tending
to zero; it also occupies only one horizontal fiber.  This does not
control spatially staggered address trees, whose nonovercounting
Carleson charge remains open.

The exact table, long-chain construction, replay, and conflict
inequality are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/subcell_contact_switch/two_tile_compatibility_and_reuse.md`.

## Scale-period-two spatial subcell collision boundary

A complete nominal table on
\[
(r\bmod2,p_1\bmod8,p_2\bmod8,\mathrm {axis})
\]
does not remain \(8\times8\) after coincident parent and child slots
are merged.  Recovering a parent residue from \(k=2p\) requires
\(k\bmod16\), so the generic physical field is period sixteen.
For each interior scale parity, the exact merge operator has rank
\(208\) over \(\mathbb Q(i)\).  Its only image restriction is that the
four period-sixteen lifts of an odd-odd address modulo eight agree.
The two interior parities have rank \(416\).  After the child-only
bottom band and parent-only top band are retained separately, the
complete finite-field rank is \(464\) or \(512\), according to the
parity of the number of tile levels.

Finite collision and quarter phases do not block dense raw switches.
There is an explicit nontrivial period-two Gaussian-rational table for
which every horizontal and vertical frame polynomial is nonzero after
all merges.  Its pure-central raw term is nonzero on \(7/8\) of parent
residues for each generator and on \(49/64\) simultaneously.  Distinct
powers-of-four frequencies prevent surrounding periodic bands from
canceling these terms in a complete-period raw mean square.

This is not contact or complete-frame energy density.  On the exact
normalized subcone
\[
0\leq\lambda\leq\frac1{2^{26}B_m},
\]
where \(B_m\) is the number of occupied physical bands, the coefficient
bound itself gives remote Lipschitz constant \(1/8\).  A strict finest
carrier then makes the complete carrier the exact McShane contact set,
and every table in the subcone satisfies an explicit complete-frame
bound tending to zero.

Fixed nonzero amplitudes remain open.  The one-band collision charge
has congestion and fanout four, but each table state is reused on at
least \(K_m/16\) levels, so this charge is not summable on the address
tree.  The exact fixed-amplitude contact set is not known.  Therefore
the \(49/64\) raw residue density proves compatibility only; it supplies
neither a positive energy floor nor uniform decay for the full ray.

The collision theorem, explicit table, safe-subcone decay, replay, and
typed exact rank record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/spatial_periodic_subcell_laminate/`.

## Fixed-amplitude full-carrier transition boundary

The earlier \(\lambda=1\) phase trace established equal parent raw
states and a positive one-sided successor contact loss, but that did
not calculate either complete successor minimum.  The missing
full-carrier audit is now complete for the concrete \(m=512\) aliases
at depths \(2,3,4\).

After scaling the finest carrier mesh by
\(Q_h=2^{15360}\) and \(Q_c=4^{15360}\), exact profile localization
reduces every requested minimum to a finite box.  Rigorous Arb
subdivision with the actual endpoint-notch pair profile excludes every
controller outside the common centered finest cell.  There the exact
change of variables
\[
z_c=z+\frac X8(y-x)
\]
separates the horizontal radius from the magnetic phase.  A complete
one-dimensional interval audit and a \(70000\)-bit carrier-mesh
isolation then give one exact minimizing controller in each symmetry
orbit.

Central translation by the complete parent period bijects the full
localized controller sets inside the genuine word ball.  Therefore the
depth-two \(x\)-parents and depth-three \(y\)-parents have identical
raw heights, envelope values, contact losses, and relative singleton
controller labels.  Their successors are genuinely different:
\[
\frac{E_3(x_0)-E_3(x_1)}
{\sqrt{C_{512}(t_{s_0+3})}}
=0.732822084645881646\ldots>0,
\]
\[
\frac{E_4(y_0)-E_4(y_1)}
{\sqrt{C_{512}(t_{s_0+4})}}
=0.205107685735794616\ldots>0.
\]
The successor contact losses and relative controller indices differ as
well.  Thus the frozen state is not successor-sufficient for this
exact instance; raw-height divergence is no longer being substituted
for the min-plus comparison.

This corrected theorem is concrete.  It does not assert the previous
every-\(m\) or every-fixed-lookahead extension, classify all
fixed-amplitude contacts, prove a positive energy floor or decay
theorem, or exhaust the periodic class.  The proof, exact controller
integers, rigorous cost intervals, finite-box counts, and replay are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/spatial_periodic_subcell_laminate/fixed_amplitude_carrier_minplus/full_carrier_controller_audit/`.

## Full 4-adic slack-tree localization boundary

The uncompressed carrier state at depth \(d\) is the complete labelled
slack profile
\[
\sigma_d^x(u)=h_d(u)+\rho_m(x,u)-E_d(x).
\]
It has the exact transition
\[
E_{d+1}(x)-E_d(x)=
\min_u\bigl(\sigma_d^x(u)+U_d(u)\bigr),\qquad
\sigma_{d+1}^x(u)=\sigma_d^x(u)+U_d(u)-\min_v(\sigma_d^x(v)+U_d(v)).
\]
For fixed horizontal carrier labels, the central congruence class
modulo \(4^S\) splits into the four classes
\(\nu+q4^S\bmod4^{S+1}\).  On complete interior orbits the old-top
child addition is invariant and the new parent-only top is multiplied
by \(1,i,-1,-i\).  At the finite word-ball boundary the same
filtration is retained with possibly empty children rather than
replaced by a cyclic quotient.

This exact tree does not have the uniform centered localization needed
by the proposed nonnegative charge.  For every \(m\ge512\), one
explicit alternating-binary carrier address has
\[
\frac14\le\tau_r\le\frac38
\]
on at least \(K_m/8-2\) consecutive prefix tops.  At each such top an
adjacent quarter-phase lift satisfies the genuine endpoint-notch bound
\[
\sigma^{x_0}(x_1)>
(1-2\tau_r)\sqrt{C_m(t_r)}
\ge\frac14\sqrt{C_m(t_r)}.
\]
All points and the corresponding \(a\)- and \(b\)-frame locations lie
strictly inside the word ball.  Thus the centered strict-notch
competitor does not reset every child.  Conversely, the reviewed
\(m=512\) centered audit shows that successor minimizers need not be
lifts of parent minimizers.

These facts exclude a uniform four-child localization or
parent-controller lift rule.  They do not prove a fixed positive
complete-frame energy floor, an all-depth decay rate, or exhaustion of
the explicit periodic laminate.  Any decay continuation still needs
an averaged all-candidate Carleson inequality for the full slack
profiles, including partial boundary cylinders.  The theorem and
exact replay are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/spatial_periodic_subcell_laminate/full_4adic_slack_tree/`.

## All-candidate cylinder-variance boundary

For a complete interior parent cylinder at top period \(P=4^S\), the
four frozen child values are the actual all-controller increments
\[
v_q=E_{d+1}(x(a,b,\nu+qP))-E_d(x(a,b,\nu+qP)),
\qquad q=0,1,2,3.
\]
Their nonnegative functional is the centered variance
\[
{\mathsf V}_4(v)=\frac14\sum_q(v_q-\bar v)^2.
\]
For a partial finite-ball cylinder the same definition uses only the
actual nonempty children; genuine frame terms whose required orbit is
incomplete are kept in a separate nonnegative boundary remainder.
Missing children are never filled periodically or assigned value zero.

The genuine pure-central step is not uniformly internal to this
four-child vector.  For an \(a\)-frame incidence it is
\(p_2P/2\), with exact denominator
\(\Phi_m(t,-8p_2t)\); for a \(b\)-incidence it is
\(-p_1P/2\), with denominator \(\Phi_m(t,8p_1t)\).
Thus positive endpoint-notch profile weights cannot change the
following residue algebra.

If the transverse address is odd, the pure-central edge alternates
between two distinct parent cylinders.  Writing their child vectors as
\(a,b\), the exact eight-cycle mean square satisfies
\[
\begin{split}
(\bar a-\bar b)^2+
\frac{2-\sqrt2}{2}
\bigl({\mathsf V}_4(a)+{\mathsf V}_4(b)\bigr)
&\le {\mathsf D}_{\rm odd}(a,b)\\
&\le
(\bar a-\bar b)^2+
\frac{2+\sqrt2}{2}
\bigl({\mathsf V}_4(a)+{\mathsf V}_4(b)\bigr).
\end{split}
\]
The separately centered Fourier block has exact eigenvalues
\(2\pm\sqrt2\).  Hence the variance omits the cross-parent mean square:
the two constant vectors \((1,1,1,1)\) and
\((-1,-1,-1,-1)\) have zero variance and positive eight-cycle energy.
For transverse residue \(4\bmod8\), the half-cycle has the opposite
kernel: \((1,-1,1,-1)\) has positive child variance and zero half-cycle
energy.

In every \(16\times16\) horizontal period, for each generator and scale
parity, 128 addresses are odd cross-parent cases, 64 are quarter-cycle
cases, 32 are half-cycle kernels, and 32 have zero shift.  This is an
interior obstruction, not a finite-ball remainder.  It retires the
proposed two-sided variance-only comparison.

The exact \(m=512\) all-controller diagnostic has zero boundary
remainder.  In new-top profile units, the two increment variance sums
lie in \((0.92,0.93)\) and \((0.89,0.90)\), while the omitted
cross-parent mean squares lie in \((0.0009,0.001)\) and
\((0.32,0.33)\).  These are consecutive-transition measurements, not
an all-depth growth theorem.

Moreover, the increments belong to truncated envelopes
\(E_{d+1}-E_d\).  Later min-plus updates are not conditional
expectations and have no proved orthogonality or persistence, so
intermediate positive variance is not a lower bound for the final
\(F_m\) energy.  The complete \(\lambda=1\) laminate therefore remains
undecided: no \(g(m)\to0\) and no fixed positive energy floor follow.
The frozen functional, exact residue proof, full-carrier diagnostic,
and typed spectrum record are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/spatial_periodic_subcell_laminate/full_4adic_slack_tree/all_candidate_cylinder_variance/`.

## Complete-period global incidence boundary

At a retained scale with parent central period \(P\), a complete
pure-central orbit has eight nodes \(n_j=\nu+jP/2\) and cyclic form
\[
{\mathsf D}_r(z)=\frac18\sum_{j\bmod8}(z_{j+r}-z_j)^2.
\]
The original frame contains all eight directed incidences in this
orbit.  Its exact regrouped contribution is therefore
\[
\frac{8{\mathsf D}_{p_2}(z^a)}{\Phi_m(t,-8p_2t)}
\quad\text{or}\quad
\frac{8{\mathsf D}_{-p_1}(z^b)}{\Phi_m(t,8p_1t)},
\]
not one copy of \({\mathsf D}_r\).  Every incidence outside a certified
complete orbit remains a direct nonnegative boundary term, and the
single normalization \(2K_m|I_m|\) is applied only after all scales are
summed.

For the reviewed parent period \(P=16\), the common central period is
64.  There are eight orbit origins \(\nu=0,\ldots,7\), each with eight
nodes.  In every \(16\times16\) horizontal period, for each generator
and scale parity, 128 addresses are odd cross-parent, 64 are
quarter-cycle, 32 are half-cycle, and 32 are zero-shift classes.  Thus
one parity has \(32768\) directed terms across both generators, and the
two parities have \(65536\).

The full-carrier replay at addresses \((1,2)\) and \((1,-2)\) remains a
valid local result: at orbit origin zero their current and separate
update quadratic data agree while their positive successor energies
differ.  These addresses are two summands of one global coefficient
field, not two complete states.  The replay does not cover the other
254 addresses, the other seven orbit origins, or the second scale
parity, so it does not establish deterministic global nonclosure.

The natural global sign extension is the carrier isometry
\[
{\cal R}(a,b,n)=(a,-b,-n).
\]
It sends magnetic coefficients to their reflected conjugates and gives
exact full-carrier covariance \(E_d^{\cal R}(x)=E_d({\cal R}x)\).
The \(a\)-incidences are permuted by
\((p_1,p_2)\mapsto(p_1,-p_2)\).  After reversing the reflected
\(b^{-L}\)-edge, the \(b\)-incidences are permuted by
\((p_1,p_2)\mapsto(p_1,-p_2)\).  Actual endpoint-notch denominators
are preserved.  Hence complete-orbit current energy, update
self-energy, polarization cross term, and successor bulk are equal for
the two reflected period states.  The local split cancels in this bulk.
Reversing a reflected \(b^{-L}\)-edge can shift its finite inner-ball
basepoint, so equality of the incomplete-orbit remainder is not
certified.

No nonsymmetric global twin is known or ruled out.  For
\(V_d=E_{d+1}-E_d\), the exact remaining obstruction is
\[
{\mathsf Q}(E_{d+1})
={\mathsf Q}(E_d)+2{\mathsf B}_{\mathsf Q}(E_d,V_d)
+{\mathsf Q}(V_d).
\]
Defining
\[
L_d=\max\{0,-2{\mathsf B}_{\mathsf Q}(E_d,V_d)-{\mathsf Q}(V_d)\}
\]
gives
\[
{\mathsf Q}(E_D)\ge {\mathsf Q}(E_d)-\sum_{j=d}^{D-1}L_j.
\]
A global suffix-persistence theorem now requires a uniform summability
bound for these negative polarization losses.  None is proved, and the
local positive separation does not refute any fixed retention
constant.  A central-fibre-only scan over all addresses and central
residues gives successor/current ratios about \(2.1009\) and \(1.7927\)
in the two scale parities, but it does not exclude off-fibre
controllers and is not evidence for retention.  The exact incidence
audit, per-address ledger, reflection proof, explicitly noncertifying
all-address vertical diagnostic, and reused typed quadratic-form record
are in
`research/routes/p2_endpoint_scale_notch/global_nonstar_translation_frame/cellwise_metric_envelope/spatial_periodic_subcell_laminate/full_4adic_slack_tree/complete_period_quadratic_persistence/global_incidence_aggregate/`.
