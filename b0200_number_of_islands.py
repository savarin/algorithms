import random


def island_count(grid):
    # type: (List[List[int]]) -> int
    """Given a 2d grid map of '1's (land) and '0's (water), count the number of
    islands. An island is surrounded by water and is formed by connecting
    adjacent lands horizontally or vertically. You may assume all four edges of
    the grid are all surrounded by water.

    https://leetcode.com/problems/number-of-islands/
    """
    # Initialize all possible points in the map
    points = set([(i, j) for i in range(len(grid)) for j in range(len(grid[0]))])
    count = 0

    # Iterate through all points in the map
    while len(points) > 0:
        # Select random point and remove from map
        selection = random.choice(list(points))
        points.remove(selection)

        # If point is water, continue
        if grid[selection[0]][selection[1]] == '0':
            continue

        # Initialize stack
        stack = [selection]

        # If point is land, explore surrounding area
        while stack:
            x, y = stack.pop()
            children = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for child in children:
                if child not in points:
                    continue

                points.remove(child)

                if grid[child[0]][child[1]] == "0":
                    continue

                # Consider surrounding area on land
                stack.append(child)

        # Once all land points considered, increment count
        count += 1

    return count


if __name__ == "__main__":
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]

    print(island_count(grid))
