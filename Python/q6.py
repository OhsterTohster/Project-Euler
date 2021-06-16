# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Which means square of sum - sum of squares


# calculate sum of squares
sumOfSquares = 0
for i in range(1,101):
    sumOfSquares+=i**2

#calculate square of sum
sumOfNumbers = 0
for i in range(1,101):
    sumOfNumbers+=i
squareOfSum = sumOfNumbers**2

answer = squareOfSum - sumOfSquares 
print(answer)
