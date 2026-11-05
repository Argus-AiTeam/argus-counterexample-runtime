---
title: Closed-surface cubed-mixed rank-three abc checkpoint
description: Four reviewed degree-24 components and the additional source-bound F0/H2 residual whose real SU(2) status is under exact classification.
---

# Closed-surface cubed-mixed rank-three `abc` checkpoint

For

```text
F=D_(b^-1 c) o (phi^3 union psi^3),
```

the invariant fiber center-character group is

```text
{(alpha,beta,beta,delta)} ~= (Z/2)^3.
```

Together with the independent stable-letter sign, the full
mapping-torus central-character group is `(Z/2)^4`.  The stable sign
acts trivially on the surface character chart.  The character
`chi_bc=(0,1,1,0)` exchanges the two members of each component orbit.

Here `P_plus` is the reviewed plastic component,
`P_minus=chi_bc(P_plus)`, `K_plus` is the known `(r,s)` component, and
`K_minus=chi_bc(K_plus)`.  These four degree-24 component ideals are
reduced and pairwise comaximal, but they do not exhaust the frozen
source ideal.

Two exact source-bound three-factor decompositions split every physical
point into nine branch pairs, and central symmetry reduces these to five
representatives.  Positive `SU(2)` Gram minors make the Cramer
determinant nonzero.  On the `F0/H2` representative, however, exact
localization away from

```text
Tb^3+3*Tb^2+2*Tb-1
```

leaves a nonzero 24-dimensional quotient over `QQ`.  Its 29 leading
monomials have exactly 24 standard monomials.  Thus the earlier
equal-dimensional argument excluding extra points on this branch was
invalid.

Each component has exactly eight real points, all irreducible `SU(2)`
characters.  The plastic count follows from two isolated real roots of
its degree-six base polynomial, positivity of both quadratic
radicands, and positivity of all three leading quaternion-Gram minors.
The known count follows from the unique real root of
`u^3-4u^2+5u-1`, two positive roots for `s^2`, and its positive
quaternion-Gram minors.

Each of the four reviewed components still has eight real irreducible
`SU(2)` points.  Their complete saturated relation lattices have rank
`8` in `Z^13`, equivalently multiplicative quotient rank `5`.  Those
componentwise facts do not classify the new residual.

The prior statement that the real physical `abc` locus has exactly 32
points is withdrawn.  The new residual still requires exact separation,
all-real-embedding isolation, compact `SU(2)` Gram signs, irreducibility,
and complete thirteen-eigenvalue lattices before either a survivor or a
no-go can be asserted.  RUR and reduced-basis timeouts are
non-conclusions.

No complete compact `SU(2)` Chern--Simons value is computed, no
`SO(3)` or `PSL(2,C)` value is substituted, no irrationality modulo
integers is proved, and no candidate is emitted.

Current proof and replay:
[`CLOSED_SURFACE_CUBED_MIXED_RANK3_ABC_CLASSIFICATION.md`](../../../../../research/CLOSED_SURFACE_CUBED_MIXED_RANK3_ABC_CLASSIFICATION.md).
