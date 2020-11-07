from heapq import heappush, heappop


def heapsort(coll):
    n = len(coll)
    heap = []
    for i in xrange(n):
        heappush(heap, coll[i])
    return [heappop(heap) for i in xrange(n)]
