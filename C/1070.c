#include <stdio.h>

int main()
{
    int x, imp, cont;

    imp = 0;
    scanf("%d", &x);

    cont = x;

    while (imp != 6) {
        if (cont % 2 != 0) {
            imp = imp + 1;
            printf("%d\n", cont);
        }
        cont = cont + 1;
    }

    return 0;
}