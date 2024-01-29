import calendar
import random

months_list = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec",]
no_of_birthdays = 12
def birthday_generator(no_of_birthdays):
    month_generated_list = [">"]
    i=0
    while i < no_of_birthdays:
        month_name = months_list[random.randrange(12)]
        #month_generated_list = month_generated_list.append(month_name)
        i += 1
    
    return print(month_name) #, month_generated_list)

birthday_generator(no_of_birthdays)
