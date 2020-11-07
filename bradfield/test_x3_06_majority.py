from x3_06_majority import majority_element


def test_majority_element():
    assert majority_element([]) == None
    assert majority_element([1]) == 1
    assert majority_element([1, 1, 2]) == 1
    assert majority_element([1, 1, 2, 2]) == None
