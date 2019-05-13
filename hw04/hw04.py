import math

def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact = fact * i
    return fact

def sieveOfEratosthenes(n):
    numbers = [i for i in range(2, n + 1)]
    j = 0
    while j < len(numbers):
        s = 2
        p = numbers[j]
        while s * p - 2 < len(numbers):
            numbers[s * p - 2] = 0
            s = s + 1
        j = j + 1
        while j < len(numbers) and numbers[j] == 0:
            j = j + 1
    primes = []
    for i in range(len(numbers)):
        if numbers[i] != 0:
            primes.append(numbers[i])
    return primes

def findPrimeFactors(n):
    primes = sieveOfEratosthenes(n)
    primeFactors = []
    for p in primes:
        if n % p == 0:
            primeFactors.append(p)
    return primeFactors

def countPrimeFactors(n, primeFactors):
    e = []
    for i in primeFactors:
        j = 2
        count = 1
        while (i ** j) <= n:
            if n % (i ** j) == 0:
                count = count + 1
            j = j + 1
        e.append(count)
    return sum(e), e

def propertiesOfS(n):
    size = factorial(n)
    primeFactors = findPrimeFactors(size)
    numFactors, exponentsOfFactors = countPrimeFactors(size, primeFactors)
    print("Size of S{} : {}".format(n, size))
    print("Prime Factorization of {}! : ".format(n), end='')
    for i in range(len(primeFactors)):
        print("({}**{})".format(primeFactors[i], exponentsOfFactors[i]), end='')
    print("", flush=True)
    print("Number of factors of {}! : {}\n".format(n, numFactors))

def prime(p):
    for i in range(2, math.floor(math.sqrt(p))):
        if p % i == 0:
            return False
    return True

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
    primeFactors = findPrimeFactors(p)
    _, exponents = countPrimeFactors(p, primeFactors)
    result = 1
    for i in range(len(primeFactors)):
        result = result * (legendre(a, primeFactors[i]) ** exponents[i])
    return result