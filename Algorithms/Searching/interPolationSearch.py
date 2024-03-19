'''
The list should be sorted.
Numbers should have equal differences.
Then and only then interpolation search works.
arr = [2,4,6,8,10,12]

ind = low + ((target-arr[low])/arr[high]-arr[low])*(high-low)

'''


def interpolation_search(arr:list,low, high, x:int):
    if low<=high and x>=arr[low] and x<=arr[high]:    
        pos = low + ((high - low) // (arr[high] - arr[low]) * (x - arr[low]))
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, high, x)
        if arr[pos] > x:
            return interpolation_search(arr, low, pos - 1, x)
    return -1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
n = len(arr)
x = 12
index = interpolation_search(arr, 0, n - 1, x)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")