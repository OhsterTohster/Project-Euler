// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
// Which means square of sum - sum of squares
#include<stdio.h>
int solve() {
    int sumOfSquares = 0;
    int sum = 0;
    for (int i = 1; i < 101; i++) {
        int square = i * i;
        sumOfSquares = sumOfSquares + square; 
        sum = sum + i;

    }
    int squareOfSum = sum * sum;
    int result = squareOfSum - sumOfSquares;
    return result;
}

int main(void) {
    int answer = solve();
    printf("%d", answer);
    return 0;
}