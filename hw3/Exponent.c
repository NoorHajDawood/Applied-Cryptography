#include <stdio.h>
#include <stdlib.h>
#include <time.h>

unsigned int Exponent_binary(long long base, long long exp, long long module)
{
    if (base < 1 || exp < 0 || module < 1)
        return -1;
    int i, length = sizeof(exp);
    char exp_binary[64];
    unsigned int result = 1;
    for (i = 0; i < length && exp; ++i)
    {
        exp_binary[i] = exp % 2;
        exp /= 2;
    }
    --i;
    while (i >= 0)
    {
        result = (result * result) % module;
        if (exp_binary[i--])
            result = (result * base) % module;
    }
    return result;
}

unsigned int Exponent_recursive(long long base, long long exp, long long module)
{
    if (base < 1 || exp < 0 || module < 1)
        return -1;
    if (exp == 0)
        return 1;
    if (exp == 1)
        return base;
    unsigned int result = Exponent_recursive(base, exp / 2, module);
    result = (result * result) % module;
    if (exp % 2)
        return (result * (base % module)) % module;
    return result;
}

unsigned int Exponent(long long base, long long exp, long long module)
{
    if (base < 1 || exp < 0 || module < 1)
        return -1;
    unsigned int result = 1;
    while (exp > 0)
    {
        if (exp % 2)
            result = (result * base) % module;
        base = (base * base) % module;
        exp /= 2;
    }
    return result;
}

int main(int argc, char const *argv[])
{
    long long x = 0LL, m = 0LL, p = 0LL;
    // srand((unsigned int) time(NULL));
    // for (char i = 1; i < 64; ++i)
    // {
    //     x = (x << 1) + (rand() % 2);
    //     m = (m << 1) + (rand() % 2);
    //     p = (p << 1) + (rand() % 2);
    // }
    // printf("%lld ^ %lld %% %lld = %u\n", x, m, p, Exponent(x, m, p));

    // x = 2LL;
    // m = 79LL;
    // p = 101LL;
    // printf("%lld ^ %lld %% %lld = %u\n", x, m, p, Exponent(x, m, p));

    // x = 3LL;
    // m = 197LL;
    // printf("%lld ^ %lld %% %lld = %u\n", x, m, p, Exponent(x, m, p));

    // user input for x^m%p
    while (1)
    {
        printf("Enter values to compute x^m%%p: (x m p)\n");
        scanf("%lld %lld %lld", &x, &m, &p);
        printf("%lld ^ %lld %% %lld = %u\n", x, m, p, Exponent(x, m, p));
    }

    return 0;
}
