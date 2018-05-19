from data_structures import SetUnion


def kruskal(G):
    total_weight = 0
    edges = sorted(list(G.iter_edges()), key=lambda e: e.weight)
    set_union = SetUnion(range(len(G)))

    for edge in edges:
        if not set_union.same_component(edge.x, edge.y):
            total_weight += edge.weight
            set_union.merge(edge.x, edge.y)

    return total_weight

