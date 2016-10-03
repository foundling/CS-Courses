#include <stdio.h>
#include <stdlib.h>

struct Dynamic_Array {
    int * data;
    int size;
    int capacity;
    int resize_count;
};

void push_back(struct Dynamic_Array * array, int value) {

    if (array->size >= array->capacity) 
    {
        int * old_data = array->data;
        int old_capacity = array->capacity;

        array->capacity *= 2;
        array->data = malloc(sizeof( sizeof(int) * array->capacity ));

        for(int i = 0; i < old_capacity; ++i)
        {
            array->data[i] = old_data[i];
        }
        free(old_data);
        ++(array->resize_count);
    }
    array->data[ (array->size)++ ] = value;
}

void show(struct Dynamic_Array * array) {
    if (array->size)
    {
        printf("dynamic array contents:\n");
        for (int i = 0, max = array->size; i < max; ++i) {
            printf("%d\n", array->data[i]);
        }
        printf("[ The array was dynamically resized %d times. ]\n", array->resize_count);
    }
    else 
    {
        printf("no contents!\n");
    }
}

int main(int argc, const char * argv[]) {

    struct Dynamic_Array d = { 0, 0, 1, 0 };
    d.data = malloc(sizeof( sizeof(int) * d.capacity ));

    for (int i = 1, max = argc; i < max; ++i) {
        push_back(&d, atoi(argv[i]));
    }
    show(&d);
}
