#include <stdio.h>

int main()

{
    // (4÷3)×3.1415×3×3×3
    float num;
    scanf("%f", &num);

    printf("VOLUME = %0.3f\n",((4.00 / 3) * 3.14159 * num * num * num));
    // printf("%f\n", num*num*num);
    return 0;
}