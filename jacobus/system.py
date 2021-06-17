########### SYSTEM to simulate transmitter and receiver operation ###########

# sit nog van die kode in die twee transmitter en receiver classes

from RSA import RSA
from PRNG_BBS import PRNG_BBS
import numpy as np

BBS = PRNG_BBS()

print("Welcome")
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
    rsaCipher = RSA(int(pLen))
    print("RECEIVER generated p : \t\t\t\t",rsaCipher.get_p())
    print("RECEIVER generated q : \t\t\t\t",rsaCipher.get_q())
    print("RECEIVER generated n : \t\t\t\t",rsaCipher.get_n())
    print("RECEIVER generated Phi(n) : \t\t\t",rsaCipher.get_phi())
    print("RECEIVER has Public key : \t\t\t",rsaCipher.get_e())
    print("RECEIVER has Private key : \t\t\t",rsaCipher.get_d())
else:
    print("Phase 1")
    rsaCipher = RSA(10,16,int(p),int(q))
    print("RECEIVER specified p : \t\t\t\t",rsaCipher.get_p())
    print("RECEIVER specified q : \t\t\t\t",rsaCipher.get_q())
    print("RECEIVER generated n : \t\t\t\t",rsaCipher.get_n())
    print("RECEIVER generated Phi(n) : \t\t\t",rsaCipher.get_phi())
    print("RECEIVER has Public key : \t\t\t",rsaCipher.get_e())
    print("RECEIVER has Private key : \t\t\t",rsaCipher.get_d())

print("")
keyInput = input("TRANSMITTER Please Enter RC4 key or Press Enter : ")
print("")
if len(keyInput) == 0:
    keyInput = []
    for i in range(256):
        keyInput.append(hex(BBS.getRandomNumberRange(0,255))[2:].upper().zfill(2))
    print("TRANSMITTER Auto Generating RC4 key : \t\t"," ".join(keyInput))
    print("")

    rc4Key = [int(x,16) for x in keyInput]

elif len(keyInput) < 256:
    while len(keyInput) < 256:
        keyInput += keyInput
    keyInput  = keyInput[:256]
    print("Length of RC4 too small, key was concatenated:\t",keyInput)

    rc4Key = [ord(x) for x in keyInput]
    print("")
    print("TRANSMITTER specified RC4 key : \t\t"," ".join([hex(x)[2:].zfill(2).upper() for x in rc4Key]))
    print("")
else:
    keyInput = keyInput[:256]
    print("Length of RC4 too large, key was shortened:\t",keyInput)
    rc4Key = [ord(x) for x in keyInput]
    print("")
    print("TRANSMITTER specified RC4 key : \t\t"," ".join([hex(x)[2:].zfill(2).upper() for x in rc4Key]))
    print("")

rc4Encrypted = rsaCipher.encryptRSA(rc4Key)
print("TRANSMITTER RSA encrypted RC4 key : \t\t",rc4Encrypted)
rc4Decrypted = rsaCipher.decryptRSA(rc4Encrypted)
print("RECEIVER RSA decrypted RC4 key : \t\t"," ".join([hex(x)[2:].zfill(2).upper() for x in rc4Decrypted]))
print("")

# moet nog die min waarde verander want dis nie 2^16 nie dis 255255 wat groter is !!!!!!!!!!!!! *facepalm

print("Phase 2")
inputMessage = input("TRANSMITTER Please Enter a message: ")
print("")

if inputMessage[len(inputMessage)-4:] == ".txt":
    print("TRANSMITTER Loading message from file '"+inputMessage+"':")
    file = open("jacobus\\"+inputMessage,"r")
    print("\""+file.read()+"\"")
elif inputMessage[len(inputMessage)-4:] == ".png":
    print("TRANSMITTER Loading image '"+inputMessage+"'...")

    # doen image goed

# doen hashing 

# doen encrypting

# Phase 3

# doen decrypting

# doen hashing