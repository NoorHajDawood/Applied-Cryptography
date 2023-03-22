#include <stdio.h>

void extended_euclid(int a, int b, int *gcd, int *m, int *n)
{
    if (b == 0)
    {
        *m = 1;
        *n = 0;
        *gcd = a;
    }
    else
    {
        int old_m, old_n;
        extended_euclid(b, a % b, gcd, &old_m, &old_n);
        *n = old_m - old_n * (a / b);
        *m = old_n;
    }
}

int inverse(int a, int p)
{
    int gcd, m, n;
    extended_euclid(a, p, &gcd, &m, &n);
    return m < 0 ? p+m : m;
}

int Solve_System(int a, int p, int b, int q)
{
    int q1, p1, result;
    a %= p;
    b %= q;
    q1 = inverse(q, p);
    p1 = inverse(p, q);
    result = (a * q * q1 + b * p * p1)%(p*q);
    if (result < 0)
        result = p*q + result;
    return result;
}
int main(int argc, char const *argv[])
{
    int a, p, b, q;
    printf("x = a mod p\nx = b mod q\n");
    printf("a: ");
    scanf("%d", &a);
    printf("p: ");
    scanf("%d", &p);
    printf("inverse: %d\n", inverse(a,p));
    printf("b: ");
    scanf("%d", &b);
    printf("q: ");
    scanf("%d", &q);
    printf("%d\n", Solve_System(a, p, b, q));
    return 0;
}
