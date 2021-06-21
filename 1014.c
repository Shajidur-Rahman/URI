#include <stdio.h>

int main()

{
    float dis,fuel; 
    scanf("%f", &dis);
    scanf("%f", &fuel);

    printf("%0.3f km/l\n", dis/fuel);
    return 0;
}