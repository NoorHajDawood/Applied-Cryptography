import random


def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)


def Exponent(base, exponent, modulus):
    if(modulus == 1):
        return 0
    result = 1
    base %= modulus
    while (exponent > 0):
        if (exponent % 2):
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result


def nBitRandom(n):
    r = 1
    for _ in range(n):
        r = (r << 1) + random.randint(0, 1)
    return r


def check_primility(n):
    e = n-1
    for _ in range(20):
        a = random.randint(2, n-2)
        if (gcd(n, a) != 1):
            return False
        while (e % 2 == 0):
            x = Exponent(a, e, n)
            if(x == (n-1)):
                return True
            if(x != 1):
                return False
            e >>= 1
    return True


def Generate_long_prime(bits):
    while True:
        x = nBitRandom(bits)
        if (x % 2 == 0):
            x += 1
        if(check_primility(x)):
            break
    return x


def extended_euclid(a, b, gcd, m, n):
    if(b == 0):
        return (a, 1, 0)
    else:
        (gcd, old_m, old_n) = extended_euclid(b, a % b, gcd, m, n)
        n = old_m - old_n * (a/b)
        m = old_n
        return (gcd, m, n)


def inverse(a, p):
    gcd = m = n = 0
    (gcd, m, n) = extended_euclid(a, p, gcd, m, n)
    return p+m if m < 0 else m
