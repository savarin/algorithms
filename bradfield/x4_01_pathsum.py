

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(tree, target):
    stack = [(tree, tree.val)]
    result = []
    while stack:
        node, val = stack.pop()
        if node.left:
            stack.append((node.left, val + node.left.val))
        if node.right:
            stack.append((node.right, val + node.right.val))
        if not node.left and not node.right:
            if val == target:
                return True
    return False
