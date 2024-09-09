list_1 = [1,2,3]
list_2 = [1,3,4]

counter_1 = 0
counter_2 = 0
combined_list = []

if len(list_2) - len(list_1) >= 0:
    counter = len(list_2)
else: counter = len(list_1) 


for i in range(0,counter):  
    counter_1 = list_1[i]
    counter_2 = list_2[i]
    if counter_1 == counter_2:
        combined_list.append(counter_1)
        combined_list.append(counter_2)
    elif counter_1 < counter_2:
        combined_list.append(counter_1)
    elif counter_1 > counter_2:
        combined_list.append(counter_2)



print(list_1)