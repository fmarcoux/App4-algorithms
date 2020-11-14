from math import gcd

def pollards_rho(n):
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n: return d

n = 86062381025757488680496918738059554508315544797
p = pollards_rho(n)
print ('{} = {} * {}'.format(n, p, n/p))