#-*- coding:utf-8 -*-

import time


def sort_name():
    f = open('/home/lastmayday/names.txt').read()
    list_name = f.replace('"','').split(',')
    return sorted(list_name)
    

def sum_name(name):
    return sum((ord(letter)-64) for letter in name)
    

if __name__ == "__main__":
    start = time.time()
    names = sort_name()
    print sum((i+1) * sum_name(names[i]) for i in xrange(0, len(names)))
    end = time.time()
    print "time: " + str(end-start)
