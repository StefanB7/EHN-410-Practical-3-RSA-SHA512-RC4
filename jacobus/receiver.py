# Classes
from RSA import RSA
from RC4 import RC4
from SHA512 import SHA512

# Libraries
from PIL import Image
import numpy as np
import math

# RC4 encryption object
RC4 = RC4()

class receiver:
    def __init__(self):
        self.hashReceived = ""
        p = input("To start a secure transmission channel, Enter RECEIVER's p value of Press Enter: ")
        print("")
        q = input("To start a secure transmission channel, Enter RECEIVER's q value of Press Enter: ")
        print("")

        while not ((len(p) == 0 and len(q) == 0) or (len(p) != 0 and len(q) != 0)):
            print("Please provide both 'p' and 'q' values or none at all")
            print("")
            p = input("To start a secure transmission channel, Enter RECEIVER's p value of Press Enter: ")
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
        self.rsaCipher = RSA(10,int(p),int(q))
    
    def getPublicKey(self):
        return self.rsaCipher.get_e()
    
    def getPublicN(self):
        return self.rsaCipher.get_n()
    
    def setEncRC4(self, encRC4):
        self.encRC4 = encRC4
    
    def decryptRC4(self):
        self.decRC4 = self.rsaCipher.decryptRSA(self.encRC4,self.rsaCipher.get_d(),self.rsaCipher.get_n())
        print("RECEIVER RSA decrypted RC4 key : \n"," ".join([hex(x)[2:].zfill(2).upper() for x in self.decRC4]))
        print("")
    
    def decryptMessage(self, encMsg):
        print("RECEIVER Decrypted message received:")
        self.decMsg_with_hash = RC4.RC4_Decrypt(False,encMsg,self.decRC4) # remove nog die hash hier

        #Get and remove the hash from the received plaintext:
        #If the plaintext is a string:
        if (isinstance(self.decMsg_with_hash, str)):
            self.hashReceived = self.decMsg_with_hash[-64:]
            self.decMsg = self.decMsg_with_hash[:-64]


        # Else if the plaintext is an image:
        elif (isinstance(self.decMsg_with_hash, np.ndarray)):
            #Get the dimensions of the image:
            numRows = self.decMsg_with_hash.shape[0]
            numColumns = self.decMsg_with_hash.shape[1]
            numLayers = self.decMsg_with_hash.shape[2]

            #Calculate the number of rows to add to fit the hash values calculated (into the first layer):
            numRowsAdded = math.ceil(64.0 / numColumns)

            self.decMsg = np.ndarray((numRows - numRowsAdded, numColumns, numLayers), dtype="u1")

            #Copy the plaintext to the new plain_plus_hash array:
            for layer in range(numLayers):
                for row in range(numRows - numRowsAdded):
                    for column in range(numColumns):
                        self.decMsg[row][column][layer] = self.decMsg_with_hash[row][column][layer]


            #Get the hash from the decrypted message:
            hashvalueString = ""
            rowIndex = numRows - numRowsAdded
            columnIndex = 0
            index = 0
            while index < 64:
                hashvalueString = hashvalueString + chr(self.decMsg_with_hash[rowIndex][columnIndex][0])
                index += 1
                columnIndex += 1
                if columnIndex >= numColumns:
                    columnIndex = 0
                    rowIndex += 1

            self.hashReceived = hashvalueString

        # Plaintext is not of type image or string, return exception
        else:
            raise Exception("Receiver: Invalid message type encountered for SHA512 hashing (Decryption)")

        print(self.decMsg)
        print("")
        if type(self.decMsg) is np.ndarray:
            Image.fromarray(self.decMsg.astype(np.uint8)).save('jacobus\\rx_dec.png')
    
    def authenticateMessage(self):
        #Calculate the received message's hash value
        hashauth = SHA512(self.decMsg)
        hashauth.calculateHash()
        print("RECEIVER Expected Hash:")
        print(hashauth.printHash())
        expectedHashValue = hashauth.getHashResultasString()

        print("")
        print("RECEIVER Received Hash:")
        print(" ".join([hex(ord(x))[2:].zfill(2).upper() for x in self.hashReceived]))
        print("")

        if self.hashReceived == expectedHashValue:
            print("Message Authenticated")
        else:
            print("Message Authentication failed")
    
    def hashMessage(self):
        print("") # delete die calculate the hash