import re
'''
picnic_items = {"Sandwiches" : 10,"Napkins" : 20,"Apples" : 7,"Rasna" : "5L"}
add_items = "Y"
while add_items == "Y":
    item = input("Enter item name :")
    if item in picnic_items:
        item_checker = input("There are already " + str(picnic_items.get(item)) + item + " in the list, would you like to add more?")
        if item_checker == "Y":
            new_number_item = input("Enter number of items :")
            previous_Qty = picnic_items[item]
            picnic_items[item] = int(number_item + new_number_item)
            
    number_item = input("Enter number of items :")
    picnic_items[item] = number_item
    add_items = input("Picnic list updated \nWould you like to add more items? (Y/N)")


def print_picnic(items_dict,left_width,right_width):
    print("PICNIC ITEMS".center(left_width + right_width , "_"))
    for k,v in items_dict.items():
        print(k.ljust(left_width,"*") + str(v).rjust(right_width,"-"))

print_picnic(picnic_items,10,5)
'''

table_input = [["apples","oranges","cherries","banana"],
               ["paper","Rock","Scissssors","spock"]]

print(table_input[0][1])

def max_lenght_finder(table_list):
    max_lenght = 0
    for i in range(len(table_list)):
        for k in range(len(table_list[i])):
            lenght =len(table_list[i][k])
            name_obj = table_list[i][k]
            #print(name_obj)
            if lenght > max_lenght:
                max_lenght = lenght
    return max_lenght

MAX_LENGHT = max_lenght_finder(table_input)
print(MAX_LENGHT)
col_width = [0] * len(table_input)
print(col_width)

# This prints Indexes of all values in the list of lists (input)
xyz = 0
abc = 0
for i,v in enumerate(table_input):
    abc +=1
    for j,v2 in enumerate(v):
        print(i,j,v2,i+j)
        xyz += 1

print(xyz,abc)
#This is printing the list with list values rjust-ified 
# for i in range(len(table_input)):
#     for k in range(len(table_input[i])):
#         lenght =len(table_input[i][k])
#         name_obj = table_input[i][k]
#         print(table_input[i][k].rjust(max_lenght_finder(table_input,max_lenght),"*"))

#for k in table_list:
#    print(k.rjust(max_lenght," ")) print(table_list[i][k].rjust(max_lenght,"*"))