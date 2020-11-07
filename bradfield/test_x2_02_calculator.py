from x2_02_calculator import evaluate_expression


def test_evaluate_expression():
    assert evaluate_expression("1 + 1") == 2
    assert evaluate_expression("1 - 1") == 0
    assert evaluate_expression("1 + 1 + 1") == 3
    assert evaluate_expression("( 1 - 1 ) - 1") == -1
    assert evaluate_expression("( 1 + 1 )") == 2
    assert evaluate_expression("1 + ( 1 + 1 )") == 3
    assert evaluate_expression("( 1 + ( 1 + 1 ) )") == 3

    assert evaluate_expression("( 1 + ( 1 + 1 ) ) )") == 3