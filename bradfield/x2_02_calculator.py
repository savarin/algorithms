digits = set([str(item) for item in xrange(10)])
operands = set(["+", "-"])


def execute_operation(digits_stack, operands_stack):
    a = digits_stack.pop()
    b = digits_stack.pop()
    operand = operands_stack.pop()
    if operand == "+":
        digits_stack.append(b + a)
    elif operand == "-":
        digits_stack.append(b - a)
    return digits_stack, operands_stack


def evaluate_expression(string):
    digits_stack = []
    operands_stack = []
    counter = 0
    for i, char in enumerate(string):
        if char == " ":
            continue
        elif char == "(":
            counter += 1
            continue
        elif char in digits:
            digits_stack.append(int(char))
            continue
        elif char in operands:
            operands_stack.append(char)
            continue
        elif char == ")":
            assert counter > 0
            counter -= 1
            digits_stack, operands_stack = execute_operation(digits_stack, operands_stack)
            continue
        else:
            raise TypeError("Character not recognized.")
    assert counter == 0
    while len(operands_stack) > 0:
        digits_stack, operands_stack = execute_operation(digits_stack, operands_stack)
    return int(digits_stack.pop())


