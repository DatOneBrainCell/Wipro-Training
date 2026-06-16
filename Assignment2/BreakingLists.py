li = [1,2,3,4,5,6,7,8,9,10]

def BreakList(lis, n):
    subLists = []
    for i in range(0, len(lis), n):
        chunk = []
        for j in range(i, i + n):
            if j < len(lis):
                chunk.append(lis[j])
        subLists.append(chunk)
    return subLists

print("Chunks:", BreakList(li, 3))