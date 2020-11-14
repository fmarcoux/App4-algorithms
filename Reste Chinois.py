from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1



#section de test de l'algo chinois
# #Si il n'y a pas de solution on va avoir une division derreur par 0
#pour que l'algo fonctionne, il faut que les modulo soit co premier entre eux
#n =  les modulos
#a = les residus de ces modulo

#Exemple avec le numero du procedural
#ENONCE :Nous avons une certaine quantité d’objets, mais nous n’en connaissons pas
#le nombre exact. Si nous les comptons par groupes de 5, il nous en reste0.
# Si nous les comptons par groupes de 7, il nous en reste 4. Si nous les
#comptons par groupes de 11, il nous en reste 7. Enfin, si nous les comptons
#par groupes de 13, il nous en reste 5. Combien y a-t-il d’objets ?

n=[5,7,11,13]
a=[0,4,7,5]
print(chinese_remainder(n,a))
