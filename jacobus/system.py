########### SYSTEM to simulate transmitter and receiver operation ###########

from RSA import RSA
from PRNG_BBS import PRNG_BBS
from receiver import receiver
from transmitter import transmitter

# Blum Blum Shub random int generator class
BBS = PRNG_BBS()

print("")
print("Welcome")

########### Phase 1

# Receiver object creation and the set of the p and q values
RX = receiver()

# Transmitter object creation and the set of the RC4 key
TX = transmitter()

# Receiver sends public key and "n" to the Transmitter
TX.setPublicKey(RX.getPublicKey())
TX.setPublicN(RX.getPublicN())

# Transmitter encrypts the RC4 key
TX.encryptRC4()

# Transmitter sends the encrypted RC4 key to the Receiver
RX.setEncRC4(TX.getEncRC4())

# Receiver decrypts the RC4
RX.decryptRC4()

########### Phase 2

print("Phase 2")

TX.loadMessage()


# doen hashing 

# doen encrypting

# Phase 3

# doen decrypting

# doen hashing