from random import choice


def find_connections(point, grid, coordinates, up=True):
    coordinates.remove(point)
    queue = [point]
    result = [point]

    while queue:
        x, y = queue.pop(0)
        height = grid[x][y]
        children = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

        for child in children:
            if child not in coordinates:
                continue
            coordinates.remove(child)
            if up:
                if height > grid[child[0]][child[1]]:
                    continue
            else:
                if height < grid[child[0]][child[1]]:
                    continue
            queue.append(child)
            result.append(child)

    return sorted(result)


def count_springs(grid):
    n = len(grid)
    m = len(grid[0])
    coordinates = set([(x, y) for x in xrange(n) for y in xrange(m)])
    unknowns = set(coordinates)
    result = []

    # find upstream values from (n, 0)
    springs_1 = find_connections((n-1, 0), grid, list(coordinates), True)
    for spring in springs_1:
        if spring in unknowns:
            unknowns.remove(spring)
            result.append(spring)

    # find upstream values from (0, m)
    springs_2 = find_connections((0, m-1), grid, list(coordinates), True)
    for spring in springs_2:
        if spring in unknowns:
            unknowns.remove(spring)
            result.append(spring)

    while unknowns:
        point = choice(list(unknowns))
        downstreams = find_connections(point, grid, list(coordinates), False)

        flow = [0, 0]
        for x, y in downstreams:
            if x == 0 or y == 0:
                flow[0] = 1
            if x == n-1 or y == m-1:
                flow[1] = 1

        if sum(flow) < 2:
            for sink in downstreams:
                if sink in unknowns:
                    unknowns.remove(sink)
        else:
            springs_3 = find_connections(point, grid, list(coordinates), True)
            print point, flow, springs_3
            for spring in springs_3:
                if spring in unknowns:
                    unknowns.remove(spring)
                    result.append(spring)

    return sorted(result)

