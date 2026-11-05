---
title: Cho--Lemke Oliver--Zaman cycle-type Kummer negative edge
description: One order-2q rational class forces a Fibonacci negative edge, but its discriminant-scale least-prime bound has no uniform linear successor cost.
---

# Cho--Lemke Oliver--Zaman cycle-type Kummer negative edge

For an odd prime \(q\ne5\), put

\[
\eta=\left(\frac{1+\sqrt5}{2}\right)^2,\qquad
L_q=\mathbb Q(\sqrt5,\zeta_q,\eta^{1/q}).
\]

The reviewed Cera degree contract gives

\[
[L_q:\mathbb Q]=2q(q-1),
\]

and the exact Galois group is

\[
\operatorname{Gal}(L_q/\mathbb Q)
\cong\operatorname{AGL}_1(\mathbb F_q)\times C_2.
\]

Writing \(\tau\) for Kummer translation and \(s\) for simultaneous
quadratic, cyclotomic, and radical inversion, all lifts of the base
inversion are \(\tau^a s\). The pure lift \(s\) has order \(2\); the
\(q-1\) lifts with \(a\ne0\) have order \(2q\) and form one rational
equivalence class \(C_q\).

On the roots of

\[
X^{2q}-3X^q+1,
\]

the class \(C_q\) is exactly the single-cycle type \((2q)\). Every
unramified prime \(p\) with Frobenius in this class has

\[
\left(\frac5p\right)=-1,\qquad p\equiv-1\pmod q,\qquad
\eta^{(p+1)/q}\ne1.
\]

Hence \(q\mid\rho_F(p)\mid p+1\), so this is a genuine negative Fibonacci
successor condition. Its density is \(1/(2q)\), the first finite stratum
of Cera's full density

\[
\frac{q}{2(q^2-1)}
=\frac1{2q}+\frac1{2q^3}+\cdots.
\]

Thus the full Cera inclusion-exclusion set must not be identified with one
Frobenius class.

For this class, Cho--Lemke Oliver--Zaman v1 Theorems 1.1 and 2.1 give,
for each fixed \(q\) and \(\epsilon>0\),

\[
p\ll_{q,\epsilon}
|\operatorname{Disc}(L_q)|^{1/q+\epsilon}.
\]

The implied constant depends on polynomial degree \(2q\) or group order
\(2q(q-1)\), and on \(\epsilon\). The field discriminant satisfies

\[
5^{q(q-1)}q^{2q(q-2)}
\le|\operatorname{Disc}(L_q)|
\le5^{q(q-1)}q^{4q^2-6q}.
\]

At the source-guaranteed effective choice
\(\epsilon=2/(q(q-1))\), this yields only

\[
p\le A_q\,5^{q+1}q^{4q+2-4/(q-1)},
\]

with no v1 bound on \(A_q\) as \(q\) varies. The condition gives minimum
exact-height gain one but no cofactor-height information. It therefore
does not imply bounded edge cost, cumulative logarithmic cost \(O(L)\), or
one fixed-exponential exact-class family. This limitation applies only to
the direct cycle-type/Kummer transfer; it is not a lower bound for actual
least successors.
