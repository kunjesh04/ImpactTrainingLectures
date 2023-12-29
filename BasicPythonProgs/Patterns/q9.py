''' 
   *
  **
 ***
****
'''

star = '*'
space = ' '
lines = int(input('Enter Number of lines : '))

for j in range(1, lines+1):
    print(space*(lines-j), star*(j))

