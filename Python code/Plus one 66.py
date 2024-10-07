digits = [1,2,3]
#output = [1,2,4]

#convert list to int/string
def list_to_string(list1):
    stringed_list = ''
    for i in range (0,len(list1)):
        stringed_list = stringed_list + str(list1[i])
    return int(stringed_list)

digits_as_int = list_to_string(digits)
output_int = str(digits_as_int + 1)
output_list = []

for i in range(0,len(output_int)):
    output_list.append(int(output_int[i]))

print(output_list, 'final')