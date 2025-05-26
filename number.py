# user to guess the number
# take intput range
# take guess of user
# tell them how close they were the number
# stop when the number is guessed
import random 

print("Welcome to Number Guessing Game!")
print("Instructions:\n1. Choose the range greater than 0.\n2. Guess the number")
num = int(input("Enter the top range number: "))

if num > 0:
    random_num = random.randint(0,num)
else:
    print("Invalid input!!")
cnt = 0
while True:
    cnt += 1
    guess_num = int(input("Guess the number:"))
    if guess_num ==  random_num:
        print(f"🎉 Correct! You guessed the number in {cnt} try.")
        break
    elif guess_num > random_num:
        print("Your guess was above the number.")
    else:
        print("Your guess was below the number.")
    print("❌ Wrong guess. Try again.")
        

