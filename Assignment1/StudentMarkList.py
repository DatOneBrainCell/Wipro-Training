studs = [["Andrew", 92, 72, 64],
         ["Benjamin", 87, 63, 91],
         ["Charlamagne", 83, 94, 67],
         ["Joan", 75, 93, 86]]

for stud in studs:
  print(stud)

newList = []

for stud in studs:
  name = stud[0]
  totalMarks = sum(stud[1:])
  newList.append([name, totalMarks])

high = 0
topStud = ""

for stud in newList:
  if stud[1] > high:
    topStud = stud[0]
    high = stud[1]

print("The one with the highest mark of ", high," is ", topStud)