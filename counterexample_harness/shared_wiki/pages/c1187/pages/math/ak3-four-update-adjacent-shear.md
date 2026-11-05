---
title: AK(3) adjacent-shear four-update boundary
description: Complete four-parameter S2 fiber and an exact all-integer, two-sign S3 exclusion for successive companion shears.
---

# AK(3) adjacent-shear four-update boundary

For

\[
K_{n,\epsilon}=
\begin{pmatrix}
-n&\epsilon\\
-1&0
\end{pmatrix},
\qquad n\in\mathbb Z,\quad\epsilon\in\{-1,+1\},
\]

consider the normalized AK(3) cell with successive bases

\[
G_2,\ H,\ K_{n,\epsilon},\ K_{n+1,\epsilon},\ I.
\]

The exact free maps are

\[
T_{n,\epsilon}=(b^\epsilon a^{-n},a^{-1}),
\qquad
T_{n,\epsilon}^{-1}=
\begin{cases}
(b^{-1},ab^{-n}),&\epsilon=1,\\
(b^{-1},b^na^{-1}),&\epsilon=-1.
\end{cases}
\]

They satisfy
\(T_{n,\epsilon}^{-1}T_{n+1,\epsilon}=(ab,b)\) as
actual free words.  The four-update determinant law is

\[
\begin{aligned}
D={}&\Delta +(AB^2-1)(AB^3-1)x
 +(B-1)(AB-1)y\\
& +(A^{-n}B^\epsilon-1)(A^{-1}-1)z\\
& +(A^{-n-1}B^\epsilon-1)(A^{-1}-1)w.
\end{aligned}
\]

Its complete unrestricted \(S_2\) fiber has free \(z\)-axes of common
augmentation \(\mu\), free \(w\)-axes of common augmentation \(\nu\),
a free \(x_+\) axis of augmentation
\(1-n\mu-(n+1)\nu\), and a free \(y_-\) axis of augmentation
\(-7+6n\mu+6(n+1)\nu\).  The other axes are

\[
x_-=T^{-2}-T^2(U_nz_-+U_{n+1}w_-),\qquad
y_+=-T^{-2}-U_2U_3x_+.
\]

Each parameter has an independent
\((A-1)(B-1)\)-multiple, so no support bound is present.  The adjacent
directions obey

\[
P_{n+1}=A^{-1}P_n+(A^{-1}-1)^2
\]

and are nonassociate for every \(n\) and both signs.  For odd \(n\),
\(A=B=-1\) annihilates the previous three determinant directions but
gives \(P_{n+1}=4\), proving the stronger ideal independence in those
cells.  No such stronger even-\(n\) assertion is used.

Exact Fox--Magnus collection starts from the original AK(3) words and
retains four arbitrary Laurent families.  Its first reduced \(S_3\)
residual contains exactly the same nine \(h,r\) monomials as the
reviewed companion-family obstruction; the third and fourth families
are identically absent before specialization.

At \(A=B=t\), where \(t\) is a primitive seventh root, the retained
states of \(a^7\) and \(b^7\) are the identity.  The middle shear is
independent of \(n\), so every residual coefficient is exactly
seven-periodic.  All fourteen sign/residue classes and all sixteen
component patterns give one Hermitian form.  Its leading minor,
determinant, and completed-square numerator are

\[
13+33s+17s^2,\quad
-56-175s-91s^2,\quad
-1583-4318s-1703s^2,
\]

where \(s=t+t^{-1}\in(-223/500,-89/200)\).  Exact endpoint bounds make
all three positive, so the first residual cannot vanish for any
finite Laurent parameters.

The four internal and two terminal relation-cycle slots have
downstream augmentation matrices

\[
H^{-1}M_{\Phi_1},\ H^{-1},\
K_{n,\epsilon}^{-1},\ K_{n+1,\epsilon}^{-1},\ I,\ I.
\]

The universal insertion response \(h^{-1}(g-1)e\) has zero ordinary
augmentation, hence the reduced \(2\times6\) outer-augmentation
operator is zero for every \(n\), both signs, and all sixteen patterns.
Arbitrary terminal powers act by nonzero Laurent units.

Therefore the complete unrestricted adjacent-shear four-update family
has no lift to \(S_3\).  This is not an Andrews--Curtis counterexample
and does not decide other four-update cells.

The proof and exact certificates are in
[`THEOREM.md`](../../../../../research/experiments/ak3-four-update-adjacent-shear/THEOREM.md),
`four-update-certificate.json`,
`four-update-relation-operator.json`, and
`adjacent-shear-certificate.json`.
