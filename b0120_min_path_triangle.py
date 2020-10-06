from typing import List


def add_layers(layer_up, layer_down):
    # type: (List[int], List[int]) -> List[int]
    """Returns the minimum sum of two adjacent layers."""
    n = len(layer_down)

    for i in range(n):
        if i == 0:
            layer_down[i] += layer_up[i]
        elif i == n - 1:
            layer_down[i] += layer_up[i - 1]
        else:
            layer_down[i] += min(layer_up[i - 1], layer_up[i])

    return layer_down


def min_path(layers):
    # type: (List[List[int]]) -> int
    """Given a triangle, find the minimum path sum from top to bottom. Each step
    you may move to adjacent numbers on the row below.
    """
    while len(layers) > 1:
        add_layers(layers[0], layers[1])
        layers = layers[1:]

    return min(layers[0])


if __name__ == "__main__":
    layers = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    print(min_path(layers))
