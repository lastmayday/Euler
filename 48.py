#-*- coding:utf-8 -*-

"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def main():
    res = 0
    for i in xrange(1, 1001):
        n = pow(i, i)
        res += n
        if len(str(res)) > 10:
            res = int(str(res)[-10:])
        print res


if __name__ == '__main__':
    main()
