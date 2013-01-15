#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

import time

def digits(n):
    s = 0
    while n > 0:
        s = s + (n % 10)
        n = n / 10
    return s


start = time.time()
print digits(pow(2,1000))
end = time.time()
print end-start
