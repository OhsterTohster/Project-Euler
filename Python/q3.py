# What is the largest prime factor of the number 600851475143?

# A prime factor is a factor that is a prime number

# tbf just throw the number into factordb and that works too lmao

num = 600851475143
divideNumber = 2
while divideNumber < num:
    if (num % divideNumber == 0):
        num /= divideNumber
        divideNumber -= 1
    divideNumber+=1


print("Largest prime factor is", num)
    
