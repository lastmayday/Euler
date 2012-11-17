#-*- coding:utf-8 -*-
#!/usr/bin/env python

'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
'''没看懂这个解法, 但是其实就是16 * 9 * 5 * 7 * 11 * 13 * 17 * 19'''

def gcd(a,b): 
    return b and gcd(b, a % b) or a

def lcm(a,b): 
    return a * b / gcd(a,b)

def main():
    n = 1
    for i in xrange(1, 21):
        n = lcm(n, i)
    print n

if __name__ == '__main__':
    main()
