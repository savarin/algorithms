

def simplify_filepath(path):
    result = path.split("/")
    stack = []
    for i, item in enumerate(result):
        if item != "..":
            stack.append(item)
        else:
            stack.pop()
    return "/".join(stack)
