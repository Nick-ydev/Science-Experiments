import pandas as pd
import random
import numpy as np

lower_bound = 23
upper_bound = 29
final_iteration = 0
this_dict = {}

def collatz_sequence (number,start_iterations):
    running_list = []
    while number > 1:
        if (number % 2) == 0:
            number /= 2
            print(number)
            running_list.append(number)
        elif (number % 2) == 1:
            number = (3*number) + 1
            print(number)
            running_list.append(number)
        start_iterations += 1
    print("No. of Iterations =", start_iterations)
    
    return running_list

for i in range(lower_bound,upper_bound):
	number = i
	current_list = collatz_sequence(number,0)
	running_dict = {number : current_list}
	print(running_dict)
	this_dict.update(running_dict)
print(this_dict)

df = pd.DataFrame(this_dict)

print(df)