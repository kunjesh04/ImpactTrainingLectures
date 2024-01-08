# Binary Search
def binarySearch(array, low, high, target):
    if low<=high:
        mid = (low+high)//2
        if target == array[mid]:
            print(f'{target} found at index {mid}')
            return
        elif target > array[mid]:
            new_low = mid + 1
            return binarySearch(array, new_low, high, target)
        else:
            new_high = mid - 1
            return binarySearch(array, low, new_high, target)
    else:
        print(f'{target} not found')


array = [1, 3, 5, 6, 7, 9, 12, 40, 88, 100, 110]
key = 7878

binarySearch(array, 0, len(array)-1, key)