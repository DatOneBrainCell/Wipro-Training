l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
newList = []

for i in range (0,len(l)):
    if i%3 == 0:
        newList.append(l[i : i + n])

for elem in newList:
    print(elem)