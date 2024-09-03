import random

STARTING_LIST = [[1,2,3,4,5,6,7,8,9,10],
                [11,12,13,14,15,16,17,18,19,20],
                [21,22,23,24,25,26,27,28,29,30],
                [31,32,33,34,35,36,37,38,39,40],
                [41,42,43,44,45,46,47,48,49,50],
                [51,52,53,54,55,56,57,58,59,60],
                [61,62,63,64,65,66,67,68,69,70],
                [71,72,73,74,75,76,77,78,79,80],
                [81,82,83,84,85,86,87,88,89,90]
]

working_list = [[1,2,3,4,5,6,7,8,9,10],
                [11,12,13,14,15,16,17,18,19,20],
                [21,22,23,24,25,26,27,28,29,30],
                [31,32,33,34,35,36,37,38,39,40],
                [41,42,43,44,45,46,47,48,49,50],
                [51,52,53,54,55,56,57,58,59,60],
                [61,62,63,64,65,66,67,68,69,70],
                [71,72,73,74,75,76,77,78,79,80],
                [81,82,83,84,85,86,87,88,89,90]
]

# open_len = len(working_list)
# print(open_len ,"len")

def ticket_maker(working_list):
    ticket_1 = []
    list_for_testing_repeating_tens = []
    for i in range (0,9):
        wrkin_len = len(working_list[i])
        list_for_testing_repeating_tens.append(i)
        #print(list_for_testing_repeating_tens,"1st")
        if wrkin_len < 1:
            i+=1
            continue
        j = random.randrange(0,wrkin_len)
        num = working_list[i][j]
        del working_list[i][j]
        ticket_1.append(num)

    while len(ticket_1) < 15:
        i = random.randrange(0,9)
        list_for_testing_repeating_tens.append(i)
        print(list_for_testing_repeating_tens,"2st")
        if list_for_testing_repeating_tens.count(i) < 4:
            wrkin_len = len(working_list[i])
            j = random.randrange(0,wrkin_len)
            num_2 = working_list[i][j]
            del working_list[i][j]
            ticket_1.append(num_2)
        else:
            continue
        
    return ticket_1

Player_1 = ticket_maker(working_list)
print (Player_1,"P1 len",len(Player_1))

Player_2 = ticket_maker(working_list)
print(Player_2,"P2 len",len(Player_2))

Player_3 = ticket_maker(working_list)
print("\n",Player_3,"P3 len",len(Player_3))
print(working_list)

Player_4 = ticket_maker(working_list)
print("\n",Player_4,"P4 len",len(Player_4))
print(working_list)

Player_5 = ticket_maker(working_list)
print("\n",Player_5,"P5 len",len(Player_5))
print(working_list)

Player_6 = ticket_maker(working_list)
print(Player_6,"P6 len",len(Player_6))
print(working_list)

# while Player_1 != []:
#     call = random.randrange(1,91)
#     if call in Player_1:
#         Player_1.remove(call)
#     k +=1

# print("player 1 wins in", k, " number of tries")


print(working_list)



    
