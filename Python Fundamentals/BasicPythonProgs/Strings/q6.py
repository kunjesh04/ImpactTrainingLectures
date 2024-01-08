from itertools import permutations

string = input('Enter the String : ')
pmts = permutations(string)

print('Permutations found : ')
for word in pmts:
    print(word)