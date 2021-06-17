from PRNG_BBS import PRNG_BBS
from RSA import RSA

# Blum Blum Shub random int generator class
BBS = PRNG_BBS()

class transmitter:
    def __init__(self):
        print("")
        keyInput = input("TRANSMITTER Please Enter RC4 key or Press Enter : ")
        print("")
        if len(keyInput) == 0:
            keyInput = []
            for i in range(256):
                keyInput.append(hex(BBS.getRandomNumberRange(0,255))[2:].upper().zfill(2))
            print("TRANSMITTER Auto Generating RC4 key : \t\t"," ".join(keyInput))
            print("")

            self.rc4Key = [int(x,16) for x in keyInput]

        elif len(keyInput) < 256:
            while len(keyInput) < 256:
                keyInput += keyInput
            keyInput  = keyInput[:256]
            print("Length of RC4 too small, key was concatenated:\t",keyInput)
            print("")

            self.rc4Key = [ord(x) for x in keyInput]

            print("TRANSMITTER specified RC4 key : \t\t"," ".join([hex(x)[2:].zfill(2).upper() for x in self.rc4Key]))
            print("")
        else:
            keyInput = keyInput[:256]
            print("Length of RC4 too large, key was shortened:\t",keyInput)
            print("")
            
            self.rc4Key = [ord(x) for x in keyInput]
            
            print("TRANSMITTER specified RC4 key : \t\t"," ".join([hex(x)[2:].zfill(2).upper() for x in self.rc4Key]))
            print("")

    def setPublicKey(self,e):
        self.publicKey = e
    
    def setPublicN(self,n):
        self.publicN = n

    def encryptRC4(self):
        temp = RSA(3)
        self.encRC4 = temp.encryptRSA(self.rc4Key,self.publicKey,self.publicN)
        print("TRANSMITTER RSA encrypted RC4 key : \t\t",self.encRC4)
        print("")
    
    def getEncRC4(self):
        return self.encRC4

    def loadMessage(self):
        inputMessage = input("TRANSMITTER Please Enter a message: ")
        print("")

        if inputMessage[len(inputMessage)-4:] == ".txt":
            print("TRANSMITTER Loading message from file '"+inputMessage+"':")
            file = open("jacobus\\"+inputMessage,"r")
            print("\""+file.read()+"\"")
            # doen text file goed hier

        elif inputMessage[len(inputMessage)-4:] == ".png":
            print("TRANSMITTER Loading image file '"+inputMessage+"'...")
            # doen image goed hier
        else:
            print("TRANSMITTER message from input: '"+inputMessage+"':")
            # doen normale txt goed hier