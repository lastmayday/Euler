#-*- coding:utf-8 -*-
#!/usr/env/bin python

'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

import math

def factor(x, min=2):
    '''判断质数'''
    temp = min
    while temp <= int(math.sqrt(x))+1:
        if x%temp == 0:
            return temp
        else:
            temp += 1
    return 1

def main():
    n = input('Input the number:')
    i = 2
    while i<= int(math.sqrt(n))+1:
        if n%i == 0:
            if factor(n/i) == 1:
                break;
            else:
                n /= i
        i += 1
    print n/i

if __name__ == '__main__':
    main()
