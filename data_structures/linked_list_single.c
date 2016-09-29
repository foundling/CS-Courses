#include <stdio.h>

struct Node {
    int value;
    struct Node * next; 
};

int main() {
    struct Node head;
    struct Node node1;

    node1.value = 1;

    node1.next = head.next;
    head.next = &node1;

    printf("%d\n", head.next->value);
}
