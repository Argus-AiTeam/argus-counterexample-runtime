---
title: Punctured-torus minus-six regulator
description: Complete SU(2) path, principal dilogarithm, even-SL flattening, cubic Bloch descent, and the unresolved real-regulator theorem gap.
---

# Punctured-torus minus-six regulator

For the unique physical root of

```text
x^3-x^2-x+2=0
```

choose the stable normalization with positive trace.  The exact
irreducible `SU(2)` representation satisfies

```text
C*T^-6=I
```

literally, with standard primitive slope `(-6,1)`.  If `s` is the
upper-half-plane meridian eigenvalue, `r=s^2`, `w=x-1`, and
`s=exp(2*pi*i*theta)`, then the representation lies on the lower Riley
arc with

```text
1/6 < theta < 1/4,
L=r^3=s^6,
beta=6*theta-1,
-6*theta+beta=-1.
```

Including the connector and solid-torus correction, the complete
second-Chern-normalized class is

```text
CS = -1/6 - 6*theta^2 + 2*theta*beta
     - 2*integral_(1/6)^theta beta_-(t) dt          (mod Z).
```

With

```text
X=2*theta,
Y=Log(w)/(2*pi*i),
a=r*w,
b=r/w,
```

the exact principal-branch expression is

```text
CS = -X + 3*X^2/2 - X*Y
     +(Li_2(a)-Li_2(b))/(4*pi^2)                    (mod Z).
```

The phase integers are `(-1,0,0)`.  In the full Goette--Zickert
even-label `SL(2,C)` convention,

```text
xi_hat=[a;4,0]-[b;-2,0]
```

has zero extended boundary and

```text
L_hat(xi_hat)=4*pi^2*CS                              (mod 4*pi^2).
```

There is an exact cubic descent.  Put

```text
y=-1/w,
z=1/(1+y^2)=y/(1-y),
y^3+2*y-1=0.
```

Five explicit five-term relations prove that the ordinary image of
`xi_hat` differs by at most 2-torsion from

```text
beta=2*[y]-[z].
```

An exact nonphysical embedding gives a strictly nonzero Bloch--Wigner
coordinate, so `beta` is non-torsion.  This excludes a reduction to
extended torsion or a pure logarithmic kernel term.

It does not prove irrationality of the physical class.  Rationality is
equivalent to rationality of the real Rogers period

```text
(2*L0(y)-L0(z))/(4*pi^2).
```

Neumann--Yang Example 9.6 contains the same abstract cubic Bloch
direction.  It separately reports an apparently irrational decimal for a
sum of Chern--Simons values and uses the Ramakrishnan conjecture only for a
trace-field containment prediction; it does not claim that the conjecture
proves the sum irrational.  Its example is `PSL(2,C)` and is not used to
change the `SU(2)` normalization here.  No unconditional theorem
currently used by the campaign decides this single real regulator
coordinate, so the special negative-six functional-reduction route is
retired without refuting irrationality.

The exact proof and replay are in
`research/PUNCTURED_TORUS_MINUS_SIX_REGULATOR.md` and
`research/verify_punctured_torus_minus_six_regulator.py`.
