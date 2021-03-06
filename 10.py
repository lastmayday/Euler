#-*- coding:utf-8 -*-

'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

from time import clock


sieve = [True] * 2000000

def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(len(sieve)**0.5)+1):
    if sieve[x]:
        mark(sieve, x)

c = clock()
print sum(i for i in xrange(2, len(sieve)) if sieve[i])
print clock()-c
