org_string = input("Enter Main String :")
sub_string = input('Enter sub String :')

if sub_string in org_string:
    print(f'{sub_string} found at {org_string.index(sub_string)}')
else:
    print('Could not find')