def swap(a, b):
    a,b = b, a

def bubbleSort(org_arr:list):
    arr = org_arr
    n = len(arr)-1
    for x in range(n):
        for i in range(n):
            if arr[i] > arr[i+1]:
                # swap(arr[i], arr[i+1])
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
            
array = []

n = int(input('Enter number of elements : '))
for x in range(n):
    num = int(input(f'Enter element {x+1} : '))
    array.append(num)

print('Original Array : ', array)
bubbleSort(array)
print('Sorted Array : ', array)