curr_num = 0
choices = [curr_num+1, curr_num+2]
players = ['P1', 'P2']
curr_player = 0

while curr_num <17:
    number = int(input(f'{players[curr_player]} enter a number from {choices}: '))
    if number not in choices:
        print('Invalid Choice')
        continue
    
    if number>=17:
        print(f'{players[curr_player]} WINS the Game')
        break
    
    print(f'{players[curr_player]} goes to {number}')
    curr_num = number
    choices = [curr_num+1, curr_num+2]
    
    curr_player = (curr_player+1)%2