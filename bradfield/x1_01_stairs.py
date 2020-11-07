from math import sqrt


def count_ways_1(n):
    if n <= 2:
        return n
    return count_ways(n-1) + count_ways(n-2)


def count_ways_2(n):
    if n <= 2:
        return n
    result = [1, 2]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result[-1]


def count_ways_3(n):
    if n <= 2:
        return n
    a, b = 1, 2
    counter = 2
    while counter < n:
        a, b = b, a + b
        counter += 1
    return b


def memoize(f):
    memo = {}
    def g(n):
        if n in memo:
            return memo[n]
        result = f(n)
        memo[n] = result
        return result
    return g


@memoize
def count_ways_4(n):
    if n <= 2:
        return n
    return count_ways(n-1) + count_ways(n-2)


def count_ways_5(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def count_ways(n):
    return count_ways_4(n)
