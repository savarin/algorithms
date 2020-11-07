from x3_01_power import power


def test_power():
    assert power(2, 0) == 1
    assert power(2, 1) == 2
    assert power(2, 2) == 4
    assert power(2, 8) == 256
    assert power(10, 2) == 100
