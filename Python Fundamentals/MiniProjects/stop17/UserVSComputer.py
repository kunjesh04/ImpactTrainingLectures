game_numbers = [z for z in range(1,18,1)]
dominance_numbers = [num for num in range(2,18,3)]
j = 0
start=[1,2]
curr= 1
user = 0
computer = 0

def game(number):
    if(number in dominance_numbers):
        user = 1
        computer_choice = number +1
        curr = computer_choice
        print(f"computer number : {computer_choice}")
        return user,computer_choice
  
    else:
        user = 0
        global j
        computer_choice = dominance_numbers[j]
        curr = computer_choice
        print(f"computer number : {computer_choice}")
        j=j+1
        return computer,computer_choice
            
while(curr<17):
    value = int(input("enter a number"))
    print(start)
    if(value in start):
        curr = value
        win,choice = game(value)
        start[0] = choice+ 1
        start[1] = choice + 2
        curr = choice
        print(curr)
    else:    
        print("invaild")
    
    
    
if(win == 1):
    print("User win the game")
else:
    print("Computer wins the game")