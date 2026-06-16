'''mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat1[i][j] += mat2[i][j]

for row in mat1:
    for col in row:
        print(col, end = ' ')
    print()'''

x = {1, 2, 3}
print(list(x))

a = [1, 2, 3]
b = a
b.append(4)
print(a)

x = [1, 2, 3]
print(x * 2)