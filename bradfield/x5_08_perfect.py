

def count_squares(n):
    if n == 1:
        return 1

    squares = [i*i for i in xrange(1, n) if i*i <= n]

    queue = [(n, 0)]
    while queue:
        remainder, depth = queue.pop(0)
        if remainder == 0:
            return depth
        children = [remainder - item for item in squares if remainder >= item]
        for child in children:
            queue.append((child, depth+1))
