#-*- coding:utf-8 -*-

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import prime

primes = prime.prime_list(1000000)
primeSum = [0]*(len(primes)+1)
num = 0

for i in xrange(0, len(primes)):
    primeSum[i+1] = primeSum[i] + primes[i]

for i in xrange(0, len(primes)):
    j = i - (num + 1)
    while j >= 0:
        if primeSum[i] - primeSum[j] > 1000000:
            break
        if primeSum[i] - primeSum[j] in primes:
            num = i - j
            res = primeSum[i] - primeSum[j]
        j -= 1

print res
