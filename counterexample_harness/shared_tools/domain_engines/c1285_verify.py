#!/usr/bin/env python3
"""Producer-independent verifier for the fresh rational-map certificate."""

from __future__ import annotations

import argparse
import copy
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def next_prime(value: int) -> int:
    candidate = value + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def crt(congruences: list[tuple[int, int]]) -> tuple[int, int]:
    value, modulus = 0, 1
    for residue, component in congruences:
        require(math.gcd(modulus, component) == 1, "CRT components are not coprime")
        step = ((residue - value) * pow(modulus, -1, component)) % component
        value = (value + modulus * step) % (modulus * component)
        modulus *= component
    return value, modulus


def least_progression_prime(residue: int, modulus: int) -> tuple[int, int]:
    candidate = residue
    rejected = 0
    while not is_prime(candidate):
        candidate += modulus
        rejected += 1
    return candidate, rejected


def trim(poly: list[int]) -> list[int]:
    result = list(poly)
    while result and result[-1] == 0:
        result.pop()
    return result


def poly_add(left: list[int], right: list[int]) -> list[int]:
    result = [0] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def poly_subtract(left: list[int], right: list[int]) -> list[int]:
    return poly_add(left, [-value for value in right])


def poly_multiply(left: list[int], right: list[int]) -> list[int]:
    require(left and right, "zero polynomial entered fixture multiplication")
    result = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            result[left_index + right_index] += left_value * right_value
    return trim(result)


def reconstruct_slp(slp: dict, coefficients: dict[str, int]) -> list[int]:
    registers = [[0, 1]]
    for gate_index, gate in enumerate(slp["gates"], start=1):
        operation = gate["op"]
        if operation == "coefficient":
            source = gate["source"]
            require(source in coefficients, "unknown coefficient register")
            result = trim([coefficients[source]])
        elif operation in {"add", "subtract", "multiply"}:
            left = gate["left"]
            right = gate["right"]
            require(
                type(left) is int
                and type(right) is int
                and 0 <= left < gate_index
                and 0 <= right < gate_index,
                "polynomial SLP source is not earlier",
            )
            if operation == "add":
                result = poly_add(registers[left], registers[right])
            elif operation == "subtract":
                result = poly_subtract(registers[left], registers[right])
            else:
                result = poly_multiply(registers[left], registers[right])
        elif operation == "square":
            source = gate["source"]
            require(
                type(source) is int and 0 <= source < gate_index,
                "square source is not earlier",
            )
            result = poly_multiply(registers[source], registers[source])
        else:
            raise AssertionError("unknown polynomial SLP operation")
        registers.append(result)
    output = slp["output_register"]
    require(
        type(output) is int and 0 <= output < len(registers),
        "invalid polynomial SLP output",
    )
    return registers[output]


def poly_evaluate(poly: list[int], value: int, modulus: int) -> int:
    result = 0
    for coefficient in reversed(poly):
        result = (result * value + coefficient) % modulus
    return result


