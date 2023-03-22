#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <math.h>

unsigned long long GCD(unsigned long long a, unsigned long long b)
{
    if (a == 0)
        return b;
    return GCD(b%a, a);
} 

unsigned long long Exponent(unsigned long long base, unsigned long long exponent, unsigned long long modulus)
{
    if(modulus == 1)
        return 0;
    unsigned long long result = 1;
    base %= modulus;
    while (exponent > 0)
    {
        if (exponent % 2)
            result = (result * base) % modulus;
        exponent >>= 1;
        base = (base * base) % modulus;
    }
    return result;
}

void random32bit(unsigned long long *n, char msb)
{
    *n = msb == 0 ? 0 : 1;
    for (char i = msb == 0 ? 0 : 1; i < 32; ++i)
    {
        *n = ((*n) << 1) + (rand() % 2);
    }
}

bool check_primility(unsigned long long n)
{
    unsigned long long a, e = n - 1, x;
    for (int i = 0; i < 20; ++i)
    {
        a = 2 + (n - 4) * (rand() / (double)RAND_MAX);
        if (GCD(n, a) != 1)
            return false;
        while (e % 2 == 0)
        {
            x = Exponent(a, e, n);
            if (x == (n - 1))
                return true;
            if (x != 1)
                return false;
            e /= 2;
        }
    }
    return true;
}

int main(int argc, char const *argv[])
{
    srand((unsigned int)time(NULL));
    unsigned long long x;
    bool flag;
    int avg = 0, N;
    do
    {
        printf("Enter number of primes to generate (N>0): ");
        scanf("%d", &N);
    } while (!N > 0);

    for (int i = 0; i < N; ++i)
    {
        unsigned int counter = 0;
        do
        {
            random32bit(&x, 1);
            x += !(x % 2);
            flag = check_primility(x);
            ++counter;
        } while (!flag);
        printf("The random prime is: %llu\nNumber of generated numbers: %u\n\n", x, counter);
        // printf("%llu\n", x);
        avg += counter;
    }
    printf("Average of %u tries: %u\n", N, avg / N + (avg % N ? 1 : 0));
    return 0;
}
