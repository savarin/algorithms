from x4_05_allsum import Node, path_sum


def test_path_sum():
    tree = Node(5, \
               Node(4, \
                   Node(11, 
                       Node(7), Node(2))), \
               Node(8,
                   Node(13), Node(4, \
                                  Node(5), Node(1))))

    assert sorted(path_sum(tree, 22)) == [[5, 4, 11, 2], [5, 8, 4, 5]]
