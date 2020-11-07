from x4_03_balanced import Node, is_balanced


def test_is_balanced():
    tree1 = Node(4, \
               Node(2, \
                   Node(1),
                   Node(3)),
               Node(7, \
                   Node(6), \
                   Node(9)))
    
    tree2 = Node(4, \
               Node(2),
               Node(7, \
                   Node(6, \
                       Node(9))))


    assert is_balanced(tree1) == True
    assert is_balanced(tree2) == False
