import random

lower_bound = 3
upper_bound = 6
final_iteration = 0


def collatz_sequence (number,start_iterations,final_iteration):
    
    while number > 1:
        if (number % 2) == 0:
            number /= 2
            print(number)
        elif (number % 2) == 1:
            number = (3*number) + 1
            print(number)
        start_iterations += 1
    print("No. of Iterations =", start_iterations)
    if start_iterations > final_iteration:
        final_iteration = start_iterations
    
    print("Maxima of Iterations=",final_iteration)
    return final_iteration

for i in range(lower_bound, upper_bound):
    number = i #random.randrange(1000,100000)
    print("The Number is" , number)
    start_iterations = 0
    collatz_sequence(number,0)



