#!/usr/bin/env python3
"""Exact replay of the terminal-relation route to the Peirce defect."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import deque
from functools import lru_cache
from pathlib import Path

import sympy as sym


HERE = Path(__file__).resolve().parent
CAMPAIGN = Path(__file__).resolve().parents[4]
TERMINAL = (
    CAMPAIGN
    / "research/parabolic_normal_form/terminal_completion"
    / "terminal-completion-certificate.json"
)
COMPRESSION = (
    CAMPAIGN
    / "research/idempotent_corner/exact-compression-certificate.json"
)
BASELINE = CAMPAIGN.parent.parent / "supervisor-evidence" / CAMPAIGN.name

q = sym.symbols("q")
y_nc, z_nc = sym.symbols("y z", commutative=False)
p, C, T = sym.symbols("p C T")

beta = q**3 + q - 1
alpha = q * (q**3 - q**2 - 1)
kappa = q * (q**2 - q - 1)
Q = (p - 1) * (p + q)
H = q**3 * p**2 + (q - 1) * p - q**3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact(value: sym.Expr) -> sym.Expr:
    return sym.factor(sym.cancel(value))


def expression_string(value: sym.Expr) -> str:
    return str(exact(value)).replace("**", "^")


def noncommutative_polynomial(expression: str) -> dict[str, sym.Expr]:
    parsed = sym.sympify(
        expression.replace("^", "**"),
        locals={"q": q, "y": y_nc, "z": z_nc},
        evaluate=False,
    ).expand()
    result: dict[str, sym.Expr] = {}
    for term in sym.Add.make_args(parsed):
        commutative, noncommutative = term.args_cnc()
        coefficient = sym.prod(commutative)
        word = ""
        for factor in noncommutative:
            if factor == y_nc:
                word += "y"
            elif factor == z_nc:
                word += "z"
            elif (
                factor.is_Pow
                and factor.base in (y_nc, z_nc)
                and factor.exp.is_Integer
            ):
                word += str(factor.base) * int(factor.exp)
            else:
                raise AssertionError(f"unexpected noncommutative factor: {factor}")
        result[word] = exact(result.get(word, 0) + coefficient)
    return {word: coefficient for word, coefficient in result.items() if coefficient}


class TerminalReducer:
    """Small exact free-algebra reducer reconstructed from the JSON basis."""

    def __init__(self, certificate: dict[str, object]) -> None:
        leading_words = certificate["leading_words"]
        basis = certificate["groebner_basis"]
        assert isinstance(leading_words, list)
        assert isinstance(basis, list)
        assert len(leading_words) == len(basis) == 9
        self.rules: list[tuple[str, dict[str, sym.Expr]]] = []
        for expected_index, (leading, record) in enumerate(
            zip(leading_words, basis), start=1
        ):
            assert isinstance(leading, str)
            assert isinstance(record, dict)
            assert record["index"] == expected_index
            polynomial = noncommutative_polynomial(str(record["polynomial"]))
            assert leading in polynomial
            leading_coefficient = polynomial[leading]
            replacement = {
                word: exact(-coefficient / leading_coefficient)
                for word, coefficient in polynomial.items()
                if word != leading
            }
            self.rules.append((leading, replacement))

    @lru_cache(maxsize=None)
    def reduce_word(
        self, word: str
    ) -> tuple[tuple[tuple[str, sym.Expr], ...], frozenset[tuple[int, str]]]:
        for index, (leading, replacement) in enumerate(self.rules, start=1):
            position = word.find(leading)
            if position < 0:
                continue
            prefix = word[:position]
            suffix = word[position + len(leading) :]
            result: dict[str, sym.Expr] = {}
            provenance: set[tuple[int, str]] = {(index, leading)}
            for middle, coefficient in replacement.items():
                reduced, used = self.reduce_word(prefix + middle + suffix)
                provenance.update(used)
                for reduced_word, reduced_coefficient in reduced:
                    result[reduced_word] = exact(
                        result.get(reduced_word, 0)
                        + coefficient * reduced_coefficient
                    )
            return (
                tuple(
                    sorted(
                        (reduced_word, coefficient)
                        for reduced_word, coefficient in result.items()
                        if coefficient
                    )
                ),
                frozenset(provenance),
            )
        return (((word, sym.S.One),), frozenset())

    def reduce_polynomial(
        self, polynomial: dict[str, sym.Expr]
    ) -> tuple[dict[str, sym.Expr], list[dict[str, object]]]:
        result: dict[str, sym.Expr] = {}
        provenance: set[tuple[int, str]] = set()
        for word, coefficient in polynomial.items():
            reduced, used = self.reduce_word(word)
            provenance.update(used)
            for reduced_word, reduced_coefficient in reduced:
                result[reduced_word] = exact(
                    result.get(reduced_word, 0)
                    + coefficient * reduced_coefficient
                )
        result = {
            word: coefficient for word, coefficient in result.items() if coefficient
        }
        sources = [
            {
                "rule_index": index,
                "leading_word_terminal": leading,
                "leading_word_current": rename_word(leading),
            }
            for index, leading in sorted(provenance)
        ]
        return result, sources


def rename_word(word: str) -> str:
    """Rename terminal (y,z) to current (z,w), rendered as (Z,W)."""
    return word.translate(str.maketrans({"y": "Z", "z": "W"}))


PREMISE_REWRITES = (
    ("idempotent_e", "EE", "E", False),
    ("compression_eze", "EZE", "E", False),
    ("compression_ez2e", "EZZE", "E", False),
    ("distant_commutation_ew", "EW", "WE", True),
    ("braid_zwz", "ZWZ", "WZW", True),
)


def rewrite_neighbors(word: str):
    for premise, left, right, reversible in PREMISE_REWRITES:
        directions = [(left, right)]
        if reversible:
            directions.append((right, left))
        for source, target in directions:
            for position in range(len(word) - len(source) + 1):
                if word[position : position + len(source)] != source:
                    continue
                yield (
                    word[:position] + target + word[position + len(source) :],
                    premise,
                    position,
                    source,
                    target,
                )


def rewrite_path(source: str, target: str) -> list[dict[str, object]]:
    queue: deque[str] = deque([source])
    previous: dict[
        str, tuple[str, str, int, str, str] | None
    ] = {source: None}
    while queue and len(previous) < 100_000:
        current = queue.popleft()
        if current == target:
            break
        for neighbor, premise, position, old, new in rewrite_neighbors(current):
            if neighbor in previous:
                continue
            previous[neighbor] = (current, premise, position, old, new)
            queue.append(neighbor)
    if target not in previous:
        raise AssertionError(f"no named-premise rewrite: {source} -> {target}")
    steps: list[dict[str, object]] = []
    current = target
    while previous[current] is not None:
        prior, premise, position, old, new = previous[current]
        steps.append(
            {
                "premise": premise,
                "position_zero_based": position,
                "from": prior,
                "to": current,
                "replaced": f"{old}->{new}",
            }
        )
        current = prior
    steps.reverse()
    return steps


# These are precisely the one-block representatives used by the terminal
# closure identities, plus the normal words in the Cp reduction.
SANDWICH_VALUES: dict[str, sym.Expr] = {
    "": sym.S.One,
    "y": sym.S.One,
    "yy": sym.S.One,
    "z": p,
    "zy": p,
    "zyy": p,
    "zz": p**2,
    "zzy": p**2,
    "zzyy": p**2,
    "yz": p,
    "yzy": p**2,
    "yzyy": p**3,
    "yzz": p**2,
    "yzzy": C,
    "yzzyy": T,
    "yyz": p,
    "yyzy": p**3,
    "yyzz": p**2,
    "zyyz": p**2,
    "zyzz": p**3,
    "zzyz": p**3,
    "zzyzz": p**4,
    "zzz": p**3,
}


def canonical_word(value: sym.Expr) -> str:
    if value == 1:
        return "E"
    if value == p:
        return "WE"
    if value == p**2:
        return "WWE"
    if value == p**3:
        return "WWWE"
    if value == p**4:
        return "WWWWE"
    if value == C:
        return "EZWWZE"
    if value == T:
        return "EZWWZZE"
    raise AssertionError(f"no canonical word for sandwich value {value}")


def sandwich_record(terminal_word: str, value: sym.Expr) -> dict[str, object]:
    current_word = rename_word(terminal_word)
    source = "E" + current_word + "E"
    target = canonical_word(value)
    steps = rewrite_path(source, target)
    return {
        "terminal_word": terminal_word or "1",
        "current_word": current_word or "1",
        "sandwich_value": expression_string(value),
        "source_with_e": source,
        "canonical_word": target,
        "rewrite_steps": steps,
    }


def closure_polynomial(record: dict[str, object]) -> dict[str, sym.Expr]:
    left_word = str(record["left_word"])
    polynomial: dict[str, sym.Expr] = {left_word: sym.S.One}
    terms = record["right_linear_combination"]
    assert isinstance(terms, list)
    for term in terms:
        assert isinstance(term, dict)
        word = "" if term["word"] == "1" else str(term["word"])
        coefficient = sym.sympify(str(term["coefficient"]), locals={"q": q})
        polynomial[word] = exact(polynomial.get(word, 0) - coefficient)
    return polynomial


def sandwich_closure(record: dict[str, object]) -> sym.Expr:
    left_word = str(record["left_word"])
    # A target z^i y^j z^k becomes W^i Z^j W^k.  Moving the
    # boundary W powers through e and compressing Z or Z^2 gives p^(i+k).
    result = p ** left_word.count("z")
    terms = record["right_linear_combination"]
    assert isinstance(terms, list)
    for term in terms:
        assert isinstance(term, dict)
        word = "" if term["word"] == "1" else str(term["word"])
        coefficient = sym.sympify(str(term["coefficient"]), locals={"q": q})
        result -= coefficient * SANDWICH_VALUES[word]
    return exact(result)


def polynomial_remainder_zero(expression: sym.Expr, divisor: sym.Expr) -> bool:
    numerator, _ = sym.together(expression).as_numer_denom()
    return exact(sym.rem(numerator, sym.expand(divisor), p)) == 0


def pair_add(left, right):
    return (exact(left[0] + right[0]), exact(left[1] + right[1]))


def pair_mul(left, right):
    return (exact(left[0] * right[0]), exact(left[1] * right[1]))


def pair_scale(scalar, value):
    return (exact(scalar * value[0]), exact(scalar * value[1]))


def pair_sub(left, right):
    return pair_add(left, pair_scale(-1, right))


def assert_pair_zero(value) -> None:
    assert exact(value[0]) == exact(value[1]) == 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.parent != HERE:
        raise SystemExit("output must stay in relation_route/")

    terminal = json.loads(TERMINAL.read_text(encoding="utf-8"))
    compression = json.loads(COMPRESSION.read_text(encoding="utf-8"))
    assert terminal["status"] == "passed"
    assert terminal["coefficient_field"] == "Q(q)"
    assert terminal["normal_basis_dimension"] == 19
    assert all(
        remainder == "0"
        for remainder in terminal["source_relation_remainders"].values()
    )
    assert compression["status"] == "passed"
    compression_rows = {
        row["exponent"]: row["identity"] for row in compression["compressions"]
    }
    assert 1 in compression_rows and 2 in compression_rows

    baseline_files = (
        "twist-extension-verification.json",
        "twist-extension-modular-verification.json",
    )
    baseline_records = {}
    for name in baseline_files:
        path = BASELINE / name
        record = json.loads(path.read_text(encoding="utf-8"))
        assert record["status"] == "passed"
        baseline_records[name] = {
            "status": "passed",
            "sha256": sha256(path),
        }

    reducer = TerminalReducer(terminal)
    cubic_z_source = noncommutative_polynomial(
        str(terminal["groebner_basis"][0]["polynomial"])
    )
    expected_cubic_z = {
        "zzz": sym.S.One,
        "zz": beta,
        "z": alpha,
        "": -q**4,
    }
    assert all(
        exact(cubic_z_source.get(word, 0) - expected_cubic_z.get(word, 0)) == 0
        for word in set(cubic_z_source) | set(expected_cubic_z)
    )
    closures = terminal["sandwich_decomposition"]["closure_identities"]
    assert isinstance(closures, list) and len(closures) == 8

    closure_replays = []
    closure_residuals: dict[str, sym.Expr] = {}
    used_sandwiches: dict[str, sym.Expr] = {}
    for index, record in enumerate(closures, start=1):
        assert isinstance(record, dict)
        word = str(record["left_word"])
        reduced, sources = reducer.reduce_polynomial(closure_polynomial(record))
        assert not reduced
        residual = sandwich_closure(record)
        closure_residuals[word] = residual
        target_value = p ** word.count("z")
        used_sandwiches[word] = target_value
        for term in record["right_linear_combination"]:
            terminal_word = "" if term["word"] == "1" else str(term["word"])
            used_sandwiches[terminal_word] = SANDWICH_VALUES[terminal_word]
        closure_replays.append(
            {
                "closure_index_one_based": index,
                "terminal_target": word,
                "current_target": rename_word(word),
                "free_algebra_remainder": "0",
                "source_rules_used": sources,
            }
        )
    used_sandwiches["zzz"] = p**3

    relation_one_raw = (
        p**3 + (beta - alpha) * p**2 + alpha * p - beta * C - T
    )
    assert exact(closure_residuals["zzyyz"] - relation_one_raw) == 0

    cubic_p = p**3 + beta * p**2 + alpha * p - q**4
    assert exact(cubic_p - sym.expand(Q * (p + q**3))) == 0
    consequence_one_residual = exact(cubic_p - relation_one_raw)
    assert consequence_one_residual == exact(beta * C + T + alpha * p**2 - q**4)

    relation_two_after_one = exact(
        closure_residuals["zzyzz"].subs(
            T, q**4 - alpha * p**2 - beta * C
        )
    )
    assert exact(relation_two_after_one - Q * H / q**3) == 0

    bezout_multiplier = q**3 * p + q - 1 - q**6
    bezout_unit = exact(q**9 - q**4)
    assert exact(H - (p + q**3) * bezout_multiplier - bezout_unit) == 0
    assert exact(bezout_unit - q**4 * (q**5 - 1)) == 0
    assert bezout_unit != 0  # Hence it is a unit in Q(q).

    # Every terminal sandwich-closure row becomes zero after relation (1)
    # and Q(p)=0; no omitted closure row supplies a C coefficient.
    closure_mod_core = {}
    for word, residual in closure_residuals.items():
        substituted = exact(
            residual.subs(T, q**4 - alpha * p**2 - beta * C)
        )
        assert polynomial_remainder_zero(substituted, Q)
        closure_mod_core[word] = "0"

    cp_reduced, cp_sources = reducer.reduce_word("yzzyz")
    cp_normal_form = dict(cp_reduced)
    expected_cp_normal_form = {
        "y": sym.S.One,
        "yy": -sym.S.One,
        "yyz": sym.S.One,
        "yzz": -sym.S.One,
        "yzzy": sym.S.One,
        "z": -sym.S.One,
        "zyy": sym.S.One,
        "zyyz": -sym.S.One,
        "zz": sym.S.One,
        "zzy": -sym.S.One,
        "zzyzz": sym.S.One,
    }
    assert cp_normal_form == expected_cp_normal_form
    cp_rhs = exact(
        sum(
            coefficient * SANDWICH_VALUES[word]
            for word, coefficient in cp_normal_form.items()
        )
    )
    assert cp_rhs == C + p**4 - 2 * p**2 + p
    for word in cp_normal_form:
        used_sandwiches[word] = SANDWICH_VALUES[word]

    # Cp and pC both braid in one step to the same sandwiched word.
    cp_braid_path = rewrite_path("EZWWZWE", "EZWZWZE")
    pc_braid_path = rewrite_path("EWZWWZE", "EZWZWZE")
    cp_product_path = rewrite_path("EZWWZEWE", "EZWWZWE")
    pc_product_path = rewrite_path("WEEZWWZE", "EWZWWZE")
    assert any(step["premise"] == "braid_zwz" for step in cp_braid_path)
    assert any(step["premise"] == "braid_zwz" for step in pc_braid_path)

    consequence_four_polynomial = p**4 - 2 * p**2 + p + kappa * (p - 1)
    consequence_four_quotient = p**2 + (1 - q) * p + q**2 - q - 1
    assert exact(
        consequence_four_polynomial - Q * consequence_four_quotient
    ) == 0

    # Projectors are checked in K[p]/(Q), where e is the corner identity.
    g_plus = (p + q) / (q + 1)
    g_minus = (1 - p) / (q + 1)
    for identity in (
        g_plus**2 - g_plus,
        g_minus**2 - g_minus,
        g_plus * g_minus,
        g_plus + g_minus - 1,
        p * g_plus - g_plus,
        p * g_minus + q * g_minus,
    ):
        assert polynomial_remainder_zero(identity, Q)
    annihilator = (p - 1) * (C + kappa)
    assert exact(
        g_minus * (C + kappa) + annihilator / (q + 1)
    ) == 0
    assert exact(kappa + q**2 - q * (q**2 - 1)) == 0
    assert exact(q**4 - alpha - (q**3 + q)) == 0
    assert exact(
        q**4 - alpha * q**2 + beta * kappa
        - q * (q**3 - q**2 + 1)
    ) == 0

    # A two-idempotent abstract corner model verifies that consequences
    # (1)--(4) leave the g_+C coordinate genuinely free.
    gamma = sym.symbols("gamma")
    e_pair = (sym.S.One, sym.S.One)
    p_pair = (sym.S.One, -q)
    C_pair = (gamma, -kappa)
    T_pair = (
        q**3 + q - beta * gamma,
        q * (q**3 - q**2 + 1),
    )
    p2_pair = pair_mul(p_pair, p_pair)
    p4_pair = pair_mul(p2_pair, p2_pair)
    assert_pair_zero(
        pair_sub(
            pair_add(pair_scale(beta, C_pair), T_pair),
            pair_sub(pair_scale(q**4, e_pair), pair_scale(alpha, p2_pair)),
        )
    )
    assert_pair_zero(
        pair_sub(
            p2_pair,
            pair_add(pair_scale(1 - q, p_pair), pair_scale(q, e_pair)),
        )
    )
    assert_pair_zero(
        pair_sub(
            pair_mul(C_pair, p_pair),
            pair_add(
                C_pair,
                pair_add(
                    p4_pair,
                    pair_add(pair_scale(-2, p2_pair), p_pair),
                ),
            ),
        )
    )
    assert_pair_zero(pair_sub(pair_mul(C_pair, p_pair), pair_mul(p_pair, C_pair)))
    assert_pair_zero(
        pair_mul(
            pair_sub(p_pair, e_pair),
            pair_add(C_pair, pair_scale(kappa, e_pair)),
        )
    )
    assert sym.diff(C_pair[0], gamma) == 1

    tau = sym.symbols("tau")
    gamma_from_tau = exact((q**3 + q - tau) / beta)
    delta_g_plus = exact((1 - tau) / beta)
    delta_g_minus = exact(-q * (q**2 - 1))
    delta_e_coefficient = exact(
        (q * delta_g_plus + delta_g_minus) / (q + 1)
    )
    delta_p_coefficient = exact(
        (delta_g_plus - delta_g_minus) / (q + 1)
    )
    gamma_delta_e = exact(q * (gamma - q**2) / (q + 1))
    gamma_delta_p = exact((gamma + q**3 - q - 1) / (q + 1))
    assert exact(gamma_delta_e.subs(gamma, gamma_from_tau) - delta_e_coefficient) == 0
    assert exact(gamma_delta_p.subs(gamma, gamma_from_tau) - delta_p_coefficient) == 0

    sandwich_records = [
        sandwich_record(word, value)
        for word, value in sorted(
            used_sandwiches.items(), key=lambda item: (len(item[0]), item[0])
        )
    ]

    payload = {
        "schema": "peirce-defect-terminal-relation-route-v1",
        "status": "passed",
        "coefficient_field": "Q(q)",
        "exact_interpreter": {
            "name": "SymPy",
            "version": sym.__version__,
            "arithmetic": "symbolic rational functions over Q(q)",
        },
        "source_certificates": {
            "terminal_completion": {
                "path": str(TERMINAL.relative_to(CAMPAIGN)),
                "sha256": sha256(TERMINAL),
                "status": terminal["status"],
                "renaming": {"terminal_y": "current_z", "terminal_z": "current_w"},
                "groebner_basis_size": 9,
                "normal_basis_dimension": 19,
            },
            "reviewed_compression": {
                "path": str(COMPRESSION.relative_to(CAMPAIGN)),
                "sha256": sha256(COMPRESSION),
                "status": compression["status"],
                "rows_used": {
                    "eze=e": compression_rows[1],
                    "ez^2e=e": compression_rows[2],
                },
            },
            "immutable_baseline_replay": baseline_records,
        },
        "named_premises": [
            {
                "name": "idempotent_e",
                "identity": "e^2=e",
                "source": "reviewed normalized terminal projector",
            },
            {
                "name": "compression_eze",
                "identity": "eze=e",
                "source": "reviewed exact compression exponent 1",
            },
            {
                "name": "compression_ez2e",
                "identity": "ez^2e=e",
                "source": "reviewed exact compression exponent 2",
            },
            {
                "name": "distant_commutation_ew",
                "identity": "ew=we",
                "source": "distant braid-generator commutation",
            },
            {
                "name": "braid_zwz",
                "identity": "zwz=wzw",
                "source": "terminal braid row",
            },
        ],
        "terminal_replay": {
            "closure_identities": closure_replays,
            "all_closure_rows_mod_core": closure_mod_core,
            "selected_sources": {
                "relation_1": {
                    "closure_index_one_based": 7,
                    "terminal_word": "zzyyz",
                    "current_word": "wwzzw",
                    "initial_leading_rule_index": 6,
                    "initial_leading_word_terminal": "zzyyz",
                    "sandwiched_identity": (
                        "p^3=alpha*p^2+beta*C+T-alpha*p-beta*p^2"
                    ),
                },
                "quadratic_auxiliary": {
                    "closure_index_one_based": 6,
                    "terminal_word": "zzyzz",
                    "current_word": "wwzww",
                    "after_relation_1": "Q(p)*H(p)/q^3=0",
                    "Q": "(p-e)(p+q*e)",
                    "H": "q^3*p^2+(q-1)*p-q^3*e",
                },
                "p_cubic": {
                    "groebner_rule_index": 1,
                    "leading_word_terminal": "zzz",
                    "leading_word_current": "www",
                    "source_polynomial_replayed": (
                        "z^3+beta*z^2+alpha*z-q^4"
                    ),
                    "identity": "Q(p)*(p+q^3*e)=0",
                },
                "Cp": {
                    "terminal_word": "yzzyz",
                    "current_word": "zwwzw",
                    "initial_leading_rule_index": 5,
                    "initial_leading_word_terminal": "yzzyz",
                    "source_rules_used": [
                        {
                            "rule_index": index,
                            "leading_word_terminal": leading,
                            "leading_word_current": rename_word(leading),
                        }
                        for index, leading in sorted(cp_sources)
                    ],
                    "normal_form": [
                        {
                            "coefficient": expression_string(coefficient),
                            "word": word or "1",
                        }
                        for word, coefficient in cp_reduced
                    ],
                    "sandwiched_identity": "Cp=C+p^4-2*p^2+p",
                },
            },
            "sandwich_substitutions": sandwich_records,
            "Cp_commutation": {
                "Cp_product_to_sandwich": cp_product_path,
                "pC_product_to_sandwich": pc_product_path,
                "Cp_to_common_braid_word": cp_braid_path,
                "pC_to_common_braid_word": pc_braid_path,
                "common_word": "EZWZWZE",
            },
        },
        "coefficient_arithmetic": {
            "alpha": expression_string(alpha),
            "beta": expression_string(beta),
            "kappa": expression_string(kappa),
            "quadratic_bezout": {
                "H_decomposition": (
                    "H=(p+q^3*e)*(q^3*p+(q-1-q^6)*e)+q^4*(q^5-1)*e"
                ),
                "unit": "q^4*(q^5-1)",
                "conclusion": "Q(p)=0 over Q(q)",
            },
            "annihilator_factorization": {
                "left": "p^4-2*p^2+p+kappa*(p-e)",
                "right": (
                    "Q(p)*(p^2+(1-q)*p+(q^2-q-1)*e)"
                ),
            },
        },
        "exact_consequences": [
            {
                "number": 1,
                "identity": "beta*C+T=q^4*e-alpha*p^2",
                "status": "proved",
            },
            {
                "number": 2,
                "identity": "p^2=(1-q)*p+q*e",
                "equivalent": "(p-e)(p+q*e)=0",
                "status": "proved",
            },
            {
                "number": 3,
                "identity": "Cp=pC=C+p^4-2*p^2+p",
                "status": "proved",
            },
            {
                "number": 4,
                "identity": "(p-e)*(C+q*(q^2-q-1)*e)=0",
                "status": "proved",
            },
            {
                "number": 5,
                "projectors": {
                    "g_plus": "(p+q*e)/(q+1)",
                    "g_minus": "(e-p)/(q+1)",
                },
                "identity": "g_minus*C=-q*(q^2-q-1)*g_minus",
                "g_plus_channel": "not constrained by consequences 1--4",
                "underdetermination_model": {
                    "e": "(1,1)",
                    "p": "(1,-q)",
                    "C": "(gamma,-q*(q^2-q-1))",
                    "T": (
                        "(q^3+q-beta*gamma,"
                        "q*(q^3-q^2+1))"
                    ),
                    "parameter": "gamma is free over Q(q)",
                    "scope": (
                        "abstract model of the displayed corner equations only; "
                        "not a representation of the universal quotient"
                    ),
                },
                "status": "proved",
            },
        ],
        "unresolved_transition": {
            "statement": "Delta=C-p^2 lies in span_K{e,p,p^2}=span_K{e,we,w^2e}",
            "status": "unresolved",
            "resolved_channel": (
                "g_minus*Delta=-q*(q^2-1)*g_minus"
            ),
            "unresolved_channel": "g_plus*Delta",
            "equivalence": (
                "The transition holds iff g_plus*C is a scalar multiple of "
                "g_plus, equivalently iff g_plus*T is a scalar multiple of "
                "g_plus."
            ),
            "smallest_additional_scalar_identity": {
                "identity": "g_plus*T=tau*g_plus for some tau in K",
                "equivalent_form": (
                    "g_plus*C=gamma*g_plus, "
                    "gamma=(q^3+q-tau)/beta"
                ),
                "resulting_T": (
                    "T=tau*g_plus+q*(q^3-q^2+1)*g_minus"
                ),
                "resulting_Delta_projectors": (
                    "Delta=((1-tau)/beta)*g_plus"
                    "-q*(q^2-1)*g_minus"
                ),
                "resulting_Delta_e_coefficient": expression_string(
                    delta_e_coefficient
                ),
                "resulting_Delta_p_coefficient": expression_string(
                    delta_p_coefficient
                ),
                "resulting_Delta_p2_coefficient": "0",
            },
        },
        "scope": (
            "Exact local consequences only. The Delta membership transition "
            "remains unresolved; no separator and no universal "
            "finite-dimensionality statement is claimed."
        ),
    }
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": "passed",
                "terminal_closures_replayed": len(closure_replays),
                "sandwich_substitutions_replayed": len(sandwich_records),
                "consequences_verified": 5,
                "transition": "unresolved",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
