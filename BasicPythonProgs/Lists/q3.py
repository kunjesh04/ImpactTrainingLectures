array = [4,7,21,17,35]

print('Using in-built function: ', sum(array)/len(array))

print('Now using traditional method...')
addition, count = 0, 0
for num in array:
    addition+=num
    count+=1
average = addition/count
print(average)