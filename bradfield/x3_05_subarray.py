

def maximum_subarray_1(coll):
    n = len(coll)
    max_result = 0
    for i in xrange(1, n+1):
        for j in range(n-i+1):
            result = sum(coll[j: j+i])
            if max_result < result:
                max_result = result
    return max_result


def maximum_subarray_2(coll):
    n = len(coll)
    max_result = 0
    for i in xrange(n):
        result = 0
        for j in xrange(i, n):
            result += coll[j]
            if max_result < result:
                max_result = result
    return max_result


def maximum_subarray_3(coll):
    if len(coll) == 0:
        return 0
    # return maximum of (1) maximum subarray of array excluding last one, and
    # (2) maximum subarray including the final element
    n = len(coll)
    result = 0
    sums_with_final = []
    for i in xrange(n-1, -1, -1):
        result += coll[i]
        sums_with_final.append(result)
    return max([maximum_subarray_3(coll[:-1])] + sums_with_final)


def maximum_subarray(coll):
    return maximum_subarray_3(coll)
