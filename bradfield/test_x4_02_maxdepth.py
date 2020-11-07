from x4_02_maxdepth import Node, find_maximum


def test_path_sum():
    tree = Node(5, \
               Node(4, \
                   Node(11, 
                       Node(7), Node(2,
                                    Node(1)))), \
               Node(8,
                   Node(13), Node(4, \
                                  None, Node(1))))
    assert find_maximum(tree) == 5
