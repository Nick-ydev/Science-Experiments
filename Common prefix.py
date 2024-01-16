# list_eng = ["flower" , "flow" , "flim"]
friends = ["Pro", "Proteur", "Proob", "Prow"]
length_list = len(friends)
first_element = friends.pop(0)
second_element = friends.pop(0)
print(first_element , second_element)

# # largest_string = len(max(friends))
# # print (largest_string)
# # print(max(friends))
k = ""
# for i in range (0,3):
i = 0

while first_element[i] == second_element[i]:
    k = k + second_element[i]
    element = first_element[i]
    print (f'element in {i}:{element} ')
    i = i+1
print(k) 


# friends = ["Pro", "Proteur", "Proob", "Prow"]

# length_friends = len(friends)
# for i in range (0,length_friends):
#     if len(friends[0]) > len(friends[i]):
#         k = len(friends[0])
#     elif len(friends[0]) < len(friends[i]):
#         k = len(friends[i])
#         print(k)
