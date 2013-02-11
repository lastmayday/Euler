#-*- coding:utf-8 -*-

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
import time

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for x in xrange(3, n+1):
            a, b = b, a+b
        return b


def main():
    t = 1
    while True:
        num = fib(t)
        if len(str(num)) == 1000 :
            print t
            break
        t = t + 1


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print "time: " + str(end-start)
