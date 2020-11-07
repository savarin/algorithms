

def search_matrix(matrix, n):
    r0 = len(matrix)
    c0 = len(matrix[0])
    return search_matrix_range(matrix, n, r0 * c0 - 1, 0)


def convert_index(n, columns):
    a = n / columns
    b = n - a * columns
    return (a, b)


def search_matrix_range(matrix, n, upper, lower):
    columns = len(matrix[0])
    if upper - lower == 1:
        r1, c1 = convert_index(upper, columns)
        r2, c2 = convert_index(lower, columns)
        print r1, c1, r2, c2
        if matrix[r1][c1] == n or matrix[r2][c2] == n:
            return True
        return False
    else:
        midpoint = (upper + lower) / 2
        r3, c3 = convert_index(midpoint, columns)
        if matrix[r3][c3] == n:
            return True
        elif matrix[r3][c3] > n:
            return search_matrix_range(matrix, n, midpoint, lower)
        else:
            return search_matrix_range(matrix, n, upper, midpoint)
