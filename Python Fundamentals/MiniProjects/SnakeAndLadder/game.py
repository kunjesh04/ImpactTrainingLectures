import random

players = ['P1', 'P2']
curr_player = 0
row = ['_' for _ in range(10)]
player_pos = [0, 0]

while True:
    input(f'{players[curr_player]} Press any key ')
    num = random.randint(0, 3) 
    print(f'{players[curr_player]} got: {num}')

    old_pos = player_pos[curr_player] 
    player_pos[curr_player] += num 

    if player_pos[curr_player] >= len(row) - 1:
        print(f'{players[curr_player]} Wins')
        break

    if player_pos[0] == player_pos[1]:
        player_pos = [0, 0]

    
    row[old_pos] = '_' 
    row[player_pos[curr_player]] = players[curr_player]

    print(row)
    curr_player = (curr_player + 1) % 2
