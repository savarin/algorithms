from x5_08_perfect import count_squares


def test_count_squares():
    assert count_squares(1) == 1
    assert count_squares(12) == 3
    assert count_squares(13) == 2
