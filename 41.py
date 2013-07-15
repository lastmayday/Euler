#-*- coding:utf-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""


import prime
from itertools import permutations

for i in permutations(range(7, 0, -1)):
    num = 0
    for n in i:
        num = num * 10 + n
    if prime.isprime(num):
        print num
        break
