from RSA import RSA

class receiver:
    def __init__(self):
        p = input("To start a secure transmission channel, Enter RECEIVER's p value of Press Enter: ")
        print("")
        q = input("To start a secure transmission channel, Enter RECEIVER's q value of Press Enter: ")
        print("")

        while not ((len(p) == 0 and len(q) == 0) or (len(p) != 0 and len(q) != 0)):
            print("Please provide both 'p' and 'q' values or none at all")
            print("")
            p = input("To start a secure transmission c563hannel, Enter RECEIVER's p value of Press Enter: ")
            print("")
            q = input("To start a secure transmission channel, Enter RECEIVER's q value of Press Enter: ")
            print("")

        if len(p) == 0 and len(q) == 0:
            print("Auto Generating Keys...")
            print("Phase 1")
            pLen = input("Please enter the length of the prime for 'p' and 'q' : ")
            if len(pLen) == 0:
                pLen = 0
            
            self.generatePandQ(pLen)

            print("RECEIVER generated p : \t\t\t\t",self.rsaCipher.get_p())
            print("RECEIVER generated q : \t\t\t\t",self.rsaCipher.get_q())
            print("RECEIVER generated n : \t\t\t\t",self.rsaCipher.get_n())
            print("RECEIVER generated Phi(n) : \t\t\t",self.rsaCipher.get_phi())
            print("RECEIVER has Public key : \t\t\t",self.rsaCipher.get_e())
            print("RECEIVER has Private key : \t\t\t",self.rsaCipher.get_d())
        else:
            print("Phase 1")

            self.createKeys(p,q)

            print("RECEIVER specified p : \t\t\t\t",self.rsaCipher.get_p())
            print("RECEIVER specified q : \t\t\t\t",self.rsaCipher.get_q())
            print("RECEIVER generated n : \t\t\t\t",self.rsaCipher.get_n())
            print("RECEIVER generated Phi(n) : \t\t\t",self.rsaCipher.get_phi())
            print("RECEIVER has Public key : \t\t\t",self.rsaCipher.get_e())
            print("RECEIVER has Private key : \t\t\t",self.rsaCipher.get_d())

    def generatePandQ(self,pLen):
        self.rsaCipher = RSA(int(pLen))
    
    def createKeys(self,p,q):
        self.rsaCipher = RSA(10,p,q)
    
    def getPublicKey(self):
        return self.rsaCipher.get_e()
    
    def getPublicN(self):
        return self.rsaCipher.get_n()
    
    def setEncRC4(self, encRC4):
        self.encRC4 = encRC4
    
    def decryptRC4(self):
        self.decRC4 = self.rsaCipher.decryptRSA(self.encRC4,self.rsaCipher.get_d(),self.rsaCipher.get_n())
        print("RECEIVER RSA decrypted RC4 key : \t\t"," ".join([hex(x)[2:].zfill(2).upper() for x in self.decRC4]))
        print("")