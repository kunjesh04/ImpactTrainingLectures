array = [1,2,4,6,8,0,4,4,2,2,6,8,1,4,0,2,8,4,1,0]
reduced_arr = []

print('Original Array : ', array)
for num in array:
    if num not in reduced_arr:
        reduced_arr.append(num)


print('Reduced Array : ', reduced_arr)
print('Using in-built function : ', set(array))
