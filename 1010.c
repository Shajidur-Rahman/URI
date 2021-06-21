#include <stdio.h>

int main()

{
    float price, price2;
    int code, unite, code2, unite2;
    scanf("%d %d %f", &code, &unite, &price);
    scanf("%d %d %f", &code2, &unite2, &price2);
    printf("VALOR A PAGAR: R$ %0.2f\n", (unite*price)+(unite2*price2));
    return 0;
}