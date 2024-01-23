def linearSearch(num, arr:list):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return 0

array = [8, 4, 2, 9, 23, 65, 1]
number = int(input('Enter Number to find : '))
result = linearSearch(number, array)
if result:
    print(f'{number} found at {result}')
else:
    print(f'{number} not found')