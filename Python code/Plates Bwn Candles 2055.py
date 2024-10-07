s = "**|**|***|"
queries = [[2,5],[5,9]]

print(len(queries) ,queries[1])

# for i in range(0,len(queries)):
#     temp_list = queries[i]
#     print(temp_list)
#     mid_step = s[temp_list]
#     plates = mid_step.count("*")
#     print(plates)

def list_to_string(list1):
    stringed_list = ''
    for i in range (0,len(list1)):
        stringed_list = stringed_list + str(list1[i])
    return int(stringed_list)


count_s = s.count("*")
print(count_s, "count")