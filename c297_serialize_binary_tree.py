class Node():
    def __init__(self, val, left=None, right=None):
        #
        """
        """
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    #
    """Serialization is the process of converting a data structure or object
    into a sequence of bits so that it can be stored in a file or memory buffer,
    or transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no
    restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary tree can be serialized to a string and
    this string can be deserialized to the original tree structure.

    Input:
              1
             / \
            2   3
               / \
              4   5

              1
             / \
            2   3
               / \
          4  56   7

              1
             / \
            10 11
               / \
     100 101 110 111

    Output: [1,2,3,null,null,4,5]

    0 = 0
    1 = 2**0 + 1
    2 = 2**0 + 2
    3 = 2**1 + 1
    4 = 2**1 + 2
    5 = 2**2 + 1
    6 = 2**2 + 2**1
    7 = 2**2 + 2**1 + 2**0
    """
    queue = [(root, "1")]
    indices = {}
    max_location = 0

    while queue:
        node, location = queue.pop(0)

        current_location = int(location, 2)
        max_location = max(max_location, current_location)
        indices[int(location, 2)] = node.val

        if node.left:
            queue.append((node.left, location + "0"))
        if node.right:
            queue.append((node.right, location + "1"))

    result = [None] * (max_location + 1)
    
    for k, v in indices.items():
        result[k] = v

    return result[1:]


def deserialize(array):
        def doit():
            try:
                val = next(array)
            except StopIteration:
                return None
            if val is None:
                return None
            node = Node(int(val))
            node.right = doit()            
            node.left = doit()
            return node

        array = iter(array)
        return doit()

if __name__ == "__main__":
    root = Node(1,
        Node(2),
        Node(3,
            Node(4),
            Node(5),
        ),
    )

    print(serialize(root))
    result = deserialize(serialize(root))

    print(result.val)
    print(result.left.val)
    print(result.left.left.val)
    print(result.left.right.val)


