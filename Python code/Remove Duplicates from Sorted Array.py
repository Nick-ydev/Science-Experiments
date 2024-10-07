from math import *

nums = [1,1,2,2,5,5,6]
nums_new = [nums[0]]
length = len(nums) #lenght for the 'for loop
element_1 = nums[0]

k = 1 #This assumes that the first element of the string is unique
for i in range(1,length): #this checks all ements agaisnt all elements to return true or false
    if element_1 != nums[i]: 
        k = k+1 #if ith element is not equal to next element then k++ , which means it has found another unique value
        element_1 = nums[i] 
        nums_new.append(nums[i]) #adds the unique element to the list
        print(nums_new)
        print (k)

for i in range(0,len(nums_new)):
    nums[i] = nums_new[i]

print(nums)
