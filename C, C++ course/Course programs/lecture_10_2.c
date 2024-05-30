#include <stdio.h>

int main(void) {
    long long int number;
    int res = scanf("%lld", &number);
    printf("res = %d, number = %lld", res, number);

    return 0;
}