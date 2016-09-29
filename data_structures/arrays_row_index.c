#include <stdio.h>

int main() {

    /* 
     *    0 1 2 3
     *   ---------
     *   | | | | |
     *   ---------
     *   | |x| | | <- target is at (1,2) in 'row-major' order
     *   ---------
     *  (1,2) -> 1-dimension array index ...
     *  row * (row-length - 1) + column
     *  1 * (4 - 1) + 2 = 1 * 3 + 2 = 5
     *
     */ 

}
