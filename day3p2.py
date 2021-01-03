# Using readlines()
inputList = open("inputDay3.txt", "r")
lines = inputList.readlines()
allColumns = len(lines[0]) - 2


def slopeTree(forest, tree):
    if forest[tree] == "#":
        return True
    return False


def slopeType(x, y):
    nrTree = 0
    columnSlope = 0
    linePos = 0
    for i in lines:
        if linePos % x == 0:
            if slopeTree(i, columnSlope):
                nrTree += 1
            columnSlope += y
            if columnSlope > allColumns:
                columnSlope = columnSlope - allColumns - 1
        linePos += 1
    return nrTree


print(slopeType(1, 1))
print(slopeType(1, 3))
print(slopeType(1, 5))
print(slopeType(1, 7))
print(slopeType(2, 1))
print(
    slopeType(1, 1)
    * slopeType(1, 3)
    * slopeType(1, 5)
    * slopeType(1, 7)
    * slopeType(2, 1)
)
