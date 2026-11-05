---
title: Endpoint-notch common-frequency telescope boundary
description: Exact pure-central spectral-gap obstruction for fixed-dimensional dyadic-rational phase-locked telescopes.
---

# Endpoint-notch common-frequency telescope boundary

The reviewed horizontal and pure-central atlases separately compress their
one-dimensional profiles, but the pure-central atlas is not translation
equivariant. A natural symplectic coupling attempt replaces it by finitely
many complex blocks. Within each block, the central carrier and every
parent-child correction use one common rational character, and consecutive
corrections telescope term by term. Carrier and correction are added in the
same coordinate, so nonorthogonal cancellation is allowed.

For any fixed number \(B\) of blocks and fixed phase denominator \(D\), the
lock shell indices leave a gap whose length grows with the depth. If
\([L,L+g]\) is a largest gap, then
\[
n=D2^{L-1},\qquad
(e,[a^n,b^n])
\]
is a genuine word-ball pair with
\[
A=0,\qquad W=-D^2 4^L.
\]
All lock frequencies below the gap repeat exactly on this commutator. Every
frequency above the gap has total normalized squared response
\(O(4^{-g})\), while all centered termwise phase-eigenfunction corrections
vanish on the vertical axis. The reviewed horizontal atlas keeps a fixed
positive normalized response on \((e,b)\), so the squared condition ratio
diverges at every sufficiently large depth.

The exact theorem and replay are
`research/routes/p2_endpoint_scale_notch/positive_spectral_shell_compression/symplectic_coupling/phase_locked_transport/phase_locked_transport_boundary.md`
and `verify_phase_locked_transport.py`.

This boundary is specific to fixed-\(B\), fixed-\(D\),
bounded-effective-carrier, termwise phase-eigencharacter telescopes. It does
not exclude the reviewed non-equivariant pure-central atlas,
growing-denominator or arbitrary-real-frequency representations, nonlinear
transports, the endpoint-notch family, or the campaign objective.
