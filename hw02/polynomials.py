"""
    This file contains all of the functions needed for polynomial arithmetic
"""

# Function removes the leading zero of a polynomial p
# Returns the polynomial, without the leading zero (if there is one)
def removeLeadingZero(p):
    if p and p[0] == 0:
        del p[0]
    return p

def removeLeadingZeros(p):
    while p and p[0] == 0:
        del p[0]
    return p

# Takes two polynomials p and q, and adds them together
# returns the sum of the polynomials
def polyAdd(p, q):
    # If the lengths of p and q are equal, we can directly add the elements and return the result
    if len(p) == len(q):
        return [p[i] + q[i] for i in range(len(p))]
    # If p has more elements that q, then add the elements of q to the lower elements of p
    elif len(p) > len(q):
        for i in range(len(q)):
            p[i + (len(p) - len(q))] += q[i]
        return p
    # If q has more elements that p, then add the elements of p to the lower elements of q      
    elif len(p) < len(q):
        for i in range(len(p)):
            q[i + (len(p) - len(q))] += p[i]
        return q

# Takes two polynomials p and q and substracts q from p (p - q)
def polySub(p, q):
    return polyAdd(p, [-i for i in q])

# Multiply the polynomial p by a scalar n
def scalePoly(p, n):
    return [i * n for i in p]

# Pads the polynomial with zeros on the right to increase the degree
def shiftPoly(p, n):
    if n > 0:
        p.extend([0] * n)
    return p

# Takes polynomials p and q and returns an m and r such that p = m*q + r
def polyDiv(p, q):
    if len(q) == 0 or sum([i**2 for i in q]) == 0:
        return None
    q = removeLeadingZeros(q)
    # Polynomial that divides 
    m = []
    # Remainder starts out as full polynomial and is slowly reduced
    r = p
    while r and len(r) >= len(q):
        # Find what the factor to make the first element that is left zero
        t = r[0] / q[0]
        # Calculate new remainder
        if t == 0:
            r = r[1:]
        else:
            m.append(t)
            r = polySub(r, shiftPoly(scalePoly(q, t), len(r) - len(q)))
            # Round to 8 point precision to counter floating point number errors
            r = [round(i, 8) for i in r]
    return m, r

# Takes polynomials p and mod, does modulus operation for polynomials
def polyMod(p, mod):
    _, r = polyDiv(p, mod)
    return r

# Finds the greatest common divisor of polynomial p and q
def polyGCD(p, q):
    if (len(q) == 1 and q[0] == 0) or len(q) == 0:
        return p
    else:
        return polyGCD(q, polyMod(p,q))

# Takes two polynomials p and q, and returns the product of the multiplication of the two
def polyMult(p, q):
    # If the length of one polynomial is zero, return the polynomial that is not empty
    if len(p) == 0 or len(q) == 0:
        p.extend(q)
        return p
    # If p or q are size one, they are just a scalar, so return the scaled polynomial
    if len(p) == 1:
        return scalePoly(q, p[0])
    elif len(q) == 1:
        return scalePoly(p, q[0])
    # Create a new list that is of size (len(p) + len(q) - 1) to make sure 
    # the coefficients correspond to the correct degree after division
    prod = [0] * (len(p) + len(q) - 1)
    for i in range(len(p)):
        for j in range(len(q)):
            prod[i + j] = prod[i + j] + p[i] * q[j]
    return prod

