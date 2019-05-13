import sys

def xor(inFile, outFile):
    # Read otp and store into array
    otpFile = open('onetimepad.txt', 'r')
    otp = otpFile.read().split('\n')
    otpFile.close()

    # Open file handles for both input and output files
    inFileHandle = open(inFile, 'rb')
    outFileHandle = open(outFile, 'wb')
    xorArray = []

    j = 0
    while True:
        # Read a byte
        byte = inFileHandle.read(1)
        
        if j < 26:
            xorArray.append(int.from_bytes(byte, 'big'))
            j += 1
            continue

        # If there is no byte, program reached end of file
        if not byte:
            break

        xorInt = int(otp[j]) ^ int.from_bytes(byte, 'big')
        xorArray.append(xorInt)

        j += 1
    outFileHandle.write(bytearray(xorArray))
    inFileHandle.close()
    outFileHandle.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Too few arguments")
        exit()
    inFilename = sys.argv[1]
    outFilename = sys.argv[2]
    xor(inFilename, outFilename)