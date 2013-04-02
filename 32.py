#-*- coding:utf-8 -*-

def isPandigital(s):
    length = len(s)
    if length > 9:
        return False
    for i in xrange(1,length+1):
        if str(i) not in s:
            return False
    return True


def pandigital(a, b):
    num = str(a) + str(b) + str(a*b)
    if len(num) != 9:
        return False
    return isPandigital(num)


def main():
    res = []
    for a in xrange(0, 100000):
        for b in xrange(0, 100000):
            if len(str(a*b) + str(a) + str(b)) > 9:
                break
            if pandigital(a, b):
                res.append(a*b)
                print a,"*",b,"=",a*b
    print sum(set(res))


if __name__ == "__main__":
    main()
