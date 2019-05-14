p = 127
q = 131
N = 16637
B = 12345

def encrypt(m, N, B):
    return (m * (m + B)) % N

print(encrypt(4410, N, B))