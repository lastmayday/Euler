#-*- coding:utf-8 -*-
#! /usr/bin/env python

"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from itertools import product

def sieve(n):
    numbers = range(2, n + 1)
    p = 2
    j = 0
    done = False
    while not done:
        for i, n in enumerate(numbers):
            if n % p == 0 and n != p:
                numbers.pop(i)
        j += 1
        p = numbers[j]
        if p ** 2 > n:
            done = True
    return numbers


def main():
    primers = sieve(10000)
    composites = set(n for n in range(2, 10000) if n not in primers)
    twicesquares = set(2 * (n ** 2) for n in range(100))

    sums = set(sum(c) for c in product(primers, twicesquares))
    print min(n for n in composites if n not in sums and n % 2 != 0)


if __name__ == '__main__':
    main()
