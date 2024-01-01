def linearSearch(arr:list, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f'{target} found at index {i}')
            return
    print(f'{target} not found')


array = [4,1,7,3,5,9,12,40]
key = 7

linearSearch(array, key)