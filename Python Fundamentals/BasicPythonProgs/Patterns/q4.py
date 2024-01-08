number = int(input('Enter number : '))
factorial = 1
for n in range(1, number+1):
    factorial *= n
    print(factorial , end=' ')
print('\n')
print(f"Factorial :", factorial)  
