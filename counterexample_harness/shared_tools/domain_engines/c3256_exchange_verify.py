#!/usr/bin/env python3
"""Exactly replay a reserved pair whose B-components cannot be flipped alone."""

import argparse
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def analyze(data):
    names = data["vertices"]
    require(len(names) == len(set(names)) and 2 <= len(names) <= 20, "Invalid vertices")
    number = {name: i for i, name in enumerate(names)}
    n = len(names)
    all_vertices = (1 << n) - 1
    topology = [tuple(number[name] for name in arc) for arc in data["topology"]]
    require(len(topology) == len(set(topology)), "Repeated topology arc")
    require(all(u != v for u, v in topology), "Topology loop")
    reach = [1 << v for v in range(n)]
    for u, v in topology:
        reach[u] |= 1 << v
    for k in range(n):
        for u in range(n):
            if reach[u] >> k & 1:
                reach[u] |= reach[k]
    require(all(not reach[v] >> u & 1 for u, v in topology), "Cyclic topology")
    require(all((u, v) in topology for u in range(n) for v in range(n)
                if u != v and reach[u] >> v & 1), "Topology is not transitive")
    ancestors = [
        sum(1 << u for u in range(n) if reach[u] >> v & 1)
        for v in range(n)
    ]
    sources = [v for v in range(n) if ancestors[v] == 1 << v]
    sinks = [v for v in range(n) if reach[v] == 1 << v]
    missing = [(u, v) for u in sources for v in sinks if not reach[u] >> v & 1]
    require(missing == [tuple(number[name] for name in data["missing_pair"])],
            "Wrong source-sink defect")
    s, t = missing[0]
    units = []
    q = data["q"]
    require(type(q) is int and q == len(data["colors"]) and q >= 3, "Invalid q")
    for color, arcs in enumerate(data["colors"]):
        converted = [tuple(number[name] for name in arc) for arc in arcs]
        require(len(converted) == len(set(converted)), "A color repeats an arc")
        for i, (u, v) in enumerate(converted):
            require((u, v) in topology, "Active unit outside original topology")
            units.append((f"J{color}:{i}", u, v, color))
    positive = {(u, v) for _, u, v, _ in units}
    tight_sources = [
        v for v in sources if sum(u == v for _, u, _, _ in units) == q
    ]
    tight_sinks = [
        v for v in sinks if sum(w == v for _, _, w, _ in units) == q
    ]
    tight = set(tight_sources + tight_sinks)
    terminal_shores = {1 << v for v in sources} | {
        all_vertices ^ (1 << v) for v in sinks
    }
    require(all(u in tight_sources or v in tight_sinks for _, u, v, _ in units),
            "A positive unit does not touch a q-tight terminal")
    require(all(not (any(u == v for u, _ in positive)
                     and any(w == v for _, w in positive)) for v in range(n)),
            "Positive incoming and outgoing support meet")
    terminals = set(sources + sinks)
    for x, v in positive:
        if v in terminals:
            continue
        for u, y in positive:
            if u not in terminals and reach[u] >> v & 1:
                require((x, y) == (s, t), "Minimal contact restriction fails")
    require(all(sum((u, v) == arc for _, u, v, _ in units) < q for arc in positive),
            "A positive arc has capacity at least q")

    cuts = []
    for shore in range(1, all_vertices):
        if any(shore >> v & 1 and ancestors[v] & ~shore for v in range(n)):
            continue
        boundary = [
            i for i, (_, u, v, _) in enumerate(units)
            if shore >> u & 1 and not shore >> v & 1
        ]
        require(len(boundary) >= q, "Original dicut below q")
        require(len(boundary) > q or shore in terminal_shores,
                "A nonterminal original dicut is tight")
        cuts.append((shore, boundary))
    require(min(len(boundary) for _, boundary in cuts) == q, "Wrong minimum dicut")
    ordinary = [
        cut for cut in cuts if not (cut[0] >> t & 1 and not cut[0] >> s & 1)
    ]
    exceptional = [cut for cut in cuts if cut not in ordinary]
    for _, boundary in ordinary:
        require({units[i][3] for i in boundary} == set(range(q)),
                "The prescribed colors are not completion dijoins")
    left = {v for v in range(n) if reach[v] >> t & 1}
    right = {v for v in range(n) if reach[s] >> v & 1}
    negative_middle = {v for _, v in positive if v not in left | right}
    canonical = left | {
        u for v in negative_middle for u in range(n) if ancestors[v] >> u & 1
    }
    canonical_shore = sum(1 << v for v in canonical)
    canonical_boundary = next(boundary for shore, boundary in exceptional
                              if shore == canonical_shore)
    require(all(set(canonical_boundary) <= set(boundary)
                for _, boundary in exceptional), "Canonical dominance fails")
    require(all(units[i][1] in left and units[i][2] in right
                for i in canonical_boundary), "Wrong canonical boundary endpoints")
    require(len(canonical_boundary) > q, "Original exceptional cut is not strict")
    counts = [sum(units[i][3] == c for i in canonical_boundary) for c in range(q)]
    require(counts[0] == 0 and counts[1] >= 2, "Not a bad/donor reserved pair")

    require(data["reserved_colors"] == [0, 1], "Unexpected reserved colors")
    reserved = [unit for unit in units if unit[3] in (0, 1)]
    reserved_number = {unit[0]: i for i, unit in enumerate(reserved)}
    cut_units = [
        (shore, [reserved_number[units[i][0]] for i in boundary
                 if units[i][3] in (0, 1)])
        for shore, boundary in cuts
    ]
    require(all(len(boundary) >= 2 for _, boundary in cut_units),
            "Reserved dicut below two")
    adjacency = [set() for _ in reserved]
    for terminal in tight:
        incident = [
            i for i, (_, u, v, _) in enumerate(reserved) if terminal in (u, v)
        ]
        require(len(incident) == 2 and {reserved[i][3] for i in incident} == {0, 1},
                "A q-tight terminal is not reserved-bichromatic")
        a, b = incident
        adjacency[a].add(b)
        adjacency[b].add(a)
    groups = []
    unseen = set(range(len(reserved)))
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack, group = [start], []
        while stack:
            a = stack.pop()
            group.append(a)
            for b in sorted(adjacency[a]):
                if b in unseen:
                    unseen.remove(b)
                    stack.append(b)
        groups.append(sorted(group))
    b_units = {
        reserved_number[units[i][0]] for i in canonical_boundary if units[i][3] == 1
    }

    def flipped(selected):
        changed = [unit[3] for unit in reserved]
        for k in selected:
            for i in groups[k]:
                changed[i] ^= 1
        return changed

    def failures(changed):
        return [
            (shore, next(iter({changed[i] for i in boundary})))
            for shore, boundary in cut_units if len({changed[i] for i in boundary}) == 1
        ]

    witnesses = {
        sum(1 << number[name] for name in shore)
        for shore in data["single_component_failure_shores"]
    }
    trials = []
    for k, group in enumerate(groups):
        if not set(group) & b_units:
            continue
        failed = failures(flipped([k]))
        require(failed, "A B-component unexpectedly works alone")
        decisive = [(shore, remaining) for shore, remaining in failed if shore in witnesses]
        require(decisive, "Missing prescribed ordinary-cut failure")
        require(all(not (shore >> t & 1 and not shore >> s & 1)
                    for shore, _ in decisive), "Failure witness is not ordinary")
        require(all(len(next(b for w, b in cut_units if w == shore)) == 2
                    and len(next(b for w, b in cuts if w == shore)) > q
                    for shore, _ in decisive), "Wrong reserved/original failure capacities")
        trials.append({
            "component": k,
            "units": [reserved[i][0] for i in group],
            "failure_count": len(failed),
            "decisive_failures": [
                {
                    "shore": [name for i, name in enumerate(names) if shore >> i & 1],
                    "remaining_color": remaining,
                    "reserved_capacity": len(next(b for w, b in cut_units if w == shore)),
                    "original_capacity": len(next(b for w, b in cuts if w == shore)),
                }
                for shore, remaining in decisive
            ],
        })
    require(len(trials) >= 2, "Fewer than two B-components were tested")
    selected = [
        next(k for k, group in enumerate(groups) if reserved_number[name] in group)
        for name in data["simultaneous_flip_component_representatives"]
    ]
    require(len(set(selected)) == 2, "The certificate is not a two-component exchange")
    changed = flipped(selected)
    require(not failures(changed), "The simultaneous exchange misses an original dicut")
    for shore, boundary in cuts:
        combined = {
            changed[reserved_number[units[i][0]]] if units[i][3] in (0, 1)
            else units[i][3] for i in boundary
        }
        require(combined == set(range(q)), "Reconstruction misses an original dicut")
    for color in range(q):
        used = [
            (u, v) for name, u, v, original in units
            if (changed[reserved_number[name]] if original in (0, 1) else original) == color
        ]
        require(len(used) == len(set(used)), "A reconstructed color repeats an arc")

    encoding = data.get("sat_encoding", "capacity_units")
    require(encoding in ("capacity_units", "tight_terminal_components"), "Unknown SAT encoding")
    component_of = {i: k for k, group in enumerate(groups) for i in group}
    variables = (
        sorted(reserved_number) if encoding == "capacity_units"
        else [f"component:{k:02}" for k in range(len(groups))]
    )
    variable_number = {name: i + 1 for i, name in enumerate(variables)}
    clauses = set()
    for _, boundary in cut_units:
        if encoding == "capacity_units":
            literals = tuple(sorted(variable_number[reserved[i][0]] for i in boundary))
        else:
            signed = {
                (component_of[i] + 1) * (1 if reserved[i][3] == 0 else -1)
                for i in boundary
            }
            if any(-literal in signed for literal in signed):
                continue
            literals = tuple(sorted(signed, key=abs))
        clauses.add(literals)
        clauses.add(tuple(-literal for literal in literals))
    ordered = sorted(clauses, key=lambda clause: tuple((abs(lit), lit > 0) for lit in clause))
    payload = {"cnf": {"variables": variables, "clauses": [list(c) for c in ordered]},
               "timeout_ms": 1000}
    output = {
        "classification": data["classification"],
        "vertices": n,
        "topology_arcs": len(topology),
        "passive_arcs": len(set(topology) - positive),
        "positive_arcs": len(positive),
        "capacity_units": len(units),
        "proper_ideals": len(cuts),
        "original_minimum_capacity": q,
        "reserved_minimum_capacity": min(len(b) for _, b in cut_units),
        "tight_sources": [names[v] for v in tight_sources],
        "tight_sinks": [names[v] for v in tight_sinks],
        "nontight_terminals": [names[v] for v in sources + sinks if v not in tight],
        "canonical_shore": [names[v] for v in sorted(canonical)],
        "canonical_color_counts": counts,
        "components": [[reserved[i][0] for i in group] for group in groups],
        "single_component_trials": trials,
        "simultaneous_flip_components": selected,
        "reconstructed_reserved_colors": {
            str(color): [reserved[i][0] for i, c in enumerate(changed) if c == color]
            for color in (0, 1)
        },
        "every_original_dicut_covered_after_reconstruction": True,
        "sat_variables": len(variables),
        "sat_clauses": len(clauses),
        "sat_encoding": encoding,
        "scope": data["scope"],
    }
    return output, payload, cut_units, reserved


