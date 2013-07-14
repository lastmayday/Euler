#-*- coding:utf-8 -*

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindromic(n):
    n_verse = str(n)[::-1]
    if str(n) == n_verse:
        n_binary = str(bin(n))[2::]
        if n_binary == n_binary[::-1]:
            print n, n_binary
            return True
    return False


def main():
    res = 0
    for i in xrange(0, 1000000):
        if is_palindromic(i):
            res += i
    print res


if __name__ == '__main__':
    main()
