

def is_square(n):
    return is_square_range(n, n / 2 + n % 2, 0)


def is_square_range(n, upper, lower):
    print n, upper, lower
    if upper - lower == 1:
        if upper * upper == n or lower * lower == n:
            return True
        return False
    else:
        x = (upper + lower) / 2
        y = x * x
        if y == n:
            return True
        elif y > n:
            return is_square_range(n, x, lower)
        else:
            return is_square_range(n, upper, x)
