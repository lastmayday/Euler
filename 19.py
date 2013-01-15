#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

import math
import time
import datetime

normal_year = 30*4 + 31*7 + 28

def main():
    sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            d = datetime.date(year, month, 1)
            if d.weekday() == 6:
                sundays = sundays + 1
    print sundays


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print "time: " + str(end-start)
