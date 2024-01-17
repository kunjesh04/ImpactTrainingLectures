def selectionSort(org_arr):
    arr = org_arr
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr    

org_arr = [10, 8, 15, 5, 2]
print(org_arr)
srt_arr = selectionSort(org_arr)
print(srt_arr)