from typing import int


def squares_list(n):
    # type: (int) -> List[int]
    """Generate list of squares less or equal to n."""
    squares = []

    i = 1
    square = 1

    while square <= n:
        squares.append(square)

        i += 1
        square = i * i

    return list(reversed(squares))


def perfect_squares(n):
    # type: (int) -> int
    """Given a positive integer n, find the least number of perfect square
    numbers (for example, 1, 4, 9, 16, ...) which sum to n.

    For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
    return 2 because 13 = 4 + 9.

    https://leetcode.com/problems/perfect-squares
    """
    squares = squares_list(n)
    counter = 0

    # BFS require use of queue, with target and depth as tuple
    queue = [(n, 0)]

    while queue:
        current_value, depth = queue.pop(0)

        if current_value == 0:
            return depth

        children = [current_value - square for square in squares if current_value >= square]

        for child in children:
            queue.append((child, depth + 1))


if __name__ == "__main__":
    assert perfect_squares(17) == 2
    assert perfect_squares(55) == 4
