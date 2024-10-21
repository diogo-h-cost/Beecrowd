#include <stdio.h>

int main()
{
    int dis;
    double cons, medio;

    scanf("%d", &dis);
    scanf("%lf", &cons);

    medio = dis / cons;

    printf("%.3lf km/l\n", medio);

    return 0;
}