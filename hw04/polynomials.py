class FiniteFieldPolynomial:
    
    def __init__(self, p = [], m = 2):
        self.p = p
        self.m = m
    
    def scale(self, n):
        return FiniteFieldPolynomial([n * i for i in self.p], self.m)

    # Function to add the polynomial in the instance of this class to another polynomial
    # Returns the result of the addition
    def add(self, q):
        self.__checkConditions(q)
        # If p and q are the same length, directly add each element
        if len(self.p) == len(q.p):
            return FiniteFieldPolynomial([(self.p[i] + q.p[i]) % self.m for i in range(len(q.p))], self.m)
        # If one polynomial is shorter than the other, add the elements of the shorter polynomial
        # to the longer polynomial offset by an amount based on their sizes
        elif len(self.p) > len(q.p):
            for i in range(len(q.p)):
                ans = FiniteFieldPolynomial(self.p, self.m)
                ans.p[i + (len(self.p) - len(q.p))] = (self.p[i + (len(self.p) - len(q.p))] + q.p[i]) % self.m
            return ans
        elif len(self.p) < len(q.p):
            for i in range(len(self.p)):
                ans = FiniteFieldPolynomial(q, self.m)
                ans.p[i + (len(q.p) - len(self.p))] = (q.p[i + (len(q.p) - len(self.p))] + self.p[i]) % self.m
            return ans

    # Function to subtract the polynomial in the instance of this class to another polynomial
    # Returns the result of the subtraction
    def sub(self, q):
        r = q.scale(-1)
        return self.add(r)
    
    # Function to multiply the polynomial in the instance of this class to another polynomial
    # Returns the result of the multiplication
    def mult(self, q):
        self.__checkConditions(q)
        # If either of the lists representing the polynomial is of length zero
        # just return the one that is not empty
        if len(self.p) == 0 or len(q.p) == 0:
            tmp = FiniteFieldPolynomial([i for i in self.p], self.m)
            tmp.p.extend(q.p)
            return tmp
        # If either of the lists representing the polynomial is of length one,
        # You are essentially just multiplying by a scalar, so use the scale function
        elif len(self.p) == 1:
            return q.scale(self.p[0]).p, self.m
        elif len(q.p) == 1:
            return self.scale(q.p[0]).p, self.m
        # For actually multiplying, create a list with the size where the length is the sum of the
        # lengths of each polynomial - 1 to represent the largest degree coming from the multiplication
        prod = [0] * (len(self.p) + len(q.p) - 1)
        # Here, multiply each element of q by the first element of p, then the second, etc...
        # Then add those in the position in the product that corresponds to the degree of the 
        # multiplication (essentially combining like terms)
        for i in range(len(self.p)):
            for j in range(len(q.p)):
                prod[i + j] = (prod[i + j] + (self.p[i] * q.p[j]) % self.m) % self.m
        return FiniteFieldPolynomial(prod, self.m)

    # Function to divide the polynomial in the instance of this class to another polynomial
    # Returns the result of the division
    def div(self, q):
        # Implementation of polynomial long division 
        # https://en.wikipedia.org/wiki/Polynomial_long_division
        self.__checkConditions(q)
        if len(q.p) == 0 or sum([i**2 for i in q.p]) == 0:
            raise ZeroDivisionError("Trying to divide polynomial by 0")
        q.p = self.__removeLeadingZeros(q.p)
        n = []
        r = FiniteFieldPolynomial(self.p, self.m)
        while r.p and len(r.p) >= len(q.p):
            t = r.p[0] // q.p[0]
            n.append(t)
            tmp = FiniteFieldPolynomial([i for i in q.p], self.m)
            tmp = tmp.scale(t)
            l = self.__shift(tmp.p, len(r.p) - len(q.p))
            r = r.sub(l)
            r.p = self.__removeLeadingZero(r.p)
        return FiniteFieldPolynomial(n, self.m), r
 
    # Function to find the modulus of the polynomial in the instance of this class and another polynomial
    # Returns the remainder (modulus)
    def mod(self, q):
        _, r = self.div(q)
        return r
    
    # Function to find the GCD of the polynomial in the instance of this class and another polynomial
    # returns g = GCD(self.p, q)
    def gcd(self, q):
        if (len(q.p) == 1 and q.p[0] == 0) or len(q.p) == 0:
            return self
        else:
            return q.gcd(self.mod(q))

    def __checkConditions(self, q):
        if not isinstance(q, FiniteFieldPolynomial):
            raise TypeError("Parameter is not type of FiniteFieldPolynomial")
        if self.m != q.m:
            raise ValueError("FiniteFieldPolynomial's do not have same moduli")

    def __removeLeadingZero(self, l):
        if l and l[0] == 0:
            del l[0]
        return l

    def __removeLeadingZeros(self,l):
        while l and l[0] == 0:
            del l[0]
        return l

    def __shift(self, l, n):
        if n > 0:
            l.extend([0] * n)
        return FiniteFieldPolynomial(l, self.m)

