from x5_07_springs import find_connections, count_springs

grid = ["12235",
        "32344",
        "24531", 
        "67145",
        "51124"]

n = len(grid)
m = len(grid[0])
coordinates = set([(x, y) for x in xrange(n) for y in xrange(m)])


def test_find_connections_up():
    assert find_connections((4, 0), grid, coordinates, True) == [(3, 0), (3, 1), (4, 0)]
    assert find_connections((0, 4), grid, coordinates, True) == [(0, 4)]


def test_find_connections_down():
    assert find_connections((1, 1), grid, coordinates, False) == [(0, 0), (0, 1), (0, 2), (1, 1)]
    

def test_count_springs():
    assert count_springs(["12235",
                          "32344",
                          "24531", 
                          "67145",
                          "51124"]) == [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)]

