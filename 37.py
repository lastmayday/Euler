#-*- coding:utf-8 -*-

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""


import prime


def l_r_primes(n):
    prime_left = prime_right = False
    for i in xrange(1, len(str(n))):
        l = n % pow(10, i)
        r = n / pow(10, i)
        if (not prime.isprime(l)) or (not prime.isprime(r)):
            return False
    return True

def main():
    i = 11
    t = 10
    res = 0
    while i > 0:
        if prime.isprime(t) and l_r_primes(t):
            res += t
            i -= 1
        t += 1
    print res

if __name__ == '__main__':
    main()
