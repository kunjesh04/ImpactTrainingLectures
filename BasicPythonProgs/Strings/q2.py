string = input('Enter the String : ')
isPalindrome = True

for i in range(0, len(string)//2):
    if string[i] != string[len(string)-i-1]:
        isPalindrome = False
        
if isPalindrome:
    print(f'{string} is Palindrome !')
else:
    print(f'{string} is NOT a Palindrome !')


'''ALTERNATE METHOD :
cString = string.lower()
if cString == cString[::-1]:
    print(f'{string} is Palindrome !')
else:
    print(f'{string} is NOT a Palindrome !')
'''