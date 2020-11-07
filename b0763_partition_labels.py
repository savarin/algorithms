


def partition_labels(string):
    #
    """
    """
    indices = {}

    for i, char in enumerate(string):
        indices[char] = i

    result = []
    left, right = -1, -1

    for i, char in enumerate(string):
        right = max(right, indices[char])

        if i == right:
            result.append(right - left)
            left = i

    return result


if __name__ == "__main__":
    print(partition_labels("ababcbacadefegdehijhklij"))
