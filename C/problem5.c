// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include<stdio.h>

int solve() {
    unsigned long int num = 20;
    while(1) {
        if (num % 3 == 0 && num % 7 == 0 && num % 11 == 0 && num % 13 == 0 && num % 15 == 0 && num % 16 == 0 && num % 17 == 0 && num % 18 == 0 && num % 19 == 0 && num % 20 == 0) {
            return num;    
        }
        num = num + 20;
    }
}

int main(void) {
    unsigned long int result = solve();
    printf("%i",result);
    return 0;
}