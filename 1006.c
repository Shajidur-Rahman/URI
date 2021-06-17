// sumof = (a/10 * 2)+ (b/10 * 3)+ (c/10 * 5)
# include<stdio.h>


int main(){

    float a,b,c;
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);

    printf("MEDIA = %0.1f\n", ((a/10) *2) + ((b/10) * 3) + ((c/10) * 5));
    return 0;

}