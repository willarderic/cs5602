import sys

def xor(file1, file2, outFile):
    # Open file handles for input and output files
    filehandle1 = open(file1, 'rb')
    filehandle2 = open(file2, 'rb')
    outFileHandle = open(outFile, 'wb')
    xorArray = []
    # Chunk size is one because the program XOR's one byte at a
    j = 0
    while True:
        # Read a byte
        if j < 26:
            byte = filehandle1.read(1)
            xorArray.append(int.from_bytes(byte, 'big'))
            j += 1
            continue
        
        byte1 = filehandle1.read(1)
        byte2 = filehandle2.read(1)
        # If there is no byte, program reached end of file
        if not byte1 or not byte2:
            break
        
        xorInt = int.from_bytes(byte1, 'big') ^ int.from_bytes(byte2, 'big')
        xorArray.append(xorInt)
        j += 1
    
    outFileHandle.write(bytearray(xorArray))
    filehandle1.close()    
    filehandle2.close()
    outFileHandle.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Too few arguments")
        exit()
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    outFilename = sys.argv[3]
    xor(filename1, filename2, outFilename)