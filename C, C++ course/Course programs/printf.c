#include <stdio.h>

int main(void) {
    int value = getchar();
    int res = putchar(value);
    printf("\n%d\n", res);
    
    return 0;
}