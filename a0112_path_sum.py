class Node():
    def __init__(self, value, left=None, right=None):
        # type: (int, Optional[Union[Node, int]], Optional[Union[Node, int]]) -> None
        """Initialize node for binary tree."""
        self.value = value
        self.left = left
        self.right = right


def path_sum(root, target):
    # type: (Node, int) -> bool
    """Given a binary tree and a sum, determine if the tree has a root-to-leaf
    path such that adding up all the values along the path equals the given sum.

    For example, given the below binary tree and sum = 22, return true, as there
    exist a root-to-leaf path 5->4->11->2 which sum is 22.

              5
             / \
            4   8
           /   / \
          11  13  4
         /   /     \
        2   2       1

    https://leetcode.com/problems/path-sum
    """
    if not root:
        return False

    stack = [(root, root.value)]

    while stack:
        tree, result = stack.pop()

        # If target sum found, return True
        if result == target and not tree.right and not tree.left:
            return True

        # Otherwise add child nodes to the stack
        if tree.left:
            stack.append((tree.left, result + tree.left.value))
        if tree.right:
            stack.append((tree.right, result + tree.right.value))

        return False


if __name__ == "__main__":
    tree1 = Node(11, 2, None)
    tree2 = Node(13, 2, None)
    tree3 = Node(4, None, 1)
    tree4 = Node(4, tree1, None)
    tree5 = Node(8, tree2, tree3)
    tree6 = Node(5, tree4, tree5)

    assert path_sum(tree1, 22) is True
    assert path_sum(tree1, 23) is False
