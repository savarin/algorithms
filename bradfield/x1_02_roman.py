
lookup = [
    (10, "x"),
    (9, "ix"),
    (5, "v"),
    (4, "iv"),
    (1, "i")
]


def to_roman(n):
    for decimal, roman in lookup:
        if decimal <= n:
            return roman + to_roman(n - decimal)
    return ""
