from x5_06_islands import count_islands


def test_count_islands():
    assert count_islands(["11110",
                          "11010",
                          "11000",
                          "00000"]) == 1
    assert count_islands(["11000",
                          "11000",
                          "00100",
                          "00011"]) == 3
