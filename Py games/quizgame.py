print("Welcome to the quiz")
play = input("Do you want to play the game? (yes/no) "  ).lower()
if play != "yes":
    quit()

score = 0

#ques 1
answer = input("CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques 2
answer = input("YOLO stands for? ")
if answer.lower() == "you only live once":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques 3
answer = input("RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques 4
answer = input("EOD stands for? ")
if answer.lower() == "end of the day":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques 5
answer = input("ASAP stands for? ")
if answer.lower() == "as soon as possible":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

#ques 6
answer = input("FYI stands for? ")
if answer.lower() == "for your information":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
 

print(f"Your score is: {score} out of 6, Precentage: {(score/6)*100}" )

    