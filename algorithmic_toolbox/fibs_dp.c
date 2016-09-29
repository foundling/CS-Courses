#include <stdio.h>
#include <stdio.h> 
#include <stdlib.h> 

/*
 * Problem: make change for a dollar with minimum coins.
 * (n - i) + 1 coins
 */

int main() {
    
    int i, j, count, val, max;
    int total = 0; 
    int current_total = 0;
    int n = 32;
    //int denoms[3] = {1, 2, 8}; 
    int denoms[3][3];

    for (int i = 0; i < 3; i++) {
        for (int i = 0; i < 3; i++) {
            denoms[i][j] = j;
        }
    }

    // a heap array space to store the values of the solutions to the sub-problems.
    // [solution for 0, solution for 1, solution for 2] 
    // index = total, value at index = num coins
    // [0, 1, 2, 2 ] 
    int * p = malloc(sizeof(n) * n);


    // initialize array to all 0s 
    for (i = 0; i < sizeof(n) * n; i++) {
        p[i] = 0;
    }

    // for each sub-problem size 
    for (i = 1; i < n; i++) {

        // find max solution via cut-and-paste method
        // take current weight, subtract it from the total weight and add the current value.
        // if that value is greater than the current weight, make it the current weight. move on.
 
        int max = 0;
        for (j = 0, count = sizeof(denoms); j < count; j++) {
            // target index is the offset of the total weight - current index, and the value at that index
            // is the solution
            val = p[n-[i][0]] + p[i][1]; 
            if (val > max) {
                max = val; 
            }
        }
        p[i] = max;
    }
}
