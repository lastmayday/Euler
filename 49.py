#-*- coding:utf-8 -*-

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?XS
"""

from itertools import permutations
import prime

def main():
    for i in xrange(1000, 10000):
        lists = sorted(list(set([int(''.join(x)) for x in permutations(str(i)) if int(''.join(x)) > 1000 and prime.isprime(int(''.join(x)))])))
        for a in xrange(0, len(lists)):
            if lists[a] == 1487:
                continue
            for b in xrange(a+1, len(lists)):
                c = (lists[a] + lists[b]) / 2
                if c in lists:
                    print str(lists[a])+str(c)+str(lists[b])
                    exit()


if __name__ == '__main__':
    main()
