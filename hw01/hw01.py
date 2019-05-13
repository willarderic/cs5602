import copy

def equalLists(a,b):
    for i in a:
        if i not in b:
            return False
    return True

# 7
def removeDuplicateCycles(cycles):
    # Remove duplicate cycles so that the cycle notation has the least amount of lists in it
    keep = []
    for i in cycles:
        add = True
        for j in keep:
            if equalLists(i, j):
                add = False
        if add == True:
            keep.append(i)
    return keep
                

# 7
def permutationToCycle(permutation):
    permuting = True
    # Make a list of lists of tracking cycles that will happen when applying permutations
    cycles = [[i + 1] for i in range(len(permutation))]
    # Make a list of incrementing numbers to be permuted
    permuted = [i + 1 for i in range(len(permutation))]
    while permuting:
        # continously permute until the cycles don't get anymore elements added to them
        previousCycles = copy.deepcopy(cycles)
        permuted = [permutation[i - 1] for i in permuted]
        for i in range(len(cycles)):
            if permuted[i] not in cycles[i]:
                cycles[i].append(permuted[i])
        if previousCycles == cycles:
            permuting = False
    # There will be duplicate cycles so they must be removed
    return removeDuplicateCycles(cycles)

# 8
def cycleToPermutation(cycles):
    # Find the size of the permutation
    totalLength = 0
    for cycle in cycles:
        totalLength = totalLength + len(cycle)
    # Create a list of the size of the permutation
    permutation = [None] * totalLength
    # Iterate through the cycles one at a time, and also iterate through the cycle's element
    # Insert in the permutation list at the index of the element the next element mod size (to wrap around)
    for cycle in cycles:
        for i in range(len(cycle)):
            permutation[cycle[i] - 1] = cycle[(i + 1) % len(cycle)]
    return permutation

# cycleToPermutation([[1,3],[2,5,4]])
def removeLeadingZero(p):
    if p and p[0] == 0:
        del p[0]
    return p

def polyAdd(p, q):
    if len(p) == len(q):
        return removeLeadingZero([p[i] + q[i] for i in range(len(p))])
    elif len(p) > len(q):
        newPoly = [0] * len(p)
        for i in range(len(p)):
            newPoly[i] = newPoly[i] + p[i]
        for i in range(len(p) - len(q), len(p)):
            newPoly[i] = newPoly[i] + q[i - (len(p) - len(q))]
        return removeLeadingZero(newPoly)
    elif len(p) < len(q):
        newPoly = [0] * len(q)
        for i in range(len(q)):
            newPoly[i] = newPoly[i] + q[i]
        for i in range(len(q) - len(p), len(q)):
            newPoly[i] = newPoly[i] + p[i - (len(q) - len(p))]
        return removeLeadingZero(newPoly)

def polySub(p, q):
    return polyAdd(p, [-i for i in q])
    
def scalePoly(p, n):
    return [i * n for i in p]

def shiftPoly(p, n):
    i = 0
    while i < n:
        p.append(0)
        i += 1
    return p

# 5
def polyDiv(dividend, divisor):
    dividend = removeLeadingZero(dividend)
    divisor = removeLeadingZero(divisor)
    q = []
    r = dividend
    while (r and r[0] != 0) and len(r) >= len(divisor):
        t = r[0] / divisor[0]
        q.append(t)
        r = polySub(r, shiftPoly(scalePoly(divisor, t), len(r) - len(divisor)))
    return [round(i, 4) for i in q], [round(i, 4) for i in r]

def polyMod(p, m):
    q, r = polyDiv(p, m)
    return r

def polyGCD(p, q):
    if (len(q) == 1 and q[0] == 0) or len(q) == 0:
        return p
    else:
        return polyGCD(q, polyMod(p,q))

def multPerm(p1, p2):
    if len(p1) != len(p2):
        return None
    else:
        return [p1[p2[i] - 1] for i in range(len(p1))]


print("~~~~~~ MULTIPLYING PERMUTATIONS ~~~~~~\n")
print("[5,3,7,6,1,9,2,4,8,10]*[9,6,2,4,10,3,5,8,7,1] = {}".format(multPerm([5,3,7,6,1,9,2,4,8,10],[9,6,2,4,10,3,5,8,7,1])))
print("[11,5,2,8,6,9,3,7,4,10,1]*[3,6,1,10,4,11,8,2,9,7,5] = {}\n".format(multPerm([11,5,2,8,6,9,3,7,4,10,1],[3,6,1,10,4,11,8,2,9,7,5])))

print("~~~~~~ DIVIDING POLYNOMIALS ~~~~~~\n")
print("[8,0,15,18,2,4,17,19,18,1,12,11] / [1,4,2,8] = {}".format(polyDiv([8,0,15,18,2,4,17,19,18,1,12,11],[1,4,2,8])))
print("[11,2,17,16,13,10,17,8,16,6,0,18] / [3,6,6,4] = {}\n".format(polyDiv([11,2,17,16,13,10,17,8,16,6,0,18],[3,6,6,4])))

print("~~~~~~ POLYNOMIAL GCD ~~~~~~\n")
print("GCD([11,14,17,19,18,10,16,15,9,13,12,9], [8,13,8,20,0,12,5,3,17,13,19]) = {}".format(polyGCD([11,16,17,19,18,10,16,15,9,13,12,9], [8,13,8,20,0,12,5,3,17,13,19])))
print("GCD([0,5,2,3,8,19,12,20,6,19,0,3], [6,8,8,7,5,6,3,4,6,5,8]) = {}\n".format(polyGCD([0,5,2,3,8,19,12,20,6,19,0,3], [6,8,8,7,5,6,3,4,6,5,8])))

print("~~~~~~ PERMUTATION TO CYCLE NOTATION ~~~~~~\n")
print("[5,3,7,6,1,9,2,4,8,10] = {}".format(permutationToCycle([5,3,7,6,1,9,2,4,8,10])))
print("[11,5,2,8,6,9,3,7,4,1,10] = {}".format(permutationToCycle([11,5,2,8,6,9,3,7,4,1,10])))
print("[3,6,1,10,4,11,8,2,9,7,5] = {}\n".format(permutationToCycle([3,6,1,10,4,11,8,2,9,7,5])))

print("~~~~~~ CYCLE NOTATION TO PERMUTATION ~~~~~~\n")
print("[[1, 3], [5, 4, 10, 7, 8, 2, 6, 11], [9]] = {}".format(cycleToPermutation([[1, 3], [5, 4, 10, 7, 8, 2, 6, 11], [9]])))
print("[[1, 11], [4, 8, 7, 3, 2, 5, 6, 9], [10]] = {}".format(cycleToPermutation([[1, 11], [4, 8, 7, 3, 2, 5, 6, 9], [10]])))
print("[[1, 5], [2, 3, 7], [8, 4, 6, 9], [10]] = {}".format(cycleToPermutation([[1, 5], [2, 3, 7], [8, 4, 6, 9], [10]])))