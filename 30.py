#-*- coding:utf-8 -*-

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_pows(n):
    s = 0
    while n>0:
        t = n%10
        n = n/10
        s = s + pow(t, 5)
    return s


def main():
    print sum(x for x in xrange(2, 200000) if sum_pows(x)==x)


if __name__ == "__main__":
    main()
