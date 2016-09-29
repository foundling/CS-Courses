#include <stdio.h>

double fibs(double n) {

    double prev = 0;
    double cur = 1; 
    double temp;

    if (n == 0 || n == 1) {
        return n;
    }

    while(n > 1) {
        temp = cur;
        cur = prev + cur;
        prev = temp;
        n--;
    }

    return cur;
}

int main() {
    double n;
    scanf("%lf", &n);
    printf("%.0f\n", fibs(n));
}
