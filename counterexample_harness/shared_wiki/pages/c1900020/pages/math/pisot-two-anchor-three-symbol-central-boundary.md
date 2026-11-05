---
title: Three-symbol two-anchor central boundary
description: Exact status and limitations of the epsilon three-symbol suffix classification.
---

For the positive unit \(u=\epsilon\), target level \(m+1\), and word

\[
(1,1),(7,B),(c,1),(d,b),(e,f),(g,k),
\]

every integral anchor has the reversible normal form

\[
D=E+eC,\quad P=\psi D+C,\quad
Q=aD+HP+O,\quad L=P-zQ.
\]

The anchor equations reduce to one trace-resonance equation, one scalar
divisibility, and the original digit inequalities. The complete \(R=0\)
branch has no determinant \(+1\) or \(-1\), without a parameter cutoff.

For \(R\ne0\), source unimodularity is equivalent to the normalized
lower-right entry being one or one of four explicit central Euclidean
distances being one. The lower-right-entry locus is now excluded for
every \(m\ge6\) and every legal \(K\)-branch. Its exact elimination is
\[
(jC-D_t)Y=F(J+\gamma d)-D_t-J(1+c);
\]
uniform trace and digit inequalities make the left side strictly larger
in absolute value than the right. Thus four distance-one loci, rather
than five central loci, remain.

Retaining both actual Euclidean quotients gives a shear-free scalar test
for each remaining position:
\[
\rho A_S+r_0B_S=-y_S,\qquad
k=\frac{y_S+\delta\rho}{B_S}\in\mathbb Z,\qquad
k\equiv-r_0\pmod\rho.
\]
The degeneration \(1-k\psi=0\) is impossible in every exceptional and
nonexceptional \(K\)-branch. The old \(m=7\) fixed-divisor obstruction
does not extend to nonzero coefficient: its target-quotient divisibility
reduces to an identity. Scalar integrality and digit inequalities are
therefore essential.

The exceptional branch \(B=7,c=1,K=2\) is completely excluded. Its
low chamber \(0\le d\le36\) is impossible without a parameter cutoff:
legality forces \(d\le2\), \(|\psi|=1\), and \(e=0\), after which the
last anchor equation gives the contradictory strict interval
\[
4-d<b<5-d.
\]

In the exceptional high chamber, the complementary source-covector
positions, which are the second and fourth central distances, are also
excluded cutoff-free for every \(m\ge6\). Exact resonance confines their
positive and negative scalar parameters to complementary intervals
between \(P/3\) and \(P/2\); the scalar test then forces either
\(0<|\psi|<1\) or the impossible endpoint remainder \(C_1=1\).
For the first and third positions, the \(h=0\) subcase has an immediate
scalar contradiction. The \(h\ge1\) kernel is excluded by the exact
quotient-free resultant identities and complementary size bounds. Thus
all four exceptional high-chamber positions are empty.

The nonexceptional branches are now also exhausted:
\[
\nu=1,\ K\ge8,\qquad\text{or}\qquad \nu=2,\ K\ge3.
\]
The second and fourth positions have the reviewed gap
\[
S(2E-C)>C+2P.
\]
For the first and third positions, retain the actual source quotient
\[
h=\left\lfloor\frac{XT-s}{U}\right\rfloor,\qquad
O=XT-s-hU,
\]
and write
\[
\begin{aligned}
E&=(K+6\nu)O-7X+6h,\\
C&=(K+7\nu)O-8X+7h.
\end{aligned}
\]
The exact source minor is
\[
M(E+eC)-C(E_b+eM)=P.
\]
Jacobian independently replays this determinant with operation
`matrix.symbolic.determinant.compute`; the local verifier checks the
full sign and inequality argument.

For the two adjacent positive resonance representatives
\[
a_-=W-NP,\qquad a_+=(N+1)P-W,
\]
every nonzero resonant \(r_\ast=1-k\psi\) has
\[
|r_\ast|\ge S:=\min(a_-,a_+).
\]
Writing \(X=10h+j\), the verifier proves at both endpoints \(h=0\)
and \(C=0\), by positive-coefficient expansions on the exact trace
cone, that
\[
\boxed{S(2E-C)>C+2P.}
\]
Concavity in \(h\) fills the complete unbounded source chamber. The
proof covers the exceptional scalar sign chamber \((e,\psi)=(0,-1)\)
where \(|r_\ast|<M\) is false and therefore cannot be assumed.

The scalar unit equation then forces \(e=0\) and \(\psi=-1\). Returning
to the original digit equations gives
\[
P(b-d)=-X(U-T)-2Pd-2s<0,
\]
contradicting \(b\ge d\). Hence the first and third nonexceptional
central distances cannot equal one either.

At \(m=7\), the coefficient-zero versions of all four central unit
systems are also exhausted exactly. With
\[
M=16T_{8}-7=1614244169=41\cdot283\cdot139123,
\]
a putative unit point forces \(g\mid M\) and an internal bound
\(u<M+(2T_7-1)\). The complete resulting classification has 666 source
classes, 4,170 target remainders, and 75,246 legal \(F\)-factorizations;
all fail the exact target-quotient divisibility. This is the requested
\(m=7\) continued-fraction control, not the full \(R\ne0\) theorem.

The same \(m=7\) control exhibits an infinite legal high-chamber
component with \(R=\psi=-1\), \(d=37+q\), and unbounded quotient \(q\).
Its four central distances are constant and greater than one, so it is
a nonreturn family and proves that finite quotient bounds cannot close
these systems.

Two stronger shortcuts are false:

- A legal \(m=6\) anchor has a mixed-sign central split vector, so raw
  coordinatewise split positivity cannot prove the four exclusions.
- In the exceptional \(B=7,c=1\) chamber, the exact legal tuple
  \((X,d,y,r,t,F,e,x)=(55,39,2147,126653,874,38925,12944,473062)\)
  has \(n=td-y=31939>36t\) while
  \(\kappa=tJ-n(2T-1)=1520779>0\). Thus positivity of \(\kappa\)
  does not supply the proposed uniform \(tX\) bound.
- A legal exact anchor makes the hypothetical forced-\(e\) expression
  fall below \(-1\), so an unconditional claim that this expression
  always lies in \((-1,1)\) cannot force \(e=0\).

No integral unimodular advancing return exists in the complete declared
epsilon three-symbol two-anchor domain. This is an exact exhausted
boundary for that construction, not a Jacobi--Perron counterexample.
Finite probes, including \(|R|\le5000,d\le40\) in the exceptional
chamber, remain discovery evidence only and are not used in the
cutoff-free conclusion.
