#include<stdio.h>
//Find the sum of all the multiple of 3 or 5 below 1000

int main(void) {
    printf("%i", solve());
    return 0;
}

int solve() {
    int i;
    int sum = 0;
    for ( i = 0; i < 1000; ++i ) {
        if (i % 3 == 0 || i % 5 == 0) {
            sum = sum + i;
        }
    }
    return sum;
}