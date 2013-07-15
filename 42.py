#-*- coding:utf-8 -*-

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import math


def is_triangle(n):
    for i in xrange(1, int(math.sqrt(2*n))+1):
        if i*(i+1) == n*2:
            return True
    return False


def main():
    num = 0
    fp = open('words.txt', 'r')
    words_string = fp.read()
    words_list = map(lambda x: x.strip('"'), words_string.split(','))
    for word in words_list:
        total = 0
        for w in word:
            total += ord(w) - ord('A') + 1
        if is_triangle(total):
            num += 1
    print num      
    fp.close()


if __name__ == '__main__':
    main()
