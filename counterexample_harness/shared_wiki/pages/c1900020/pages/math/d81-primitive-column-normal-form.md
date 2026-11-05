---
title: D81 primitive-column normal form boundary
description: Every quotient section has one primitive column, orientation, Bezout shear, and shared exact normalization carry; the P_n escape family is incoming-infeasible.
---

For a fixed level, let
\[
L=\begin{pmatrix}\mu_1&\mu_2\\ \nu_1&\nu_2\end{pmatrix}
\]
be the incoming/outgoing quotient form. Every complete quotient section
is uniquely represented, up to translating its shear index, by a
primitive column \(c=(x,y)^t\), an orientation
\(\delta\in\{-1,1\}\), one Bezout completion \(d_0\), and
\[
H_k=[c,d_0+kc],\qquad k\in\mathbf Z.
\]
Its tail coordinates are
\[
s=\mu_1x+\mu_2y,\quad \beta=\nu_1x+\nu_2y,\quad
t_k=t_0+ks,\quad\gamma_k=\gamma_0+k\beta.
\]

If the normalized \(k=0\) basis is \((C,y_0,z)\), the one shared carry
\[
c_k=-\left\lfloor\frac{y_0-kz}{C}\right\rfloor
\]
gives
\[
[Y]_{B_k}=(r_0-sc_k,s,t_0+ks),\qquad
[Z]_{B_k}=(\alpha_0-\beta c_k,\beta,\gamma_0+k\beta).
\]
Thus all Bezout representatives, shears, and normalization carries are
retained without fixed anchors.

At every fixed level, \(0\le s\le F_0\) and
\(|\beta|\le2F_1\) bound the primitive columns because \(\det L\ne0\);
the remaining tail inequalities then give a finite derived interval for
each shear. This finiteness is not uniform across levels because the
lattice, bounds, conductor cosets, carries, and true-word matrices move.

For the \(h=21,j=0\) discriminator \(P_n=(n,n^2+1)^t\),
\[
s(n)=-(8754288959n^2+783715063n+8754288959)<0
\]
for every integer \(n\), since the quadratic in parentheses has negative
discriminant. Hence the primitive family used to prove finite-anchor
incompleteness contains no feasible incoming section, under either
orientation or any shear. The unresolved directions are the primitive
columns in the moving thin strip where
\(\mu_1x+\mu_2y\) nearly cancels.

Adjacent levels remain coupled by
\[
W_j=B_j(t_j^{2h}B_{j+1})^{-1}.
\]
Complete equality-aware peeling of \(W_j\) is necessary and sufficient,
but no recursive accepting component or uniform all-level exclusion is
currently known.
