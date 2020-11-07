from x3_03_square import is_square


def test_is_square():
    assert is_square(1) == True
    assert is_square(4) == True
    assert is_square(100) == True
    assert is_square(2) == False
    assert is_square(5) == False
    assert is_square(99) == False