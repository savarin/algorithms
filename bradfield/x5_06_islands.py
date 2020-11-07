from random import choice


def count_islands(grid):
    n = len(grid)
    m = len(grid[0])
    coordinates = set([(x, y) for x in xrange(n) for y in xrange(m)])
    islands = 0

    while coordinates:
        point = choice(list(coordinates))
        coordinates.remove(point)

        if grid[point[0]][point[1]] == "0":
            continue

        stack = [point]
        while stack:
            x, y = stack.pop(0)
            children = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
            for child in children:
                if child not in coordinates:
                    continue
                coordinates.remove(child)
                if grid[child[0]][child[1]] == "0":
                    continue
                stack.append(child)

        islands += 1

    return islands
