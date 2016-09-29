#include <stdio.h>

int mod10(int n) {
    return n % 10;
}

int fibs(int n) {

    int prev = 0;
    int cur = 1; 
    int temp;

    if (n == 0 || n == 1) {
        return n % 10;
    }

    while(n > 1) {
        temp = cur % 10;
        cur = (prev % 10) + (cur % 10);
        prev = temp;
        n--;
    }

    return cur % 10;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fibs(n));
}
