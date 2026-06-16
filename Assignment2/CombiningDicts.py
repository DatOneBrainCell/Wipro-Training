dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict3 = {}

for k in dict1.keys():
    dict3[k] = dict1[k]

for k in dict2:
    dict3[k] = dict2[k]

print(dict3)