from collections import OrderedDict
import operator

letterFrequency = {}
with open('letterFrequency.tsv') as f:
    text = f.read()
    letterAndFreq = text.split('\n')
    for i in letterAndFreq:
        tmp = i.split('\t')
        letterFrequency[tmp[0]] = float(tmp[1])

cipherText = '53$$%305))6*;4826)4$.)4$);806*;48%8@60))85;;]8*;:$*8%83(88)5*%;46(;88*96*?;8)*$(;485);5*%2:*$(;4956*2(5*-4)8@8*;4069285);)6%8)4$$;1($9;48081;8:8$1;48%85;4)485%528806*81($9;48;(88;4($?34;48)4$;161;:188;$?;'

cipherTextCount = OrderedDict()
bigramCount = OrderedDict()
trigramCount = OrderedDict()
for i in range(len(cipherText)):
    ch1 = cipherText[i]
    if i < len(cipherText) - 2:
        ch2 = cipherText[i + 1]
    if i < len(cipherText) - 3:
        ch3 = cipherText[i + 2]
    
    if ch1 in cipherTextCount.keys():
        cipherTextCount[ch1] += 1
    else:
        cipherTextCount[ch1] = 1
    
    bi = ch1 + ch2
    if bi in bigramCount.keys():
        bigramCount[bi] += 1
    else:
        bigramCount[bi] = 1

    tri = bi + ch3
    if tri in trigramCount.keys():
        trigramCount[tri] += 1
    else:
        trigramCount[tri] = 1

for key in cipherTextCount.keys():
    cipherTextCount[key] /= len(cipherText)
    cipherTextCount[key] *= 100
    cipherTextCount[key] = round(cipherTextCount[key], 2)

for key in bigramCount.keys():
    bigramCount[key] /= len(cipherText)
    bigramCount[key] *= 100
    bigramCount[key] = round(bigramCount[key], 2)

for key in trigramCount.keys():
    trigramCount[key] /= len(cipherText)
    trigramCount[key] *= 100
    trigramCount[key] = round(trigramCount[key], 2)

print(letterFrequency)

print("Top Letters")
i = 0
for key, value in sorted(cipherTextCount.items(), key=lambda item: item[1], reverse = True):
    print("\t", key, value)
    i += 1
    if i > 10:
        break

print("Top Bigrams")
i = 0
for key, value in sorted(bigramCount.items(), key=lambda item: item[1], reverse = True):
    print("\t", key, value)
    i += 1
    if i > 5:
        break

print("Top Trigrams")
i = 0
for key, value in sorted(trigramCount.items(), key=lambda item: item[1], reverse = True):
    print("\t", key, value)
    i += 1
    if i > 5:
        break

print(cipherText[:62])
print(cipherText[61:123])
print(cipherText[123:185])
print(cipherText[185:])
print()
while True:
    letter = str(input('Letter to be replaced: '))
    replacement = str(input('Replacement: '))
    cipherText = cipherText.replace(letter, replacement)
    print()
    print(cipherText[:62])
    print(cipherText[61:123])
    print(cipherText[123:185])
    print(cipherText[185:])
    print()
