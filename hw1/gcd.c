#include <stdio.h>

void GCD(int a, int b, int *gcd, int *m, int *n)
{
    if(b == 0)
    {
        *m = 1;
        *n = 0;
        *gcd = a;
    }
    else
    {
        int old_m, old_n;
        GCD(b, a%b, gcd, &old_m, &old_n);
        *n = old_m - old_n * (a/b);
        *m = old_n;
    }
}

int main(int argc, char const *argv[])
{
    int a, b, gcd, m, n;
    a = 2;
    b = 7;
    GCD(a, b, &gcd, &m, &n);
    printf("%d = %d*%d + %d*%d\n", gcd, m, a, n, b);

    a = 2689;
    b = 4001;
    GCD(a, b, &gcd, &m, &n);
    printf("%d = %d*%d + %d*%d\n", gcd, m, a, n, b);
    return 0;
}
