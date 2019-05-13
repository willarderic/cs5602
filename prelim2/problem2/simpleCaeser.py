filename = 'File777.bin'

f = open(filename, 'rb')

# Use a dictionary to map values for decoding
reverseEncoding = {}

decodedFile = open("WILLARDprob2a.bin", "wb")
decryptedEncodedFile = open("WILLARDprob2b.bin", "wb")
decodedArray = []
for i in range(10000):
    # Read one byte at a time
    byte = f.read(1)
    intFromByte = int.from_bytes(byte, 'big')
    if i < 26:
        # Keep the first 26 characters the same
        reverseEncoding[intFromByte] = 65 + i
        decodedArray.append(intFromByte)
    else:
        # Append each decoded byte to an array
        decodedArray.append(reverseEncoding[intFromByte])

# Write out the decode array to a file for part (a)
decodedFile.write(bytearray(decodedArray))


# CODE TO FIND THE SHIFT (manually checked the text for something readable)
# for i in range(1, 26):
#     for j in range(26, 10000):
#         decodedArray[j] = (((decodedArray[j] - 65) + 1) % 26) + 65
#     print(i, "".join([chr(c) for c in decodedArray][26:400]))
#     print()
# SHIFT ENDED UP BEING 17!

# Create a dictionary to serve as the actually encoding map
encoding = dict((v,k) for k,v in reverseEncoding.items())
decryptedEncodedArray = []

for i in range(10000):
    if i < 26:
        # Keep the original 26 characters the same
        decryptedEncodedArray.append(decodedArray[i])
    else:
        # Encode the shifted characters
        decryptedEncodedArray.append(encoding[(((decodedArray[i] - 65) + 17) % 26) + 65])
# Write answer to file
decryptedEncodedFile.write(bytearray(decryptedEncodedArray))

# Close files
decryptedEncodedFile.close()
f.close()