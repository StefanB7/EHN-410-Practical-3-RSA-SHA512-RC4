#SHA512 Implementation
#EHN 410 - Practical 3 - 2021
#©Stefan Buys, Jacobus Oettle
#Group 7 - Created 21 May 2021

import struct

class SHA512(object):
    _message = None
    _messageLength = 0
    _paddedLength = 0
    _hashBuffer = [0x6A09E667F3BCC908, 0xBB67AE8584CAA73B, 0x3C6EF372FE94F82B, 0xA54FF53A5F1D36F1, 0x510E527FADE682D1,
                   0x9B05688C2B3E6C1F, 0x1F83D9ABFB41BD6B, 0x5BE0CD19137E2179]
    _k = [0x428a2f98d728ae22,0x7137449123ef65cd,0xb5c0fbcfec4d3b2f,0xe9b5dba58189dbbc,0x3956c25bf348b538,0x59f111f1b605d019,
          0x923f82a4af194f9b,0xab1c5ed5da6d8118,0xd807aa98a3030242,0x12835b0145706fbe,0x243185be4ee4b28c,0x550c7dc3d5ffb4e2,
          0x72be5d74f27b896f,0x80deb1fe3b1696b1,0x9bdc06a725c71235,0xc19bf174cf692694,0xe49b69c19ef14ad2,0xefbe4786384f25e3,
          0x0fc19dc68b8cd5b5,0x240ca1cc77ac9c65,0x2de92c6f592b0275,0x4a7484aa6ea6e483,0x5cb0a9dcbd41fbd4,0x76f988da831153b5,
          0x983e5152ee66dfab,0xa831c66d2db43210,0xb00327c898fb213f,0xbf597fc7beef0ee4,0xc6e00bf33da88fc2,0xd5a79147930aa725,
          0x06ca6351e003826f,0x142929670a0e6e70,0x27b70a8546d22ffc,0x2e1b21385c26c926,0x4d2c6dfc5ac42aed,0x53380d139d95b3df,
          0x650a73548baf63de,0x766a0abb3c77b2a8,0x81c2c92e47edaee6,0x92722c851482353b,0xa2bfe8a14cf10364,0xa81a664bbc423001,
          0xc24b8b70d0f89791,0xc76c51a30654be30,0xd192e819d6ef5218,0xd69906245565a910,0xf40e35855771202a,0x106aa07032bbd1b8,
          0x19a4c116b8d2d0c8,0x1e376c085141ab53,0x2748774cdf8eeb99,0x34b0bcb5e19b48a8,0x391c0cb3c5c95a63,0x4ed8aa4ae3418acb,
          0x5b9cca4f7763e373,0x682e6ff3d6b2b8a3,0x748f82ee5defb2fc,0x78a5636f43172f60,0x84c87814a1f0ab72,0x8cc702081a6439ec,
          0x90befffa23631e28,0xa4506cebde82bde9,0xbef9a3f7b2c67915,0xc67178f2e372532b,0xca273eceea26619c,0xd186b8c721c0c207,
          0xeada7dd6cde0eb1e,0xf57d4f7fee6ed178,0x06f067aa72176fba,0x0a637dc5a2c898a6,0x113f9804bef90dae,0x1b710b35131c471b,
          0x28db77f523047d84,0x32caab7b40c72493,0x3c9ebe0a15c9bebc,0x431d67c49c100d4c,0x4cc5d4becb3e42b6,0x597f299cfc657e2a,
          0x5fcb6fab3ad6faec,0x6c44198c4a475817]

    def __init__(self, InputMessage = None):
        if not(InputMessage == None):
            self.setMessage(InputMessage)


    def setMessage(self, InputMessage):
        if isinstance(InputMessage, str):
            # Update the length of the internal message:
            self._messageLength = len(InputMessage)

            # Populdate the internal message bytearray:
            self._message = bytearray(self._messageLength)
            for i in range(self._messageLength):
                self._message[i] = ord(InputMessage[i])

            #Pad the message:
            self.padMessage()
        else:
            raise Exception("SHA512 Hash: Invalid data type passed")

    def padMessage(self):
        #Determine the number of bytes left that doesn't fit into 1024 bit blocks:
        numNoFit = self._messageLength % 128

        #Determine the number of bytes that should be added:
        if numNoFit >= 112:
            numtoAdd = (128 - numNoFit) + 112
        else:
            numtoAdd = 112 - numNoFit

        #Add the bytes to the message:

        #The first byte should contain a 1 in the MSB position:
        self._message.append(0x80) #1000 0000
        numtoAdd -= 1

        #Add all of the padding bytes:
        for i in range(numtoAdd):
            self._message.append(0x00)

        #Update the padded message length:
        self._paddedLength = len(self._message)

        #Add the length of the message to the end of the message:
        lengthBytearray = self._messageLength.to_bytes(16, byteorder="big", signed=False)
        for i in range(len(lengthBytearray)):
            self._message.append(lengthBytearray[i])

        self.calculateSingleHash(self._message)

    def calculateSingleHash(self, inputBytearray):
        #Calculate the message key schedule:
        w = [0]*80

        #The first 16 values are taken from the input as is:
        for i in range(16):
            w[i] = struct.unpack("!1Q", inputBytearray[i*8:(i+1)*8])

        #The rest of the values are calculated according to the key schedule

        print(w)

    def rotateRight(self, value, numPositions):
        return ((value >> numPositions) | (value << (64 - numPositions))) & 0xFFFFFFFFFFFFFFFF

toets = SHA512("Hello")
print(toets._message)

print(len(toets._message))
