#include <stdio.h>
#include <stdlib.h>
#define STACK_SIZE 50

struct Stack {
    int data[STACK_SIZE];
    int top_index;
};

void show(struct Stack * stack) {

    int i = 0;

    while(stack->data[i] > 0) {
        printf("%d\n", stack->data[i]);        
        ++i;
    }
}

void push(struct Stack * stack, int value) {

    if (stack->top_index + 1 == STACK_SIZE)
        return;

    stack->data[ stack->top_index++ ] = value;  

}

int top(stack) {
    return 1;
}

int pop(struct Stack * stack) {

    if (stack->top_index == 0) {
        return -1;
    }
    int item = stack->data[ stack->top_index ];
    stack->data[ --stack->top_index ] = -1;

    return item;
}

int empty(data) {
    return 1;
}

int main() {

    struct Stack stack = {{0,0}};
    struct Stack * stackp = &stack;

    push(stackp, 5);
    push(stackp, 9);
    //top(stackp);
    //pop(stackp);
    //empty(stackp);
    show(stackp);

}
