import MyCryptoLib
import random


class DSA_Signature:
    def generate_keyPare(self, p, q, alpha, d=0):
        """ 
        Generates a new private key.
        And returns the public key
        """
        self.privateKey = random.randint(1, q-1)
        if(d != 0):
            self.privateKey = d
        self.publicKey = MyCryptoLib.Exponent(alpha, self.privateKey, p)
        return self.publicKey

    def DSA_Sign(self, p, q, alpha, message, ke=0):
        """
        sign the message and return (r, s)
        """
        keph = random.randint(1, q-1)
        if(ke != 0):
            keph = ke
        r = MyCryptoLib.Exponent(alpha, keph, p) % q
        s = (((message+self.privateKey*r) % q)
             * MyCryptoLib.inverse(keph, q)) % q
        return r, s


def DSA_Verify( p, q, alpha, beta, r, s, message):
    """
    validate the DSA signature and return boolean
    """
    w = MyCryptoLib.inverse(s, q)
    u1 = (w * message) % q
    u2 = (w * r) % q
    v = ((MyCryptoLib.Exponent(alpha, u1, p) *
         MyCryptoLib.Exponent(beta, u2, p)) % p) % q
    return v == r


def main():
    Bob = DSA_Signature()
    # 1
    message = 17
    keph = 25
    p = 59
    q = 29
    alpha = 3
    d = 23
    print(f'p={p}, q={q}, a={alpha}, d={d}')
    print(f'1) h(x)={message}, Keph={keph}')
    beta = Bob.generate_keyPare(p, q, alpha, d)
    print(f'\tbeta={Bob.publicKey}')
    print('sign:')
    r, s = Bob.DSA_Sign(p, q, alpha, message, keph)
    print(f'\t(r, s)=({r}, {s})')
    verify = DSA_Verify(p, q, alpha, beta, r, s, message)
    print(f'verify: {verify}')

    # 2
    print('\n')
    message = 2
    keph = 13
    print(f'p={p}, q={q}, a={alpha}, d={d}')
    print(f'2) h(x)={message}, Keph={keph}')
    beta = Bob.generate_keyPare(p, q, alpha, d)
    print(f'\tbeta={Bob.publicKey}')
    print('sign:')
    r, s = Bob.DSA_Sign(p, q, alpha, message, keph)
    print(f'\t(r, s)=({r}, {s})')
    verify = DSA_Verify(p, q, alpha, beta, r, s, message)
    print(f'verify: {verify}')

    # 3
    print('\n')
    message = 21
    keph = 8
    print(f'p={p}, q={q}, a={alpha}, d={d}')
    print(f'3) h(x)={message}, Keph={keph}')
    beta = Bob.generate_keyPare(p, q, alpha, d)
    print(f'\tbeta={Bob.publicKey}')
    print('sign:')
    r, s = Bob.DSA_Sign(p, q, alpha, message, keph)
    print(f'\t(r, s)=({r}, {s})')
    verify = DSA_Verify(p, q, alpha, beta, r, s, message)
    print(f'verify: {verify}')

if __name__ == "__main__":
    main()
