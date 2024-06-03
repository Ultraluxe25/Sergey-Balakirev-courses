#include <stdio.h>

int main(void) {
    double height, a;
    int variables = scanf("%lf %lf", &height, &a);

    if(variables != 2) {
        printf("Error!");
    }

    double result = height * a / 2.0;
    printf("%.2f\n", result);

    return 0;
}
