def insertion_sort(inp_arr):
    arr = inp_arr
    for i in range(1, len(arr)):
        key = arr[i]
        j =i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

array = [2, 7, 3, 9, 1, 5]
print(array)
srt_arr = insertion_sort(array)
print(srt_arr)