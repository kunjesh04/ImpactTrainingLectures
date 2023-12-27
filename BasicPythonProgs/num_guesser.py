# Guess The Number Game
import random

org_num = random.randint(1, 50)
chances = 5
game_end = False

print('Number Chosen from 1 to 50')

while not game_end and chances>0:
    user_num = int(input('Guess the Number : '))
    if user_num==org_num:
        game_end = True
        print('Number Guessed Correctly!')
        print('Number was : ', org_num)
        break
    elif user_num > org_num:
        print('Guess Lower')
        chances -= 1
        print('Chances Left : ', chances)
    elif user_num < org_num:
        print('Guess Higher')
        chances -= 1
        print('Chances Left : ', chances)
        
        
if chances == 0 and not game_end:
        print('Game OVER')
        print('Number Not Guessed')
        print('Original Number was : ', org_num)