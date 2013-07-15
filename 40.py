#-*- coding:utf-8 -*-

"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def digit_at(n):
    digits = 1
    n = n - 1
    while True:
        numbers = 9 * pow(10, digits-1) * digits
        if n > numbers:
            n = n - numbers
        else:
            break
        digits = digits + 1
    num = n / digits + pow(10, digits-1)
    return int(str(num)[n % digits])

print digit_at(1) * digit_at(10) * digit_at(100) * digit_at(1000) * digit_at(10000) * digit_at(100000) * digit_at(1000000)
