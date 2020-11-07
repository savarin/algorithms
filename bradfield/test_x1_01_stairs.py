import timeit
from time import time
from x1_01_stairs import *


def test_count_ways():
    assert count_ways(1) == 1
    assert count_ways(2) == 2
    assert count_ways(3) == 3
    assert count_ways(4) == 5


n = 300

def time_count_ways_1():
    count_ways_1(n)

def time_count_ways_2():
    count_ways_2(n)

def time_count_ways_3():
    count_ways_3(n)

def time_count_ways_4():
    count_ways_4(n)

def time_count_ways_5():
    count_ways_5(n)


if __name__ == '__main__':
    # problem - constant time for all of 3
    # print "1:", timeit.timeit("time_count_ways_1", setup="from __main__ import time_count_ways_1")
    # print "2:", timeit.timeit("time_count_ways_2", setup="from __main__ import time_count_ways_2")
    # print "3:", timeit.timeit("time_count_ways_3", setup="from __main__ import time_count_ways_3")

    start = time()

    time_count_ways_1()
    time1 = time()
    print "1:", time1 - start

    time_count_ways_2()
    time2 = time()
    print "2:", time2 - time1

    time_count_ways_3()
    time3 = time()
    print "3:", time3 - time2

    time_count_ways_4()
    time4 = time()
    print "4:", time4 - time3

    time_count_ways_5()
    time5 = time()
    print "5:", time5 - time4
