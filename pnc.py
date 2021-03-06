from operator import mul
from functools import reduce


def fact(n):
    if n == 0:
        return 1
    else:
        return reduce(mul, list(range(1, n + 1)))

def ncr(n,r):
    return fact(n)/(fact(r)*fact(n-r))

def npr(n,r):
    return fact(n)/fact(n-r)

