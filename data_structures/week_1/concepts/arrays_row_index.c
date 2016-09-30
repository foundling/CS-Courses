#include <stdio.h>
#define ROWS 4
#define COLS 4

// passing 2-d array into function: http://c-faq.com/aryptr/pass2dary.html
char get_letter(int coords[2], char arr[ROWS][COLS]) {

     /*
     *  coords (x,y) -> index z
     *  formula: row * (row_length - 1) + column
     */
    int i = (coords[0] * sizeof(arr[0])/sizeof(arr[0][0])) + coords [1];
    return **arr + i;
} 

int main() {

 
    char letters[ROWS][COLS] = { 
        {'a','b','c','d'},
        {'e','f','g','h'}
    };
    int first[2] = {0,0};
    int sixth[2] = {1,1};
    int last[2] = {1,3};

    printf("%c\n", get_letter(first, letters));
    printf("%c\n", get_letter(sixth, letters));
    printf("%c\n", get_letter(last, letters));
}
