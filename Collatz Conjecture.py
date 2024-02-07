import math

number = 28

remainder = number % 2

iterations = 0
while number > 1:
    if (number % 2) == 0:
        number /= 2
        print(number)
    elif (number % 2) == 1:
        number = (3*number) + 1
        print(number)
    iterations += 1

print("No. of Iterations =", iterations)


