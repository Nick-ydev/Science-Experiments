l1 = [1,9,4,7,9,0,9]
l2 = [9,9,0,9]

#Equate both strings by adding 0
if len(l1) != len(l2):
    if len(l1) > len(l2):
        while len(l1) != len(l2):
            l2.append(0)
    elif len(l1) < len(l2):
        while len(l1) != len(l2):
            l1.append(0)

print(l1,l2,"equal lenght")

#list ko string banao
def list_to_string(list1):
    stringed_list = ''
    for i in range ((len(list1)-1),-1,-1):
        stringed_list = stringed_list + str(list1[i])
    
    return int(stringed_list)

print(list_to_string(l1))

#call function to 
num1_asint = list_to_string(l1)
num2_asint = list_to_string(l2)

output_int = str(num1_asint + num2_asint)
print(output_int)

output_list = []

#string ko list
for i in range((len(output_int)-1),-1,-1):
    output_list.append(int(output_int[i]))

print(output_list, 'final')
