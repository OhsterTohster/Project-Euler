#Find the largest palindrome made from the product of two 3-digit numbers.

# 3 digit number means 100 to 999 inclusive
largestPalindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if (str(product) == str(product)[::-1]):
            if (product > largestPalindrome):
                largestPalindrome = product

print(largestPalindrome)
        
