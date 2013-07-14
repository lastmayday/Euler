#-*- coding:utf-8 -*-

def perimeter(p):
    count = 0
    for a in xrange(2, p/3, 2):
        if p*(p-2*a) % (2*p-2*a) == 0:
            count += 1
    return count


def main():
    max_count = 0
    max_p = 0
    for p in xrange(2, 1001):
        count = perimeter(p)
        if count > max_count:
            max_count = count
            max_p = p
    print max_p


if __name__ == "__main__":
    main()
