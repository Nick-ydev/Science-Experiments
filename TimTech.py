import random

token = ["R","P","S"]
user_wins = 0
computer_wins = 0

no_of_games = 0
draw_index = 0

while no_of_games < 6:
    computer_guess = token[random.randrange(3)]
    print(computer_guess)
    user_guess = input("Type one from Rock Paper Scissor R/P/S! ")
    if user_guess == "R" and computer_guess == "P":
        print("Computer selected",computer_guess, "CPU wins")
        computer_wins += 1
    elif user_guess == "P" and computer_guess == "S":
        print("Computer selected",computer_guess, "CPU wins")
        computer_wins += 1
    elif user_guess == "S" and computer_guess == "R":
        print("Computer selected",computer_guess, "CPU wins")
        computer_wins += 1
    elif user_guess == computer_guess:
        draw_index += 1
        print ("Match Draw")
    else:
        print("Congratzi You WIN")
        user_wins += 1
    no_of_games += 1

print("No. of matches",no_of_games,"Draws:", draw_index,"Computer wins:", computer_wins, "User wins:" ,user_wins)