''' 
****
 ***
  **
   *
'''

star = '*'
space = ' '
lines = int(input('Enter Number of lines : '))

for j in range(lines, 0, -1):
    print(space*(lines-j), star*(j))

