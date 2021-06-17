// By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
// find the sum of the even-valued terms.
#include<stdio.h>
int main(void)  {
    int result = solve();
    printf("%i", result);
}

int solve() {
    int sumOfEvenNumbers = 2;
    int nextNumber = 0;
    int previousNumber1 = 2;
    int previousNumber2 = 1;
    while (nextNumber < 4000000) {
        nextNumber = previousNumber1 + previousNumber2;
        if (nextNumber % 2 == 0) {
            sumOfEvenNumbers = sumOfEvenNumbers + nextNumber;
        }
        previousNumber2 = previousNumber1;
        previousNumber1 = nextNumber;
    }
    return sumOfEvenNumbers;
}