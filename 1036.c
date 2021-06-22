#include <stdio.h>

int main()

{
    float a,b,c;
    float x1,x2;

    scanf("%f %f %f", &a,&b,&c);

    x1 = (-b + (0.5*(b*b) - 4*a*c))/(2*a);

    x2 = (-b - (0.5*(b*b) - 4*a*c))/(2*a);


    printf("R1 = %0.5f", x1);
    printf("R2 = %0.5f", x2);

    return 0;
}