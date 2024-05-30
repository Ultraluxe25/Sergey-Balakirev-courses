#include <stdio.h>

int main(void)
{
    // здесь продолжайте программу
    int var_a, var_b;
    double var_c, var_d;
    
    scanf("%d, %d, %*lf, %lf", &var_a, &var_b, &var_d);  // var_c пропускаем
    printf("%d %d %.2f", var_a, var_b, var_d);
    
    return 0;
}
