outputFile = 'WILLARDProb4File6.txt'
filenamePrefix = 'WILLARDProb4File{}.bin'


def readData(filename):
    data = []
    with open(filename, 'rb') as f:
        j = 0
        while True:
            byte = f.read(1)
            
            if j < 26:
                j += 1
                continue

            if not byte:
                return data

            i = int.from_bytes(byte, 'big')
            data.append(chr(i))
    
def countCharOccurences(data):
    counts = {}
    for i in range(len(data)):
        char = data[i]
        if char not in counts.keys():
            counts[char] = 1
        else:
            counts[char] += 1
    return counts


def countBigramOccurences(data):
    countBigrams = {}
    for i in range(len(data)):
        if i < len(data) - 1:
            bigram = data[i] + data[i +1]
            if bigram not in countBigrams:
                countBigrams[bigram] = 1
            else:
                countBigrams[bigram] += 1
    return countBigrams

def countTrigramOccurences(data):
    countTrigrams = {}
    for i in range(len(data)):
        if i < len(data) - 2:
            trigram = data[i] + data[i + 1] + data[i + 2]
            if trigram not in countTrigrams:
                countTrigrams[trigram] = 1
            else:
                countTrigrams[trigram] += 1
    return countTrigrams

with open(outputFile, "w+") as of:
    for i in range(1, 6):
        data = readData(filenamePrefix.format(i))
        countChars = countCharOccurences(data)
        countBigrams = countBigramOccurences(data)
        countTrigrams = countTrigramOccurences(data)
        k = 0
        for key, val in sorted(countChars.items(), key=lambda item: item[1], reverse = True):
            if k > len(countChars):
                of.write("ord(???) count(????)\n")
            else:
                of.write("ord({:03}) count({:04})\n".format(ord(key), val))
            if k >= 25:
                break
            k += 1
        k = 0
        for key, val in sorted(countBigrams.items(), key=lambda item: item[1], reverse = True):
            of.write("ord({:03}) ord({:03}) count({:04})\n".format(ord(key[0]), ord(key[1]), val))
            if k >= 9:
                break
            k += 1
        k = 0
        for key, val in sorted(countTrigrams.items(), key=lambda item: item[1], reverse = True):
            of.write("ord({:03}) ord({:03}) ord({:03}) count({:04})\n".format(ord(key[0]), ord(key[1]), ord(key[2]), val))
            if k >= 9:
                break
            k += 1
