# 
people = [1,2,3,4,5,6,7,8,9,10,11,12, 13, 14, 15]
slot_size = int(input('Enter size of slot : '))

# MATHEMATICAL APPROACH :
print('====================MATHEMATICAL APPROACH====================')
num_of_people = len(people)
num_sets = num_of_people // slot_size

last_set_ind = int(num_sets / 2) + 1
print('Last set Number : ', last_set_ind)

nums_to_skip = (last_set_ind-1)*slot_size

last_set = people[nums_to_skip:nums_to_skip+slot_size]
print('Last Set : ', last_set)
if num_sets % 2 == 0: # Even Num of Sets
    last_num = last_set[0]
else: # Odd Num of Sets
    last_num = last_set[-1]
print('Last Number to enter : ', last_num)

# TWO-POINTER APPROACH
print('====================TWO-POINTER APPROACH====================')
i, j = 0, num_of_people-1
cave = []
while len(cave) != num_of_people:
    for x in range(slot_size):
        cave.append(people[i])
        i += 1
    if len(cave) != num_of_people:
        for x in range(slot_size):
            cave.append(people[j])
            j -= 1
    print('Cave After curr pass : ', cave)
last_entry = cave[-1]
print(last_entry)

# 2P with Flag
print('====================2P with Flag APPROACH====================')
left, right = 0, num_of_people-1
flag = 0
while (right-left >= slot_size):
    if flag == 0:
        left += slot_size
        flag = 1
    else :
        right -= slot_size
        flag = 0
if flag:
    print(people[left])
else:
    print(people[right])