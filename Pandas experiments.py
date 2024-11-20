import pandas as pd
import random
import numpy as np

number = random.randrange(1,100)
print("The Number is" , number)
remainder = number % 2

iteration_list = np.array([0])
number_track = np.array([number])

iterations = 0
while number > 1:
    if (number % 2) == 0:
        number /= 2
        print(number)
    elif (number % 2) == 1:
        number = (3*number) + 1
        print(number)
    iterations += 1
    iteration_list.append(iterations)
    number_track.append(number)

print("No. of Iterations =", iterations)
data = {
  "iterations": iteration_list,
  "number": number_track
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 