def lucas_v(index: int, parameter: int, modulus: int) -> int:
    def pair(position: int) -> tuple[int, int]:
        if position == 0:
            return 2 % modulus, parameter % modulus
        left, right = pair(position // 2)
        even = (left * left - 2) % modulus
        odd = (left * right - parameter) % modulus
        if position % 2 == 0:
            return even, odd
        return odd, (right * right - 2) % modulus

    return pair(index)[0]


def legendre(value: int, prime: int) -> int:
    value %= prime
    if value == 0:
        return 0
    symbol = pow(value, (prime - 1) // 2, prime)
    return -1 if symbol == prime - 1 else symbol


def reconstruct_bad_set(
    prime: int,
    ell_minus: int,
    ell_plus: int,
) -> tuple[set[int], dict[str, int]]:
    minus_order = (prime - 1) // ell_minus
    plus_order = (prime + 1) // ell_plus
    direct = {
        value
        for value in range(1, prime)
        if pow(value, minus_order, prime) == 1
    }
    split = {(value + pow(value, prime - 2, prime)) % prime for value in direct}
    nonsplit = {
        parameter
        for parameter in range(prime)
        if (
            parameter in {2, prime - 2}
            or legendre(parameter * parameter - 4, prime) == -1
        )
        and lucas_v(plus_order, parameter, prime) == 2
    }
    require(len(direct) == minus_order, "direct subgroup size changed")
    require(len(split) == (minus_order + 2) // 2, "split image size changed")
    require(len(nonsplit) == (plus_order + 2) // 2, "nonsplit image size changed")
    bad = {0} | direct | split | nonsplit
    upper = 1 + (3 * minus_order + plus_order) // 2
    require(len(bad) <= upper, "reviewed local set bound failed")
    require(Fraction(len(bad), prime) < Fraction(3, ell_minus), "density bound failed")
    return bad, {
        "direct_subgroup_size": len(direct),
        "split_image_size": len(split),
        "nonsplit_image_size": len(nonsplit),
        "fixed_bad_set_size": len(bad),
        "reviewed_upper_bound": upper,
    }


def reconstruct_history(certificate: dict, modulus: int, first_sample: int) -> dict[str, int]:
    records = certificate["history_coefficient_registers"]["operations"]
    values: dict[str, int] = {}
    for record in records:
        name = record["name"]
        require(name not in values, "duplicate coefficient register")
        operation = record["op"]
        if operation == "literal":
            value = record["value"]
        elif operation == "prior_sample":
            require(record["sample"] == "x1", "unexpected sample register")
            value = first_sample
        elif operation == "multiply_mod":
            require(record["left"] in values and record["right"] in values, "late scalar source")
            value = values[record["left"]] * values[record["right"]] % modulus
        elif operation == "add_mod":
            require(record["left"] in values and record["right"] in values, "late scalar source")
            value = (values[record["left"]] + values[record["right"]]) % modulus
        else:
            raise AssertionError("unknown coefficient-register operation")
        require(type(value) is int and 0 <= value < modulus, "invalid coefficient value")
        values[name] = value
    require(list(values) == ["one", "c0", "c0_square", "c1"], "history recipe changed")
    require(values["one"] == 1 and values["c0"] == first_sample, "history anchor changed")
    require(
        values == certificate["history_coefficient_registers"]["values"],
        "recorded coefficient values changed",
    )
    return values


def reconstruct_bank(certificate: dict, coefficients: dict[str, int]) -> tuple[list[dict], int]:
    bank = certificate["round_two_bank"]
    require(
        [record["name"] for record in bank]
        == ["identity", "history_reciprocal", "history_quadratic_over_linear"],
        "second-round bank names changed",
    )
    derived = []
    degree_sum = 0
    for record in bank:
        numerator = reconstruct_slp(record["numerator"], coefficients)
        denominator = reconstruct_slp(record["denominator"], coefficients)
        require(
            numerator == record["expected_numerator_coefficients_ascending"],
            "numerator SLP expansion changed",
        )
        require(
            denominator == record["expected_denominator_coefficients_ascending"],
            "denominator SLP expansion changed",
        )
        require(numerator and denominator, "zero rational coordinate")
        require(numerator[-1] == denominator[-1] == 1, "coordinate is not monic")
        d_p = len(numerator) - 1
        d_q = len(denominator) - 1
        require(d_p != d_q, "coordinate degrees are equal")
        degree = max(d_p, d_q)
        require(
            (d_p, d_q, degree)
            == (
                record["numerator_degree"],
                record["denominator_degree"],
                record["maximum_degree"],
            ),
            "recorded coordinate degree changed",
        )
        degree_sum += degree
        derived.append(
            {
                "name": record["name"],
                "numerator": numerator,
                "denominator": denominator,
                "numerator_degree": d_p,
                "denominator_degree": d_q,
                "maximum_degree": degree,
            }
        )
    summary = certificate["round_two_map_summary"]
    require(summary["map_count"] == len(bank), "map count changed")
    require(
        summary["total_polynomial_slp_gates"]
        == sum(
            len(record["numerator"]["gates"]) + len(record["denominator"]["gates"])
            for record in bank
        ),
        "SLP gate count changed",
    )
    require(summary["history_coefficient_register_count"] == 4, "register count changed")
    require(summary["maximum_degree_sum"] == degree_sum == 4, "degree sum changed")
    return derived, degree_sum


def analyze_local(
    prime: int,
    bad: set[int],
    bank: list[dict],
) -> tuple[dict, set[int]]:
    union: set[int] = set()
    maps = []
    for record in bank:
        poles = set()
        pullback = set()
        fibers: Counter[int] = Counter()
        for value in range(prime):
            q_value = poly_evaluate(record["denominator"], value, prime)
            if q_value == 0:
                poles.add(value)
                continue
            mapped = (
                poly_evaluate(record["numerator"], value, prime)
                * pow(q_value, -1, prime)
                % prime
            )
            fibers[mapped] += 1
            if mapped in bad:
                pullback.add(value)
        unsafe = poles | pullback
        degree = record["maximum_degree"]
        d_q = record["denominator_degree"]
        algebraic_bound = d_q + degree * len(bad)
        require(len(poles) <= d_q, "pole count exceeds degree")
        max_fiber = max((fibers[target] for target in bad), default=0)
        require(max_fiber <= degree, "P-uQ fiber exceeds degree")
        require(
            len(unsafe) <= algebraic_bound <= 2 * degree * len(bad),
            "rational pullback bound failed",
        )
        union |= unsafe
        maps.append(
            {
                "name": record["name"],
                "pole_count": len(poles),
                "bad_value_pullback_count": len(pullback),
                "unsafe_count": len(unsafe),
                "maximum_bad_value_fiber": max_fiber,
                "denominator_degree": d_q,
                "maximum_degree": degree,
                "degree_plus_target_bound": algebraic_bound,
                "two_degree_target_bound": 2 * degree * len(bad),
                "all_residuals_nonzero_by_distinct_monic_degrees": True,
            }
        )
    bank_bound = sum(item["degree_plus_target_bound"] for item in maps)
    require(len(union) <= bank_bound, "bank union exceeds bound")
    safe = next(value for value in range(prime) if value not in union)
    return {
        "prime": prime,
        "fixed_bad_set_size": len(bad),
        "maps": maps,
        "bank_unsafe_union_size": len(union),
        "bank_algebraic_upper_bound": bank_bound,
        "least_fully_safe_input": safe,
    }, union


def denominator_tag(value: int, modulus: int) -> tuple[str, int]:
    divisor = math.gcd(value, modulus)
    if divisor == 1:
        return "ONE", divisor
    if divisor == modulus:
        return "WHOLE", divisor
    return "PROPER", divisor


def evaluate_scenario(
    name: str,
    sample: int,
    modulus: int,
    factors: tuple[int, int],
    bad_sets: dict[int, set[int]],
    bank: list[dict],
) -> dict:
    outcomes = []
    for record in bank:
        p_value = poly_evaluate(record["numerator"], sample, modulus)
        q_value = poly_evaluate(record["denominator"], sample, modulus)
        tag, divisor = denominator_tag(q_value, modulus)
        mapped_value = (
            p_value * pow(q_value, -1, modulus) % modulus if tag == "ONE" else None
        )
        local = []
        for prime in factors:
            local_q = q_value % prime
            if local_q == 0:
                local.append({"prime": prime, "pole": True, "mapped_is_safe": False})
            else:
                local_y = p_value % prime * pow(local_q, -1, prime) % prime
                local.append(
                    {
                        "prime": prime,
                        "pole": False,
                        "mapped_value": local_y,
                        "mapped_is_safe": local_y not in bad_sets[prime],
                    }
                )
        outcomes.append(
            {
                "name": record["name"],
                "numerator_mod_N": p_value,
                "denominator_mod_N": q_value,
                "denominator_tag": tag,
                "denominator_gcd": divisor,
                "mapped_value_mod_N": mapped_value,
                "local": local,
            }
        )
    return {"name": name, "sample": sample, "map_outcomes": outcomes}


def as_fraction(record: dict[str, int]) -> Fraction:
    return Fraction(record["numerator"], record["denominator"])


def gf25_multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return (
        (left[0] * right[0] + 3 * left[1] * right[1]) % 5,
        (left[0] * right[1] + left[1] * right[0]) % 5,
    )


def gf25_add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return ((left[0] + right[0]) % 5, (left[1] + right[1]) % 5)


def gf25_residual(value: tuple[int, int]) -> tuple[int, int]:
    square = gf25_multiply(value, value)
    linear = ((3 * value[0]) % 5, (3 * value[1]) % 5)
    return gf25_add(gf25_add(square, linear), (3, 0))


def verify_jacobian(
    certificate: dict,
    discovery_path: Path,
    contract_path: Path,
    payload_path: Path,
    output_path: Path,
) -> dict:
    discovery = json.loads(discovery_path.read_text(encoding="utf-8"))
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    output = json.loads(output_path.read_text(encoding="utf-8"))
    expected = certificate["jacobian"]
    operation = "finite_field.polynomial_map.table.compute"
    require(
        any(item["operation_id"] == operation for item in discovery["result"]["matches"]),
        "Jacobian operation was not discovered",
    )
    require(
        not any("rational" in item["operation_id"] for item in discovery["result"]["matches"]),
        "bounded discovery rational-operation flag changed",
    )
    require(contract["result"]["operation"]["operation_id"] == operation, "contract changed")
    require(output["request"]["operation_id"] == operation, "operation id changed")
    require(output["request"]["payload"] == payload, "payload/output mismatch")
    require("error" not in output["result"], "Jacobian structured error")
    polynomial = payload["polynomial_map"]["polynomial"]["coefficients"]
    require(
        [item["coordinates"] for item in polynomial] == [[3, 0], [3, 0], [1, 0]],
        "Jacobian residual polynomial changed",
    )
    entries = output["result"]["output"]["entries"]
    require(len(entries) == 25, "Jacobian table is incomplete")
    seen = set()
    roots = 0
    for entry in entries:
        argument = tuple(entry[0]["coordinates"])
        image = tuple(entry[1]["coordinates"])
        require(argument not in seen, "Jacobian table repeats an input")
        seen.add(argument)
        require(image == gf25_residual(argument), "Jacobian table value changed")
        roots += image == (0, 0)
    require(seen == {(a, b) for b in range(5) for a in range(5)}, "domain changed")
    actual = {
        "operation_id": operation,
        "protocol_version": output["protocol_version"],
        "server_version": output["server"]["version"],
        "runtime_ms": output["result"]["runtime_ms"],
        "field_size": len(entries),
        "residual_coefficients_ascending": [3, 3, 1],
        "residual_origin": {
            "first_sample_mod_5": 1,
            "c1_mod_5": 2,
            "target_u": 3,
            "identity": "P-uQ=X^2+3X+3",
        },
        "root_count": roots,
        "degree_bound": 2,
        "adapter_error": None,
        "timeout": False,
        "direct_rational_operation_in_bounded_discovery": False,
    }
    require(actual == expected, "Jacobian summary changed")
    require(roots == 2, "Jacobian root count changed")
    return actual


def verify(
    certificate: dict,
    discovery_path: Path,
    contract_path: Path,
    payload_path: Path,
    output_path: Path,
    max_prime: int,
) -> dict:
    require(certificate["schema_version"] == 1, "unsupported certificate schema")
    require(
        certificate["kind"] == "fresh_monic_rational_slp_two_round_exact_certificate",
        "unexpected certificate kind",
    )
    rate = certificate["asymptotic_rate_fixture"]
    delta = as_fraction(rate["delta"])
    critical = as_fraction(rate["critical_rate"])
    gap = as_fraction(rate["gap"])
    kappa = as_fraction(rate["kappa"])
    require(delta == Fraction(1, 21), "delta fixture changed")
    require(critical == Fraction(25, 518), "critical rate changed")
    require(gap == critical - delta == Fraction(1, 1554), "critical gap changed")
    require(kappa == gap / 2 == Fraction(1, 3108), "kappa changed")

    fixture = certificate["fixture"]
    h = fixture["h"]
    ell_minus = next_prime(2**h)
    ell_plus = next_prime(ell_minus)
    require((h, ell_minus, ell_plus) == (6, 67, 71), "canonical h=6 fixture changed")
    require(
        (fixture["ell_minus"], fixture["ell_plus"]) == (ell_minus, ell_plus),
        "protected primes changed",
    )
    residue_one, progression_modulus = crt(
        [(1, ell_minus), (-1, ell_plus), (1, 8)]
    )
    residue_three, second_modulus = crt(
        [(1, ell_minus), (-1, ell_plus), (3, 8)]
    )
    require(progression_modulus == second_modulus, "progression modulus changed")
    require(
        (
            fixture["progression_modulus"],
            fixture["residue_mod_8_equals_1"],
            fixture["residue_mod_8_equals_3"],
        )
        == (progression_modulus, residue_one, residue_three),
        "recorded CRT data changed",
    )
    p, p_rejected = least_progression_prime(residue_one, progression_modulus)
    q, q_rejected = least_progression_prime(residue_three, progression_modulus)
    require(max(p, q) <= max_prime, "finite prime ceiling exceeded")
    require((p, q) == (fixture["p"], fixture["q"]), "progression prime changed")
    require(
        (p_rejected, q_rejected)
        == (
            fixture["p_progression_terms_rejected"],
            fixture["q_progression_terms_rejected"],
        ),
        "progression rejection count changed",
    )
    modulus = p * q
    require(modulus == fixture["N"], "semiprime changed")
    require(p != q and p % 8 == 1 and q % 8 == 3, "factor separation changed")
    require(
        all(
            (prime - 1) % ell_minus == 0 and (prime + 1) % ell_plus == 0
            for prime in (p, q)
        ),
        "protected order divisibility changed",
    )

    bad_sets = {}
    local_count_summaries = {}
    first_local_safe = {}
    for prime in (p, q):
        bad, summary = reconstruct_bad_set(prime, ell_minus, ell_plus)
        bad_sets[prime] = bad
        local_count_summaries[prime] = summary
        first_local_safe[prime] = next(value for value in range(prime) if value not in bad)
    first_sample, first_modulus = crt(
        [(first_local_safe[p], p), (first_local_safe[q], q)]
    )
    require(first_modulus == modulus, "first-sample CRT modulus changed")
    round_one = certificate["round_one"]
    require(round_one["bank"] == "identity X/1", "first bank changed")
    require(
        round_one["local_safe_residues"]
        == [
            {"prime": p, "residue": first_local_safe[p]},
            {"prime": q, "residue": first_local_safe[q]},
        ],
        "first local safe residues changed",
    )
    require(round_one["accepted_sample"] == first_sample, "first sample changed")
    require(
        round_one["all_local_values_safe"]
        and all(first_sample % prime not in bad_sets[prime] for prime in (p, q)),
        "first round is not safe",
    )

    coefficients = reconstruct_history(certificate, modulus, first_sample)
    bank, degree_sum = reconstruct_bank(certificate, coefficients)

    derived_locals = []
    unsafe_sets = {}
    algebraic_probability = Fraction()
    for prime, recorded in zip((p, q), certificate["locals"], strict=True):
        require(recorded["prime"] == prime, "local prime order changed")
        derived, unsafe = analyze_local(prime, bad_sets[prime], bank)
        for key, value in local_count_summaries[prime].items():
            require(recorded[key] == value, f"local subgroup count changed: {key}")
        for key, value in derived.items():
            require(recorded[key] == value, f"local pullback record changed: {key}")
        unsafe_sets[prime] = unsafe
        algebraic_probability += Fraction(derived["bank_algebraic_upper_bound"], prime)
        derived_locals.append(
            {
                "prime": prime,
                "bad_set_size": len(bad_sets[prime]),
                "unsafe_union_size": len(unsafe),
                "algebraic_upper_bound": derived["bank_algebraic_upper_bound"],
                "least_safe_input": derived["least_fully_safe_input"],
            }
        )

    safe_sample, safe_modulus = crt(
        [
            (derived_locals[0]["least_safe_input"], p),
            (derived_locals[1]["least_safe_input"], q),
        ]
    )
    require(safe_modulus == modulus, "safe-sample CRT modulus changed")
    c0 = coefficients["c0"]
    c1 = coefficients["c1"]
    q_other = next(value for value in range(q) if value not in {c0 % q, c1 % q})
    p_other = next(value for value in range(p) if value not in {c0 % p, c1 % p})
    pole_p_sample, _ = crt([(c0 % p, p), (q_other, q)])
    pole_q_sample, _ = crt([(p_other, p), (c0 % q, q)])
    expected_scenarios = [
        evaluate_scenario(
            "reciprocal_pole_mod_p_only",
            pole_p_sample,
            modulus,
            (p, q),
            bad_sets,
            bank,
        ),
        evaluate_scenario(
            "reciprocal_pole_mod_q_only",
            pole_q_sample,
            modulus,
            (p, q),
            bad_sets,
            bank,
        ),
        evaluate_scenario(
            "reciprocal_whole_pole",
            c0,
            modulus,
            (p, q),
            bad_sets,
            bank,
        ),
        evaluate_scenario(
            "fully_safe_second_sample",
            safe_sample,
            modulus,
            (p, q),
            bad_sets,
            bank,
        ),
    ]
    require(
        certificate["round_two_scenarios"] == expected_scenarios,
        "round-two scenario replay changed",
    )
    reciprocal = [scenario["map_outcomes"][1] for scenario in expected_scenarios]
    require(
        [
            (outcome["denominator_tag"], outcome["denominator_gcd"])
            for outcome in reciprocal[:3]
        ]
        == [("PROPER", p), ("PROPER", q), ("WHOLE", modulus)],
        "reciprocal denominator tags changed",
    )
    require(
        all(
            outcome["denominator_tag"] == "ONE"
            and all(local["mapped_is_safe"] for local in outcome["local"])
            for outcome in expected_scenarios[3]["map_outcomes"]
        ),
        "fully safe scenario changed",
    )

    exact_bad_residues = (
        len(unsafe_sets[p]) * q
        + len(unsafe_sets[q]) * p
        - len(unsafe_sets[p]) * len(unsafe_sets[q])
    )
    exact_probability = Fraction(exact_bad_residues, modulus)
    reviewed_probability = Fraction(12 * degree_sum, ell_minus)
    probability = certificate["conditional_one_sample_probability"]
    require(
        probability["exact_bad_crt_residues"] == exact_bad_residues,
        "exact CRT unsafe count changed",
    )
    require(as_fraction(probability["exact_probability"]) == exact_probability, "exact probability changed")
    require(
        as_fraction(probability["algebraic_union_bound"]) == algebraic_probability,
        "algebraic probability bound changed",
    )
    require(
        as_fraction(probability["reviewed_twelve_degree_sum_over_ell_minus"])
        == reviewed_probability,
        "reviewed probability bound changed",
    )
    require(
        exact_probability <= algebraic_probability < reviewed_probability < 1,
        "conditional probability bound chain failed",
    )

    jacobian = verify_jacobian(
        certificate,
        discovery_path,
        contract_path,
        payload_path,
        output_path,
    )
    require(all(certificate["conditions"].values()), "certificate records a failed condition")
    require(certificate["all_conditions_pass"], "aggregate certificate condition failed")
    require(
        certificate["verdict"] == "FRESH_MONIC_RATIONAL_TWO_ROUND_REPLAY_PASSED",
        "certificate verdict changed",
    )
    return {
        "ok": True,
        "scope": certificate["scope"],
        "rate": {
            "delta": str(delta),
            "critical_rate": str(critical),
            "gap": str(gap),
            "kappa": str(kappa),
        },
        "fixture": {
            "h": h,
            "ell_minus": ell_minus,
            "ell_plus": ell_plus,
            "p": p,
            "q": q,
            "N": modulus,
        },
        "history": {
            "first_sample": first_sample,
            "coefficient_registers": coefficients,
            "second_bank_depends_on_first_sample": True,
        },
        "maps": [
            {
                "name": record["name"],
                "numerator_degree": record["numerator_degree"],
                "denominator_degree": record["denominator_degree"],
                "maximum_degree": record["maximum_degree"],
            }
            for record in bank
        ],
        "locals": derived_locals,
        "denominator_scenarios": {
            "proper_p": p,
            "proper_q": q,
            "whole": modulus,
            "fully_safe": True,
        },
        "conditional_one_sample_probability": {
            "exact": str(exact_probability),
            "algebraic_union_bound": str(algebraic_probability),
            "reviewed_bound": str(reviewed_probability),
        },
        "jacobian": jacobian,
        "claim_boundary": {
            "finite_replay": "passed",
            "asymptotic_theorem_source": "analysis.md equations (10)-(14)",
            "general_factoring": "not established",
        },
    }


def mutation_checks(
    certificate: dict,
    discovery_path: Path,
    contract_path: Path,
    payload_path: Path,
    output_path: Path,
    max_prime: int,
) -> list[str]:
    mutations = []

    changed_first_sample = copy.deepcopy(certificate)
    changed_first_sample["round_one"]["accepted_sample"] += 1
    mutations.append(("changed_first_sample", changed_first_sample))

    destroyed_monic_map = copy.deepcopy(certificate)
    destroyed_monic_map["round_two_bank"][2]["numerator"]["gates"][0] = {
        "op": "coefficient",
        "source": "one",
    }
    mutations.append(("destroyed_monic_map", destroyed_monic_map))

    changed_safe_sample = copy.deepcopy(certificate)
    changed_safe_sample["round_two_scenarios"][3]["sample"] += 1
    mutations.append(("changed_safe_sample", changed_safe_sample))

    changed_kappa = copy.deepcopy(certificate)
    changed_kappa["asymptotic_rate_fixture"]["kappa"]["numerator"] += 1
    mutations.append(("changed_kappa", changed_kappa))

    rejected = []
    for label, mutated in mutations:
        try:
            verify(
                mutated,
                discovery_path,
                contract_path,
                payload_path,
                output_path,
                max_prime,
            )
        except AssertionError:
            rejected.append(label)
        else:
            raise AssertionError(f"verifier accepted mutation: {label}")
    return rejected


def main() -> int:
    route = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=route / "certificate.json",
    )
    parser.add_argument(
        "--jacobian-discovery",
        type=Path,
        default=route / "evidence" / "jacobian-discovery.json",
    )
    parser.add_argument(
        "--jacobian-contract",
        type=Path,
        default=route / "evidence" / "jacobian-contract.json",
    )
    parser.add_argument(
        "--jacobian-payload",
        type=Path,
        default=route / "evidence" / "jacobian-payload.json",
    )
    parser.add_argument(
        "--jacobian-output",
        type=Path,
        default=route / "evidence" / "jacobian-output.json",
    )
    parser.add_argument("--max-prime", type=int, default=100_000)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    require(args.max_prime > 2, "max-prime must exceed two")
    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    result = verify(
        certificate,
        args.jacobian_discovery,
        args.jacobian_contract,
        args.jacobian_payload,
        args.jacobian_output,
        args.max_prime,
    )
    if args.self_test:
        result["mutations_rejected"] = mutation_checks(
            certificate,
            args.jacobian_discovery,
            args.jacobian_contract,
            args.jacobian_payload,
            args.jacobian_output,
            args.max_prime,
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
