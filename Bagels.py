import random
no_of_digits = input("For how many digits(atleast) would you like to play?")

upper_bound = 9*no_of_digits
print(upper_bound)
computer_guess = str(random.randrange(100,1000))

#str(random.randrange(100,1000))

# print(computer_guess)
no_of_guesses = 0
i=0 
while no_of_guesses < 11:
    user_guess = str(input("Guess the number?"))
    if user_guess == computer_guess:
        print ("You Won")
        break
    for i in range(0,3):
        if user_guess[i] == computer_guess[i]:
            print("Fermi")
        elif user_guess[i] in computer_guess:
            print("Pico")
        else:
            print("Bagels")
        
    no_of_guesses += 1

print(computer_guess)
    
        

