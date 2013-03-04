#-*- coding:utf-8 -*-

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import time

MAX = 1001/2

def add():
    x = 1
    s = 1
    y = 2
    n = 0
    while True:
        for t in xrange(0, 4):
            x = x + y
            s = s + x
        y = y + 2
        n = n + 1
        if n == MAX:
            break
    print s

if __name__ == "__main__":
    start = time.time()
    add()
    end = time.time()
    print "time: " + str(end-start)        
