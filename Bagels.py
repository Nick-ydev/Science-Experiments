import random
max_guesses = 11

no_of_digits = 3 #int(input("For how many digits(atleast) would you like to play?"))
lower_bound  = 10 ** (no_of_digits-1)
print(lower_bound)
upper_bound = int("9" *no_of_digits)
print(upper_bound)
#units_place = str(random.randrange(0,10))
#computer_guess = units_place * no_of_digits
computer_guess = str(random.randrange(lower_bound,(upper_bound +1)))

#print (computer_guess)
no_of_guesses = 0

while no_of_guesses < max_guesses:
    fermi_count = 0
    pico_count = 0
    bagels_count = 0
    user_guess = str(input("Guess the number?"))
    if user_guess == computer_guess:
        print ("You Won")
        break
    for i in range(0,no_of_digits):
        if user_guess[i] == computer_guess[i]:
            fermi_count += 1
        elif user_guess[i] in computer_guess:
            pico_count += 1
        
    if fermi_count > 0 and pico_count > 0:
        print("Fermi " * fermi_count ,"Pico " * pico_count)
    elif pico_count > 0:
        print ("Pico " * pico_count)
    elif fermi_count > 0:
        print ("Fermi " * fermi_count)
    else:
        print ("bagels")
        
    no_of_guesses += 1

   
        

