# Ip : BBBGGGBG, d(distance)=2
# Op : 3
# ===================
# Ip : 

input_arr = ['B', 'G', 'B', 'G', 'G', 'G', 'B', 'G']
valid_dist = 2

result = 0
max_pairs = 0

i, j = input_arr.index('B'), input_arr.index('G')

# for i in range(valid_dist+1):

while i<len(input_arr) and j<len(input_arr):
    if abs(i-j)<=valid_dist:
        result += 1
        while i<len(input_arr) and input_arr[i] != 'B':
            i += 1
        while j<len(input_arr) and input_arr[j] != 'G':
            j += 1
print(result)
            