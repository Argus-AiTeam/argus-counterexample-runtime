---
title: Periodic-extension Nielsen-torsion boundary
description: Exact AC3 failure of the unmodified torsion and a balanced-lift obstruction for the smallest recovered power tuple.
---

The unmodified Lustig--Moriah Nielsen torsion does not descend to the
Andrews--Curtis relation. Let

\[
G=F(x,y)/(F(x,y)^7\gamma_7(F(x,y))),\qquad
\mathcal U=(x,y),
\]

and apply one AC3 move with \(h=xy\):

\[
\mathcal V=(hxh^{-1},y).
\]

The group \(G\) is a finite periodic nilpotent \(7\)-group, and both tuples
minimally generate it. In

\[
A=\mathbb F_7[X,Y]/(X,Y)^6,\qquad x\mapsto1+X,\quad y\mapsto1+Y,
\]

the Fox ideal vanishes. Seventh-power derivatives contain
\((u-1)^6=0\), while derivatives of \(\gamma_7(F)\) lie in
\((X,Y)^6=0\). The component-conjugation Fox matrix has determinant

\[
1-x+xy=1+Y+XY.
\]

The typed Jacobian operation `matrix.symbolic.determinant.compute`
independently returns \(1-x+xy\). None of the 98 trivial-unit images

\[
\pm(1+X)^a(1+Y)^b,\qquad a,b\in\mathbb F_7,
\]

equals \(1+Y+XY\). Constant and linear terms would force \(1+Y\), which
misses the nonzero \(XY\) term. Thus one AC3 move changes the
Lustig--Moriah torsion class.

The smallest power tuple recoverable from the cited Moriah--Shpilrain
application is \((x^2,y^2)\) in \(B(2,7)\). Every free lift has
exponent-sum matrix congruent to \(2I_2\) modulo seven, hence determinant
four modulo seven. A pair normally generating \(F_2\) must have integer
abelianization determinant \(\pm1\), which reduces to one or six modulo
seven. Therefore this tuple has no balanced normal-generating free lift.

These are exact negative witnesses for the proposed route. They retire the
unmodified Nielsen-torsion mechanism and this recovered source tuple, not
every possible quotient of the torsion group and not any unrelated
torsion invariant. They yield no Andrews--Curtis counterexample, and
campaign claim C1187 remains open.

The complete proof, source-access boundary, deterministic verifier,
certificate, and typed Jacobian record are in
`research/experiments/periodic-extension-n-torsion/`.
