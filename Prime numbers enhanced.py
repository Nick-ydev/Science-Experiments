import math

n = 1196

#list of numbers
Number_list = range[2,n+1]

print("List of Numbers" , Number_list)

def prime_calc(n,list_of_numbers):
    for i in range (2,int(n/2)):
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


primes_list = prime_calc(n,Number_list)
print("1st call" , primes_list)

# prime_bound = 2 * math.floor(math.sqrt(n))
# print("upper bound" ,prime_bound)

# list_of_prime = prime_calc(prime_bound,Number_list)
# print("primes" ,list_of_prime)