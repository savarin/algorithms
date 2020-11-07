from x1_02_roman import to_roman


def test_to_roman():
    assert to_roman(1) == "i"
    assert to_roman(2) == "ii"
    assert to_roman(3) == "iii"
    assert to_roman(4) == "iv"
    assert to_roman(5) == "v"
    assert to_roman(6) == "vi"
    assert to_roman(7) == "vii"
    assert to_roman(8) == "viii"
    assert to_roman(9) == "ix"
    assert to_roman(10) == "x"
    assert to_roman(11) == "xi"
    assert to_roman(12) == "xii"
