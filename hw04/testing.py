from hw04 import legendre, jacobi, propertiesOfS

legendreMatrix = []
with open("legendre.txt") as f:
    text = f.read()
    rows = text.split("\n")

    for row in rows:
        legendreMatrix.append(row.split("\t"))

print("Correct Legendre Matrix")
for i in range(len(legendreMatrix)):
    print(legendreMatrix[i][0], [int(k) for k in legendreMatrix[i][1:]])

for i in range(len(legendreMatrix)):
    for j in range(1, len(legendreMatrix[i])):
        print("Matrix at ({}, {}) = {}, legendre({},{}) = {}. Equal? -> {}".format(
            i,j,legendreMatrix[i][j], j, legendreMatrix[i][0], legendre(j, int(legendreMatrix[i][0])), legendre(j, int(legendreMatrix[i][0])) == int(legendreMatrix[i][j]))
            )

jacobiMatrix = []
with open("jacobi.txt") as f:
    text = f.read()
    rows = text.split("\n")

    for row in rows:
        jacobiMatrix.append(row.split("\t"))

print("Correct Jacobi Matrix")
for i in range(len(jacobiMatrix)):
    print(jacobiMatrix[i][0], [int(k) for k in jacobiMatrix[i][1:]])

for i in range(len(jacobiMatrix)):
    for j in range(1, len(jacobiMatrix[i])):
        print("Matrix at ({}, {}) = {}, jacobi({},{}) = {}. Equal? -> {}".format(
            i,j,jacobiMatrix[i][j], j, jacobiMatrix[i][0], jacobi(j, int(jacobiMatrix[i][0])), jacobi(j, int(jacobiMatrix[i][0])) == int(jacobiMatrix[i][j]))
            )


# for i in range(1, 31):
#     print(i, legendre(i, 13))

# for i in range(1, 31):
#     print(i, jacobi(i, 25))

# for i in range(1, 11):
#     propertiesOfS(i)
# propertiesOfS(100)