# RSA

# skyrf in report hvl round van die miller rabin jy moet doen check 302 vir hvl rondtes connect dit met hoe groot prime gesoek word

# https://crypto.stackexchange.com/questions/10805/how-does-one-deal-with-a-negative-d-in-rsa

from PRNG_BBS import PRNG_BBS

class RSA:
    def __init__(self,primeDigits,p=None,q=None,e=None,d=None):
        self.BBS = PRNG_BBS()

        if p is None:
            pq = self.getRandomPrimes(primeDigits)

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

            if e is not None:
                # Public key {e,n}, e (calculate it), must be relatively prime to ETF(n) (gcd -> 1) and smaller than ETF(n)
                self.e = e

                # Private key {d,n}, d calculated
                self.d = d

            else:
                ed = self.getEandD(self.ETF(self.p,self.q))

                # Public key {e,n}, e (calculate it), must be relatively prime to ETF(n) (gcd -> 1) and smaller than ETF(n)
                self.e = ed[0]

                # Private key {d,n}, d calculated
                self.d = ed[1]

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
    def getRandomPrimes(self,length):

        minLength = 3

        # Since the two primes must be in a certain range the min and max values for both can be calculated:
        # Min value for primes is still set by the blocksize
        if length < minLength:
            print("\nWARNING: Length chosen is smaller than minimum length set by blocksize...")
            print("Min length set to: ",minLength)
            print("")
            length = minLength
            minRange = 506
        elif length > minLength:
            minRange = pow(10,length-1)
        else:
            minRange = 506
        
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
        while True:
            # choose random large e and test if coprime
            e = self.BBS.getRandomNumberRange(int(phi*0.75),phi-2)
            if self.extended_euclidean_algo(e,phi)[0] == 1:
                d = self.extended_euclidean_algo(e,phi)[1]
                while d < 0:
                    d = d + phi
                return [e,d]

    # pretty sure die zfill moet 3 wees want getalle kan 255 wees bv. !!!!!!!!!1
    def encryptRSA(self,plain, publicKey, n):
        enc = []
        for i in range(len(plain)//2):
            P = int(str(plain[2*i]).zfill(3) + str(plain[2*i +1]).zfill(3))
            # print("P"+str(i)+" : "+str(P))
            enc.append(pow(P,publicKey,n))
            # print("C"+str(i)+" : "+str(enc[len(enc)-1])+"\n")

        return enc

    def decryptRSA(self,cipher, privateKey, n):

        dec = []
        for j in range(len(cipher)):
            # print("C"+str(j)+" : "+str(cipher[j]))
            P = pow(cipher[j],privateKey,n)
            # print("P"+str(j)+" : "+str(P).zfill(4)+"\n")
            dec.append(int(str(P).zfill(6)[:3]))
            dec.append(int(str(P).zfill(6)[3:]))

        return dec
