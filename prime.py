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
