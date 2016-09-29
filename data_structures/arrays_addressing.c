#include <stdio.h>

int main() {

    /* arrays are contiguous segments of equal-sized memory, 
       which gives us a constant time read and write access */

    int a[5] = {3,9,13,40,0};
    long int start = (long int)&a;
    int i = 4; // 4th offset from start address
    long int diff = start + (i * sizeof(a[i])) - start; 

    /* address of array element i 
       array_addr + ( elem_size * n ) */ 

    printf("Array index of interest:\n%d.\n", i);
    printf("Array starts at address:\n%ld.\n", start);
    printf("array index 4 starts at address:\n%ld.\n", start + (i * sizeof(a[i])));
    printf("Difference / sizeof each array element:\n %ld\n", diff/i);
}
