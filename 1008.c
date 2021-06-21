#include <stdio.h>

int main()

{
    int number;
    float hour, sele;

    scanf("%d", &number);
    scanf("%f", &hour);
    scanf("%f", &sele);

    printf("NUMBER = %d\n", number);
    printf("SALARY = U$ %0.2f\n", hour*sele);
    return 0;
}