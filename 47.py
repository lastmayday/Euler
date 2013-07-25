#-*- coding:utf-8 -*-

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

from prime import factor

ci = 1
nf = 4
ns = 4
n = 2 * 3 * 5 * 7
while ci != ns:
    n += 1
    if len(factor(n)) == nf:
        ci += 1
    else:
        ci = 0

print n - nf + 1
