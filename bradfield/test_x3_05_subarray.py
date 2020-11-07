from x3_05_subarray import maximum_subarray


def test_maximum_subarray():
    assert maximum_subarray([1]) == 1
    assert maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6
