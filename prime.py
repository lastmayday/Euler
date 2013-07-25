def primesgen():
    '''Returns a generator, which makes you infinite ammount of prime numbers.
To limit output, give an argument, which number you wish to generate your prime numbers to.'''
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def isprime(n):
    '''Checks for primeness of number.'''
    if n==1:
        return False
    if n == 2 or n==3:
        return True
    if n % 2 == 0 or n%3==0:
        return False
    max = n**0.5+1
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i+=2
    return True


def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n


def factor(n):
    if n in [0, -1, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n % p == 0:
            e += 1
            n /= p
        F.append((p, e))
    F.sort()
    return F
