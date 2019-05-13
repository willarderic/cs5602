"""
    This file generates files with random polynomials to be used in testing
"""
import random

# Create a list of random polynomials and save it to a file
# The coefficients of the polynomials are CSVs and each polynomial is separated by a new line
with open("randomPolynomials.txt", "w+") as f:
    for i in range(15):
        degree = random.randint(10,20)
        for j in range(degree):
            f.write(str(random.randint(0, 100)))
            if j < degree - 1:
                f.write(",")
        if i < 14:
            f.write("\n")

# Generate random data for the division function and save it to a file
# The coeffeicients of the polynomials are CSVs and dividend/divisor's are separated by ":"
# each pair is separated by a new line character
with open("polyDividendsAndDivisors.txt", "w+") as f:
    for i in range(15):
        # dividend will have a higher degree than divisor to make division more interesting
        degreeDividend = random.randint(10,20)
        degreeDivisor = random.randint(2,10)
        for j in range(degreeDividend):
            f.write((str(random.randint(0,100))))
            if j < degreeDividend - 1:
                f.write(",")
        f.write(":")
        for j in range(degreeDivisor):
            f.write((str(random.randint(0,10))))
            if j < degreeDivisor - 1:
                f.write(",")
        if i < 14:
            f.write("\n")