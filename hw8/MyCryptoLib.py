import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


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
    for _ in range(20):
        e = n-1
        a = random.randint(2, n-2)
        if (gcd(n, a) != 1):
            return False
        while (e % 2 == 0):
            x = Exponent(a, e, n)
            if(x == (n-1)):
                break
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


def extended_euclid(a, b):
    if(b == 0):
        return a, 1, 0
    gcd, old_m, old_n = extended_euclid(b, a % b)
    n = old_m - old_n * int(a/b)
    m = old_n
    return gcd, m, n


# def inverse(a, p):
#     (gcd, m, n) = extended_euclid(a, p)
#     return m % p
def inverse(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % m


def solve_system(a, p, b, q):
    q1 = inverse(q, p)
    p1 = inverse(p, q)
    a %= p
    b %= q
    return (a * q * q1 + b * p * p1) % (p*q)
