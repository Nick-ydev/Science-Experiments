import math 

BRACKETS_LIST = "()[]{}"
print(len(BRACKETS_LIST))
for i in range(0,6):
    if str(BRACKETS_LIST[i]) == str(BRACKETS_LIST[i+1]):
        print("True")
    i =+1