array = [1,1,2,4,2,6,7,1,4,7,95,6,5,4,2,765,12345,6,999,34,54,2,3,45,22,6]
unique_nums = []

print('Using traditional Method...')
for num in array:
    if num not in unique_nums:
        unique_nums.append(num)
        count = 0
        for x in range(len(array)):
            if array[x] == num:
                count+=1
        print(f"{num} occurs {count} times")

print(' ')
unique_nums = []
print('Using in-built function...')
for num in array:
    if num not in unique_nums:
        unique_nums.append(num)
        print(f"{num} occurs {array.count(num)} times")
    else:
        continue