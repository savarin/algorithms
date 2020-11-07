

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_maximum(tree):
    stack = [(tree, 1)]
    max_depth = 1
    while stack:
        node, depth = stack.pop()
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
        if not node.left and not node.right:
            if max_depth < depth:
                max_depth = depth
    return max_depth
