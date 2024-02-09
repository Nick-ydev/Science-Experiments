import random

player_pot = 4000
print("You have ", player_pot,"rupees," )
player_bet =  5000 #int(input("How much would you like to bet?"))
roll_1 = random.randrange(1,7)
print(roll_1)
roll_2 = random.randrange(1,7)
print(roll_2)

if (roll_1 + roll_2) % 2 == 0:
    dealer_choice = "Cho"
elif (roll_1 + roll_2)%2 == 1 :
    dealer_choice = "Han"
    

player_choice = input("What is your choice Cho(even)/Han(odd) >")
print("The dealer lifts the cup to reveal:")
print(roll_1, "-",roll_2)

if player_choice == dealer_choice :
    winning_amt = player_bet *2
    print("You Won, you get ", winning_amt, "rupees")
    house_fees = winning_amt // 20
    print("The house collects a", house_fees , "Rupee fee")
    player_pot = player_pot + winning_amt - house_fees
else: 
    player_pot -= player_bet
    print(" You lost , you now have ",player_pot, "Rupees left.")


    