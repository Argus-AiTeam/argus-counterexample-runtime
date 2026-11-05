"""Six-terminal extension of the reviewed edge-set counting algebra."""

import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from full_signatures import (  # noqa: E402
    Signature,
    add_edge,
    catalog,
    forget,
    glue,
    join_table,
    leaf,
    project,
    relabel,
)
from routing_signatures import Routing  # noqa: E402

BOUNDARY_LIMIT = 6


def introduce(signature):
    size = signature.boundary_size
    if size >= BOUNDARY_LIMIT:
        raise ValueError("Introduction would exceed six terminals")
    old, _ = catalog(size)
    new, lookup = catalog(size + 1)
    counts = [0] * len(new)
    for routing, count in zip(old, signature.counts):
        target = Routing(routing.degrees + (0,), routing.pairs, routing.closed)
        counts[lookup[target]] = count
    return Signature(signature.degrees + (0,), signature.edges, tuple(counts))


def unary_specs(signature):
    size = len(signature.degrees)
    if size < BOUNDARY_LIMIT:
        yield {"op": "introduce"}
    for a, b in itertools.combinations(range(size), 2):
        if (
            (a, b) not in signature.edges
            and signature.degrees[a] < 4
            and signature.degrees[b] < 4
        ):
            yield {"op": "edge", "edge": (a, b)}
    for vertex, degree in enumerate(signature.degrees):
        if degree == 4:
            yield {"op": "forget", "vertex": vertex}


def apply_unary(signature, spec):
    operation = spec["op"]
    if operation == "introduce":
        value = introduce(signature)
    elif operation == "edge":
        value = add_edge(signature, *spec["edge"])
    elif operation == "forget":
        value = forget(signature, spec["vertex"])
    else:
        raise ValueError(f"Unknown unary operation: {operation}")
    return project(value)


def boundary_graph(size, edges):
    result = leaf()
    for _ in range(size):
        result = introduce(result)
    for edge in edges:
        result = add_edge(result, *edge)
    return result


def support(signature):
    return sum(1 << i for i, count in enumerate(signature.counts) if count)


def marker_only(signature, marker):
    return Signature(
        signature.degrees,
        signature.edges,
        tuple(int(i == marker) for i in range(len(signature.counts))),
    )


def classify_selected(boundary, vertices, edges):
    """Classify by concrete components, independently of the virtual-edge join."""
    adjacency = {vertex: [] for vertex in vertices}
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    positions = {vertex: i for i, vertex in enumerate(boundary)}
    if any(
        len(neighbors) > 2
        or (vertex not in positions and len(neighbors) != 2)
        for vertex, neighbors in adjacency.items()
    ):
        return None
    unseen = {vertex for vertex, neighbors in adjacency.items() if neighbors}
    pairs = []
    cycles = 0
    while unseen:
        pending = [min(unseen)]
        component = set()
        while pending:
            vertex = pending.pop()
            if vertex in component:
                continue
            component.add(vertex)
            pending.extend(adjacency[vertex])
        unseen.difference_update(component)
        endpoints = [
            vertex for vertex in component if len(adjacency[vertex]) == 1
        ]
        if endpoints:
            if len(endpoints) != 2 or any(v not in positions for v in endpoints):
                return None
            pairs.append(tuple(sorted(positions[v] for v in endpoints)))
        else:
            cycles += 1
    if cycles > 1 or (cycles and pairs):
        return None
    return Routing(
        tuple(len(adjacency[v]) for v in boundary),
        tuple(sorted(pairs)),
        bool(cycles),
    )


def enumerate_signature(boundary, vertices, edges):
    boundary = tuple(boundary)
    vertices = set(vertices)
    edges = tuple(tuple(sorted(edge)) for edge in edges)
    if (
        len(set(boundary)) != len(boundary)
        or len(boundary) > BOUNDARY_LIMIT
        or not set(boundary) <= vertices
        or len(set(edges)) != len(edges)
        or any(a == b or a not in vertices or b not in vertices for a, b in edges)
    ):
        raise ValueError("Invalid simple graph or boundary")
    degree = {vertex: 0 for vertex in vertices}
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    if any(degree[v] > 4 for v in boundary) or any(
        degree[v] != 4 for v in vertices - set(boundary)
    ):
        raise ValueError("Invalid partial quartic degree conditions")
    types, lookup = catalog(len(boundary))
    counts = [0] * len(types)
    for mask in range(1 << len(edges)):
        selected = tuple(edge for i, edge in enumerate(edges) if mask >> i & 1)
        routing = classify_selected(boundary, vertices, selected)
        if routing is not None:
            counts[lookup[routing]] += 1
    positions = {vertex: i for i, vertex in enumerate(boundary)}
    boundary_edges = tuple(
        sorted(
            tuple(sorted((positions[a], positions[b])))
            for a, b in edges
            if a in positions and b in positions
        )
    )
    return (
        Signature(
            tuple(degree[v] for v in boundary),
            boundary_edges,
            tuple(min(2, count) for count in counts),
        ),
        tuple(counts),
    )


def materialize(data, target):
    """Expand a construction DAG with fresh interiors and an explicit bag tree."""
    rows = data["rows"]
    next_vertex = 0
    bags = []
    tree_edges = []

    def bag(boundary, children):
        node = len(bags)
        bags.append(tuple(boundary))
        tree_edges.extend((child, node) for child in children)
        return node

    def visit(index):
        nonlocal next_vertex
        row = rows[index]
        term = row["construction"]
        operation = term["op"]
        if operation == "leaf":
            boundary, vertices, edges, children = [], set(), set(), []
        elif operation == "join":
            b1, v1, e1, root1 = visit(term["left"])
            b2, v2, e2, root2 = visit(term["right"])
            b2 = [b2[i] for i in term["right_order"]]
            rename = dict(zip(b2, b1))
            mapped_edges = {
                tuple(sorted((rename.get(a, a), rename.get(b, b))))
                for a, b in e2
            }
            if e1 & mapped_edges:
                raise ValueError("Construction introduces a duplicate edge")
            right_nodes = []
            pending = [root2]
            while pending:
                node = pending.pop()
                right_nodes.append(node)
                pending.extend(a for a, b in tree_edges if b == node)
            for node in right_nodes:
                bags[node] = tuple(rename.get(v, v) for v in bags[node])
            boundary = b1
            vertices = v1 | {rename.get(v, v) for v in v2}
            edges = e1 | mapped_edges
            children = [root1, root2]
        else:
            boundary, vertices, edges, root = visit(term["child"])
            children = [root]
            if operation == "introduce":
                boundary.append(next_vertex)
                vertices.add(next_vertex)
                next_vertex += 1
            elif operation == "edge":
                edge = tuple(sorted(boundary[i] for i in term["edge"]))
                if edge in edges:
                    raise ValueError("Construction introduces a duplicate edge")
                edges.add(edge)
            elif operation == "forget":
                del boundary[term["vertex"]]
            else:
                raise ValueError(f"Unknown construction operation: {operation}")
        boundary = [boundary[i] for i in row["canonical_order"]]
        if len(boundary) > BOUNDARY_LIMIT:
            raise ValueError("Construction exceeds six terminals")
        root = bag(boundary, children)
        return boundary, vertices, edges, root

    boundary, vertices, edges, root = visit(target)
    return {
        "boundary": boundary,
        "vertices": sorted(vertices),
        "edges": sorted(edges),
        "bags": bags,
        "tree_edges": tree_edges,
        "root": root,
    }
