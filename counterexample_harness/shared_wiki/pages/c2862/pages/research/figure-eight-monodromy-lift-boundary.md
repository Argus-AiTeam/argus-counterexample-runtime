---
title: Figure-eight monodromy lift boundary
description: Exact bundle presentation, twist-eigenvalue rank, and the classical compact-boundary lift limitation.
---

# Figure-eight monodromy lift boundary

In the fixed Kirk--Klassen convention, the figure-eight exterior has the
once-punctured-torus bundle presentation

```text
<alpha,beta,t |
  t alpha t^-1 = alpha beta alpha,
  t beta  t^-1 = beta alpha>.
```

The exact two-way change of generators is

```text
t=x,
alpha=x y x^-2,
beta=x y^-1 x y x^-2,

x=t,
y=alpha beta^-1 t.
```

The preferred peripheral words are `mu=t` and
`lambda=[alpha,beta]`, so the half-surgery relation is
`t^-1[alpha,beta]^2=1`.  With the declared based twists

```text
D_alpha^+: alpha -> alpha,         beta -> beta alpha,
D_beta^+:  alpha -> alpha beta^-1, beta -> beta,
```

the monodromy is `D_alpha^+ o (D_beta^+)^-1` and has matrix
`[[2,1],[1,1]]`.

For every certified branch with `rho(y)=A`, `rho(x)=B`,

```text
rho(alpha)=B A B^-2,
rho(beta)=B A^-1 B A B^-2.
```

Their traces are `r(T)` and `T^2-r(T)-1`.  The corresponding algebraic
unit eigenvalues are multiplicatively independent modulo roots of unity:
the two quadratic discriminants define independent square classes over
`Q(T)`, and neither eigenvalue is a root of unity.  Thus the two actual
twist angles have multiplicative rank two, not one.

Goldman supplies the base Hamiltonian twist flow, Marche supplies a
closed-surface angle-flow lift, and the fixed-point/mapping-torus phase
theorem exists for closed or suitably punctured surfaces.  The audited
sources do not identify these with Freed's pointed, parametrized,
trivialized compact-boundary line and its correction one-form, nor with
the Kirk--Klassen solid-torus trivialization.  A projective quantum phase
cannot replace that missing classical calibration.  Therefore no
twist-derived scalar is currently proved equal to the four reviewed
`SU(2)` periods in `R/Z`.
