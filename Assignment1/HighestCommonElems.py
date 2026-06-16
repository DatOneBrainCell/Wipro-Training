a = [1, 5, 10, 20]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80]
a = set(a)
b = set(b)
c = set(c)
d = a.intersection(b)
d = a.intersection(c)
d = list(d)
print(d)