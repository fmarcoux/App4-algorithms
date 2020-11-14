from typing import Tuple

def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modinv(a: int, b: int) -> Tuple[int, int, int]:
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b


#section pour execute l'algo
#Pour le pgcd de deux chiffre, utiliser xgcd, le premier chiffre sera le plus grand commun diviseur
#Pour l'inverser modulo d'un nombre, utiliser modinv
#print(65464651321/1412451408578)


#print(xgcd(150,250)) # va donner 50

#print(modinv(9,40)) # donne 9 puisque l'inverse modulaire de 9 modulo 40 c'est 9