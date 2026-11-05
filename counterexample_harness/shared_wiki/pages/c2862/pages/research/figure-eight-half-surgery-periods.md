---
title: Figure-eight half-surgery periods
description: Exact branch lifts, surgery correction, dilogarithmic formulas, the rho_1 extended Bloch obstruction, and the remaining transcendence gap.
---

# Figure-eight half-surgery periods

For each of the four unitary roots `T_j` of

```text
P(T)=T^7+2T^6-6T^5-12T^4+5T^3+10T^2-1,
```

the upper-half-plane meridian eigenvalue

```text
s_j=(T_j+i sqrt(4-T_j^2))/2
```

is algebraic.  With `u_j=r(T_j)-2`, the four endpoints lie on the two
Riley arcs in the order `u_-,u_+,u_+,u_-`.  The continuously lifted
longitude angles satisfy

```text
-theta_j+2 beta_j = 0,2,1,-1
```

for `rho_1,...,rho_4`, respectively.

For the filling matrix `(p,q)=(-1,2)`, `(c,d)=(0,-1)`, the complete
second-Chern `SU(2)` formula is

```text
CS(rho_j) =
  -1/6 + 2 beta_j^2
  -2 integral_(1/6)^(theta_j) beta_e(t) dt          (mod Z).
```

The `+2 beta_j^2` term is the solid-torus correction.  The initial
`-1/6` comes from the Kirk--Klassen connector integral `1/12`.
Orientation reversal negates the class; the `SO(3)` first-Pontryagin
normalization is four times this value.

Andersen--Hansen's principal-branch formula gives the same classes as

```text
Psi_n^(0,b)(x,y)
 = b y - n^2/2 + x^2/8 + n x/2 - x y
   +(Li_2(s^2 w)-Li_2(s^2/w))/(4 pi^2),
```

with `(b,n)=(0,0),(1,0),(0,1),(1,1)`.

Arb 320-bit enclosures give

| branch | certified `CS` in `[0,1)` |
|---|---|
| `rho_1` | `(0.82811712718492, 0.82811712718494)` |
| `rho_2` | `(0.23515976637046, 0.23515976637048)` |
| `rho_3` | `(0.51412567950423, 0.51412567950424)` |
| `rho_4` | `(0.05393357576718, 0.05393357576719)` |

These intervals uniquely identify the four Kirk--Klassen rows within
`10^-5`, but show that several last printed digits were not correctly
rounded.  They are numerical checks only.

The exact values are weight-two logarithmic/dilogarithmic periods at
algebraic endpoints.  Baker--Wustholz results apply to linear relations
among logarithms and ordinary `1`-periods, not to these iterated periods.
Bloch-group regulator results likewise do not prove that a selected real
coordinate is outside `pi^2 Q`; the stronger relevant injectivity statement
is conjectural.  No irrational `SU(2)` Chern--Simons candidate follows.

## `rho_1` extended Bloch class

For `rho_1`, put `q=s^2`, `a=qw`, and `b=q/w`.  The Riley and filling
relations give

```text
ab=q^2,  (1-a)(1-b)=q,
ell=(1-a)/(w(1-b))=L^-1,  L^2=s.
```

Hence `xi=[a]-[b]` has zero ordinary Bloch boundary.  With principal
logarithms, the exact full-`SL(2,C)` even flattening is

```text
xi_hat=[a;2,0]-[b;0,0],
L_hat(xi_hat)=4*pi^2*Psi_0^(0,0)  (mod 4*pi^2).
```

A rationally isolated nonphysical embedding has `Im(a)<0<Im(b)`, so its
Bloch--Wigner coordinate `D(a)-D(b)` is strictly negative.  Thus `xi` has
infinite order.  Five-term relations preserve this ordinary image, while
root-of-unity corrections lie in the forgetful kernel.  The proposed
torsion/root-of-unity reduction to a pure logarithmic expression is
therefore impossible.

This does not prove the physical real regulator irrational: non-torsion is
detected at another embedding, and no theorem excludes
`L_hat(xi_hat) in 4*pi^2 Q`.  The exact derivation and interval certificate
are in `research/RHO1_EXTENDED_BLOCH.md` and
`research/verify_rho1_bloch.py`.
