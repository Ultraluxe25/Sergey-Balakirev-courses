#include <stdio.h>

int main(void) {
    char var_1 = '0';
    char var_2 = '0';

    int res = scanf("%c %c", &var_1, &var_2);
    printf("res = %d, var_1 = %c, var_2 = %c", res, var_1, var_2);

    return 0;
}