#include <stdio.h>

long gcd(long a, long b) {
    printf("%ld\n",a);
    return (b == 0) ? a : gcd(b, a%b);
}

long lcm(long a, long b) {
    /*
     * lcm(a,b) is just the product of a and b, divided by their gcd
     */

    return (a * b)/gcd(a,b); 
}

int main() {

    long a;
    long b;

    scanf("%ld %ld", &a, &b);

    printf("%.0ld\n", lcm(a,b));

    return 0;
}
