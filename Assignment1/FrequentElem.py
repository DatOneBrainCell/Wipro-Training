high = 0
highNum = 0
anotherListOnceAgain = [1, 3, 3, 2, 1, 1, 4, 3, 3]
for i in range(1, max(anotherListOnceAgain)+1):
  temp = anotherListOnceAgain.count(i)
  if temp > high:
    high = temp
    highNum = i
print(highNum)