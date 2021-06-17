# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# We can reuse code from Problem 7 here

import math
def checkPrime(num):
    isPrime = True
    if (num % 2 == 0):
        isPrime = False
        return isPrime
    for i in range(3,math.ceil(math.sqrt(num))+1,2):
        if (num % i == 0):
            isPrime = False
            break
    return isPrime

def solve():
    sumOfPrimes = 2 #we know that the first and only even prime number is 2, thereafter all prime numbers will be an odd number
    for i in range(3,2000000,2): #thus the for loop begins at 3, and increments by 2 to ensure that each number being tested is odd
        if (checkPrime(i)):
            sumOfPrimes+=i
    
    print(sumOfPrimes)

solve()




