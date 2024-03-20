from math import *

# color = "Red"
# Plural_noun = "Shakira"
# Celebrity = "trains"

# def mad_Libs (color, Plural_noun, Celebrity):
#     print ("roses are " + color)
#     print (Plural_noun + " are Blue")
#     print (Celebrity + " ,I Love you")

# print (mad_Libs(color, Plural_noun, Celebrity))
# 1:18;26
# friends = ["Pro", "amateur", "noob", "Crow"]
# friends[2] = "Mike"

# print (friends[-1])

Num_pali = "-101"
mid = ceil(len(Num_pali)/2)
#mid = (len(Num_pali) // 2) if len(Num_pali) % 2 ==0 else (len(Num_pali)//2) +1
print (mid)
last_char = len(Num_pali)
num_flag = False

for i in range (0,mid):

    if str(Num_pali[i]) == str(Num_pali[(last_char)-1-i]):
        print ("It is not a palindrome!")
        num_flag = True
        break

if not num_flag:
    print ("It is a palindrome!")

