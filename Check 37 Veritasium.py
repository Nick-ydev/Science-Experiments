import math

Veritasium = 37

multiple = 9953
reverse_multiple = ''
new_multiple = ''

def reverse_int(x,y):
    #x = 10080808001
    #y = len(str(x))
    floored_quotient = x // 10
    remainder_raised = 0 + ((x % 10) * (10 ** (y-1)))
    #print(remainder_raised)
    for i in range(1,y):
            remainder = floored_quotient % 10
            #print("2nd",remainder)
            remainder_raised = remainder_raised + remainder * (10 ** (y-i-1))
            #print("2ndrr",remainder_raised)
            floored_quotient = floored_quotient // 10
            #print(floored_quotient)
            #print("i=",i)
    return remainder_raised


#print(reverse_int(multiple,4))
# This is checking if the divided answer contains a decimal or not.

for i in range(len(str(reverse_int(multiple,4)))):
    reverse_multiple = reverse_multiple + str(reverse_int(multiple,4))[i] + '0'
    print(reverse_multiple)



for i in range(28,33):
    multiple = Veritasium * i
    y = len(str(multiple))
    Inverse_num = reverse_int(multiple,y)
    if (Inverse_num % 37) != 0:
        print("Contains Decimal")
    else: 
        print("Does not")
         