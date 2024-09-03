import math

list_of_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

Num_1 = 26
Num_2 = 46

def factors(Num,list_of_primes):
    Num_1factors = []
    upper_bound = int(Num/2) + 1
    for i in range(0, upper_bound):
        divisor = list_of_primes[i]
        while divisor <= Num and Num % divisor == 0:
            Num_1factors.append(divisor)
            Num = Num // divisor
            i += 1

    return Num_1factors

Num_1factors = factors(Num_1,list_of_primes)
Num_2factors = factors(Num_2,list_of_primes)

print(Num_1factors,"2nd", Num_2factors)