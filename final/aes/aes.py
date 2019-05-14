Nk = 4
Nb = 4
Nr = 10

S = [
    #  0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f 
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],   # 0
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],   # 1
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],   # 2
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],   # 3
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],   # 4
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],   # 5
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],   # 6
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],   # 7
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],   # 8
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],   # 9
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],   # a
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],   # b
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],   # c
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],   # d
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],   # e
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']    # f
]

iS = [
    #  0     1     2     3     4     5     6     7     8     9     a     b     c     d     e     f   
    ['52', '09', '6a', 'd5', '30', '36', 'a5', '38', 'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],   # 0
    ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87', '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],   # 1
    ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d', 'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],   # 2
    ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2', '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],   # 3
    ['72', 'f8', 'f6', '64', '86', '68', '98', '16', 'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],   # 4
    ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da', '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],   # 5
    ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a', 'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],   # 6
    ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02', 'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],   # 7
    ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea', '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],   # 8 
    ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85', 'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],   # 9
    ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89', '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],   # a
    ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20', '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],   # b
    ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31', 'b1', '12', '10', '59', '27', '80', 'ec', '5f'],   # c
    ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d', '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],   # d
    ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0', 'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],   # e
    ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26', 'e1', '69', '14', '63', '55', '21', '0c', '7d']    # f
]

Rcon = [
    '01000000',
    '02000000',
    '04000000',
    '08000000',
    '10000000',
    '20000000',
    '40000000',
    '80000000',
    '1b000000',
    '36000000'
]

# Helper function to print the state
def printState(state):
    for i in range(4):
        print("{}, {}, {}, {}".format(state[i][0], state[i][1], state[i][2], state[i][3]))
    print()

def xorWord(w, r):
    x = ""
    i = 0
    while i < len(w):
        x += hex(int(w[i], 16) ^ int(r[i], 16))[2:] + hex(int(w[i + 1], 16) ^ int(r[i + 1], 16))[2:]
        i += 2
    return x

# subWord uses the SBox to substitute each byte in a word w with sbox at [nibble1][nibble2]
def subWord(w):
    sub = ""
    i = 0
    while i < len(w):
        sub += S[int(w[i], 16)][int(w[i + 1], 16)]
        i += 2
    return sub

def getStateMatrix(plaintext):
    state = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            index = (i * 8) + (j * 2)
            state[j].append(plaintext[index : index + 2])
    return state

# Implementation of multiplication on GF(2^8)
def gmult(a, b):
    p = 0
    for i in range(8):
        if ((b & 1) != 0):
            p = p ^ a

        highBitSet = (a & 0x80) != 0 # Check if the modulus needs to be taken
        a = a << 1
        # Take the modulus
        if highBitSet:
            a = a ^ 0x11B # x^8 + x^4 + x^3 + x + 1
        b = b >> 1 
    return p

def getTextFromState(state):
    stateString = ""
    for i in range(4):
        for j in range(4):
            stateString += state[j][i]
    return stateString

def addRoundKey(state, w):
    for i in range(4):
        for j in range(4):
            state[j][i] = xorWord(state[j][i], w[i][j * 2 : j * 2 + 2])
    return state


'''
    AES ENCRYPTION CODE
'''

def subBytes(state):
    for i in range(4):
        for j in range(4):
            state[j][i] = subWord(state[j][i])
    return state

def shiftRows(state):
    for i in range(4):
        for j in range(i):
            state[i].append(state[i][0])
            del state[i][0]
    return state

def mixColumns(state):
    # Make a copy of state to use for calculations
    tmp = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            tmp[i].append(int(state[i][j], 16))

    for i in range(4):
        state[0][i] = "{0:02x}".format(gmult(0x02, tmp[0][i]) ^ gmult(0x03, tmp[1][i]) ^ tmp[2][i] ^ tmp[3][i])
        state[1][i] = "{0:02x}".format(tmp[0][i] ^ gmult(0x02, tmp[1][i]) ^ gmult(0x03, tmp[2][i]) ^ tmp[3][i])
        state[2][i] = "{0:02x}".format(tmp[0][i] ^ tmp[1][i] ^ gmult(0x02, tmp[2][i]) ^ gmult(0x03, tmp[3][i]))
        state[3][i] = "{0:02x}".format(gmult(0x03, tmp[0][i]) ^ tmp[1][i] ^ tmp[2][i] ^ gmult(0x02, tmp[3][i]))

    return state    

