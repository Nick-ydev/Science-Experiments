import pandas as pd
import random
import numpy as np

lower_bound = 3
upper_bound = 6

iteration_list = [0]

start_iterations = 0
final_iterations = 0

for i in range(lower_bound,upper_bound):
    number = i
    number_track = [number]
    while number > 1:
        if (number % 2) == 0:
            number /= 2
            print(number)
        elif (number % 2) == 1:
            number = (3*number) + 1
            print(number)
        start_iterations += 1
        if start_iterations > final_iterations:
            final_iterations = start_iterations
        number_track.append(number)

#Append no. of iteration in a list for numpy to execute
for i in range(0,final_iterations):
    iteration_list.append(i)
    print("The Number is" , number)

# iteration_list_numpy = np.array(iteration_list)
# number_track_numpy = np.array(number_track)

print("No. of Iterations =", start_iterations)
data = {
  "iterations": iteration_list,
  "number": number_track
}

#load data into a DataFrame object:
df = pd.DataFrame(data, index = (iteration_list))

# saving the dataframe and exporting in CSV
#df.to_csv(r'D:\Power BI thing\file3.csv')
print(df) 