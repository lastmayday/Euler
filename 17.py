#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
import time

words = [
    (1, 'one', ''),
    (2, 'two', ''),
    (3, 'three', ''),
    (4, 'four', ''),
    (5, 'five', ''),
    (6, 'six', ''),
    (7, 'seven', ''),
    (8, 'eight', ''),
    (9, 'nine', ''),
    (10, 'ten', ''),
    (11, 'eleven', ''),
    (12, 'twelve', ''),
    (13, 'thirteen', ''),
    (14, 'fourteen', ''),
    (15, 'fifteen', ''),
    (16, 'sixteen', ''),
    (17, 'seventeen', ''),
    (18, 'eighteen', ''),
    (19, 'nineteen', ''),
    (20, 'twenty', ''),
    (30, 'thirty', ''),
    (40, 'forty', ''),
    (50, 'fifty', ''),
    (60, 'sixty', ''),
    (70, 'seventy', ''),
    (80, 'eighty', ''),
    (90, 'ninety', ''),
    (100, 'hundred', 'and'),
    (1000, 'thousand', 'and')
]

words.reverse()

def spell(n, words):
    word = []
    while n > 0:
        for num in words:
            if num[0] <= n:
                div = n / num[0]
                n = n % num[0]
                if num[2]: 
                    word.append(' '.join(spell(div, words)))
                word.append(num[1])
                if num[2] and n: 
                    word.append(num[2])
                break
    return word


start = time.time()
print sum(len(word) for n in xrange(1, 1001) for word in spell(n, words))
end = time.time()

print "time: " + str(end-start)
