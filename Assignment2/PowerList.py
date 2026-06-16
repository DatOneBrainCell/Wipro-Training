listThing = [1, 2, 3]
subsetList = [[]]

for element in listThing:
    newSubsets = []
    for subset in subsetList:
        newSubset = []
        for item in subset:
            newSubset.append(item)
        newSubset.append(element)
        newSubsets.append(newSubset)

    for s in newSubsets:
        subsetList.append(s)

print(subsetList)