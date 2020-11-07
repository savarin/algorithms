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


def get_height(tree):
    if not tree:
        return 0
    return 1 + max(get_height(tree.left), get_height(tree.right))


def is_balanced(tree):
    queue = [tree]
    while queue:
        node = queue.pop()
        if abs(get_height(node.left) - get_height(node.right)) >= 2:
            return False
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return True
