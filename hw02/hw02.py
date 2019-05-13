"""
    This file runs the polynomial gcd, division, and modulus functions and saves their results into a file to be verified
    as working correctly
"""
from polynomials import *

outputFolder = "./outputs/"

# Read in the polynomials we want to use to for division
# Polynomial coefficitents are CSVs and the dividends/divisors are separated by :
# Each pair is separated by a new line
file = open("polyDividendsAndDivisors.txt")
content = file.read()
dividends = []
divisors = []
lines = content.split("\n")
for k in range(len(lines)):
    polynomials = lines[k].split(":")
    polynomials[0] = [float(i) for i in polynomials[0].split(",")]
    polynomials[1] = [float(i) for i in polynomials[1].split(",")]
    dividends.append(polynomials[0])
    divisors.append(polynomials[1])
file.close()

# Read in random polynomials file to use as data for GCD
# Coefficients of polynomails are CSVs and each polynomial is separated by a new line
file = open("randomPolynomials.txt")
content = file.read()
polynomials = [i.split(",") for i in content.split("\n")]

# Convert to floats
for i in range(len(polynomials)):
    polynomials[i] = [float(j) for j in polynomials[i]]

# Open files to save data to
quotientAndRemainders = open(outputFolder + "quotientAndRemainders.txt","w+")
modulus = open(outputFolder + "modulus.txt", "w+")
gcd = open(outputFolder + "gcd.txt", "w+")
checkDivision = open(outputFolder + "checkDivision.txt", "w+")

# Run the code and save the results to each file they belong to
for k in range(len(dividends)):

    # Run division function and save results
    m, r = polyDiv(dividends[k], divisors[k])
    for i in range(len(m)):
        quotientAndRemainders.write(str(m[i]))
        if i < len(m) - 1:
            quotientAndRemainders.write(",")
    quotientAndRemainders.write(":")
    for i in range(len(r)):
        quotientAndRemainders.write(str(r[i]))
        if i < len(r) - 1:
            quotientAndRemainders.write(",")
    quotientAndRemainders.write("\n")
    
    # Do the reverse of the division operation and save the result to check
    # if division worked correctly
    check = polyAdd(polyMult(divisors[k], m), r)
    for i in range(len(check)):
        checkDivision.write(str(check[i]))
        if i < len(check) - 1:
            checkDivision.write(",")
    checkDivision.write("\n")

    # Take the modulus of polynomials and save result to a file
    mod = polyMod(dividends[k], divisors[k])
    for i in range(len(mod)):
        modulus.write(str(mod[i]))
        if i < len(mod) - 1:
            modulus.write(",")
    modulus.write("\n")

# Run the GCD code and save it to a file
# Not ran with others because it uses different data
for k in range(len(polynomials) - 1):
    g = polyGCD(polynomials[k], polynomials[k + 1])
    for i in range(len(g)):
        gcd.write(str(g[i]))
        if i < len(g) - 1:
            gcd.write(",")
    gcd.write("\n")

# Close all the file handlers
quotientAndRemainders.close()
modulus.close()
gcd.close()
checkDivision.close()