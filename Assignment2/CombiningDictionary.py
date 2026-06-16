keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

res = {}
for i in range(len(keys)):
    res[keys[i]] = values[i]

print("Dictionary: ", res)