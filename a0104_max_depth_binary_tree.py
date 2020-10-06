from typing import Any


def max_depth(tree):
    # type: (Dict[str, Any]) -> int
    """Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.

    https://leetcode.com/problems/maximum-depth-of-binary-tree
    """
    stack = [(tree, 0)]
    result = []

    while stack:
        node, count = stack.pop()

        left = node.get('left')
        right = node.get('right')

        if left:
            stack.append((left, count + 1))
        if right:
            stack.append((right, count + 1))
        if not left and not right:
            result.append(count)

    return max(result)


if __name__ == "__main__":
    tree = {
        'value': 'A',
        'left': {
            'value': 'B',
            'left': {'value': 'D'},
            'right': {'value': 'E'}
        },
        'right': {
            'value': 'C',
            'right': {'value': 'F'}
        }
    }

    print(max_depth(tree))
