arr = [1,2,3,4,5]

def swap_fl(array:[]):
    array[0], array[-1] = array[-1], array[0]
    return array

print(f"Original Array : {arr}")
swapped_array = swap_fl(array=arr)
print(f"Swapped Array : {swapped_array}")