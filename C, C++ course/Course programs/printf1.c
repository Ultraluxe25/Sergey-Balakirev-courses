#include <stdio.h>

int main(void) {
    int var_i = -1283;
    double var_d = 54.34675;

    printf("[%-10d]\n", var_i);
    printf("[%-10f]\n", var_d);

    printf("[%+.7d]\n", var_i);
    printf("[%#X]\n", var_i);
    printf("[%+.2f]\n", var_d);

    return 0;
}