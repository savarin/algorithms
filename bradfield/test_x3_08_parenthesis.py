from x3_08_parenthesis import evaluate_parenthesis


def test_evaluate_parenthesis():
    assert evaluate_parenthesis("2-1-1") == [0, 2]
    assert evaluate_parenthesis("2*3-4*5") == [-34, -14, -10, 10]
