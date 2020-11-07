from x4_01_pathsum import Node, path_sum


def test_path_sum():
    tree = Node(5, \
               Node(4, \
                   Node(11, 
                       Node(7), Node(2))), \
               Node(8,
                   Node(13), Node(4, \
                                  None, Node(1))))

    assert path_sum(tree, 22) == True
    assert path_sum(tree, 100) == False
