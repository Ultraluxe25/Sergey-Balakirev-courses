#include <stdio.h>

int main(void) {
    char byte;
    int count = scanf("%c", &byte);
    printf("count = %d, byte = %c", count, byte);

    return 0;
}