import MyCryptoLib


def elliptic_curve_plus(x1, y1, x2, y2, a, p):
    if(x1 == -1 and y1 == -1):
        return (x2, y2)
    if(x2 == -1 and y2 == -1):
        return (x1, y1)
    if(x1 != x2 or y1 != y2):
        if(x1 == x2):
            return (-1, -1)
        dividend = (y2 - y1) % p
        divisor = (x2 - x1) % p
    else:
        if(y1 == 0):
            return (-1, -1)
        dividend = 3*x1*x1+a
        divisor = 2*y1
    if(dividend % divisor == 0):
        s = int(dividend/divisor) % p
    else:
        s = (dividend * MyCryptoLib.inverse(divisor, p)) % p
    x3 = (s*s - x1 - x2) % p
    y3 = (s*(x1 - x3)-y1) % p
    return (x3, y3)


def double_and_add(x, y, k, a, p):
    if(p == 1):
        return (-1, -1)
    if(k == 0):
        return (x, y)
    x %= p
    y %= p
    (x1, y1) = (-1, -1)
    while (k > 0):
        if (k % 2):
            (x1, y1) = elliptic_curve_plus(x1, y1, x, y, a, p)
        k >>= 1
        (x, y) = elliptic_curve_plus(x, y, x, y, a, p)
    return (x1, y1)


def main():
    # print(elliptic_curve_plus(3, 6, 3, 6, 2, 17))
    # print(double_and_add(0, 3, 5, 3, 7))
    print(f'a=6 , B=(5,9) , y^2=x^3+x+6 mod 11: sesion key = {double_and_add(5, 9, 6, 1, 11)}')

if __name__ == "__main__":
    main()
