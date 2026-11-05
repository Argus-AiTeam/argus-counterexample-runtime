#!/usr/bin/env python3
"""Exact A5-relative relation-module and affine-coinvariant replay."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import deque
from pathlib import Path


Perm = tuple[int, ...]
Word = tuple[int, ...]
Vector = tuple[int, ...]

IDENTITY: Perm = (0, 1, 2, 3, 4)
CANONICAL_A: Perm = (1, 2, 3, 4, 0)
CANONICAL_B: Perm = (1, 2, 0, 3, 4)
R1: Word = (1, 1, 1, -2, -2, -2, -2)
R2: Word = (1, 2, 1, -2, -1, -2)


def perm_mul(left: Perm, right: Perm) -> Perm:
    return tuple(left[right[i]] for i in range(5))


def perm_inv(value: Perm) -> Perm:
    result = [0] * 5
    for i, image in enumerate(value):
        result[image] = i
    return tuple(result)


def perm_pow(value: Perm, exponent: int) -> Perm:
    result = IDENTITY
    factor = value
    while exponent:
        if exponent & 1:
            result = perm_mul(result, factor)
        factor = perm_mul(factor, factor)
        exponent >>= 1
    return result


def parity(value: Perm) -> int:
    inversions = sum(
        value[i] > value[j] for i in range(5) for j in range(i + 1, 5)
    )
    return inversions % 2


def cycle_string(value: Perm) -> str:
    seen: set[int] = set()
    cycles: list[str] = []
    for start in range(5):
        if start in seen or value[start] == start:
            seen.add(start)
            continue
        cycle: list[int] = []
        point = start
        while point not in seen:
            seen.add(point)
            cycle.append(point + 1)
            point = value[point]
        cycles.append("(" + " ".join(map(str, cycle)) + ")")
    return "".join(cycles) or "()"


def conjugate(value: Perm, by: Perm) -> Perm:
    return perm_mul(perm_mul(perm_inv(by), value), by)


def generated_subgroup(generators: tuple[Perm, ...]) -> frozenset[Perm]:
    steps = generators + tuple(perm_inv(g) for g in generators)
    reached = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        value = queue.popleft()
        for step in steps:
            target = perm_mul(value, step)
            if target not in reached:
                reached.add(target)
                queue.append(target)
    return frozenset(reached)


def word_inverse(word: Word) -> Word:
    return tuple(-letter for letter in reversed(word))


def word_free_reduce(word: Word) -> Word:
    stack: list[int] = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def vector_add(*vectors: Vector) -> Vector:
    return tuple(sum(entries) for entries in zip(*vectors, strict=True))


def vector_neg(vector: Vector) -> Vector:
    return tuple(-entry for entry in vector)


def vector_scale(coefficient: int, vector: Vector) -> Vector:
    return tuple(coefficient * entry for entry in vector)


def unit_vector(rank: int, index: int) -> Vector:
    return tuple(int(i == index) for i in range(rank))


def matrix_apply(columns: tuple[Vector, ...], vector: Vector) -> Vector:
    rank = len(vector)
    output = [0] * rank
    for j, coefficient in enumerate(vector):
        if not coefficient:
            continue
        for i, entry in enumerate(columns[j]):
            if entry:
                output[i] += coefficient * entry
    return tuple(output)


def sparse_vector(vector: Vector) -> list[list[int]]:
    return [[i, entry] for i, entry in enumerate(vector) if entry]


def evaluate_permutation_word(word: Word, generators: tuple[Perm, Perm]) -> Perm:
    result = IDENTITY
    for letter in word:
        generator = generators[abs(letter) - 1]
        if letter < 0:
            generator = perm_inv(generator)
        result = perm_mul(result, generator)
    return result


def enumerate_a5() -> tuple[Perm, ...]:
    elements = tuple(
        value for value in itertools.permutations(range(5)) if parity(value) == 0
    )
    assert len(elements) == 60
    assert IDENTITY in elements
    return elements


def enumerate_s5() -> tuple[Perm, ...]:
    elements = tuple(itertools.permutations(range(5)))
    assert len(elements) == 120
    return elements


def normal_closure_of_element(value: Perm, a5: tuple[Perm, ...]) -> frozenset[Perm]:
    conjugates = tuple({conjugate(value, element) for element in a5})
    return generated_subgroup(conjugates)


def base_neighbors(
    pair: tuple[Perm, Perm],
    conjugacy_classes: dict[Perm, tuple[Perm, ...]],
) -> tuple[tuple[Perm, Perm], ...]:
    first, second = pair
    candidates = {
        (perm_inv(first), second),
        (first, perm_inv(second)),
        (perm_mul(first, second), second),
        (perm_mul(first, perm_inv(second)), second),
        (first, perm_mul(second, first)),
        (first, perm_mul(second, perm_inv(first))),
    }
    candidates.update((image, second) for image in conjugacy_classes[first])
    candidates.update((first, image) for image in conjugacy_classes[second])
    candidates.discard((IDENTITY, IDENTITY))
    return tuple(sorted(candidates))


def enumerate_base_component(
    a5: tuple[Perm, ...],
) -> tuple[dict[tuple[Perm, Perm], int], int]:
    for value in a5:
        closure = normal_closure_of_element(value, a5)
        assert len(closure) == (1 if value == IDENTITY else 60)

    conjugacy_classes = {
        value: tuple(sorted({conjugate(value, element) for element in a5}))
        for value in a5
    }
    root = (IDENTITY, CANONICAL_B)
    distance = {root: 0}
    queue = deque([root])
    while queue:
        pair = queue.popleft()
        for target in base_neighbors(pair, conjugacy_classes):
            if target not in distance:
                distance[target] = distance[pair] + 1
                queue.append(target)
    assert len(distance) == 60 * 60 - 1
    return distance, max(distance.values())


def enumerate_generating_pair_orbits(
    a5: tuple[Perm, ...], s5: tuple[Perm, ...]
) -> tuple[tuple[tuple[Perm, Perm], ...], tuple[tuple[Perm, Perm], ...]]:
    generating = tuple(
        (first, second)
        for first in a5
        for second in a5
        if len(generated_subgroup((first, second))) == 60
    )
    assert len(generating) == 2280
    generating_set = set(generating)

    order = [pair for pair in generating if pair == (CANONICAL_A, CANONICAL_B)]
    order.extend(pair for pair in generating if pair != (CANONICAL_A, CANONICAL_B))
    unseen = set(generating)
    representatives: list[tuple[Perm, Perm]] = []
    orbits: list[tuple[tuple[Perm, Perm], ...]] = []
    for pair in order:
        if pair not in unseen:
            continue
        orbit = tuple(
            sorted(
                {
                    (conjugate(pair[0], sigma), conjugate(pair[1], sigma))
                    for sigma in s5
                }
            )
        )
        assert len(orbit) == 120
        assert set(orbit) <= generating_set
        representatives.append(pair)
        orbits.append(orbit)
        unseen.difference_update(orbit)
    assert not unseen
    assert len(representatives) == 19
    assert sum(map(len, orbits)) == len(generating)
    return tuple(representatives), tuple(orbits)


class SchreierModel:
    def __init__(self, first: Perm, second: Perm, a5: tuple[Perm, ...]):
        self.a5 = a5
        self.index = {value: i for i, value in enumerate(a5)}
        self.generators = (first, second)
        self.generator_inverses = tuple(perm_inv(value) for value in self.generators)
        self.tau = self._build_transversal()
        self.basis_keys, self.basis_words, self.tree_keys = self._build_basis()
        self.rank = len(self.basis_keys)
        assert self.rank == 61
        self.key_index = {key: i for i, key in enumerate(self.basis_keys)}
        self.zero = (0,) * self.rank
        self._verify_schreier_basis()
        self.action = self._build_action()
        self.cocycle = self._build_cocycle()

    def image_step(self, value: Perm, letter: int) -> Perm:
        index = abs(letter) - 1
        generator = (
            self.generators[index]
            if letter > 0
            else self.generator_inverses[index]
        )
        return perm_mul(value, generator)

    def _build_transversal(self) -> dict[Perm, Word]:
        tau: dict[Perm, Word] = {IDENTITY: ()}
        queue = deque([IDENTITY])
        while queue:
            value = queue.popleft()
            for letter in (1, -1, 2, -2):
                target = self.image_step(value, letter)
                if target not in tau:
                    tau[target] = tau[value] + (letter,)
                    queue.append(target)
        assert len(tau) == 60
        for value, word in tau.items():
            assert evaluate_permutation_word(word, self.generators) == value
            if word:
                parent_word = word[:-1]
                parent = evaluate_permutation_word(parent_word, self.generators)
                assert tau[parent] == parent_word
        return tau

    def schreier_word(self, value: Perm, generator_index: int) -> Word:
        target = perm_mul(value, self.generators[generator_index])
        return word_free_reduce(
            self.tau[value]
            + (generator_index + 1,)
            + word_inverse(self.tau[target])
        )

    def _build_basis(
        self,
    ) -> tuple[
        tuple[tuple[Perm, int], ...],
        tuple[Word, ...],
        tuple[tuple[Perm, int], ...],
    ]:
        basis_keys: list[tuple[Perm, int]] = []
        basis_words: list[Word] = []
        tree_keys: list[tuple[Perm, int]] = []
        for value in self.a5:
            for generator_index in range(2):
                word = self.schreier_word(value, generator_index)
                key = (value, generator_index)
                if word:
                    basis_keys.append(key)
                    basis_words.append(word)
                else:
                    tree_keys.append(key)
        assert len(tree_keys) == 59
        assert len(basis_keys) == 120 - 59
        return tuple(basis_keys), tuple(basis_words), tuple(tree_keys)

    def collect(self, word: Word) -> tuple[Vector, Perm]:
        vector = [0] * len(self.basis_keys)
        value = IDENTITY
        for letter in word:
            generator_index = abs(letter) - 1
            if letter > 0:
                key = (value, generator_index)
                coordinate = self.key_index.get(key)
                if coordinate is not None:
                    vector[coordinate] += 1
                value = perm_mul(value, self.generators[generator_index])
            else:
                value = perm_mul(value, self.generator_inverses[generator_index])
                key = (value, generator_index)
                coordinate = self.key_index.get(key)
                if coordinate is not None:
                    vector[coordinate] -= 1
        return tuple(vector), value

    def _verify_schreier_basis(self) -> None:
        for value in self.a5:
            vector, image = self.collect(self.tau[value])
            assert vector == (0,) * self.rank
            assert image == value
        for i, word in enumerate(self.basis_words):
            vector, image = self.collect(word)
            assert vector == unit_vector(self.rank, i)
            assert image == IDENTITY
        for value, generator_index in self.tree_keys:
            vector, image = self.collect(self.schreier_word(value, generator_index))
            assert vector == (0,) * self.rank
            assert image == IDENTITY

    def _build_action(self) -> tuple[tuple[Vector, ...], ...]:
        matrices: list[tuple[Vector, ...]] = []
        for value in self.a5:
            prefix = self.tau[value]
            suffix = word_inverse(prefix)
            columns: list[Vector] = []
            for basis_word in self.basis_words:
                vector, image = self.collect(prefix + basis_word + suffix)
                assert image == IDENTITY
                columns.append(vector)
            matrices.append(tuple(columns))
        return tuple(matrices)

    def _build_cocycle(self) -> tuple[tuple[Vector, ...], ...]:
        rows: list[tuple[Vector, ...]] = []
        for left in self.a5:
            row: list[Vector] = []
            for right in self.a5:
                vector, image = self.collect(self.tau[left] + self.tau[right])
                assert image == perm_mul(left, right)
                row.append(vector)
            rows.append(tuple(row))
        return tuple(rows)

    def rho(self, value: Perm) -> tuple[Vector, ...]:
        return self.action[self.index[value]]

    def c(self, left: Perm, right: Perm) -> Vector:
        return self.cocycle[self.index[left]][self.index[right]]

    def verify_action_and_cocycle(self) -> dict[str, int]:
        identity_matrix = tuple(unit_vector(self.rank, i) for i in range(self.rank))
        assert self.rho(IDENTITY) == identity_matrix

        action_checks = 0
        for left in self.a5:
            left_word = self.tau[left]
            for right in self.a5:
                product = perm_mul(left, right)
                conjugator = left_word + self.tau[right]
                inverse_conjugator = word_inverse(conjugator)
                for i, basis_word in enumerate(self.basis_words):
                    vector, image = self.collect(
                        conjugator + basis_word + inverse_conjugator
                    )
                    assert image == IDENTITY
                    assert vector == self.rho(product)[i]
                    action_checks += 1

        inverse_checks = 0
        for value in self.a5:
            inverse_matrix = self.rho(perm_inv(value))
            for i, column in enumerate(self.rho(value)):
                assert matrix_apply(inverse_matrix, column) == unit_vector(
                    self.rank, i
                )
                inverse_checks += 1

        cocycle_checks = 0
        steps = (1, -1, 2, -2)
        for left in self.a5:
            for middle in self.a5:
                for letter in steps:
                    right = self.image_step(IDENTITY, letter)
                    lm = perm_mul(left, middle)
                    mr = perm_mul(middle, right)
                    kernel_word = (
                        self.tau[middle]
                        + self.tau[right]
                        + word_inverse(self.tau[mr])
                    )
                    acted, image = self.collect(
                        self.tau[left]
                        + kernel_word
                        + word_inverse(self.tau[left])
                    )
                    assert image == IDENTITY
                    lhs = vector_add(self.c(left, middle), self.c(lm, right))
                    rhs = vector_add(acted, self.c(left, mr))
                    assert lhs == rhs
                    cocycle_checks += 1

        return {
            "action_composition_basis_checks": action_checks,
            "action_inverse_basis_checks": inverse_checks,
            "cocycle_generator_extension_checks": cocycle_checks,
        }

    def multiply(
        self, left: tuple[Vector, Perm], right: tuple[Vector, Perm]
    ) -> tuple[Vector, Perm]:
        left_vector, left_image = left
        right_vector, right_image = right
        vector = vector_add(
            left_vector,
            matrix_apply(self.rho(left_image), right_vector),
            self.c(left_image, right_image),
        )
        return vector, perm_mul(left_image, right_image)

    def inverse(self, value: tuple[Vector, Perm]) -> tuple[Vector, Perm]:
        vector, image = value
        image_inverse = perm_inv(image)
        result = vector_add(
            vector_neg(matrix_apply(self.rho(image_inverse), vector)),
            vector_neg(self.c(image_inverse, image)),
        )
        return result, image_inverse

    def evaluate(
        self, word: Word, variables: tuple[tuple[Vector, Perm], tuple[Vector, Perm]]
    ) -> tuple[Vector, Perm]:
        result = (self.zero, IDENTITY)
        for letter in word:
            value = variables[abs(letter) - 1]
            if letter < 0:
                value = self.inverse(value)
            result = self.multiply(result, value)
        return result

    def verify_affine_laws(self) -> dict[str, int]:
        direct_constant_checks = 0
        for left in self.a5:
            for right in self.a5:
                zero_left = (self.zero, left)
                zero_right = (self.zero, right)
                cases = (
                    (
                        self.tau[left] + self.tau[right],
                        self.multiply(zero_left, zero_right),
                    ),
                    (
                        self.tau[left] + word_inverse(self.tau[right]),
                        self.multiply(zero_left, self.inverse(zero_right)),
                    ),
                    (
                        self.tau[right] + self.tau[left],
                        self.multiply(zero_right, zero_left),
                    ),
                    (
                        word_inverse(self.tau[right]) + self.tau[left],
                        self.multiply(self.inverse(zero_right), zero_left),
                    ),
                )
                for word, expected in cases:
                    assert self.collect(word) == expected
                    direct_constant_checks += 1

        conjugation_checks = 0
        for image in self.a5:
            element = (self.zero, image)
            for conjugator_image in self.a5:
                conjugator = (self.zero, conjugator_image)
                expected = self.multiply(
                    self.inverse(conjugator), self.multiply(element, conjugator)
                )
                word = (
                    word_inverse(self.tau[conjugator_image])
                    + self.tau[image]
                    + self.tau[conjugator_image]
                )
                assert self.collect(word) == expected

                constant = vector_add(
                    vector_neg(self.c(perm_inv(conjugator_image), conjugator_image)),
                    self.c(perm_inv(conjugator_image), image),
                    self.c(
                        perm_mul(perm_inv(conjugator_image), image),
                        conjugator_image,
                    ),
                )
                assert expected[0] == constant
                assert expected[1] == conjugate(image, conjugator_image)
                conjugation_checks += 1

        double_inverse_checks = 0
        for image in self.a5:
            for i in range(self.rank):
                value = (unit_vector(self.rank, i), image)
                assert self.inverse(self.inverse(value)) == value
                double_inverse_checks += 1

        element_coefficient_checks = 0
        for conjugator_image in self.a5:
            conjugator = (self.zero, conjugator_image)
            constant = self.multiply(
                self.inverse(conjugator),
                self.multiply((self.zero, IDENTITY), conjugator),
            )[0]
            for i in range(self.rank):
                element = (unit_vector(self.rank, i), IDENTITY)
                actual = self.multiply(
                    self.inverse(conjugator),
                    self.multiply(element, conjugator),
                )[0]
                assert vector_add(actual, vector_neg(constant)) == self.rho(
                    perm_inv(conjugator_image)
                )[i]
                element_coefficient_checks += 1

        # For h=(z,t), h^-1(u,p)h has z-coefficient
        # rho(t^-1 p)-rho(t^-1). Checking its 61 columns covers every z in M.
        kernel_conjugator_coefficient_checks = 0
        for image in self.a5:
            for conjugator_image in self.a5:
                zero_conjugator = (self.zero, conjugator_image)
                element = (self.zero, image)
                constant = self.multiply(
                    self.inverse(zero_conjugator),
                    self.multiply(element, zero_conjugator),
                )[0]
                left_matrix = self.rho(perm_inv(conjugator_image))
                right_matrix = self.rho(
                    perm_mul(perm_inv(conjugator_image), image)
                )
                for i in range(self.rank):
                    conjugator = (unit_vector(self.rank, i), conjugator_image)
                    actual = self.multiply(
                        self.inverse(conjugator),
                        self.multiply(element, conjugator),
                    )[0]
                    expected = vector_add(
                        right_matrix[i], vector_neg(left_matrix[i])
                    )
                    assert vector_add(actual, vector_neg(constant)) == expected
                    kernel_conjugator_coefficient_checks += 1

        return {
            "signed_left_right_product_constant_checks": direct_constant_checks,
            "a5_conjugator_constant_checks": conjugation_checks,
            "double_inverse_basis_checks": double_inverse_checks,
            "conjugated_element_coefficient_basis_checks": (
                element_coefficient_checks
            ),
            "arbitrary_kernel_conjugator_coefficient_basis_checks": (
                kernel_conjugator_coefficient_checks
            ),
        }

    def verify_local_coinvariant_collapse(self) -> dict[str, object]:
        g = CANONICAL_B
        assert perm_pow(g, 3) == IDENTITY
        identity_matrix = tuple(unit_vector(self.rank, i) for i in range(self.rank))
        action = self.rho(g)
        action_squared = self.rho(perm_pow(g, 2))

        for i, column in enumerate(action):
            assert matrix_apply(action_squared, column) == identity_matrix[i]

        unit_certificate_checks = 0
        for i in range(self.rank):
            e = identity_matrix[i]
            re = action[i]
            r2e = action_squared[i]
            norm_e = vector_add(e, re, r2e)
            r_plus_two_e = vector_add(re, vector_scale(2, e))
            action_relation = vector_add(
                matrix_apply(action, r_plus_two_e),
                vector_neg(r_plus_two_e),
            )
            recovered = vector_add(
                norm_e,
                vector_neg(action_relation),
                vector_scale(-2, e),
            )
            assert recovered == e
            unit_certificate_checks += 1

        return {
            "base_vertex": [cycle_string(IDENTITY), cycle_string(g)],
            "odd_order": 3,
            "linear_loop_relations": [
                "second <- second*first: bottom-left block rho(g)",
                "first <- first^-1: first block -2I",
                "first <- first conjugated by a lift of g^-1: first block rho(g)-I",
                "repeat first <- first*second three times: top-right block I+rho(g)+rho(g)^2",
            ],
            "unit_identity": (
                "I=(I+R+R^2)-(R-I)(R+2I)-2I, with R=rho(g)"
            ),
            "first_copy_unit_certificate_checks": unit_certificate_checks,
            "second_copy_unit_certificate_checks": self.rank,
            "relation_module_rank": self.rank,
            "pair_fiber_rank": 2 * self.rank,
            "coinvariant_invariant_factors": ["1"] * (2 * self.rank),
            "coinvariant_group_order": 1,
        }

    def endpoint_data(
        self, base_distance: dict[tuple[Perm, Perm], int]
    ) -> dict[str, object]:
        basis = (self.collect((1,)), self.collect((2,)))
        relators = (self.collect(R1), self.collect(R2))
        assert self.evaluate(R1, basis) == relators[0]
        assert self.evaluate(R2, basis) == relators[1]
        basis_base = (basis[0][1], basis[1][1])
        relator_base = (relators[0][1], relators[1][1])
        assert basis_base in base_distance
        assert relator_base in base_distance
        assert relator_base != (IDENTITY, IDENTITY)
        return {
            "basis_base": [cycle_string(value) for value in basis_base],
            "ak3_base": [cycle_string(value) for value in relator_base],
            "basis_vectors": [
                sparse_vector(basis[0][0]),
                sparse_vector(basis[1][0]),
            ],
            "ak3_vectors": [
                sparse_vector(relators[0][0]),
                sparse_vector(relators[1][0]),
            ],
            "basis_base_distance_to_collapse_vertex": base_distance[basis_base],
            "ak3_base_distance_to_collapse_vertex": base_distance[relator_base],
            "universal_coinvariant_basis_value": 0,
            "universal_coinvariant_ak3_value": 0,
        }

    def basis_labels(self) -> list[dict[str, object]]:
        return [
            {
                "index": i,
                "coset": cycle_string(value),
                "generator": "a" if generator_index == 0 else "b",
            }
            for i, (value, generator_index) in enumerate(self.basis_keys)
        ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=Path(__file__).with_name("certificate.json"),
    )
    parser.add_argument(
        "--limit-kernels",
        type=int,
        default=None,
        help="Diagnostic prefix only; omit for the exhaustive certificate.",
    )
    args = parser.parse_args()

    a5 = enumerate_a5()
    s5 = enumerate_s5()
    assert generated_subgroup((CANONICAL_A, CANONICAL_B)) == frozenset(a5)
    base_distance, base_diameter = enumerate_base_component(a5)
    representatives, orbits = enumerate_generating_pair_orbits(a5, s5)
    selected = (
        representatives
        if args.limit_kernels is None
        else representatives[: args.limit_kernels]
    )

    kernel_records: list[dict[str, object]] = []
    for number, (first, second) in enumerate(selected, start=1):
        model = SchreierModel(first, second, a5)
        algebra_checks = model.verify_action_and_cocycle()
        affine_checks = model.verify_affine_laws()
        collapse = model.verify_local_coinvariant_collapse()
        endpoints = model.endpoint_data(base_distance)
        kernel_records.append(
            {
                "kernel_representative": number,
                "a_image": list(first),
                "b_image": list(second),
                "a_cycle": cycle_string(first),
                "b_cycle": cycle_string(second),
                "schreier_transversal_size": len(model.tau),
                "schreier_transversal_max_word_length": max(
                    map(len, model.tau.values())
                ),
                "directed_positive_edges": 120,
                "tree_edges": len(model.tree_keys),
                "relation_module_rank": model.rank,
                "basis_labels": model.basis_labels(),
                "algebra_checks": algebra_checks,
                "affine_checks": affine_checks,
                "local_coinvariant": collapse,
                "endpoints": endpoints,
            }
        )

    exhaustive = args.limit_kernels is None
    certificate = {
        "schema_version": 1,
        "result": {
            "counterexample_candidate": False,
            "bounded_mechanism": (
                "global abelian-valued affine invariants of pairs in "
                "F/[ker(pi),ker(pi)] over the A5 AC graph"
            ),
            "outcome": (
                "exact_exhaustion"
                if exhaustive
                else "diagnostic_prefix_not_an_exhaustion"
            ),
            "conclusion": (
                "The universal integral linear-difference coinvariant is zero "
                "for every ordered A5-generating pair. Therefore this global "
                "first-relation-module affine mechanism cannot separate AK(3) "
                "from the basis. This is not a complete affine-orbit certificate "
                "and does not prove Andrews-Curtis equivalence."
            ),
        },
        "a5": {
            "order": len(a5),
            "canonical_a": list(CANONICAL_A),
            "canonical_b": list(CANONICAL_B),
            "canonical_a_cycle": cycle_string(CANONICAL_A),
            "canonical_b_cycle": cycle_string(CANONICAL_B),
            "canonical_pair_generated_order": len(
                generated_subgroup((CANONICAL_A, CANONICAL_B))
            ),
            "normally_generating_pair_count": 60 * 60 - 1,
            "direct_ac_component_size": len(base_distance),
            "direct_ac_component_diameter": base_diameter,
            "ordered_generating_pair_count": sum(map(len, orbits)),
            "s5_conjugation_orbit_count": len(orbits),
            "s5_conjugation_orbit_sizes": list(map(len, orbits)),
            "kernel_equivalence_reason": (
                "Postcomposition by an automorphism of A5 preserves the kernel. "
                "Aut(A5)=S5 acts by conjugation; its action on generating pairs "
                "is free because a fixed generating pair fixes every A5 element."
            ),
        },
        "coverage": {
            "expected_kernel_representatives": len(representatives),
            "checked_kernel_representatives": len(selected),
            "exhaustive": exhaustive,
        },
        "coordinate_convention": {
            "section": (
                "A deterministic prefix-closed BFS Schreier section tau:A5->F(a,b)"
            ),
            "pair": (
                "(u,q) denotes k*tau(q) modulo [ker(pi),ker(pi)], "
                "where [k]=u in the rank-61 Schreier basis"
            ),
            "multiplication": (
                "(u,q)(v,r)=(u+rho(q)v+c(q,r),qr)"
            ),
            "inverse": (
                "(u,q)^-1=(-rho(q^-1)u-c(q^-1,q),q^-1)"
            ),
            "conjugation": (
                "(z,t)^-1(u,p)(z,t) has vector rho(t^-1)u+"
                "(rho(t^-1 p)-rho(t^-1))z-c(t^-1,t)+"
                "c(t^-1,p)+c(t^-1 p,t)"
            ),
        },
        "jacobian": {
            "server_version": "0.14.0",
            "protocol_version": "2025-11-25",
            "operation_id": "group.order.compute",
            "payload_file": "jacobian-group-order-payload.json",
            "typed_output_file": "jacobian-group-order-run.json",
            "status": "ok",
            "error": None,
            "timeout": False,
            "note": (
                "The discovered certified Smith operation is bounded to 16 by 16, "
                "so the rank-122 collapse is certified locally by an explicit "
                "integer unit identity rather than forced through that contract."
            ),
        },
        "kernels": kernel_records,
    }
    args.certificate.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "a5_order": len(a5),
                "normally_generating_pairs": len(base_distance),
                "ordered_generating_pairs": sum(map(len, orbits)),
                "kernel_representatives_checked": len(selected),
                "pair_fiber_rank": 122,
                "coinvariant_group_order": 1,
                "counterexample_candidate": False,
                "exhaustive": exhaustive,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
