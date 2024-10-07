from math import *

# rng_phrase = "Prodigy yadav"
# print (rng_phrase.index("a"))
# print (rng_phrase.upper())

# Num_rand = 7.2134

# print (sqrt(pow(Num_rand,3)))

x = 3
y = 75
operation_math = "*"

def Calculator (x , y):
    if operation_math == "+":
        return (x + y)
    elif operation_math == "-":
        return (x - y)
    elif operation_math == "*":
        return (x * y)
    elif operation_math == "/":
        return (x / y)
    else: print("Choose a valid operator from +,-,/,*")
    
print (Calculator(x , y))

nums_list = [1,32,78,345,87,9,34]

largest_num = None
smallest_num = None
for number in [1,32,78,34,87,9,384]:
    if largest_num == None:
        largest_num  = number
    elif number > largest_num:
        largest_num = number
        print (largest_num,number)

for thing in [214,32,78,345,87,9,34]:
    if smallest_num == None:
        smallest_num = thing
    elif thing < smallest_num:
        smallest_num = thing
        print (smallest_num, thing)