from x2_02_brackets import valid_brackets_single, valid_brackets_multiple


def test_valid_brackets_single():
    assert valid_brackets_single("()") == True
    assert valid_brackets_single("()()") == True
    assert valid_brackets_single("(())") == True
    assert valid_brackets_single("(") == False
    assert valid_brackets_single(")") == False
    assert valid_brackets_single(")(") == False


def test_valid_brackets_multiple():
    assert valid_brackets_multiple("()") == True
    assert valid_brackets_multiple("()()") == True
    assert valid_brackets_multiple("(())") == True
    assert valid_brackets_multiple("(") == False
    assert valid_brackets_multiple(")") == False
    assert valid_brackets_multiple(")(") == False
    assert valid_brackets_multiple("()[]{}") == True
    assert valid_brackets_multiple("([{}])") == True
    assert valid_brackets_multiple("([)]") == False
    assert valid_brackets_multiple("(]") == False
