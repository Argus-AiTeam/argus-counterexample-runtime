---
title: Kirby Problem 1.3 scope boundary
description: Exact quantifiers, primary-source results, excluded substitutions, and the bounded status search through 2026-08-29.
---

# Kirby Problem 1.3 scope boundary

## Exact target

K3 Problem 1.3, printed p. 12, asks:

1. whether the connected sum of \(n\) nontrivial knots has unknotting
   number at least \(n\); and
2. whether unknotting number is invariant under mutation.

Campaign 2662 therefore needs either an integer \(n\) and nontrivial knots
\(K_1,\ldots,K_n\) with
\[
u(K_1\#\cdots\#K_n)<n,
\]
or an explicit Conway-mutant pair \(K,K'\) with \(u(K)\ne u(K')\).
Strict nonadditivity
\[
u(K\#J)<u(K)+u(J)
\]
is a different, weaker inequality.

Source: R. Inanc Baykur, Robion C. Kirby, and Daniel Ruberman, eds.,
*K3: A New Problem List in Low-Dimensional Topology*, AMS Mathematical
Surveys and Monographs 295 (2026), ISBN 978-1-4704-8433-0,
[public preliminary text](https://math.berkeley.edu/sites/default/files/surv-295-ruberman-watermarked-author-pdf.pdf),
Problem 1.3 and Remarks (1)-(3), printed p. 12.

## Primary-source boundary

| Result | Exact source and locator | Applicable statement | Consequence here |
|---|---|---|---|
| Two-factor exclusion | Martin G. Scharlemann, "Unknotting number one knots are prime," *Invent. Math.* 82 (1985), 37-55, [DOI](https://doi.org/10.1007/BF01394778), [public scan](https://gdz.sub.uni-goettingen.de/dms/resolveppn/?PPN=GDZPPN002102099), unnumbered theorem concluding item (1.3), p. 39 | Every knot in \(S^3\) with unknotting number one is prime. | If \(K,J\) are nontrivial, \(K\#J\) is nontrivial and composite, so its integer-valued unknotting number is neither 0 nor 1: \(u(K\#J)\ge2\). This closes only \(n=2\); for \(n\ge3\) the same theorem still gives only the constant lower bound 2. |
| Mutation at \(u=1\) | C. McA. Gordon and John Luecke, "Knots with unknotting number 1 and essential Conway spheres," *Algebr. Geom. Topol.* 6 (2006), 2051-2116, [DOI](https://doi.org/10.2140/agt.2006.6.2051), [version-of-record PDF](https://msp.org/agt/2006/6-5/agt-v6-n5-p02-s.pdf), Section 7 and Theorem 7.1, pp. 2082-2083 | For knots, having unknotting number 1 is invariant under mutation by any of the three nonidentity half-turns of the four-punctured sphere. | Mutation is involutive, hence \(u(K)=1\) iff \(u(K')=1\). Thus an unequal pair cannot have value exactly 1 on either side. The relevant result is Theorem 7.1, not Corollary 9.3. This theorem alone does not exclude \(u=0\) on one side, so that branch remains open here absent a separately sourced result that mutation preserves the unknot. |
| First nonadditivity | Mark Brittenham and Susan Hermiller, "Unknotting number is not additive under connected sum," [arXiv:2506.24088v2](https://arxiv.org/abs/2506.24088v2), Theorem 1.2 p. 3; diagrammatic certificate pp. 4-9 and 18-20; Question 4.4 p. 17 | For \(K=7_1=T(2,7)\), \(u(K)=3\) and \(u(K\#\overline K)\le5<6=u(K)+u(\overline K)\). | This proves strict nonadditivity, not \(u(K\#\overline K)<2\). The exact value of the sum is not proved. Repeating the construction amplifies additive defect but does not put total unknotting number below the number of prime factors. |
| Smaller symbionts | Mark Brittenham and Susan Hermiller, "Unknotting number and connected sums: The knots \(4_1\) and \(5_1\)," [arXiv:2601.18757v1](https://arxiv.org/abs/2601.18757v1), Theorems 1.1-1.3 pp. 2-3; Lemma 4.1 p. 11; Conjecture 5.1 p. 15 | \(u(4_1\#9_{10})\le3\) with summand values 1 and 3; \(u(5_1\#8_2)\le3\) with summand values 2 and 2 for the stated mirror choice; \(u(3_1\#10_6)\le3\) with \(u(10_6)\in\{2,3\}\). | Every displayed sum has two nontrivial factors and upper bound 3, whereas this campaign would need a bound below 2. The \(4_1\)-\(9_{10}\) result is a one-shot non-increase relative to \(u(9_{10})\); no theorem iterates that non-increase over four or more prime factors. "Symbiont" means pairwise strict nonadditivity only. |
| Latest \(10_6\) attempt | Justin Gebel and William Prangley, "Obstructing Unknotting Number Two For Some Alternating Knots," [arXiv:2608.25256v1](https://arxiv.org/abs/2608.25256v1), Introduction and Theorems 1-4, pp. 1-2 | The authors report that the project grew from a failed attempt to prove \(u(10_6)=3\), state that \(u(10_6)\) remains unknown, and instead determine 194 individual alternating-knot values \(u=3\) plus further bounds and sign restrictions. | This does not complete Brittenham-Hermiller Theorem 1.3 and supplies no connected-sum or mutation counterexample. |

## Bounded search status

The cutoff was 2026-08-29. The search covered the current K3 list; arXiv
queries for unknotting number with mutation, mutants, and connected sums;
Crossref and citation trails from Gordon-Luecke and
Brittenham-Hermiller; KnotInfo's 2026-08-01 data; Stoimenow's mutation
tables through 15 crossings; and the public code/data repositories
attached to recent unknotting-number papers.

No public source found in that scope supplied either exact target together
with all of:

- canonical diagrams or DT/PD codes;
- an explicit connected-sum decomposition or Conway sphere and half-turn;
- a replayable crossing-change upper bound; and
- a rigorous lower bound with its hypotheses checked.

The low-crossing mutant lead \(12a102/12a107\) is not a candidate:
McCoy-Park, arXiv:2603.10732v2, Table 2, report both values as 4, while a
conflicting uncertified computation reports 3 for \(12a107\) without
publishing its crossing-change trajectory. The accessible mutation table
also does not retain the Conway sphere and rotation for this pair.

This is bounded negative retrieval evidence, not a proof that no example
exists and not a novelty claim. Private, delayed, unindexed, and
inaccessible material is outside the conclusion. No `reviewed-facts.md`
exists under campaign 2662 or elsewhere in the assigned
`counterexample-batch-1` tree, so no prior independently reviewed fact
bundle was available for reuse.

## Retired substitutions

- Two nontrivial summands cannot meet the factor-count target.
- A mutant counterexample cannot use unknotting number 1 on either side;
  the cited theorem does not by itself eliminate unknotting number 0.
- Ordinary nonadditivity cannot be substituted for a total below the
  factor count.
- Database labels, overlapping intervals, invariant differences, and
  double-branched-cover data alone cannot replace the required object,
  upper-bound, and lower-bound certificates.

## Bounded Jacobian probe

The standalone Jacobian catalog exposed 607 operations and no knot-theory
operation, so no nearby operation was treated as evidence about a knot.
After inspecting its typed contract, the exact operation
`algebraic_number.compare` was used only for the arithmetic boundary
between the Brittenham-Hermiller 2026 upper bound 3 and the two-factor
threshold 2.

Exact payload:

```json
{"left":{"polynomial":["1","-3"],"real_root_index":0},"right":{"polynomial":["1","-2"],"real_root_index":0}}
```

Typed output:

```json
{"comparison_basis":"ORDERED_REAL_ROOT_ISOLATION","left":{"polynomial":["1","-3"],"real_root_index":0},"left_isolating_interval":{"interval_type":"SINGLETON","lower":{"den":"1","num":"3"},"upper":{"den":"1","num":"3"}},"order":"GT","right":{"polynomial":["1","-2"],"real_root_index":0},"right_isolating_interval":{"interval_type":"SINGLETON","lower":{"den":"1","num":"2"},"upper":{"den":"1","num":"2"}}}
```

The run returned in 2 ms with exit status 0 and no timeout or structured
operation error. The standalone CLI response exposed neither a server
version nor MCP protocol metadata, so neither is asserted.
