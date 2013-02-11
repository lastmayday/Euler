#-*- coding:utf-8 -*-

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools
import time

NUM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def main():
    perm = list(itertools.permutations(NUM, 10))
    perm_str = map(lambda x: ''.join(x), perm)
    print sorted(perm_str)[999999]
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print "time: " + str(end-start)
