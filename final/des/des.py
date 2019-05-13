'''
    Custom DES Encryption for CS 5602 Intro to Cryptography
    S-Boxes should be permutated in the order '75368214'
    Meaning the values of S-Box 1 would populate the vales of S-Box 7,
    the values of S-Box 2 would populate the values of S-Box 5, etc...
'''

# Initial Permutation

IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17,  9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Inverse of Initial Permutation

IPInverse = [40, 8, 48, 16, 56, 24, 64, 32,
             39, 7, 47, 15, 55, 23, 63, 31,
             38, 6, 46, 14, 54, 22, 62, 30,
             37, 5, 45, 13, 53, 21, 61, 29,
             36, 4, 44, 12, 52, 20, 60, 28,
             35, 3, 43, 11, 51, 19, 59, 27,
             34, 2, 42, 10, 50, 18, 58, 26,
             33, 1, 41,  9, 49, 17, 57, 25]

# Expansion Permutation

E = [32,  1,  2,  3,  4,  5,
      4,  5,  6,  7,  8,  9,
      8,  9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32,  1]

# PBox Permutation

PBox = [16,  7, 20, 21,
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25]

# PC-1 and PC-2 Permutations

# PC-1 Permutes the 64-bit key and shrinks it into a 56-bit key
PC1 = [57, 49, 41, 33, 25, 17,  9,
        1, 58, 50, 42, 34, 26, 18,
       10,  2, 59, 51, 43, 35, 27,
       19, 11,  3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
       14,  6, 61, 53, 45, 37, 29,
       21, 13,  5, 28, 20, 12,  4]

# PC-2 Permutes the 56-bit and shrinks it into a 48-bit key
PC2 = [14, 17, 11, 24, 1,   5,
        3, 28, 15,  6, 21, 10,
       23, 19, 12,  4, 26,  8,
       16,  7, 27, 20, 13,  2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]


# S-Boxes in the custom order following the permutation '75368214'
S = [0] * 9
# S1 -> S7
S[7] = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

# S2 -> S5
S[5] = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

# S3 -> S3
S[3] = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

# S4 -> S6
S[6] = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

# S5 -> S8
S[8] = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

# S6 -> S2
S[2] = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

# S7 -> S1
S[1] = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

# S8 -> S4
S[4] = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

'''
    Helper functions
'''
def xor(s1, s2):
    result = ""
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            result += "1"
        else:
            result += "0"
    return result

def permute(s, p):
    tmp = [0] * len(p)
    for i in range(len(p)):
        tmp[i] = s[p[i] - 1]
    return tmp

def expansion(s, p):
    tmp = [0] * len(p)
    for i in range(len(p)):
        tmp[i] = s[p[i] - 1]
    return tmp

def shrink(s, p):
    tmp = [0] * len(p)
    for i in range(len(p)):
        if i % 8 == 0:
            continue
        tmp[i] = s[p[i] - 1]
    return tmp

'''
    This function encrypts a given plaintext with the key provided
    Input must be a string of binary digits
'''
def encrypt(plaintext, key):
    # Apply Initial Permutation
    ipText = permute(plaintext, IP)

    # Split into left and right
    L0 = ipText[:32]
    R0 = ipText[32:]
    
    L, R = feistel(L0, R0, key)
    # Append R to L
    L += R

    # Apply inverse of initial permutation
    cipherText = permute(L, IPInverse)
    
    return cipherText


'''
    This method decrypts a given ciphertext using the same key that was used to
    encrypt it with
'''
def decrypt(ciphertext, key):
    # Apply Initial Permutation
    ipText = permute(ciphertext, IP)
    # Split into left and right
    L0 = ipText[:32]
    R0 = ipText[32:]

    # Run reverse feistel
    L, R = dfeistel(L0, R0, key)

    # Append R to L
    L += R

    # Apply inverse of initial permutation
    plaintext = permute(L, IPInverse)
    
    return plaintext

'''
    This function is an implementation of the feistel cipher algorithm
'''
def feistel(L0, R0, key):
    # Feistel Cipher Algorithm
    # Previous L and R are initialized to L0 and R0
    prevL = L0
    prevR = R0

    rkeys = calculateRoundKeys(key)
    # Feistel Cipher runs 16 rounds
    for i in range(16):
        # L is assigned to the previous R
        L = prevR

        # R is assigned to F XOR'd with previous L
        R = xor(F(prevR, rkeys[i]), prevL)

        # L and R are now previous L and R
        prevL = L
        prevR = R

    return R, L

