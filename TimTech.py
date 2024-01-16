import random

token = ["R","P","S"]

computer_guess = token[random.randrange(3)]
print(computer_guess)
user_guess = input("Type one from Rock Paper Scissor R/P/S! ")

draw_index = 0
while user_guess == computer_guess:
    print("Match Draw")
    computer_guess = token[random.randrange(3)]
    print(computer_guess)
    user_guess = input("Type one from Rock Paper Scissor R/P/S! ")
    draw_index += 1
    

if user_guess == "R" and computer_guess == "P":
    print("Computer selected",computer_guess, "CPU wins")
elif user_guess == "P" and computer_guess == "S":
    print("Computer selected",computer_guess, "CPU wins")
elif user_guess == "S" and computer_guess == "R":
    print("Computer selected",computer_guess, "CPU wins")
else:
    print("Congratzi Nazi")


print("No. of rematches", draw_index)