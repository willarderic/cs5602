filename = 'File280.bin'

f = open(filename, 'rb')

# Use a dictionary to map values for decoding
reverseEncoding = {}

decodedFile = open("WILLARDProb4File2.bin", "wb")
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