# This functions finds and returns the multiplicative inverse of a polynomial with coefficients 
# in integers mod 2. p is a polynomial and m is and irreducible polynomial
def multiplicativeInverseMod2(p, m):
    if not isinstance(p, FiniteFieldPolynomial) or not isinstance(m, FiniteFieldPolynomial):
            raise TypeError("Parameter is not type of FiniteFieldPolynomial")
    if p.m != m.m:
        raise ValueError("FiniteFieldPolynomial's do not have same moduli")
    t = FiniteFieldPolynomial([1], p.m)
    # Starting at i = 1
    i = 1
    while not polyIsZero(t.mod(m)):
        # Transform i into it's binary representation which can be converted into a polynomial representation
        # and used iterate through every element of the group to find p's inverse
        t = FiniteFieldPolynomial([int(n) for n in bin(i)[2:]], 2)
        # If the remainder without all the leading zeros is just the list with 1 in it, then 
        # the multiplication mod m equals 1 which means that the t is the inverse of p
        if removeLeadingZeros(p.mult(t).mod(m).p) == [1]:
            return t
        i += 1
    return None

def removeLeadingZeros(l):
        while l and l[0] == 0:
            del l[0]
        return l

def polyIsZero(p):
    ans = sum([i**2 for i in p.p])
    if ans == 0:
        return True
    return False

def isPolynomialPrimeMod2(p):
    if not isinstance(p, FiniteFieldPolynomial):
        raise TypeError("Parameter is not type of FiniteFieldPolynomial")
    i = 3
    t = FiniteFieldPolynomial([int(n) for n in bin(i)[2:]], 2)
    while len(t.p) < len(p.p):
        t = FiniteFieldPolynomial([int(n) for n in bin(i)[2:]], 2)
        q, r = p.div(t)
        if polyIsZero(r):
            return t, q, False
        i += 1
    return None, None, True

def checkResult(t, q, prime):
    if prime == False:
        print(t.p, q.p, prime)
    else:
        print(t,q,prime)

p = FiniteFieldPolynomial([1,1,1,1,1,1,1,1], 2)
t, q, prime = isPolynomialPrimeMod2(p)
checkResult(t, q, prime)
p = FiniteFieldPolynomial([1,0,1,1,1,1,1,1], 2)
t, q, prime = isPolynomialPrimeMod2(p)
checkResult(t, q, prime)
p = FiniteFieldPolynomial([1,1,0,1,1,1,1,1], 2)
t, q, prime = isPolynomialPrimeMod2(p)
checkResult(t, q, prime)
p = FiniteFieldPolynomial([1,1,1,0,1,1,1,1], 2)
t, q, prime = isPolynomialPrimeMod2(p)
checkResult(t, q, prime)
p = FiniteFieldPolynomial([1,1,1,1,0,1,1,1], 2)
t, q, prime = isPolynomialPrimeMod2(p)
checkResult(t, q, prime)
p = FiniteFieldPolynomial([1,1,1,1,1,0,1,1], 2)
t, q, prime = isPolynomialPrimeMod2(p)
checkResult(t, q, prime)
p = FiniteFieldPolynomial([1,1,1,1,1,1,0,1], 2)
t, q, prime = isPolynomialPrimeMod2(p)
checkResult(t, q, prime)
