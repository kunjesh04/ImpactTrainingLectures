def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

num1 = int(input('Enter Number 1 : '))
num2 = int(input('Enter Number 2 : '))
operator = input('Enter Operator [+, *, /, -] : ')
if (operator == '+'):
    print(f' {num1} {operator} {num2} = {add(num1, num2)}')
elif (operator == '-'):
    print(f' {num1} {operator} {num2} = {subtract(num1, num2)}')
elif (operator == '*'):
    print(f' {num1} {operator} {num2} = {multiply(num1, num2)}')
elif (operator == '/'):
    print(f' {num1} {operator} {num2} = {divide(num1, num2)}')
else :
    print('Pls Enter suitable operators : [+, *, /, -]')
