#SHA512 Implementation
#EHN 410 - Practical 3 - 2021
#©Stefan Buys, Jacobus Oettle
#Group 7 - Created 21 May 2021

import struct

class SHA512(object):
    _message = None
    _messageLength = 0
    _paddedLength = 0
    _hashBuffer = [0x6A09E667F3BCC908, 0xBB67AE8584CAA73B, 0x3C6EF372FE94F82B, 0xA54FF53A5F1D36F1, 0x510E527FADE682D1, 0x9B05688C2B3E6C1F, 0x1F83D9ABFB41BD6B, 0x5BE0CD19137E2179]

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

toets = SHA512("Hello")
print(toets._message)

print(len(toets._message))