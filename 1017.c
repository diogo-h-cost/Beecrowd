#include <stdio.h>

int main()
{
    int h, v;

    scanf("%d", &h);
    scanf("%d", &v);

    printf("%.3lf\n", (h * v) / 12.0);

    return 0;
}