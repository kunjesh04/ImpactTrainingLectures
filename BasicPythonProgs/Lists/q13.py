# Insertion Sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key<array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key

arr = [3, 8, 1, 10, 5, 17, 0, 4]
insertion_sort(arr)
print(arr)