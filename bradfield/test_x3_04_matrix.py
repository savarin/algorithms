from x3_04_matrix import convert_index, search_matrix


def test_convert_index():
    assert convert_index(0, 10) == (0, 0)
    assert convert_index(1, 10) == (0, 1)
    assert convert_index(10, 10) == (1, 0)
    assert convert_index(11, 10) == (1, 1)


def test_search_matrix():
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
    ]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 16) == True
    assert search_matrix(matrix, 50) == True
    assert search_matrix(matrix, 9) == False
    assert search_matrix(matrix, 19) == False
    assert search_matrix(matrix, 69) == True
