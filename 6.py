#-*- coding:utf-8 -*-

'''The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def main():
    i = 1
    sum1 = 0
    sum2 = 0
    while i<= 100:
        sum1 += i
        sum2 += i**2
        i += 1
    squre1 = sum1**2
    squre2 = sum2
    print squre1 - squre2

if __name__ == '__main__':
    main()
