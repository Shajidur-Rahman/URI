#include <stdio.h>

int main()

{
    float seleary, sale;
    char name;
    scanf("%s", &name);
    scanf("%f", &seleary);
    scanf("%f", &sale);

    printf("TOTAL = R$ %0.2f\n", ((15*sale)/100)+ seleary);
    
    return 0;
}