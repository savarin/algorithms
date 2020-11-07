
def valid_brackets_single(string):
    stack = []
    for i, char in enumerate(string):
        if char == "(":
            stack.append(char)
            continue
        elif char == ")":
            if len(stack) == 0:
                return False
            item = stack.pop()
            if item != "(":
                return False

    if len(stack) > 0:
        return False
    return True


def valid_brackets_multiple(string):
    stack = []
    brackets_open = {"(": ")", "[": "]", "{": "}"}
    brackets_close = {")": "(", "]": "[", "}": "{"}
    for i, char in enumerate(string):
        if char in brackets_open:
            stack.append(char)
            continue
        elif char in brackets_close:
            if len(stack) == 0:
                return False
            item = stack.pop()
            if item != brackets_close[char]:
                return False

    if len(stack) > 0:
        return False
    return True
