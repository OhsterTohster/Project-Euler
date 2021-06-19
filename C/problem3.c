// What is the largest prime factor of the number 600851475143?

#include<stdio.h>

int solve() {
    unsigned long long int number = 600851475143;
    int divideNumber = 2;

    while (divideNumber < number) {

        if (number % divideNumber == 0) {
            number = number / divideNumber;
            divideNumber = divideNumber - 1;
        }
        divideNumber = divideNumber + 1;

    }
    return divideNumber;
}
int main(void) {
    int result = solve();
    printf("%i", result);
    return 0;
}

