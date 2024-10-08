import math

Veritasium = 37

multiple = 1258
###Intitally blank strings
reverse_multiple = ''
new_multiple = ''

def reverse_int(x,y):
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
    print(remainder_raised,'def')
    return remainder_raised

#print(reverse_int(multiple,4))
# This is checking if the divided answer contains a decimal or not.
for i in range(len(str(reverse_int(multiple,4)))):
    reverse_multiple = reverse_multiple + str(reverse_int(multiple,4))[i] + '0'
    print(reverse_multiple)

#The first Number >1000 & a multiple of 37 is 37*28
#This is just to create a sample szize and check divisibility
for i in range(28,33):
    multiple = Veritasium * i
    y = len(str(multiple))
    Inverse_num = reverse_int(multiple,y)
    if (Inverse_num % 37) != 0:
        print("Not Divisble")
    else: 
        print("Divisble")
