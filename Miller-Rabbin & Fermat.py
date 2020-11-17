import random

from mpmath.libmp.backend import xrange


def miller_rabin(n, k):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in xrange(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in xrange(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


print(miller_rabin(1068522512900119147557173208241671116649415470577282880246316447896772822847296055763408358990225038564394875651124083651221230420679921054094436578154107,128))
print(miller_rabin(67039039649712985497870124991029230637396829102961966888617807218608820150367734884009371490834517138450159290932430254268769414059732849732168245030420659,128))



