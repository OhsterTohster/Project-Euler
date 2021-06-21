// Find the largest palindrome made from the product of two 3-digit numbers.
#include<stdlib.h>
#include<stdio.h>
#include<string.h>

int solve() {
    
    int largestPalindrome = 0;
    for (int i = 100; i < 1000; i++) {
        for (int j = 100; j < 1000; j++) {
            int product = i * j;
            char str[7] = "";
            sprintf(str, "%ld", product);
            char reverse[7] = "";
            int reverseIndex = 0;
            for (int index = strlen(str) -1; index >=0; index--) {
                
                reverse[reverseIndex] = str[index];
                reverseIndex = reverseIndex + 1;
                
            }
            
            if (strcmp(str,reverse) == 0) {
                if (product > largestPalindrome) {
                    largestPalindrome = product;
                }
            }
        }
    }
    
    return largestPalindrome;
}
int main() {
    int result = solve();
    printf("%d", result);
    return 0;
}