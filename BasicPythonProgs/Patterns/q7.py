'''
Pattern : 
****
***
**
*

'''

lines = int(input('Enter number of Lines :'))

for i in range(lines+1):
    for j in range(lines, i, -1):
        print('*', end=' ')
    print('')

'''
Other Method:
for i in range(lines, 1, -1):
    print('*'*i)

'''