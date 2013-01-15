#!/usr/bin/env python
#-*- coding:utf-8 -*-

upper, lower = 1, 1

for i in xrange(40, 20, -1):
    upper *= i

for i in xrange(1, 21):
    lower *= i

res = upper / lower
print res
