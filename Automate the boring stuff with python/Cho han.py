import random


roll_1 = random.randrange(1, 7)
print(roll_1)
roll_2 = random.randrange(1, 7)
print(roll_2)

snake_eyes = False
if (roll_1 + roll_2) % 2 == 0:
    dealer_choice = "Cho"
else:
    dealer_choice = "Han"

if roll_1 == roll_2:
    snake_eyes = True

# PLAYER 1 DEETS
player1_pot = 4000
# print("You have ", player1_pot,"rupees," )
player1_bet = 500  # int(input("How much would you like to bet?"))
player1_choice = "Cho"  # input("P1 what is your choice Cho(even)/Han(odd) >")

# PLAYER 2 DEETS
player2_pot = 4000
# print("You have ", player2_pot,"rupees," )
player2_bet = 500  # int(input("How much would you like to bet?"))
player2_choice = "Han"  # input("P2 what is your choice Cho(even)/Han(odd) >")


def result_calc(player_choice, dealer_choice, player_bet, player_pot, snake_eyes):
    while snake_eyes:
        print("SNAKE EYESS!! All players get a bonus to their wager")
        player_bet += player_bet * 0.1
        snake_eyes = False
    if player_choice == dealer_choice:
        winning_amt = player_bet * 2
        # print("You Won, you get ", winning_amt, "rupees")
        house_fees = winning_amt // 20
        print("The house collects a", house_fees, "Rupee fee from the winner")
        player_pot = player_pot + winning_amt - house_fees
    else:
        player_pot -= player_bet
        # print(" You lost , you now have ",player_pot, "Rupees left.")
    return player_pot


player1_result = result_calc(
    player1_choice, dealer_choice, player1_bet, player1_pot, snake_eyes
)
player2_result = result_calc(
    player2_choice, dealer_choice, player2_bet, player2_pot, snake_eyes
)

print("The dealer lifts the cup to reveal:")
print(roll_1, "-", roll_2)

if player1_result > player1_pot:
    print("P1 wins", player1_bet * 2, "rupees ,P1 current pot is", player1_result)
    print("The house collects a", (player1_bet // 10), "rupees as fee")
    print("P2 lost", player2_bet, "rupees ,P2 current pot is", player2_result)
else:
    print("P2 wins", player2_bet * 2, "rupees, P2 current pot is", player2_result)
    print("The house collects a", (player2_bet // 10), "rupees as fee")
    print("P1 lost", player1_bet, "rupees ,P1 current pot is", player1_result)

# if player2_result > player2_pot:
# print("P2 wins, you won",player2_bet*2,"Your current pot is",player2_result)
# else:
# print("P2 wins, you lost",player2_bet,"Your current pot is",player2_result)
