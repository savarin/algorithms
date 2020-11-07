from x3_02_heapsort import heapsort


def test_heapsort():
    assert heapsort([1]) == [1]
    assert heapsort([1, 3, 2]) == [1, 2, 3]
    assert heapsort([3, 2, 1]) == [1, 2, 3]