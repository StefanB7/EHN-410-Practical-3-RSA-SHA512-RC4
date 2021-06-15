# Blum Blum Shub - PRNG

# Permission granted by Gustan Naude
import time

# Number of digits, thus between 10^(numDigits-1) to (10^numDigits)-1
numDigits = 6

rndMax = 10**(numDigits-1)
rndMin = (10**numDigits)-1

# Euler totient function for prime numbers
def ETF(a,b): 
    return (a-1)*(b-1)

# get GCD
def extended_euclidean_algo(a,b):
    # Base Case 
    if a == 0 :  
        return b,0,1

    gcd,x1,y1 = extended_euclidean_algo(b%a, a) 
    
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
    
    return gcd,x,y

# get largest value that is coprime
def getE(max,p,q):
    
    for j in range(max,-1,-1):
        if extended_euclidean_algo(j,ETF(p,q))[0] == 1:
            return j

# two large prime numbers, that also equals 3 when modded with 4
p = 1000000123
q = 1000000223

n = p*q

# relative prime to n
s = getE(ETF(p,q),p,q)

##### !!!!!! op die oomblik bly die seed dieselfed, kyk of jy time mag gebruik om seed te randomize

# Generate ceil(log2((10^numDigits)-1)) bits and then scale to the 10^(numDigits-1) to (10^numDigits)-1 range using
# (random % (max-min))+min

# Get number of bits by checking the amount of bits in (10^numDigits)-1 
numBits = len(bin(10**numDigits-1)[2:])


x = []
b = []
x.append(s**2 % n)
bits = ""
for i in range(numBits):
    x.append(x[len(x)-1]**2 % n)
    b.append(x[len(x)-1] % 2)
    bits += str(b[len(b)-1])

rndNumber = (int(bits,2) % (rndMax-rndMin)) + rndMin

print(rndNumber)





# bits = ""
# for i in range(numBits):
#     x.append(x[len(x)-1]**2 % n)
#     b.append(x[len(x)-1] % 2)
#     bits += str(b[len(b)-1])

# rndNumber = (int(bits,2) % (rndMax-rndMin)) + rndMin

# print(rndNumber)

# bits = ""
# for i in range(numBits):
#     x.append(x[len(x)-1]**2 % n)
#     b.append(x[len(x)-1] % 2)
#     bits += str(b[len(b)-1])

# rndNumber = (int(bits,2) % (rndMax-rndMin)) + rndMin

# print(rndNumber)

# bits = ""
# for i in range(numBits):
#     x.append(x[len(x)-1]**2 % n)
#     b.append(x[len(x)-1] % 2)
#     bits += str(b[len(b)-1])

# rndNumber = (int(bits,2) % (rndMax-rndMin)) + rndMin

# print(rndNumber)

# bits = ""
# for i in range(numBits):
#     x.append(x[len(x)-1]**2 % n)
#     b.append(x[len(x)-1] % 2)
#     bits += str(b[len(b)-1])

# rndNumber = (int(bits,2) % (rndMax-rndMin)) + rndMin

# print(rndNumber)