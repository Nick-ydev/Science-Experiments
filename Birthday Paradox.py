import calendar
import random

months_dict = {"Jan":31 ,"Feb":29,"Mar":31,"Apr":30,"May":31,"Jun":30,"Jul":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
#made dictionary for key value pair

months_list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec",]
#made list for all months to call dictionary object
no_of_birthdays = 56

def birthday_generator(no_of_birthdays):
    global month_generated_list
    month_generated_list = []
    i=0
    while i < no_of_birthdays:
        month_name = months_list[random.randrange(12)]
        month_max_days = months_dict[month_name]
        birth_date = (month_name + " " + str(random.randrange(1,month_max_days)))
        month_generated_list.append(birth_date)
        
        i += 1
    
    return month_generated_list

print(birthday_generator(no_of_birthdays))


def duplicate_checker():
    global match_found
    matching_birthday = 0
    count_duplicates = 0
    for i in range (0,len(birthday_generator(no_of_birthdays))):
        if month_generated_list[i] in month_generated_list:
            match_found = month_generated_list[i]
            count_duplicates = month_generated_list.count(match_found)
        if count_duplicates > 1:
            matching_birthday += 1
        
    return matching_birthday

if duplicate_checker() >= 1:
    print("In this simulation, multiple people have a birthday on " + match_found + "... running more")

i =0
match_exists = 0
while i < 100000:
    birthday_generator(no_of_birthdays)
    if duplicate_checker() != 0:
        match_exists += 1
    if i % 10000 == 0:
        print( str(i) + ' simulations run .....')
    i +=1

print("Total matches = ") 
print(match_exists)
print(str(match_exists/1000) + '%')