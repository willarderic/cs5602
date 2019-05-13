from collections import OrderedDict
import operator
import re
import math

with open("File601.txt", 'rb') as f:
    data = f.read()
    outputfile = open("WILLARDProb6.bin","wb")
    outputfile.write(data)
    outputfile.close()

# filename = 'File601.bin'

# f = open(filename, 'rb')

# # Use a dictionary to map values for decoding
# reverseEncoding = {}

# decodedArray = []
# for i in range(10000):
#     # Read one byte at a time
#     byte = f.read(1)
#     intFromByte = int.from_bytes(byte, 'big')
#     if i < 26:
#         # Keep the first 26 characters the same
#         reverseEncoding[intFromByte] = 65 + i
#         decodedArray.append(intFromByte)
#     else:
#         # Append each decoded byte to an array
#         decodedArray.append(reverseEncoding[intFromByte])
# decryptedArray = []

# decodedArray = decodedArray[:100]

# key = "SINGE"
# for i in range(len(decodedArray)):
#     if i < 26:
#         # print(chr(decodedArray[i]))
#         decryptedArray.append(decodedArray[i])
#     else:
#         print(decodedArray[i])
#         print((((decodedArray[i] - 65) + (ord(key[(i - 26) % len(key)]) - 65)) % 26))
#         print(((((decodedArray[i] - 65) + (ord(key[(i - 26) % len(key)]) - 65)) % 26) + 65))
#         print("\n")
#         # decryptedArray.append()

# print("".join([chr(i) for i in decryptedArray]))

# SINGE

# KEY LENGTH MOST LIKELY 5
# cipherTextCount = OrderedDict()
# bigramCount = OrderedDict()
# trigramCount = OrderedDict()
# for i in range(len(cipherText)):
#     ch1 = cipherText[i]
#     if i < len(cipherText) - 2:
#         ch2 = cipherText[i + 1]
#     if i < len(cipherText) - 3:
#         ch3 = cipherText[i + 2]
    
#     if ch1 in cipherTextCount.keys():
#         cipherTextCount[ch1] += 1
#     else:
#         cipherTextCount[ch1] = 1
    
#     bi = ch1 + ch2
#     if bi in bigramCount.keys():
#         bigramCount[bi] += 1
#     else:
#         bigramCount[bi] = 1

#     tri = bi + ch3
#     if tri in trigramCount.keys():
#         trigramCount[tri] += 1
#     else:
#         trigramCount[tri] = 1

# for key in bigramCount.keys():
#     bigramCount[key] /= len(cipherText)
#     bigramCount[key] *= 100
#     bigramCount[key] = round(bigramCount[key], 2)

# for key in trigramCount.keys():
#     trigramCount[key] /= len(cipherText)
#     trigramCount[key] *= 100
#     trigramCount[key] = round(trigramCount[key], 2)

# print("Top Bigrams")
# i = 0
# for key, value in sorted(bigramCount.items(), key=lambda item: item[1], reverse = True):
#     print("\t", key, value)
#     i += 1
#     if i > 5:
#         break

# print("Top Trigrams")
# i = 0
# for key, value in sorted(trigramCount.items(), key=lambda item: item[1], reverse = True):
#     print("\t", key, value)
#     i += 1
#     if i > 5:
#         break

# indexesOfBigram = [m.start() for m in re.finditer('LW', cipherText)]

# possibleKeyLengths = {}

# for i in range(len(indexesOfBigram)):
#     for j in range(i, len(indexesOfBigram)):
#         g = math.gcd(indexesOfBigram[i], indexesOfBigram[j])
#         if g not in possibleKeyLengths.keys():
#             possibleKeyLengths[g] = 1
#         else:
#             possibleKeyLengths[g] += 1

# print(sorted(possibleKeyLengths.items(), key=lambda item: item[1], reverse = True))