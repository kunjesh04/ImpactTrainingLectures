string = input('Enter the String : ')

hasChar = False

for char in string:
    if ord(char) < 48 or (57 < ord(char) < 65) or (90 < ord(char) < 97) or ord(char) > 122:
        hasChar = True

if not hasChar:
    print(f'{string} does NOT have any character')
else:
    print('Character Found ')