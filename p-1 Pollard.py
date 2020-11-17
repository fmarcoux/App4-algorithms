# Python code for Pollard p-1
# factorization Method


from math import gcd

from mpmath.tests.test_basic_ops import long


def pminus1(n):
    m = 2
    ans=[]
    max = n
    for i in range(max):
        if(i>0):
            m = (m**i)%n
            if (gcd(int(n),m-1) != 1):
                return gcd(int(n),m-1)


n=71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513

p=pminus1(n)

print(p)


q=n//p
print(q)

