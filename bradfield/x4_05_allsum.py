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


def path_sum(tree, target):
    stack = [(tree, [tree.val])]
    result = []
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            if sum(path) == target:
                result.append(path)
        if node.left:
            left_path = list(path)
            left_path.append(node.left.val)
            stack.append((node.left, left_path))
        if node.right:
            right_path = list(path)
            right_path.append(node.right.val)
            stack.append((node.right, right_path))
    return result
