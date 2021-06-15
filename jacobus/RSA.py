# RSA


# moet kan random getalle generate van n sekere lengte (bv 5 of 6 digiits) GLOBAL variable!

# check lengte van n teenoor die lengte van die boodskap (of die byets wat encrypt moet word) 



import numpy as np

# exploit modular arightmatic properties om exponents vinniger uit te werk p 299
# exploit CRT vir private key goed p300


# Euler totient function for prime numbers
def ETF(a,b): 
    return (a-1)*(b-1)

# get random prime numbers in the range 2^i < n <= 2^(i+1), a < n1*n2 <= b
def getRandomPrimes(a,b):

    # Since the two primes must be in a certain range the min and max values for both can be calculated:
    minRange = np.ceil(np.sqrt(a))
    maxRange = np.floor(np.sqrt(b))

    result = []

    for i in range(2):
        i = np.random.randint(minRange,maxRange) 
        r = miller_rabin(i,4)
        
        # find random number in the given range
        while r == False:
            i = np.random.randint(minRange,maxRange)
            r = miller_rabin(i,4)
        
        result.append(i)

    return result

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
        a = np.random.randint(2,n-1) # random int between and including 2 and n-2
        comp = True
        if a**q % n == 1:
            comp = False # probably prime
            continue

        for j in range(k): # range 0 to k-1
            if a**((2**j)*q) % n == n-1:
                comp = False # probably prime
                continue
    
        if comp == True:
            return False
    
    return True

# get GCD
def extended_euclidean_algo(a,b):
    # Base Case 
    if a == 0 :  
        return b,0,1
    
    # print("ri ",a)
    # print("q ", (b//a))
    gcd,x1,y1 = extended_euclidean_algo(b%a, a) 
    
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
    
    return gcd,x,y

# get largest value that is coprime
def getE(max,p,q):
    
    # test if this value works
    if extended_euclidean_algo(65537,ETF(p,q))[0] == 1:
        return 65537
    

    for j in range(max,-1,-1):
        if extended_euclidean_algo(j,ETF(p,q))[0] == 1:
            return j

# Multiplicative inverse 
def inverseModulo(a,phi):
    for i in range(1,phi):
        if (a*i)%phi == 1:
            return i
    
    print("NO inverse!")

# a^b mod n
def powz(a,b,n):
    b_bin = bin(b)[2:]

    f = 1
    for i in range(len(b_bin)):
        f = (f**2) % n
        if int(b_bin[i]) == 1:
            f = (f*a) % n     

    return f

def cleanString(strText):
    # s = strText.lower()
    s = ''.join(str(ord(i))+',' for i in strText if i.isalpha())
    return np.fromstring(s, dtype=int, sep=',')

    # return np.array(bytearray(strText.encode(encoding="ascii")),dtype=np.ubyte)

# print(cleanString("How are you?"))



def encryptRSA(s):


    plain = [33,14,22,62,0,17,4,62,24,14,20,66]



    blocksize = 16 # 2 bytes
    pq = getRandomPrimes(2**blocksize,2**(blocksize + 1))

    print(pq)

#     # 1st prime number
#     p = 17
#     #p = pq[0]

#     # 2nd prime number
#     q = 11
#     #q = pq[1]

#     # n calculated pow(2, i) < n <= pow(2, i + 1), i -> block size
#     n = 11023
#     # n = p*q

#     # Public key {e,n}, e (calculate it), must be relatively prime to ETF(n) (gcd -> 1) and smaller than ETF(n)
#     e = 11
#     # e = getE(ETF(p,q),p,q)

#     # Private key {d,n}, d calculated
#     d = 5891
#     # d = inverseModulo(e,ETF(p,q))

#     enc = []
#     # check dat alle blocks encrypt word!!
#     for i in range(len(plain)//2):
#         P = int(str(plain[2*i]).zfill(2) + str(plain[2*i +1]).zfill(2))
#         print("P"+str(i)+" : "+str(P))
#         enc.append(powz(P,e,n))
#         print("C"+str(i)+" : "+str(enc[len(enc)-1])+"\n")
    
#     print("encrypted ", enc)


#     dec = []
#     for j in range(len(enc)):
#         print("C"+str(j)+" : "+str(enc[j]))
#         P = powz(enc[j],d,n)
#         print("P"+str(j)+" : "+str(P).zfill(4)+"\n")
#         dec.append(int(str(P).zfill(4)[:2]))
#         dec.append(int(str(P).zfill(4)[2:]))

#     print("decrypted ",dec)

# encryptRSA("a")




# test primes, moet nog kyk hkm 40 goeie getal is
# j = 0 
# for i in range(0,100000):
#     if miller_rabin(i,4) == True:
#         j = j + 1
#         print(i)

# print("Total ",j)

# 4 rounds kon almal so ver kry, dink dis fine