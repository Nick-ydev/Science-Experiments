num1 = [1,9,4,7,9,0,9]
num2 = [9,9,0,9]

#Equate both strings by adding 0
if len(num1) != len(num2):
    if len(num1) > len(num2):
        while len(num1) != len(num2):
            num2.append(0)
    elif len(num1) < len(num2):
        while len(num1) != len(num2):
            num1.append(0)

print(num1,num2,"equal lenght")

#list ko string banao
def list_to_string(list1):
    stringed_list = ''
    for i in range ((len(list1)-1),-1,-1):
        stringed_list = stringed_list + str(list1[i])
    
    return int(stringed_list)

print(list_to_string(num1))

#call function to 
num1_asint = list_to_string(num1)
num2_asint = list_to_string(num2)

output_int = str(num1_asint + num2_asint)
print(output_int)

output_list = []

#string ko list
for i in range((len(output_int)-1),-1,-1):
    output_list.append(int(output_int[i]))

print(output_list, 'final')