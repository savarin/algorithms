from itertools import permutations


def operate_digits(a, b, operand):
    if operand == "+":
        return a + b
    elif operand == "-":
        return a - b
    elif operand == "*":
        return a * b
    else:
        raise RuntimeError("Operand not recognized.")


def evaluate_parenthesis(string):
    digits_source = []
    operands_source = []
    result = []
    for i in xrange(len(string)):
        if i % 2 == 0:
            digits_source.append(int(string[i]))
        else:
            operands_source.append(string[i])
    for item in permutations(list(xrange(len(operands_source)))):
        digits = list(digits_source)
        operands = list(operands_source)
        item = list(item)
        while len(item) > 0:
            index = item.pop()
            a = digits[index]
            b = digits.pop(index + 1)
            operand = operands.pop(index)
            digits[index] = operate_digits(a, b, operand)
            item = [i if i < index else i - 1 for i in item]
        result.append(digits[0])
    return sorted(list(set(result)))
