import math

list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

Num_1 = 44
Num_2 = 36

def factors(Num,list_of_primes): #This gives out prime factors of numbers
    Num_1factors = []
    upper_bound = int(Num/2) + 1
    for i in range(0, upper_bound):
        divisor = list_of_primes[i]
        while divisor <= Num and Num % divisor == 0:
            Num_1factors.append(divisor)
            Num = Num // divisor
            i += 1

    return Num_1factors

Num_1fact = []
Num_2fact = []

def LCM_factors(Num_1factors,Num_2factors): 
    #This is comparing list 1 to list 2 and gives out common elements 
    LCM_list = []
    for i in range (0,len(Num_1factors)):
        if Num_1factors[i] in LCM_list:
            LCM_list.append(Num_1factors[i])
            continue
        if Num_1factors[i] in Num_2factors:
            #checks count of prime number in both lists
            c1 = Num_1factors.count(Num_1factors[i])
            c2 = Num_2factors.count(Num_1factors[i])
            print(c1,c2)
            if c1 == c2: #if equal 
                for x in range(0,c1):
                    LCM_list.append(Num_1factors[i])
                    x += 1
            elif c1 > c2:
                for x in range(0,c1):
                    LCM_list.append(Num_1factors[i])
                    x += 1
            elif c1 < c2:
                for x in range(0,c2):
                    LCM_list.append(Num_1factors[i])
                    x += 1
        else: 
            LCM_list.append(Num_1factors[i])
    return LCM_list

#To check if the input itself is a prime
if (Num_1 in list_of_primes) and (Num_2 in list_of_primes):
    print("LCM =" , Num_1 * Num_2)
elif Num_1 in list_of_primes:
    Num_1fact.append(Num_1)
    Num_2fact = factors(Num_2,list_of_primes)
elif Num_2 in list_of_primes:
    Num_2fact.append(Num_2)
    Num_1fact = factors(Num_1,list_of_primes)
else: #If neither are prime then call comparison for both numbers
    Num_1fact = factors(Num_1,list_of_primes)
    Num_2fact = factors(Num_2,list_of_primes)


print(Num_1fact , "2nd", Num_2fact)
LCM_list = LCM_factors(Num_1fact,Num_2fact)
print(LCM_list, "L1 OG")

LCM_reverse = LCM_factors(Num_2fact,Num_1fact)
print(LCM_reverse)

#joins the 2 lists
LCM_list.extend(LCM_reverse)
print(LCM_list, "L1 extd")

LCM = 1
for i in range (0,len(LCM_list)):
    LCM = LCM * LCM_list[i]

print(LCM)
