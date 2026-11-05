---
title: Hypergraph-container chain sieve
description: Exact partite trajectory completion and the Saxton--Thomason top-codegree barrier at the one-transversal scale.
---

# Hypergraph-container chain sieve

For each fixed chain sector and length, the bounded start and multiplier
coordinates have finite exact projections. Completing every forbidden
prefix through all later coordinates, merging duplicate modular rows,
and adding endpoint-invalid full assignments gives a simple partite
uniform hypergraph. Its independent full transversals are exactly the
bounded all-prime trajectories. This completion retains strict
\(p<P_j\) equality corrections, repeated roots, unbounded allowed
multipliers, and exact endpoint floors.

Saxton--Thomason arXiv:1204.6595v3 Definition 3.2 has an unavoidable top
codegree term. For a nonempty simple \(s\)-uniform hypergraph with
\(N_+\) nonisolated vertices,

\[
\delta(H,\tau)\ge
\frac{2^{s-2}N_+}{s\,e(H)\tau^{s-1}}.
\]

Combining this with Corollary 3.6 gives

\[
\epsilon e(H)>12s!\,2^{2s-3}\ge48.
\]

The cited sparse-container theorem therefore cannot make its guaranteed
residual edge count smaller than one. The iterated theorem fails on the
induced one-edge hypergraph at the same threshold. A fixed all-two word
also produces shared multiplier vertices and a direct codegree
obstruction.

The paper's entropy bound counts containers but does not count
independent transversals inside them. Its own \(F\)-free application
adds a separate supersaturation theorem. At one trajectory, the
corresponding statement is false for arbitrary full transversals (one
bad trajectory induces one edge) and is the desired exclusion itself
when restricted to independent transversals.

This retires only the natural prefix-completion plus sparse-edge
container transfer. It is not a general impossibility theorem for
hypergraph methods, a universal chain exclusion, or a Problem 1055
counterexample.
