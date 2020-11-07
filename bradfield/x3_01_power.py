

def power(x, n):
    # return 0 if n == 1
    # return x * power(x, n-1) if n is odd
    # return power(x, n/2) ** 2 if n is even
    if n == 0:
        return 1
    elif n % 2 == 1:
        return x * power(x, n-1)
    else:
        result = power(x, n/2)
        return result * result
