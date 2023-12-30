matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

# matrix1 = [
#     [1,2],
#     [3,4],
#     ]
# matrix2 = [
#     [1,2],
#     [3,4],
# ]

multiplied = []

for i in range(len(matrix1)):
    row1 = matrix1[i]
    mult_row = []

    for l in range(len(row1)):
        final_sum = 0
        sum = 0
        col = []
        for row in matrix2:
            col.append(row[l])
        # print(col)
        for k in range(len(row1)):
            a = row1[k]
            b = col[k]
            sum += a*b
            # print(a, b, sum)
        final_sum += sum
        # print(f'Final sum appended : {final_sum}')
        mult_row.append(final_sum)
    multiplied.append(mult_row)



print('Matrix 1:')
for row in matrix1:
    print(row) 
print('\n')

print('Matrix 2:')
for row in matrix2:
    print(row) 
print('\n')

print('Multiplied:')
for row in multiplied:
    print(row)     