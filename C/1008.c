#include <stdio.h>

int main()
{
    int x, y;
    double sal;

    scanf("%d", &x);
    scanf("%d", &y);
    scanf("%lf", &sal);

    printf("NUMBER = %d\n", x);
    printf("SALARY = U$ %.2lf\n", y*sal);

    return 0;
}