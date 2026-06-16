lis = [10, -5, 20, -1, 0, -8]
i = 0
while i < len(lis):
  if lis[i] < 0:
    lis.pop(i)
  else:
    i += 1;
print(lis)