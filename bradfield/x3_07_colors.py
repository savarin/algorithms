from heapq import heappush, heappop


def sort_colors(coll):
    result = []
    for i in xrange(len(coll)):
        heappush(result, coll[i])
    return [heappop(result) for i in xrange(len(coll))]
