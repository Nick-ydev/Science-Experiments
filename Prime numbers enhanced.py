import math

n = 150
Number_list = []
#list of numbers\
for i in range(3,n+1,2): #2++ eliminates all multiples of 2
    Number_list.append(i)

print("List of Numbers" , Number_list)

upper_bound = int(n/2)

def prime_calc(n,list_of_numbers,i_ka_upperbound):
    
    for i in range (2,i_ka_upperbound):
        print("This is i" ,i)
        k = n // i
        for j in range (k,i,-1):
            print("This is j" ,j)
            Multiple = i * j
            print(Multiple)
            if Multiple in list_of_numbers:
                list_of_numbers.remove(Multiple)
        print (Number_list)
        i += 1
        # if i == prime_bound:
        #     return list_of_numbers
        # else: 
        #     i += 1
    return Number_list


primes_list = prime_calc(n,Number_list,upper_bound)

upper_bound = int(round(math.sqrt(n)))

primes_list_2 = prime_calc(n,Number_list,upper_bound)

if primes_list == primes_list_2:
    print("FUCK YEAHHHHHHHHHH!!!!!!!!!!!")
else:
    print("false")
print("1st call" , primes_list)
print("2nd",primes_list_2)

# prime_bound = 2 * math.floor(math.sqrt(n))
# print("upper bound" ,prime_bound)

# list_of_prime = prime_calc(prime_bound,Number_list)
# print("primes" ,list_of_prime)