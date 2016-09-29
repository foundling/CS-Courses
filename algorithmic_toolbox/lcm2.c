#include <stdio.h>
#include <math.h>

double gcd(double a, double b) {
    if (b == 0) {
        return a;
    }

    return gcd(b, fmod(a,b));
}

double lcm(double a, double b) {
    return a * b/gcd(a,b);
}

int main() {

    double a;
    double b;

    scanf("%lf %lf", &a, &b);

    printf("%.0lf\n", lcm(a,b));

    return 0;
}
