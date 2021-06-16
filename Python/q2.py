#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

fibonacciNumbers = [1,2]
nextNumber = 0
i = 2

while (nextNumber <= 4000000):
    nextNumber = fibonacciNumbers[i-1] + fibonacciNumbers[i-2]
    fibonacciNumbers.append(nextNumber)
    i+=1

sumOfNumbers = 0
for number in fibonacciNumbers:
    if (number % 2 == 0) :
        sumOfNumbers += number

print(sumOfNumbers)

