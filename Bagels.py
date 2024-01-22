import random

computer_guess = str(369)

#str(random.randrange(100,1000))

print(computer_guess)

user_guess = str(432)

for i in range(0,3):
    if user_guess[i] == computer_guess[i]:
        print("Fermi")
    else:
        user_guess[i] in computer_guess[i]
        print("Pico")

