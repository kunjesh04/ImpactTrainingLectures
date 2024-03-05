def countingsort(array, place):
    size = len(array)
    count = [0]*size
    output = [0]*size
    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = size-1
    while i>=0:
        index = array[i] // place
        output[count[index % 10]-1] = array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(size):
        array[i] = output[i]

def radixsort(array):
    max_elem = max(array)
    place = 1
    while max_elem // place > 0:
        countingsort(array, place)
        place *= 10


data = [15, 1, 321, 9999, 10, 802, 2, 123, 90, 109, 11, 6790, 1324]
radixsort(data)
print(data)