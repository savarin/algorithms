
class Node():
    def __init__(self, value, left=None, right=None):
        #
        """
        """
        self.value = value
        self.left = left
        self.right = right


def merge_trees(tree1, tree2):
    #
    """
    """
    if tree1 is None:
        return tree2

    if tree2 is None:
        return tree1

    tree1.value = tree1.value + tree2.value
    tree1.left = merge_trees(tree1.left, tree2.left)
    tree2.right = merge_trees(tree1.left, tree2.left)

    return tree1


if __name__ == "__main__":
    tree1 = Node(1, Node(2, 3))
    tree2 = Node(1, Node(1))

    print(merge_trees(tree1, tree2))
    print(merge_trees(tree1, tree2).value)
    print(merge_trees(tree1, tree2).left)
    print(merge_trees(tree1, tree2).left.left)
    print(merge_trees(tree1, tree2).left.right)
    print(merge_trees(tree1, tree2).right)
    