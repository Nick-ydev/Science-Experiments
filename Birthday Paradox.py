import calendar
import random

months_dict = {"Jan":31 ,"Feb":29,"Mar":31,"Apr":30,"May":31,"Jun":30,"Jul":31,"Aug":31,"Sep":30,"Oct":31,"Nov":30,"Dec":31}
#made dictionary for key value pair

months_list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec",]
#made list for all months to call dictionary object
no_of_birthdays = 23

def birthday_generator(no_of_birthdays):
    global month_generated_list
    month_generated_list = []
    i=0
    while i < no_of_birthdays:
        month_name = months_list[random.randrange(12)]
        month_max_days = months_dict[month_name]
        birth_date = (month_name + " " + str(random.randrange(month_max_days)))
        month_generated_list.append(birth_date)
        
        i += 1
    
    return print(month_generated_list)

birthday_generator(no_of_birthdays)

'''
def duplicate_checker():
    for i in range (0,len(month_generated_list)):
        global matching_birthday
        matching_birthday = 0
        while month_generated_list[i] in month_generated_list:
            matching_birthday += 1

    return matching_birthday

duplicate_checker()
'''