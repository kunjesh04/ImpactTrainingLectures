mat1 = [
    [1,2,3, 4, 5],
    [4,5,6, 7, 8],
    ]
mat2 = [
    [9,8,7, 6, 5],
    [6,5,4, 3,2],
]

cctd = []
for i in range(len(mat1)):
    row_1 = mat1[i]
    row_2 = mat2[i]
    row_final = []
    for m in range(len(row_1)):
        sum = str(row_1[m]) + str(row_2[m])
        row_final.append(int(sum))
    cctd.append(row_final)


print('Matrix 1:')
for row in mat1:
    print(row) 
print('\n')

print('Matrix 2:')
for row in mat2:
    print(row) 
print('\n')

print('Concatenated Matrix:')
for row in cctd:
    print(row) 
        