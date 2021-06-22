#include <stdio.h>

int main()

{
    float hour, km;
    scanf("%f", &hour);
    scanf("%f", &km);

    printf("%0.3f\n", (hour*km)/12);
    return 0;
}