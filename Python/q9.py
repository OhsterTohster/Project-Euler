# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Maximum value of a is 332, minimum value of C is 335
# Using the formula, m^2-n^2 <= 332
import math
for b in range(1000):
    for a in range(1,b):
        c = math.sqrt(a**2 + b**2)
        if (a + b + c == 1000):
            print(a,"\n",b,"\n",c)
            print("Product:", a*b*c)
            