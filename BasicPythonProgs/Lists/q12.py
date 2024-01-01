# Bubble Sort
def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [3, 8, 1, 10, 5, 17, 0, 4]  
bubble_sort(arr)
print(arr)