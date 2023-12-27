# WAP to show working of simple calculator 

num1 = int(input('Enter Number 1 : '))
num2 = int(input('Enter Number 2 : '))
operator = input('Enter Operator [+, *, /, -] : ')

if (operator == '+'):
    ans = num1 + num2
    print(ans)
elif (operator == '-'):
    ans = num1 - num2
    print(ans)
elif (operator == '*'):
    ans = num1 * num2
    print(ans)
elif (operator == '/'):
    ans = num1/num2
    print(ans)
else :
    print('Pls Enter suitable operators : [+, *, /, -]')
