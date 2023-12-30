mat1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]


for i in range(len(mat1)):
    add = 0
    row = mat1[i]
    for j in range(len(row)):
        add += row[j]
    print(f'Sum of row {i} : {add}')

for i in range(len(mat1)):
    add = 0
    row = mat1[i]
    for j in range(len(row)):
        if i==j:
            add += row[j]
    print(f'Sum of Column {i} : {add}')