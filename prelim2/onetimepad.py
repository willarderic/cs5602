from random import randint

with open('onetimepad.txt', 'w+') as f:
    for i in range(10000):
        f.write(str(randint(0, 255)))
        if i < 9999:
            f.write('\n')