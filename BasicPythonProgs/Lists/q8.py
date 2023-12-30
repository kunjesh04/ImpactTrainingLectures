mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
mat2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

added = []
for i in range(len(mat1)):
    row_1 = mat1[i]
    row_2 = mat2[i]
    row_final = []
    for m in range(len(row_1)):
        sum = row_1[m] + row_2[m]
        row_final.append(sum)
    added.append(row_final)

print('Matrix 1:')
for row in mat1:
    print(row) 
print('\n')

print('Matrix 2:')
for row in mat2:
    print(row) 
print('\n')

print('Addition:')
for row in added:
    print(row) 
        