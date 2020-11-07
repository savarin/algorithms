from math import log, ceil


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        stack = [(self, "root ", 0)]
        result = ""
        while stack:
            node, direction, depth = stack.pop()
            result += "\t" * depth + direction + str(node.val) + "\n"
            if node.left:
                stack.append((node.left, " left ", depth + 1))
            if node.right:
                stack.append((node.right, " right ", depth + 1))
        return result


def tree_to_list(tree):
    queue = [tree]
    result = [None]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def list_to_inverted_tree(coll):
    # calculate how many levels needed
    n = int(ceil(log(len(coll), 2)))
    levels = [[coll[1]]]
    result = []
    # split into value by level, e.g. [[4], [7, 2], [3, 1, 9, 6]]
    for i in xrange(1, n):
        levels.append(coll[2**i:2**(i+1)][::-1])
    item = levels.pop()
    # create individual nodes from the bottom layer of tree
    for i in xrange(len(levels[-1])):
        levels[-1][i] = Node(levels[-1][i], Node(item[2*i]), Node(item[2*i+1]))
    # collect nodes created into higher-level nodes
    while len(levels) > 1:
        item = levels.pop()
        for i in xrange(len(levels[-1])):
            levels[-1][i] = Node(levels[-1][i], item[2*i], item[2*i+1])
    return levels[0][0]


def invert_tree(tree):
    return list_to_inverted_tree(tree_to_list(tree))
