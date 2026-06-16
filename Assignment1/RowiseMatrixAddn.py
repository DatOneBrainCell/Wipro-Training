mat1 = [[2, 4, 6], [1, 2, 3]]
mat2 = [[1, 2, 3], [2, 4, 6]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat1[i][j] += mat2[i][j]

for row in mat1:
    for col in row:
        print(col, end = ' ')
    print()