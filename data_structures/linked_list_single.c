#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;           // x is valid if x >= 0
    struct Node * next; 
};

void show_list(struct Node * p) {
    while (p->next) {
        p = p->next;
        printf("%d\n", p->data);
    }
}

void push_front(struct Node * head, int data) {
    struct Node * node = malloc(sizeof(struct Node));
    node->data = data;
    node->next = head->next;
    head->next = node;
}

int top_front(struct Node head) {
    return 1;
}

int pop_front(struct Node head) {
    return 1;
}

void push_back(int value) {
}

int top_back() {
    return 1;
}

int pop_back() {
    return 1;
}

int find(int value) {
    return 1;
}

int delete(int value) {
    return 1;
}

int empty(head) {
    return 1;
}

void splice(Node, Key) {
}

int main() {

    struct Node head;
    struct Node node1;

    head.next = NULL;
    head.data = -1;
    node1.data = 1;
    node1.next = head.next;
    head.next = &node1;

    push_front(&head, 2); 
    push_front(&head, 3); 
    push_front(&head, 4); 
    push_front(&head, 5); 

    show_list(&head);
}
