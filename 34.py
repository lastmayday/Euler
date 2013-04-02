#-*- coding:utf-8 -*-

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import time


def muti(n):
    i = 1
    for t in xrange(1, n):
        i *= t
    return i


def main():
    res = []
    for i in xrange(3, 100000):
        t = i
        sum_i = 0
        while t != 0:
            sum_i += muti(t%10+1)
            t = t/10
        if sum_i == i:
            res.append(sum_i)
    print sum(res)


if __name__ == "__main__":
    start = time.time()
    main()
    print "time:", time.time()-start
