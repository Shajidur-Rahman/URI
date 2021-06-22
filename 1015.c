#include <stdio.h>
#include <math.h>

int main()

{
    float x1, x2, res, final;
    float y1, y2;
    scanf("%f %f", &x1, &y1);
    scanf("%f %f", &x2, &y2);

    res = (x2 -x1)*(x2 -x1) + (y2 -y1)*(y2 -y1);
    final = sqrt(res);
    printf("%0.4f\n", final);

    return 0;
}