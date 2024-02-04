import math
'''
number = 2

remainder = number % 2

iterations = 0
while number > 1:
    if (number % 2) == 0:
        number = number / 2
        print(number)
    elif (number % 2) == 1:
        number = (3*number) + 1
        print(number)
    iterations += 1

print("No. of Iterations =", iterations)
'''
months_list = ['Apr 1', 'Aug 13','Jan 28', 'Aug 13', 'Jan 3', 'Jul 1', 'Nov 27', 'Mar 4', 'Jul 1']
matching_birthday = 0

for i in range (0,len((months_list))):
    for months_list[i] in months_list[i+1]:
        print(months_list[i])
        matching_birthday +=1

print(matching_birthday)