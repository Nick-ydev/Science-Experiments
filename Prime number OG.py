import math

Number_list = []
n = 1000

#list of numbers
for i in range (2,n+1):
    Number_list.append(i)

print("1st print" , Number_list)
#print(Number_list)

#Check for primes

for i in range (2,int(n/2)):
    print("This is i" ,i)
    k = n // i
    for j in range (k,1,-1):
        print("This is j" ,j)
        Multiple = i * j
        print(Multiple)
        if Multiple in Number_list:
            Number_list.remove(Multiple)
    k -= 1
    i += 1
    print(Number_list)
