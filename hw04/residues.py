def legendre(a, p):
    if a == 0:
        return 0
    else:
        ans = (a ** ((p - 1) // 2)) % p
        if ans == p - 1:
            return -1
        else:
            return ans

def jacobi(a, p):
    

for i in range(1, 31):
    print(i, legendre(i, 13))