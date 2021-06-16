# RSA

# moet kan random getalle generate van n sekere lengte (bv 5 of 6 digiits) GLOBAL variable!

# check lengte van n teenoor die lengte van die boodskap (of die byets wat encrypt moet word) 

# skyrf in report hvl round van die miller rabin jy moet doen check 302 vir hvl rondtes connect dit met hoe groot prime gesoek word

# https://crypto.stackexchange.com/questions/10805/how-does-one-deal-with-a-negative-d-in-rsa

from PRNG_BBS import PRNG_BBS
import numpy as np

class RSA:
    def __init__(self,primeDigits,blocksize=16,p=None,q=None,e=None,d=None):
        self.BBS = PRNG_BBS()

        if p is None:
            pq = self.getRandomPrimes(blocksize,primeDigits)

            # 1st prime number
            self.p = pq[0]

            # 2nd prime number
            self.q = pq[1]

            self.n = self.p * self.q

            ed = self.getEandD(self.ETF(self.p,self.q))

            # Public key {e,n}, e (calculate it), must be relatively prime to ETF(n) (gcd -> 1) and smaller than ETF(n)
            self.e = ed[0]

            # Private key {d,n}, d calculated
            self.d = ed[1]

            # print("self.p = ",self.p)
            # print("self.q = ",self.q)
            # print("self.n = ",self.n)
            # print("self.e = ",self.e)
            # print("self.d = ",self.d)

        else:
            # 1st prime number
            self.p = p

            # 2nd prime number
            self.q = q

            self.n = self.p * self.q

            # Public key {e,n}, e (calculate it), must be relatively prime to ETF(n) (gcd -> 1) and smaller than ETF(n)
            self.e = e

            # Private key {d,n}, d calculated
            self.d = d
    
    # getters
    def get_p(self):
        return self.p

    def get_q(self):
        return self.q

    def get_n(self):
        return self.n

    def get_phi(self):
        return self.ETF(self.p,self.q)

    def get_e(self):
        return self.e

    def get_d(self):
        return self.d
    
    # Euler totient function for prime numbers
    def ETF(self,p,q): 
        return (p-1)*(q-1)

    # get random prime numbers in the range 2^i < n <= 2^(i+1), a < p*q <= b
    def getRandomPrimes(self,blocksize,length):

        minLength = len(str(int(np.ceil(np.sqrt(pow(2,blocksize))))))

        # Since the two primes must be in a certain range the min and max values for both can be calculated:
        # Min value for primes is still set by the blocksize
        if length < minLength:
            print("\nWARNING: Length chosen is smaller than minimum length set by blocksize...")
            print("Min length set to: ",minLength)
            print("")
            length = minLength
            minRange = np.ceil(np.sqrt(pow(2,blocksize)))
        elif length > minLength:
            minRange = pow(10,length-1)
        else:
            minRange = np.ceil(np.sqrt(pow(2,blocksize)))
        
        # Max length set by length
        maxRange = (pow(10,length))-1

        result = []

        while len(result) != 2:
            
            i = self.BBS.getRandomNumberRange(int(minRange),int(maxRange))
            r = self.miller_rabin(i,10)

            # find random number in the given range
            while r == False:
                i = self.BBS.getRandomNumberRange(int(minRange),int(maxRange))
                r = self.miller_rabin(i,10)
            
            
            if len(result) == 1:
                # ensure two different primes, and fit in the range
                if result[0] != i and result[0]*i > minRange:
                    result.append(i)
            else:
                result.append(i)

        return result

    # Test for prime
    def miller_rabin(self,n, rounds):
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
            a = self.BBS.getRandomNumberRange(2,n-2) # random int between and including 2 and n-2 
            comp = True
            if pow(a,q,n) == 1:
                comp = False # probably prime
                continue

            for j in range(k): # range 0 to k-1
                if pow(a,pow(2,j)*q,n) == n-1:
                    comp = False # probably prime
                    continue
        
            if comp == True:
                return False
        
        return True

    # get GCD
    def extended_euclidean_algo(self,a,b):

        # Base Case 
        if a == 0 :  
            return b,0,1
        
        # print("ri ",a)
        # print("q ", (b//a))
        gcd,x1,y1 = self.extended_euclidean_algo(b%a, a) 

        # Update x and y using results of recursive 
        # call 
        x = y1 - (b//a) * x1 
        y = x1 
        
        # print("X1 ",x1)
        # print("Y1 ",y1)
        # print("X ",x)
        # print("Y ",y)
        return gcd,x,y

    # get largest value that is coprime
    def getEandD(self,phi):
        for e in range(phi-2,-1,-1):
            if self.extended_euclidean_algo(e,phi)[0] == 1:
                d = self.extended_euclidean_algo(e,phi)[1]
                while d < 0:
                    d = d + phi
                return [e,d]

    # overflow error? 
    # nie waarvan ek weet nie maar om veilig te bly gebruik ek maar normale pow

    # a^b mod n 
    # def powz(self,a,b,n):
    #     b_bin = bin(b)[2:]

    #     f = 1
    #     for i in range(len(b_bin)):
    #         f = pow(f,2,n)
    #         if int(b_bin[i]) == 1:
    #             f = (f*a) % n     

    #     return f

    def cleanString(self,strText):
        # s = strText.lower()
        s = ''.join(str(ord(i))+',' for i in strText if i.isalpha())
        return np.fromstring(s, dtype=int, sep=',')

        # return np.array(bytearray(strText.encode(encoding="ascii")),dtype=np.ubyte)

    def encryptRSA(self,plain):
        enc = []
        for i in range(len(plain)//2):
            P = int(str(plain[2*i]).zfill(2) + str(plain[2*i +1]).zfill(2))
            # print("P"+str(i)+" : "+str(P))
            enc.append(pow(P,self.e,self.n))
            # print("C"+str(i)+" : "+str(enc[len(enc)-1])+"\n")
        
        print("encrypted ", enc)

        return enc

    def decryptRSA(self,cipher):
        dec = []
        for j in range(len(cipher)):
            # print("C"+str(j)+" : "+str(cipher[j]))
            P = pow(cipher[j],self.d,self.n)
            # print("P"+str(j)+" : "+str(P).zfill(4)+"\n")
            dec.append(int(str(P).zfill(4)[:2]))
            dec.append(int(str(P).zfill(4)[2:]))
        print("decrypted ",dec)

test = RSA(5)

plain = [33,14,22,62,0,17,4,62,24,14,20,66]

enc = test.encryptRSA(plain)
test.decryptRSA(enc)