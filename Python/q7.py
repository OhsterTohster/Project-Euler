# What is the 10 001st prime number?
#idk whats wrong with the code but something is wrong somewhere because 10001st prime number would mean 10001 elements in the list and thus 
# primeNumbers[10000] right?
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
    primeNumbers = [2,3,5,7,11,13]
    currentNumber = 13
    while True:
        if (len(primeNumbers) > 10001):
            break 
        else:
            checkValue = checkPrime(currentNumber)
            if (checkValue == True):
                primeNumbers.append(currentNumber)

        currentNumber+=2
    
    print(primeNumbers[10001])
    print(len(primeNumbers))

solve()




