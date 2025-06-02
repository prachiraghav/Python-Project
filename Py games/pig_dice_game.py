'''
input numer of players : ok 
player 1 turn : ask the player if they want to roll the dice(y/n)  
roll the dice
rolled number added to the score
if the rolled numbe = 1 the player 2 turn and score of player 1 = 0 for that turn. 
'''

import random 

def roll():
    roll_dice= random.randint(1,6)
    return roll_dice

while True:
    players = int(input("Number of players (2-4): "))
    
    if 2<= players <= 4:
        break
    else:
        print("Enter the number of players in the range (2-4).")

max_score = 10
player_score = [0 for _ in range(players)]# to store each player score

while max(player_score) < max_score:
    for player_idx in range (players):
        print(f"Player {player_idx + 1} you turn. \n \n")
        current_score = 0
        
        while True:
            play = input("Would you like to roll the dice (Y/N)").lower()
            if play != 'y':
                break
            
            else:
                dice = roll()
                if dice == 1:
                 print("You rolled 1. Next players turn.\n")
                 current_score=0
                 break
                else: 
                    current_score += dice
                    print(f"You rolled: {dice}")
            print(f"Your current score is: {current_score}")
        player_score[player_idx] += current_score
        print(f"Total score is: {player_score[player_idx]}")
max_score=max(player_score)
win_idx = player_score.index(max_score)
print(f"player number {win_idx +1}, score : {max_score}")