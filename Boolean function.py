
x = str(8238)
y = len(str(x))

# Units = ( x % 10**(y-2))
# new_units = Units

# tens = (x % 10**(y-1)) - Units
# new_Tens = tens // 10

# Hundreds = (x % 10**y) - tens - Units
# new_hundreds = Hundreds // 100

#print (f"{Units},{tens},{Hundreds}")

mid = y // 2
print(mid)
num_flag = True
list_x = []
# for i in range (1,y+1):
#     if i <= mid:
#         current_digit = (x % 10)
#         list_x.append(current_digit)
#         x = x // 10
#         print(list_x)
#     else:
#         if list_x == []:
#             break
#         print(current_digit)
#         RHS = int(list_x.pop())
#         print(RHS)
#         #print(f"{RHS},{current_digit}")
#         if RHS == current_digit:
#             print ("It a palindrome!")
#             num_flag = False
#             break
reverse_x = " "
for i in range(y-1,0,-1):
    reverse_x = reverse_x + x[i]
    print(reverse_x)

print (list_x)

# print (f"{new_hundreds},{new_Tens},{new_units}")

