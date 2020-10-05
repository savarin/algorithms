class Node():
    def __init__(self, value, left=None, right=None):
        #
        """
        """
        self.value = value
        self.left = left
        self.right = right


def path_sum(root, target):
    #
    """Given a binary tree and a sum, determine if the tree has a root-to-leaf
    path such that adding up all the values along the path equals the given sum.

    For example, given the below binary tree and sum = 22, return true, as there
    exist a root-to-leaf path 5->4->11->2 which sum is 22.

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
    """
    if not root:
        return False

    stack = [(root, root.value)]

    while stack:
        tree, result = stack.pop()

        if result == target and not tree.right and not tree.left:
            return True
        if tree.left:
            stack.append((tree.left, result + tree.left.value))
        if tree.right:
            stack.append((tree.right, result + tree.right.value))

        return False


def test_path_sum():
    #
    """
    """
    tree1 = Node(11, 7, 2)
    tree2 = Node(4, None, 1)
    tree3 = Node(4, tree1, None)
    tree4 = Node(8, 13, tree2)
    tree5 = Node(5, tree3, tree4)

    assert path_sum(tree1, 22) is True
    assert path_sum(tree1, 23) is False
