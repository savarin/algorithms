import random


def topological_sort(graph):
    # type: Dict[str, List[str]] -> Optional[List[Tuple[Union[str, int]]]]
    """Return linear ordering of the vertices of a directed graph.

    https://leetcode.com/problems/course-schedule (analogous)
    """
    result = []
    counter = len(graph)

    # Select random node
    node = random.choice(list(graph.keys()))
    visited = set([node])

    while True:
        # If node does not point to any other node, remove from graph
        if len(graph[node]) == 0:
            # Remove node from targets
            for k, v in graph.items():
                if node in v:
                    v.remove(node)

            # Remove node from source
            del graph[node]

            # Append node with current counter and decrement counter
            result.append((node, counter))
            counter -= 1

            # If all nodes accounted for, break from loop
            if counter == 0:
                break
            # Otherwise select another random node and reset nodes visited
            else:
                node = random.choice(list(graph.keys()))
                visited = set()

        # If node does point to other nodes, check if there's a cycle
        else:
            targets = graph[node]
            node = random.choice(targets)

            # If going down target nodes ends up in a cycle, return early
            if node in visited:
                return None

            visited.add(node)

    return result


if __name__ == "__main__":
    graph_1 = {
        'A': ['B', 'C'],
        'B': [],
        'C': ['B'],
        'D': ['C'],
        'E': ['D'],
        'F': ['E'],
    }

    graph_2 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A', 'E'],
        'D': ['A'],
        'E': [],
    }

    print(topological_sort(graph_1))
    print(topological_sort(graph_2))
