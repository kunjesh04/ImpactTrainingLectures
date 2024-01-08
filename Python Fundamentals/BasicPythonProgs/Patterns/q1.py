# WAP to print odd number in the given range
start = int(input("Enter starting number : "))
end = int(input("Enter ending number : "))

for i in range(start, end):
    if i%2!=0:
        print(i)