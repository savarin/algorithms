from x3_07_colors import sort_colors


def test_sort_colors():
    assert sort_colors([]) == []
    assert sort_colors([0]) == [0]
    assert sort_colors([0, 1, 2]) == [0, 1, 2]
    assert sort_colors([1, 2, 0]) == [0, 1, 2]