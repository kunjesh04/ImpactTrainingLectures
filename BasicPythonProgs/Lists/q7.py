matrix = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

'''
Dynamic Matrix
rows = int(input('Number of Rows : '))
cols = int(input('Number of Columns : '))
for i in range(rows):
    row_i = []
    for j in range(cols):
        num = int(input(f'Enter Element at row {i} and column {j} : '))
        row_i.append(num)
    matrix.append(row_i)
'''

print('Original Matrix:')
for row in matrix:
    print(row)

transposed = []
for i in range(len(matrix[0])):
    inner_list = []
    for j in range(len(matrix)):
        inner_list.append(matrix[j][i])
    transposed.append(inner_list)
print('\n')      
print('Transposed')
for row in transposed:
    print(row)