#!/usr/bin/env 
#-*- coding:utf-8 -*-

'''
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time

def main():
    multi = 1
    for i in xrange(1, 101):
        multi = multi * i
    multi = list(str(multi))
    print sum(map(int, multi))

    
start = time.time()
main()
end = time.time()
print "time: " + str(end-start)
    
