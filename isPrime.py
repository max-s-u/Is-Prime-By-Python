import itertools as it
from kanren import isvar, membero, var, run, eq
from kanren.core import success, fail, condeseq
from sympy.ntheory.generate import prime, isprime

def check_prime(x) : #Is this prime number?
    if isvar(x) :
        return condeseq([eq(x, p)] for p in map(prime, it.count(1)))
    else :
        return success if isprime(x) else fail

x = var()
print(run(100, x, (check_prime, x)))
#run(displayable-number, count, check_prime(count))