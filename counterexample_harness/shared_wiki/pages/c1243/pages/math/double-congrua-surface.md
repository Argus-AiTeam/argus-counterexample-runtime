---
title: Double-congrua surface for the normalized Lucas square
description: Exact parameterization, collision locus, tangent ansatz, and elliptic quotient used by the R2 construction.
---

# Double-congrua surface

Let

\[
\delta(z)=\frac{4z(1-z^2)}{(1+z^2)^2}.
\]

The identities

\[
1+\delta(z)=\left(\frac{z^2-2z-1}{1+z^2}\right)^2,\qquad
1-\delta(z)=\left(\frac{z^2+2z-1}{1+z^2}\right)^2
\]

parameterize every rational \(q\) for which \(1+q\) and \(1-q\) are
rational squares. For the normalized Lucas square, put

\[
x=\delta(b),\qquad y=\delta(a).
\]

Then all nine cells are rational squares exactly when there are rational
\(s,t\) such that

\[
\delta(t)=\delta(a)+\delta(b),\qquad
\delta(s)=\delta(b)-\delta(a).
\]

Indeed, \(a,b,t,s\) respectively supply square roots for the symmetric
pairs with deviations \(y,x,x+y,x-y\). Conversely, parameterizing each
pair of rational squares whose sum is \(2\) recovers \(a,b,t,s\).

With \(N(z)=4z(1-z^2)\) and \(H(z)=(1+z^2)^2\), the affine surface is the
complete intersection

\[
\begin{aligned}
N(t)H(a)H(b)-N(a)H(t)H(b)-N(b)H(t)H(a)&=0,\\
N(s)H(a)H(b)-N(b)H(s)H(a)+N(a)H(s)H(b)&=0.
\end{aligned}
\]

Because \(H(z)>0\) over \(\mathbb Q\), clearing these denominators adds no
rational affine components.

## Exact collision locus

The nine deviations from the center are all linear forms
\(\alpha x+\beta y\) with \((\alpha,\beta)\in\{-1,0,1\}^2\). Two cells
coincide exactly on one of eight lines. Thus pairwise distinctness is
equivalent to

\[
xy(x^2-y^2)(x^2-4y^2)(4x^2-y^2)\ne0.
\]

Equivalently, the degenerate locus is the vanishing set of that product
after substituting \(x=\delta(b)\) and \(y=\delta(a)\).

## Tangent addition ansatz

The natural angle-addition substitution

\[
t=\frac{a+b}{1-ab},\qquad s=\frac{b-a}{1+ab}
\]

does not produce a nondegenerate point. Its two exact residuals factor as

\[
\frac{32ab(a+b)(ab-1)}{(1+a^2)^2(1+b^2)^2},\qquad
\frac{-32ab(a-b)(ab+1)}{(1+a^2)^2(1+b^2)^2}.
\]

Outside \(ab=0\), simultaneously choosing one factor from each numerator
is either inconsistent or forces \(a,b\in\{1,-1\}\). In every rational
case \(\delta(a)\delta(b)=0\), which lies on the collision locus.

## Elliptic quotient of a fixed \(a\)-fiber

Fix \(y=\delta(a)\ne0\). If \(P=R^2\) and \(Q=S^2\) encode the differences
of signed roots for the \(x\) and \(x+y\) square pairs, their quotient
cubic is

\[
(P+Q)(PQ+y^2)=8PQ.
\]

Writing \(u=P+Q\), \(v=P-Q\), the map

\[
X=\frac{y^2(u-8)}u,\qquad
Y=\frac{4y^2(8-u)v}{u^2}
\]

lands on

\[
Y^2=X^3+(16-2y^2)X^2+y^4X.
\]

An elliptic point contributes to the original surface only when its
inverse values \(P,Q\) are both nonzero rational squares; the remaining
\(x-y\) pair must then be tested separately. For \(y=n/d\), the integral
model is

\[
y_E^2=x_E^3+(16d^2-2n^2)x_E^2+n^4x_E,
\quad x_E=d^2X,\quad y_E=d^3Y.
\]

### Verified scope at \(a=1/4\)

For \(y=240/289\), the integral curve is

\[
y_E^2=x_E^3+1221136x_E^2+3317760000x_E.
\]

It has a certified rank-one full basis, saturated through 1000, and
complete torsion \(C_8\). In the coefficient interval \([-100,100]\)
crossed with all torsion, exactly 1,608 elliptic points occur. Eight have
nonzero square \(P,Q\); four fail the remaining pair and four complete
points have \(x=0\). This is only a finite fixed-fiber exclusion.
