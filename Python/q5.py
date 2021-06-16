# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# From the problem, it may seem like an easy bruteforce at first, which does work, but optimisations can be made.
from timeit import default_timer as timer
def main():
    bruteForce1()
    bruteForce2()

def bruteForce1(): #takes 21.4690071 seconds 
    start = timer()
    i = 1
    while True:
        if ((i % 1 == 0) and (i % 2 == 0) and (i % 3 == 0) and (i % 4 == 0) and (i % 5 == 0) and (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0) and (i % 9 == 0) and (i % 10 == 0) and (i % 11 == 0) and (i % 12 == 0) and (i % 13 == 0) and (i % 14 == 0) and (i % 15 == 0) and (i % 16 == 0) and (i % 17 == 0) and (i % 18 == 0) and (i % 19 == 0) and (i % 20 == 0)):
            print(i)
            break
        i+=1
    elapsedTime = timer() - start
    print(elapsedTime)

def bruteForce2(): #takes 1.5343350999999998 seconds
    start = timer()
    i = 20 # we know that the number has to be divisible by 20, as such we can start from 20
    while True:
        if ((i % 1 == 0) and (i % 2 == 0) and (i % 3 == 0) and (i % 4 == 0) and (i % 5 == 0) and (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0) and (i % 9 == 0) and (i % 10 == 0) and (i % 11 == 0) and (i % 12 == 0) and (i % 13 == 0) and (i % 14 == 0) and (i % 15 == 0) and (i % 16 == 0) and (i % 17 == 0) and (i % 18 == 0) and (i % 19 == 0) and (i % 20 == 0)):
            print(i)
            break
        i+=20 #increment by 20 as we need the number to be divisible by 20
    elapsedTime = timer() - start
    print(elapsedTime)

main()
