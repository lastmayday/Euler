#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time

def devide(x):
    for i in xrange(1, int(x**0.5)):
        if x/i*i == x:
            yield i
            yield x/i

def triangle():
    n = 1
    while n:
        x = sum(i for i in xrange(n))
        num = len(list(devide(x)))
        if num > 500:
            return x
        else:
            n += 1
            
def main():
    res = triangle()
    print res

if __name__ == '__main__':
    start = time.time()
    main()
    print time.time()-start

