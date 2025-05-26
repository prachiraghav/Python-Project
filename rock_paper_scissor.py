'''
user input for R,P,S
random computer selection r,p,s
count score wins and losses
quit if user wants
'''
 
import random

print("Welcome to the game!")
print("Rock! Paper! Scissor!")
print("Instructins: \n\n1.Choose a number(0-3) \n 0-quit \n 1-rock \n 2-paper \n 3-scissors")

options = {1:"rock",2:"paper",3:"scissor"}
user_score = 0
comp_score = 0
tie = 0

#user draw
while True:
    user  = int(input("Enter your choice. \n0(quit) 1(rock) 2(paper) 3(scissor): "))
    comp = random.randint(1,3)
    if user == 0:
        print(f"Wins: {user_score}, Loses:{comp_score}, Tie: {tie}")
        break
    elif  user not  in options:
        print("Invalid input")
        print(comp)
    else:
        #rules
        if user == comp:
            print("TIE!!")
            tie +=1
        elif user == 1 and comp == 3:
            print("You win!")
            user_score += 1 
    
        elif user == 2 and comp == 1:
            print("You win!")
            user_score += 1 
    
        elif user == 3 and comp == 2:
            print("You win!")
            user_score += 1 
    
        else:
            print("You lost!")
            comp_score += 1

