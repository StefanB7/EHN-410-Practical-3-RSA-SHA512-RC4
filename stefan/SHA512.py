#SHA512 Implementation
#EHN 410 - Practical 3 - 2021
#©Stefan Buys, Jacobus Oettle
#Group 7 - Created 21 May 2021

import struct

# class SHA512(object):
#     _message = None
#     _hashBuffer = [0x6A09E667F3BCC908, 0xBB67AE8584CAA73B, 0x3C6EF372FE94F82B, 0xA54FF53A5F1D36F1, 0x510E527FADE682D1, 0x9B05688C2B3E6C1F, 0x1F83D9ABFB41BD6B, 0x5BE0CD19137E2179]
#

array = ""
for i in range(128):
    array = array + "h"
bytearray = array.encode("ascii")
array = struct.unpack("!16Q", bytearray);
print(array)