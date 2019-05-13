'''
    This file contains functions used for operating on permutations
'''

import copy
import random

# Determines of two lists a and b are equal
def equalLists(a,b):
    for i in a:
        if i not in b:
            return False
    return True

# RemoveDuplicateCycles removes the duplicate cycles from turning cycle notation into list notation
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

# PermutationToCycle is a function that turns a list permutation into a cycle permutation
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

# CycleToPermutation is a function that turns a cycle notation permutation into list notation
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

# multPerm multiplies two list notation permutations together
def multPerm(p1, p2):
    # If they are not the same length they cannot be multiplied
    if len(p1) != len(p2):
        return None
    else:
        # Works by returning the list where both permutations are applied
        return [p1[p2[i] - 1] for i in range(len(p1))]

# multCyclePerm is a function that multiplies two permutations in cycle notation together
def multCyclePerm(p1, p2):
    # turn them into list cycles
    l1 = cycleToPermutation(p1)
    l2 = cycleToPermutation(p2)
    # do list cycle multiplication
    result = multPerm(l1, l2)
    return permutationToCycle(result)

# Test going from permutation to cycle and back by generating random ones and checking
# That doing the operation and reverse will be the same as the original
with open("listandcycletest.txt", "w") as f:
    for i in range(500):
        perm = [i for i in range(1,11)]
        random.shuffle(perm)
        permCycle = permutationToCycle(perm)
        permAgain = cycleToPermutation(permCycle)
        f.write("{} -> {} -> {} : Equal? -> {}\n".format(perm, permCycle, permAgain, perm == permAgain))

# Test multiplying permutations, mult in cycle and then mult in list and make sure the answer are the same
with open("multtest.txt", "w") as f:
    for i in range(500):
        listPerm1 = [i for i in range(1,11)]
        listPerm2 = [i for i in range(1,11)]
        random.shuffle(listPerm1)
        random.shuffle(listPerm2)    
        cyclePerm1 = permutationToCycle(listPerm1)
        cyclePerm2 = permutationToCycle(listPerm2)
        f.write("{} * {} = {} | {} * {} = {}: Equal? -> {}\n".format(listPerm1, listPerm2, multPerm(listPerm1, listPerm2), cyclePerm1,cyclePerm2, multCyclePerm(cyclePerm1, cyclePerm2), permutationToCycle(multPerm(listPerm1, listPerm2)) == multCyclePerm(cyclePerm1, cyclePerm2)))