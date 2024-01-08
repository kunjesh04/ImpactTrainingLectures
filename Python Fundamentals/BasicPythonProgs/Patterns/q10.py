'''
print the following pattern..

    *
  *-*-* 
*-*-*-*-* 
  *-*-* 
    *


'''

star = '* '
space = ' '
lines = int(input("enter number of lines"))

for i in range(1, (lines//2)+2):
    print(space*(lines-(i*2-1)), star*(i*2-1))
for j in range((lines-1)//2, 0, -1):
    print(space*(lines-(j*2-1)), star*(j*2-1))
    