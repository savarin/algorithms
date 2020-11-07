from x4_04_invert import Node, tree_to_list, invert_tree


def test_tree_to_list():
    tree = Node(4, \
               Node(2, \
                   Node(1),
                   Node(3)),
               Node(7, \
                   Node(6), \
                   Node(9)))
    assert tree_to_list(tree) == [None, 4, 2, 7, 1, 3, 6, 9]


def test_invert_tree():
    tree = Node(4, \
               Node(2, \
                   Node(1),
                   Node(3)),
               Node(7, \
                   Node(6), \
                   Node(9)))
    inverted_tree = Node(4, \
               Node(7, \
                   Node(9),
                   Node(6)),
               Node(2, \
                   Node(3), \
                   Node(1)))
    assert tree_to_list(invert_tree(tree)) == tree_to_list(inverted_tree)
