from math import sqrt


def appendEs2Sequences(sequences, es):
    result=[]
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result+=[seq+[e] for seq in sequences]
    return result


def cartesianproduct(lists):
    return reduce(appendEs2Sequences, lists, [])


def primefactors(n):
    i = 2
    while i<=sqrt(n):
        if n%i==0:
            l = primefactors(n / i)
            l.append(i)
            return l
        i+=1
    return [n]


def factorGenerator(n):
    '''Generates prime factors for given number.'''
    p = primefactors(n)
    factors={}
    for p1 in p:
        try:
            factors[p1]+=1
        except KeyError:
            factors[p1]=1
    return factors


def divisors(n, included=False):
    '''Generates divisors for given number.'''
    factors = factorGenerator(n)
    divisors=[]
    listexponents=[map(lambda x: k**x, range(0, factors[k]+1)) for k in factors.keys()]
    listfactors=cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    if not included:
        del(divisors[len(divisors)-1])
    return divisors