'''
    This function is the decryption version of feistel which applies the round keys backwards
'''
def dfeistel(L0, R0, key):
    # Feistel Cipher Algorithm
    # Previous L and R are initialized to L0 and R0
    prevL = R0
    prevR = L0

    rkeys = calculateRoundKeys(key)
    # Feistel Cipher runs 16 rounds
    for i in range(15, -1, -1):
        R = prevL
        L = xor(F(prevL, rkeys[i]), prevR)
        # L and R are now previous L and R
        prevL = L
        prevR = R

        #print(L, R)
    return L, R

'''
    This function is an implementation of the mysterious F function in the
    feistel cipher
    Takes 32-bits and uses the round key to permute and return 32 scrambled bits
'''
def F(R, rkey):
    # Expansion Permutation on R
    R = expansion(R, E)

    # XOR R with Round key
    R = xor(R, rkey)

    # Apply S-Boxes
    newR = ""
    for i in range(8):
        bits = R[i * 6:i * 6 + 6]
        # Calculate Row and column in S-Box
        row = int(bits[0] + bits[-1], 2)
        col = int(bits[1:5], 2)
        #print(row, col)
        newR += "{0:04b}".format(S[i+1][row][col])

    # Apply P-Box
    newR = permute(newR, PBox)
    return newR

'''
    This function calculates the round keys used in the feistel cipher
'''
def calculateRoundKeys(key):
    rkeys = []
    # Shrink the key to 56 bits
    key56 = permute(key, PC1)
    # C is first half of key, and D is second half of key
    C = key56[:28]
    D = key56[28:]
    # Run for 16 rounds, 1 to 16
    for i in range(1, 17):
        # If the round is 1,2,9, or 16 shift C and D by 1
        if i == 1 or i == 2 or i == 9 or i == 16:
            C.append(C[0])
            C = C[1:]
            D.append(D[0])
            D = D[1:]
        # If round is not 1,2,9, or 16, shift C and D by 2
        else:
            C.append(C[0])
            C.append(C[1])
            C = C[2:]
            D.append(D[0])
            D.append(D[1])
            D = D[2:]

        # Combine C and D together
        CD = []
        CD.extend(C)
        CD.extend(D)
        # Shrink round key once again with PC-2 to create a 48-bit key
        rkey = permute(CD, PC2)
        rkeys.append(rkey)
    return rkeys

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes(len(s) // 8, byteorder='big')

# Test plaintext
# des('0000000100100011010001010110011110001001101010111100110111101111','0001001100110100010101110111100110011011101111001101111111110001')

# Student ID to binary
# for i in '8144361':
#     print("{0:08b}".format(int(i)))

# Key with parity bits here:
#00010001 00000011 00001001 00001001 00000110 00001100 00000011

# 00001000 00000001 00000100 00000100 00000011 00000110 00000001

# How to read in files into a list of binary digits
# with open("output.txt", "rb") as f:
#     with open("output2.txt", "wb") as o:
#         bitstring = ""
#         while True:
#             byte = f.read(1)
#             sbyte = ""

#             if not byte:
#                 break
                
#             intByte = int.from_bytes(byte, 'big')
#             for i in range(8):
#                 bit =  intByte & 1
#                 sbyte = str(bit) + sbyte
#                 intByte = intByte >> 1
#             bitstring += sbyte
#         if len(bitstring) % 64 != 0:
#             bitstring += "0" * (64 - len(bitstring) % 64)

#         output = ""
#         for i in range(len(bitstring) // 64):
#             block = bitstring[i * 64:i * 64 + 64]
#             output += "".join(des(block,'0001001100110100010101110111100110011011101111001101111111110001'))
#         o.write(bitstring_to_bytes(output))

input = "This is some input that is going to be used for my custom DES encryption algorithm."

bitstring = ""
for c in input:
    intByte = ord(c)
    sbyte = ""
    for i in range(8):
        bit =  intByte & 1
        sbyte = str(bit) + sbyte
        intByte = intByte >> 1
    bitstring += sbyte

if len(bitstring) % 64 != 0:
    bitstring += "0" * (64 - len(bitstring) % 64)
print(bitstring)

output = ""
for i in range(len(bitstring) // 64):
    block = bitstring[i * 64:i * 64 + 64]
    output += "".join(encrypt(block,'0001001100110100010101110111100110011011101111001101111111110001'))
print(output)

output2 = ""
for i in range(len(output) // 64):
    block = output[i * 64:i * 64 + 64]
    output2 += "".join(decrypt(block,'0001001100110100010101110111100110011011101111001101111111110001'))
print(output2)

print(bitstring == output2)