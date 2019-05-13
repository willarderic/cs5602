prelimPrefix = 'EncryptedPrelims/Prelim2Num'
outputDir = 'decryptedPrelims/Prelim2Num'

for i in range(15):
    otpFile = open('onetimepad.txt', 'r')
    otp = otpFile.read().split('\n')
    otpFile.close()
    if i < 10:
        encryptedPrelim = open(prelimPrefix + '{}{}.bin'.format(0, i), 'rb')
        decryptedPrelim = open(outputDir + '{}{}.txt'.format(0, i), 'w+')
    else:
        encryptedPrelim = open(prelimPrefix + '{}.bin'.format(i), 'rb')
        decryptedPrelim = open(outputDir + '{}.txt'.format(i), 'w+')
    chunkSize = 1
    j = 0
    while True:
        byte = encryptedPrelim.read(chunkSize)
        
        if not byte:
            break
          
        writeByte = int(otp[j]) ^ int.from_bytes(byte, 'big')
        decryptedPrelim.write(str(chr(writeByte)))
        # print(int.from_bytes(byte, 'big'))
        j += 1
    encryptedPrelim.close()
    decryptedPrelim.close()