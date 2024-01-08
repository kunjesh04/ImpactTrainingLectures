# WAP to no. of digits in given number

num = int(input('Enter any digit number : '))
print('Using in-built function')
print(len(str(num)))

print('Without Using in-built function')

digits = 0

while num!=0:    
    num = num//10
    digits+=1

print(digits)