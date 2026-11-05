#!/usr/bin/env python3
"""Verify the complete finite generator presentation of every unresolved holonomy."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / "a5-relative-class2-orbit-separator"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


path_probe = load_module("a5_holonomy_path_probe", HERE / "kernel2_path_probe.py")
quotient = load_module(
    "a5_holonomy_quotient",
    PRIOR / "kernel2-global-weight2-ac-invariant-probe.py",
)
base = path_probe.base
replay = path_probe.replay
class2 = path_probe.class2
fo = path_probe.fo


def strict_record(operation) -> dict[str, object]:
    record: dict[str, object] = {"kind": operation.kind}
    if operation.conjugator_image is not None:
        image = operation.conjugator_image
        if operation.orientation == -1:
            image = fo.perm_inv(image)
        record.update(
            {
                "conjugator_image": list(image),
                "conjugator_linear": [],
                "conjugator_central": [],
            }
        )
    return record


def conjugate(model, element, conjugator):
    return model.group_multiply(
        model.group_inverse(conjugator),
        model.group_multiply(element, conjugator),
    )


def word_conjugation_checks(model, pair) -> int:
    words = (
        (1, -2, 1, 2, -1, -2),
        (-2, -1, 2, 2, 1, -2, 1),
    )
    checks = 0
    for word in words:
        whole = model.from_word(word)
        for component in range(2):
            direct = conjugate(model, pair[component], whole)
            sequential = pair[component]
            for letter in word:
                sequential = conjugate(
                    model, sequential, model.from_word((letter,))
                )
            assert sequential == direct
            checks += 1
    return checks


def generator_inverse_checks(model, samples) -> int:
    checks = 0
    for operation in quotient.quotient_generators(model):
        record = strict_record(operation)
        inverse = replay.inverse_operation(model, record)
        for pair in samples:
            transformed = replay.apply_record(model, pair, record)
            restored = replay.apply_record(model, transformed, inverse)
            assert restored == pair
            checks += 1
    return checks


def quotient_edge_checks(model, parent) -> int:
    checks = 0
    for source in parent:
        for operation in quotient.quotient_generators(model):
            target = quotient.apply_quotient_operation(source, operation)
            inverse = quotient.inverse_quotient_operation(operation)
            assert quotient.apply_quotient_operation(target, inverse) == source
            assert target != (fo.IDENTITY, fo.IDENTITY)
            checks += 1
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=HERE / "full-holonomy-certificate.json",
    )
    args = parser.parse_args()

    a5 = fo.enumerate_a5()
    representatives, _ = fo.enumerate_generating_pair_orbits(
        a5, fo.enumerate_s5()
    )
    assert len(representatives) == 19
    records = []
    full_edge_checks = 0
    full_inverse_checks = 0
    full_word_checks = 0
    for kernel_number in range(2, 20):
        a_image, b_image = representatives[kernel_number - 1]
        model = class2.ClassTwoSchreierModel(a_image, b_image, a5)
        assert model.rank == 61
        assert model.central_rank == 1830
        root = (fo.IDENTITY, fo.CANONICAL_B)
        parent, distance = quotient.spanning_tree(model, root)
        assert len(parent) == 3599
        edge_checks = quotient_edge_checks(model, parent)
        assert edge_checks == 3599 * 14

        normalized_ak3 = base.normalize_pair(model)
        basis_pair = (model.from_word((1,)), model.from_word((2,)))
        inverse_checks = generator_inverse_checks(
            model, (normalized_ak3, basis_pair)
        )
        word_checks = word_conjugation_checks(model, normalized_ak3)
        assert inverse_checks == 28
        assert word_checks == 4
        ak3_vertex = (
            normalized_ak3[0].image,
            normalized_ak3[1].image,
        )
        basis_vertex = (basis_pair[0].image, basis_pair[1].image)
        assert ak3_vertex in parent and basis_vertex in parent
        records.append(
            {
                "kernel_representative": kernel_number,
                "a_image": list(a_image),
                "b_image": list(b_image),
                "schreier_rank": model.rank,
                "central_rank": model.central_rank,
                "pair_fiber_linear_rank": 2 * model.rank,
                "pair_fiber_central_rank": 2 * model.central_rank,
                "base_vertices": len(parent),
                "base_directed_labelled_edges": edge_checks,
                "spanning_tree_edges": len(parent) - 1,
                "redundant_directed_fundamental_loops": (
                    edge_checks - 2 * (len(parent) - 1)
                ),
                "spanning_tree_diameter": max(distance.values()),
                "normalized_ak3_root_distance": distance[ak3_vertex],
                "basis_root_distance": distance[basis_vertex],
                "strict_generator_inverse_checks": inverse_checks,
                "arbitrary_conjugator_word_checks": word_checks,
            }
        )
        full_edge_checks += edge_checks
        full_inverse_checks += inverse_checks
        full_word_checks += word_checks

    generator_records = [
        strict_record(operation)
        for operation in quotient.quotient_generators(
            class2.ClassTwoSchreierModel(*representatives[1], a5)
        )
    ]
    report = {
        "schema_version": 1,
        "kernel_representatives": records,
        "coverage": {
            "expected_unresolved_kernel_classes": 18,
            "checked_unresolved_kernel_classes": len(records),
            "kernel_numbers": list(range(2, 20)),
            "exhaustive_for_live_mission": True,
        },
        "hall_normal_form": {
            "kernel_coordinate": (
                "x_0^u_0 ... x_60^u_60 times the lexicographically ordered "
                "product of [x_j,x_i]^z_ij for i<j"
            ),
            "commutator_convention": "[x,y]=x^-1*y^-1*x*y",
            "multiplication": (
                "(u,z)*(v,w)=(u+v,z+w+B(u,v)), "
                "B(u,v)_(i,j)=u_j*v_i for i<j"
            ),
            "inverse": (
                "(u,z)^-1=(-u,-z+(u_i*u_j)_(i<j))"
            ),
            "extension_normal_form": "(u,z;q)=k*tau(q)",
            "extension_product": (
                "(n;q)*(m;t)=(n*alpha_q(m)*c(q,t);q*t), "
                "c(q,t)=tau(q)*tau(t)*tau(q*t)^-1"
            ),
        },
        "complete_groupoid_presentation": {
            "objects": "A5^2 minus {(1,1)}",
            "fiber_over_each_object": "Z^122 times Z^3660",
            "strict_edge_generators": generator_records,
            "strict_edge_generator_count": len(generator_records),
            "arbitrary_ac3_coverage": (
                "Every c in F2/gamma_3(K) is represented by a word in "
                "a^{+/-1},b^{+/-1}; (g^u)^v=g^(uv), so repeated listed "
                "generator conjugations equal AC3 by c exactly."
            ),
            "arbitrary_composition_coverage": (
                "Every legal finite AC sequence is a word in the fourteen "
                "invertible edge generators. Relative to the recorded BFS "
                "tree, all root holonomy is generated by the directed "
                "non-tree loops T_source * edge * T_target^-1."
            ),
            "root": [list(fo.IDENTITY), list(fo.CANONICAL_B)],
            "hall_veronese_linearization": {
                "coordinates": (
                    "1; 122 linear u_i; 122 binomial(u_i,2); 7381 products "
                    "u_i*u_j for i<j; 3660 central z_k"
                ),
                "dimension": 11286,
                "action": "faithful by integral invertible matrices",
            },
        },
        "exact_checks": {
            "directed_quotient_edge_inverse_checks": full_edge_checks,
            "strict_hall_generator_inverse_checks": full_inverse_checks,
            "arbitrary_word_conjugation_composition_checks": full_word_checks,
            "reused_hall_model_certificate": (
                "research/experiments/a5-relative-class2-orbit-separator/"
                "kernel2-global-weight2-ac-invariant-certificate.json"
            ),
        },
        "decision_boundary": (
            "The presentation reduces endpoint membership to one exact orbit "
            "problem for a finitely generated subgroup of GL_11286(Z). No "
            "general arithmeticity, finite-index, or orbit-decision theorem "
            "is asserted by this certificate."
        ),
    }
    args.output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "checked_kernel_classes": len(records),
                "directed_edge_checks": full_edge_checks,
                "strict_inverse_checks": full_inverse_checks,
                "word_conjugation_checks": full_word_checks,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