def main():
    parser = argparse.ArgumentParser()
    directory = Path(__file__).resolve().parent
    parser.add_argument("--certificate", type=Path, default=directory / "exchange_example.json")
    parser.add_argument("--output", type=Path, default=directory / "exchange_verification.json")
    parser.add_argument("--sat-payload", type=Path,
                        default=directory / "jacobian" / "exchange_sat_canonical_payload.json")
    parser.add_argument("--adapter-output", type=Path)
    parser.add_argument("--canonicalizer-output", type=Path)
    args = parser.parse_args()
    if args.canonicalizer_output and not args.adapter_output:
        parser.error("--canonicalizer-output requires --adapter-output")
    output, payload, cuts, reserved = analyze(json.loads(args.certificate.read_text()))
    if args.adapter_output:
        require(json.loads(args.sat_payload.read_text()) == payload, "SAT payload changed")
        envelope = json.loads(args.adapter_output.read_text())
        require(envelope["request"]["operation_id"] == "sat.solve", "Wrong operation")
        require(envelope["request"]["payload"] == payload, "Adapter request mismatch")
        require(envelope["result"]["operation_id"] == "sat.solve", "Wrong typed operation")
        result = envelope["result"]["output"]
        require(result["source"] == payload, "SAT typed source mismatch")
        require(result["outcome"] == "SAT", "No SAT assignment to replay")
        assignment = result["assignment"]
        variables = payload["cnf"]["variables"]
        require(len(assignment) == len(variables) and all(type(x) is bool for x in assignment),
                "Invalid SAT assignment")
        values = dict(zip(variables, assignment))
        if output["sat_encoding"] == "capacity_units":
            unit_values = {unit[0]: values[unit[0]] for unit in reserved}
        else:
            original_values = {name: bool(color) for name, _, _, color in reserved}
            unit_values = {
                name: original_values[name] ^ values[f"component:{k:02}"]
                for k, group in enumerate(output["components"]) for name in group
            }
        require(all(len({unit_values[reserved[i][0]] for i in boundary}) == 2
                    for _, boundary in cuts), "SAT assignment misses an original dicut")
        require(all(any(assignment[abs(lit) - 1] == (lit > 0) for lit in clause)
                    for clause in payload["cnf"]["clauses"]), "SAT clause failure")
        output["jacobian"] = {
            "operation_id": "sat.solve",
            "outcome": "SAT",
            "server_version": envelope["server"]["version"],
            "protocol_version": envelope["protocol_version"],
            "exact_payload_and_typed_source_match": True,
            "assignment_replayed_on_every_original_dicut": True,
        }
        if args.canonicalizer_output:
            normalized = json.loads(args.canonicalizer_output.read_text())
            named = {
                "variable_names": variables,
                "clauses": [list(c) for c in sorted(tuple(c) for c in payload["cnf"]["clauses"])],
            }
            require(normalized["request"]["operation_id"] == "sat.cnf.canonicalize",
                    "Wrong canonicalizer operation")
            require(normalized["request"]["payload"] == named, "Named CNF request mismatch")
            require(normalized["result"]["operation_id"] == "sat.cnf.canonicalize",
                    "Wrong canonicalizer typed operation")
            require(normalized["result"]["output"]["cnf"] == payload["cnf"],
                    "Canonicalizer output mismatch")
            output["jacobian"]["canonicalization_bound_to_original_clause_set"] = True
    else:
        args.sat_payload.write_text(json.dumps(payload, separators=(",", ":")) + "\n")
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, separators=(",", ":")))


if __name__ == "__main__":
    main()
