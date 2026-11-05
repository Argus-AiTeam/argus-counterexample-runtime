---
title: Fixed-translate conformal cusp candidate
description: Exact alpha=2/3 model-cusp construction and its source-fidelity boundary.
---

# Fixed-translate conformal cusp candidate

For \(\alpha=2/3\), let

\[
\Omega=\{\zeta:|\zeta-1|<1/4,\ \operatorname{Im}\zeta>0\},
\qquad
f(\zeta)=\zeta^2+i\zeta^3,
\qquad
D=f(\Omega).
\]

The real-part bound
\(\operatorname{Re}f'(\zeta)\ge3/8\) makes \(f\) injective on the closed
half-disk.  Writing \(f(u+iv)=X+iY\), the exact identity

\[
Y^2-X^3
=v\bigl[u^2(3v^2-3v+1)+v(1-v)^3\bigr]
\bigl[(3u^2-v^2)^2+4u^2\bigr]
>0
\]

shows \(D\subset C_{2/3}\).  The diameter interval
\([7/8,9/8]\) maps to

\[
E=\{u^2+iu^3:7/8\le u\le9/8\}
\subset\partial D\cap\partial C_{2/3}.
\]

An explicit map from \(D\) to the upper half-plane sends \(E\) to
\([1/9,9]\) and the pole
\(q_0=313/512+i\,77/64\) to \(-7/25+i\,24/25\).  The Poisson formula gives

\[
\omega_D^{q_0}(E)\ge\frac5{51\pi}>0,
\]

and positivity holds for every pole.

This is a fixed model-cusp mechanism: the whole domain and every relevant
local component use the same translate \(0+C_{2/3}\), and the tested arc lies
on that translate's curved boundary.  It is distinct from distant-translate,
tangent-disk, contact-predicate, and origin-pinned routes.  Independent review
still has to decide whether this satisfies the published contact convention;
the accessible text does not explicitly name the contact point.

The full proof and exact replay are in
`research/routes/conformal-cusp-model/certificate.md` and
`research/routes/conformal-cusp-model/verify_certificate.py`.
