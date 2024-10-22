import random
max_guesses = 11

no_of_digits = int(input("For how many digits(atleast) would you like to play?"))
lower_bound  = int('1' + '0' * (no_of_digits-1)) #10 ** (no_of_digits-1) #int('1' + '0' * (no_of_digits-1))
print("lower limit =" + str(lower_bound))
upper_bound = int(('1' + '0' * no_of_digits)) -1 #int("9" * no_of_digits)
print("upper limit =" + str(upper_bound)) # int(('1' + '0' * no_of_digits)) -1
#units_place = str(random.randrange(0,10)) #tried to pick a repititive digit number
#computer_guess = units_place * no_of_digits
computer_guess = str(random.randrange(lower_bound,(upper_bound +1))) #computer guess converted to string

#print (computer_guess) #for checking
no_of_guesses = 0

while no_of_guesses < max_guesses:
    fermi_count = 0
    pico_count = 0
    bagels_count = 0
    user_guess = str(input("Guess the number?"))
    if len(user_guess) != no_of_digits or not user_guess.isnumeric(): #Dad tried to enter 4 digits and the code ran hence added an exception
        #Also he wanted to know how many guesses were remaining, so made changes
        print("Kindly enter proper number OR within range specified," "\nYou have ", (max_guesses - no_of_guesses),"guesses remaining")
        continue
    if user_guess == computer_guess:
        print ("You Won")
        break
        # break out of the loop if number matches
    for i in range(0,no_of_digits): #To keep track of how many f3ermi / Pico, also helps for repeating digits"
        if user_guess[i] == computer_guess[i]: 
            fermi_count += 1
        elif user_guess[i] in computer_guess:
            pico_count += 1
    no_of_guesses += 1
    if fermi_count > 0 and pico_count > 0: #To print Fermi and Pico at the same time
        print("Fermi " * fermi_count ,"Pico " * pico_count ,"\nYou have ", (max_guesses - no_of_guesses),"guesses remaining") #string multiplication
    elif pico_count > 0: 
        print ("Pico " * pico_count,"\nYou have ", (max_guesses - no_of_guesses),"guesses remaining") 
    elif fermi_count > 0:
        print ("Fermi " * fermi_count,"\nYou have ", (max_guesses - no_of_guesses),"guesses remaining")
    else:
        print ("bagels","\nYou have ", (max_guesses - no_of_guesses),"guesses remaining")

    

print ("Computer guess was " ,computer_guess) 



        

