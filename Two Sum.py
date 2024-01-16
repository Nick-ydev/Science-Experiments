from math import *

Nums = [1,6,2,5,3,7]
length = len(Nums)
target = 9
list_1 = []
for i in range(0,length):
    for j in range (i,length):
        if Nums[i] + Nums[j] == target:
            list_1.append(i)
            list_1.append(j)
            print(list_1)
            break
    if len(list_1) != 0:
        break




# for i in range (0,length_r): 

#     if r[i] == "I" and r[i+1] =="V":
#         integer_r =  integer_r + thisdict["V"]
#         continue
#     if r[i] == "I":
#         integer_r = integer_r + thisdict["I"]

# print(integer_r)

r = "MCMXVI"
length_r = len(r)
integer_r = 0

thisdict = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}