# Plaintext and key are 128-bit hexadecimal strings
def encrypt(plaintext, key):
    # Initial state matrix and do the key expansion on the key to get the round keys
    state = getStateMatrix(plaintext)
    w = keyExpansion(key)
    
    state = addRoundKey(state, w[0 : Nb])

    for r in range(1, Nr):
        state = subBytes(state)
        state = shiftRows(state)
        state = mixColumns(state)
        addRoundKey(state, w[r * Nb : (r + 1) * Nb])

    state = subBytes(state)
    state = shiftRows(state)
    state = addRoundKey(state, w[Nr * Nb: (Nr + 1) * Nb])

    ciphertext = getTextFromState(state)
    return ciphertext

'''
    AES DECRYPTION CODE
'''

def invSubWord(w):
    sub = ""
    i = 0
    while i < len(w):
        sub += iS[int(w[i], 16)][int(w[i + 1], 16)]
        i += 2
    return sub

def invSubBytes(state):
    for i in range(4):
        for j in range(4):
            state[j][i] = invSubWord(state[j][i])
    return state

def invShiftRows(state):
    for i in range(4):
        for j in range(i):
            state[i].insert(0, state[i][-1])
            del state[i][-1]
    return state

def invMixColumns(state):
    # Make a copy of state to use for calculations
    tmp = [[],[],[],[]]
    for i in range(4):
        for j in range(4):
            tmp[i].append(int(state[i][j], 16))

    for i in range(4):
        state[0][i] = "{0:02x}".format(gmult(0x0e, tmp[0][i]) ^ gmult(0x0b, tmp[1][i]) ^ gmult(0x0d, tmp[2][i]) ^ gmult(0x09, tmp[3][i]))
        state[1][i] = "{0:02x}".format(gmult(0x09, tmp[0][i]) ^ gmult(0x0e, tmp[1][i]) ^ gmult(0x0b, tmp[2][i]) ^ gmult(0x0d, tmp[3][i]))
        state[2][i] = "{0:02x}".format(gmult(0x0d, tmp[0][i]) ^ gmult(0x09, tmp[1][i]) ^ gmult(0x0e, tmp[2][i]) ^ gmult(0x0b, tmp[3][i]))
        state[3][i] = "{0:02x}".format(gmult(0x0b, tmp[0][i]) ^ gmult(0x0d, tmp[1][i]) ^ gmult(0x09, tmp[2][i]) ^ gmult(0x0e, tmp[3][i]))

    return state   

def decrypt(ciphertext, key):
    state = getStateMatrix(ciphertext)
    w = keyExpansion(key)
    
    state = addRoundKey(state, w[Nr * Nb: (Nr + 1) * Nb])

    for r in range(Nr - 1, 0, -1):
        state = invShiftRows(state)
        state = invSubBytes(state)
        addRoundKey(state, w[r * Nb : (r + 1) * Nb])
        state = invMixColumns(state)

    state = invShiftRows(state)
    state = invSubBytes(state)
    state = addRoundKey(state, w[0 : Nb])

    plaintext = getTextFromState(state)
    return plaintext

'''
    KEY EXPANSION CODE 
'''

# rotWord moves the rotates left a byte and appends to the end of the word
def rotWord(w):
    w += w[:2]
    return w[2:]

# Implementation of key expansion algorithm from AES paper
# The implementations is for the 128-bit key version of AES
def keyExpansion(key):
    i = 0
    
    w = [0] * (Nb * (Nr + 1))

    while i < Nk:
        w[i] = key[8 * i : 8 * i + 8]
        i = i + 1

    i = Nk
    j = 0
    while (i < (Nb * (Nr + 1))):
        temp = w[i - 1]
        if i % Nk == 0:
            temp = xorWord(subWord(rotWord(temp)), Rcon[j])
            j = j + 1
        w[i] = xorWord(w[i - Nk], temp)
        i = i + 1
    return w
    
'''
    END KEY EXPANSION CODE
'''

testKey = "000102030405060708090a0b0c0d0e0f"#2b7e151628aed2a6abf7158809cf4f3c"
testInput = "00112233445566778899aabbccddeeff"#3243f6a8885a308d313198a2e0370734"
ciphertext = encrypt(testInput, testKey)
print(ciphertext)
plaintext = decrypt(ciphertext, testKey)
print(plaintext)
print(plaintext == testInput)
#print(hex(gmult(0x02, 0xdb) ^ gmult(0x03, 0x13) ^ 0x53 ^ 0x45))
#keyExpansion(testKey)
#xorWord('2b7e1516', '1b000000') = '307e1516'
#print(S[int('5', 16)][int('1', 16)])