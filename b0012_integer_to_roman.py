
lookup = [
    (10, "x"),
    (9, "ix"),
    (5, "v"),
    (4, "iv"),
    (1, "i"),
]

def to_roman(integer):
    #
    """
    """
    for decimal, roman in lookup:
        if decimal <= integer:
            return roman + to_roman(integer - decimal)

    return ""


def main():
    print(to_roman(1))
    print(to_roman(2))
    print(to_roman(4))
    print(to_roman(5))
    print(to_roman(6))
    print(to_roman(9))
    print(to_roman(10))
    print(to_roman(11))
    print(to_roman(36))


if __name__ == "__main__":
    main()
