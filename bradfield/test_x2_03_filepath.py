from x2_03_filepath import simplify_filepath


def test_simply_filepath():
    assert simplify_filepath("/usr") == "/usr"
    assert simplify_filepath("/usr/local") == "/usr/local"
    assert simplify_filepath("/usr/local/../local") == "/usr/local"
    assert simplify_filepath("/usr/local/../local/../lib") == "/usr/lib"
