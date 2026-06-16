def RotateLeft(lst, k):
    k = k % len(lst)
    newList = []
    for i in range(k, len(lst)):
        newList.append(lst[i])
    for i in range(0, k):
        newList.append(lst[i])
    return newList

print("Rotated List:", RotateLeft([1, 2, 3, 4, 5], 2))