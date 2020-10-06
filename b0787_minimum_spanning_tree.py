import heapq


def minimum_spanning_tree(graph):
    # type: (Dict[str, Dict[str, int]]) -> Dict[str[Dict[str, int]]]
    """Returns the subset of the edges that connects all the vertices together
    with the minimum possible total edge weight.

    https://leetcode.com/problems/cheapest-flights-within-k-stops (analogous)
    """
    edges = []

    for k1, v1 in graph.items():
        for k2, v2 in v1.items():
            # Store edges in distance-from-to format
            if k1 < k2:
                edges.append((v2, k1, k2))

    heapq.heapify(edges)

    nodes_visited = set()
    node_count = len(graph)

    # Create dictionary of dictionaries to store result
    result = {key: {} for key in graph}

    # Continue until all nodes are visited
    while len(nodes_visited) < node_count:
        # Select edge with minimum distance
        cost, node_from, node_to = heapq.heappop(edges)

        # Include to result if from or to node not in visited set
        if node_from not in nodes_visited or node_to not in nodes_visited:
            nodes_visited.add(node_from)
            nodes_visited.add(node_to)
            result[node_from][node_to] = cost
            result[node_to][node_from] = cost

    return result


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
        'C': {'A': 3, 'B': 1, 'F': 5},
        'D': {'B': 1, 'E': 1},
        'E': {'B': 4, 'D': 1, 'F': 1},
        'F': {'C': 5, 'E': 1, 'G': 1},
        'G': {'F': 1},
    }

    print(minimum_spanning_tree(graph))
