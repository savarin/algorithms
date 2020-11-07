

def daily_temperatures_1(array):
    #
    """
    """
    result = []

    # Iterate through days
    for i, item1 in enumerate(array[:-1]):
        for j, item2 in enumerate(array[1:]):
            # If next day is warmer, append 1 to day
            if item1 < item2 and i < j + 1:
                result.append(j + 1 - i)
                break

    if len(result) < len(array):
        result += [0] * (len(array) - len(result))

    return result


def daily_temperatures_2(array):
    #
    """
    """
    result = []
    stack = []

    for i, item in enumerate(array):
        while stack and stack[-1][1] < item:
            index, temperature = stack.pop()
            result[index] = i - index

        stack.append((len(result), item))
        result.append(0)

    return result


if __name__ == "__main__":
    print(daily_temperatures_2([73, 74, 75, 71, 69, 72, 76, 73]))

