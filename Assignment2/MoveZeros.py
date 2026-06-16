def MoveZeros(lis):
    finalList = []
    zeroCount = 0

    for num in lis:
        if num!= 0:
            finalList.append(num)
        else:
            zeroCount = zeroCount + 1

    for i in range(zeroCount):
        finalList.append(0)

    return finalList

li = [0, 1, 0, 3, 12]
print(MoveZeros(li))