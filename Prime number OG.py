import math

Number_list = []
n = 100

#list of numbers
for i in range (2,n+1):
    Number_list.append(i)

print("1st print" , Number_list)
#print(Number_list)
arr = [2,3,5,7]
#Check for primes
for i in range (0,4):
    l = arr[i]
    print("This is i" ,arr[i])
    k = n // l
    for j in range (k,1,-1):
        print("This is j" ,j)
        Multiple = l * j
        print(Multiple)
        if Multiple in Number_list:
            Number_list.remove(Multiple)
    k -= 1
    i += 1
    print(Number_list)
