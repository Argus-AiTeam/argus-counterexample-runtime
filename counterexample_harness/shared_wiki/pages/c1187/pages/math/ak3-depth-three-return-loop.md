---
title: AK(3) depth-three G2 return-loop boundary
description: Complete unrestricted S2 fiber, five-column first-relative-grade operator, and an exact diagonal norm obstruction for the G2,H,G2,I cell.
---

# AK(3) depth-three \(G_2\) return-loop boundary

For

\[
G_2=((1,2),(1,3)),\qquad H=((0,1),(1,1)),
\]

no point of the complete unrestricted \(S_2\) Laurent fiber of the
three-internal-update cell with successive bases

\[
G_2,\ H,\ G_2,\ I
\]

lifts to \(S_3=F/F'''\), in any of the eight ordered component
patterns. This excludes one fixed depth-three cell, not other basis
sequences or longer cells, and it is not an Andrews--Curtis
counterexample.

## Word-derived three-update law

Starting with the original AK(3) words, exact free Nielsen maps with
the required cumulative bases are

\[
\begin{aligned}
\Phi_0(a,b)&=(ab^2,ab^3),\\
\Phi_1(a,b)&=(a^{-1}b,ab^{-1}a),\\
\Phi_2(a,b)&=(ba,ba^2),\\
\Phi_3(a,b)&=(ab^{-1}ab^{-1}a,a^{-1}b).
\end{aligned}
\]

Their composite is the identity as a free-group automorphism. A
three-variable Fox-matrix recurrence, checked in every component
pattern before specialization, gives

\[
D=\Delta+(AB^2-1)(AB^3-1)(f_1+f_3)
 +(B-1)(AB-1)f_2.
\]

Every mixed or higher formal coefficient is zero. Separate direct
free-word computations reproduce the same matrices.

The determinant law is the reviewed \(n=2\) depth-two law with first
parameter \(f_1+f_3\) and second parameter \(f_2\). Its complete
fiber is therefore

\[
\begin{aligned}
f_1&=\rho,\\
f_1+f_3&=F(B)+A^2-1+(A-1)(B-1)p,\\
f_2&=-B^{-2}-(1+B)(1+B+B^2)F(B)\\
&\quad+K(A^{-1})+7+(A-1)(B-1)q,
\end{aligned}
\]

where \(F(1)=1\), \(K(1)=-7\), and
\(\rho,F,K,p,q\) have arbitrary finite Laurent support. Thus the
first/third split is genuinely unrestricted.

## Complete five-column image

In the first relative grade, retain the three internal relation-cycle
slots and both terminal slots. After removing endpoint factors, the
operator in pattern \((i,j,k)\) is

\[
N_{ijk}=[P_i,Q_j,P_k,C_a,C_b].
\]

The entries \(P_i,Q_j,C_a,C_b\) are the reviewed \(n=2\) columns; the
third \(P_k\) is reconstructed independently from the third word
update. Exact relation-word responses and every terminal axis-power
pair in \(\{-1,0,1\}^2\) are checked in all eight patterns. With
\(\mathfrak a=(X-1,Y-1)\) and

\[
A^-=\ker(1+\sigma)=\operatorname{im}(1-\sigma),\qquad
\sigma(U,V)=(X/U,Y/V),
\]

the complete image is

\[
\operatorname{im}N_{ijk}=\mathfrak a(A^-)^2.
\]

Hence the cokernel is obtained by \(X=Y=1\), with
\(t^*=t(U^{-1},V^{-1})\). Terminal axis powers become outer units and
do not change this cokernel.

## Diagonal obstruction

Write

\[
f_1+f_3=A^2+(B-1)h,\qquad f_1=\rho.
\]

Enlarging \(f_2\) to an arbitrary Laurent polynomial \(g\) only makes
nonmembership harder. Direct second-Fox collection from the original
words gives, in every component pattern,

\[
\Psi_{ijk}(h,\rho,g)-\Phi_2(h)\in(UV-1)\Lambda,
\]

where \(\Phi_2\) is the reviewed complete \(n=2\) residual. If
\(z=L-Dh\) and \(\mathcal N=L^*L+DC\), then

\[
z^*z=\mathcal N-D\Phi_2(h).
\]

At

\[
(U,V)=(\zeta_3^{-1},\zeta_3),
\]

the return-loop correction vanishes because \(UV=1\), while exact
cyclotomic arithmetic gives

\[
\mathcal N(\zeta_3^{-1},\zeta_3)=-14.
\]

A zero residual would therefore imply \(z^*z=-14\). But for
\(z=x+y\zeta_3\),

\[
z^*z=x^2-xy+y^2\geq0.
\]

This contradiction covers arbitrary finite support in the complete
fiber and all five relation-cycle slots.

The exact derivation and replays are in
[`THEOREM.md`](../../../../../research/experiments/ak3-depth-three-return-loop/THEOREM.md),
`s2_fiber.py`, `depth_three_probe.py`, and
`diagonal_obstruction.py`.
