import random

def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b%a, a)

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
        r = (r<<1) + random.randint(0, 1)
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

# avg = 0
# print("Enter number of primes to generate (N>0): ", end = '')
# N = int(input())
# print("Enter number of desired bits (bits>0): ", end = '')
# bits = int(input())


# for _ in range(N):
#     counter = 0
#     while True:
#         x = nBitRandom(bits)
#         if (x%2 == 0):
#             x += 1
#         counter += 1
#         if(check_primility(x)):
#             break
#     print("The random prime is: ", x)
#     print("Number of generated numbers: ", counter, '\n')
#     avg += counter
# print("Average number of generated numbers: ", avg/N)
print("451: ", check_primility(451))