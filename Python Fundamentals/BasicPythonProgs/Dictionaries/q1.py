result = dict()

numKeys = int(input('Enter number of Keys : '))
rKeys = []
rVals = []

for i in range(numKeys):
    keyName = input(f'Enter Key{i} name : ')
    rKeys.append(keyName)

numProps = int(input('Enter number of values for each key : '))
for i in range(numProps):
    keyName = input(f'Enter Value : ')
    rKeys.append(keyName)