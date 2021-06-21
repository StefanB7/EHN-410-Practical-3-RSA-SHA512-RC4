# Blum Blum Shub - PRNG
# EHN 410 - Practical 3 - 2021
# Stefan Buys, Jacobus Oettle
# Group 7 - Created 15 June 2021

# Permission granted by Gustan Naude
import time

class PRNG_BBS:
    def __init__(self):

        # increment the seed value to ensure random numbers are not the same when function is called repeatedly
        self.seedInc = 0
        
        # Number of digits, thus between 10^(numDigits-1) to (10^numDigits)-1
        # Default case is 5 digits
        self.numDigits = 5

        # two large prime numbers, that also equals 3 when modded with 4
        self.p = 1000000123
        self.q = 1000000223

        self.n = self.p*self.q

        # seed that is relative prime to n
        self.s = self.getSeed(self.p,self.q)

    # Euler totient function for prime numbers
    def ETF(self,a,b): 
        return (a-1)*(b-1)

    # get GCD
    def extended_euclidean_algo(self,a,b):
        # Base Case 
        if a == 0 :  
            return b,0,1

        gcd,x1,y1 = self.extended_euclidean_algo(b%a, a) 
        
        # Update x and y using results of recursive 
        # call 
        x = y1 - (b//a) * x1 
        y = x1 
        
        return gcd,x,y

    def getSeed(self,p,q):
        
        # Max value the seed can be
        max = self.ETF(p,q)

        # Seed must not be too small
        min = max // 2

        while True:
            testS = pow(round(time.time()*1000)+self.seedInc,3,max-min+1) + min
            self.seedInc = (self.seedInc + 1) % round(time.time()*1000)

            if self.extended_euclidean_algo(testS,max)[0] == 1:
                return testS
    
    def getRandomNumberRange(self, min, max):

        # seed that is relative prime to n
        self.s = self.getSeed(self.p,self.q)

        # Generate ceil(log2((10^numDigits)-1)) bits and then scale to the 10^(numDigits-1) to (10^numDigits)-1 range using
        # (random % (max-min+1))+min

        # Get number of bits by checking the amount of bits in (10^numDigits)-1 
        numBits = len(bin(int(max))[2:])

        rndMax = max
        rndMin = min

        x = []
        b = []
        x.append(pow(self.s,2,self.n))

        bits = ""
        for i in range(numBits):
            x.append(pow(x[len(x)-1],2,self.n))
            b.append(x[len(x)-1] % 2)
            bits += str(b[len(b)-1])

        rndNumber = (int(bits,2) % (rndMax-rndMin+1)) + rndMin

        return rndNumber

