#include <stdio.h>

int main(void)
{
    int a;
    short b;
    float c;
    double d;

    // здесь продолжайте программу
    scanf("%d %hd %f %lf", &a, &b, &c, &d);  // %hd для short и %lf для 
    printf("%d %d %.2f %.2f", a, b, c, d);

    return 0;
}
