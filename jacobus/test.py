import math
from PRNG_BBS import PRNG_BBS

# def xgcd(a,b):
#     prevx, x = 1, 0; prevy, y = 0, 1
#     while b:
#         q = a//b
#         x, prevx = prevx - q*x, x
#         y, prevy = prevy - q*y, y
#         a, b = b, a % b
#     return a, prevx, prevy


# print(xgcd(321637,321640))

# print(math.gcd(321637,321640))

# # mod
# print((321637*107213)%321640)

def powz(a,b,n):
    b_bin = bin(b)[2:]

    f = 1
    for i in range(len(b_bin)):
        f = (f**2) % n
        if int(b_bin[i]) == 1:
            f = (f*a) % n     

    return f

BBS = PRNG_BBS()

    # Test for prime
def miller_rabin(n, rounds):
    # n - 1  = (2^k)*q, k > 0 and q odd
    
    if n == 0:
        return False

    if n == 1:
        return False

    if n == 2:
        return True

    if n == 3:
        return True

    if n % 2 == 0:
        return False

    q = n-1
    k = 0
    while q % 2 == 0:
        q = q // 2
        k = k +1
    
    for r in range(rounds):
        a = BBS.getRandomNumberRange(2,n-2) # random int between and including 2 and n-2 
        comp = True
        if powz(a,q,n) == 1:
            comp = False # probably prime
            continue

        for j in range(k): # range 0 to k-1
            if powz(a,(pow(2,j)*q),n) == n-1:
                comp = False # probably prime
                continue
    
        if comp == True:
            return False
    
    return True


print(miller_rabin(38245692384756928347569238475629384756293847562938456293846238947,10))

