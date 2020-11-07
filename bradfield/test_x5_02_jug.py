from x5_02_jug import minimum_pours


def test_minimum_pours():
    assert minimum_pours(3, 5, 3) == (True, 1)
    assert minimum_pours(3, 5, 5) == (True, 1)
    assert minimum_pours(3, 5, 2) == (True, 2)
    assert minimum_pours(3, 5, 1) == (True, 4)
    assert minimum_pours(3, 5, 4) == (True, 6)


def test_minimum_pours():
    assert minimum_pours(3, 3, 2) == (False, -1)
