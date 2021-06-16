# What is the largest prime factor of the number 600851475143?

# A prime factor is a factor that is a prime number

#tbf just throw the number into factordb and that works too lmao

num = 600851475143
largestNumber = 0
for i in range(2, num+1):
    isPrime = False
    if (num % i == 0):
        isPrime = True
        
        for j in range(2,i//2 +1):
            if (i % j == 0):
                isPrime = False
                break
    
    if (isPrime == True):
        largestNumber = i
        print(largestNumber)


print("Largest prime factor is", largestNumber)
    
