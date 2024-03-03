import re

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

