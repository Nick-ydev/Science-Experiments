
x = 8723278
y = len(str(x))


Units = (x % 10**(y-2))
new_units = Units

tens = (x % 10**(y-1)) - Units
new_Tens = tens // 10

Hundreds = (x % 10**y) - tens - Units
new_hundreds = Hundreds // 100

# print (f"{Units},{tens},{Hundreds}")
mid = y // 2
num_flag = True
list_x = list()
for i in range (1,y+1):
    if i <= mid:
        Units = (x % 10)
        list_x.append(Units)
        x = x // 10
    else:
        if i == mid:
            continue
        Units = x % 10
        RHS = list_x.pop()
        print(f"{RHS},{Units}")
        if RHS != Units:
            print ("It is not a palindrome!")
            num_flag = False
            break


print (list_x)

# print (f"{new_hundreds},{new_Tens},{new_units}")

