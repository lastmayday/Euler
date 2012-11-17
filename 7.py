#-*- coding:utf-8 -*-
import math

def isPrime(num):
    for i in xrange(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return i
    return 1

def main():
    num = 2
    x = 0
    while num:
        if isPrime(num) == 1:
            x += 1
        if x == 10001:
            print num
            break
        num += 1

if __name__ == '__main__':
    main()
