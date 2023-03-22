import MyCryptoLib


class RSA_member:
    def generate_keyPare(self):
        """ 
        Generates a new private key.

        And returns the public key.
        """
        self.p = MyCryptoLib.Generate_long_prime(32)
        self.q = MyCryptoLib.Generate_long_prime(32)
        self.n = self.p*self.q
        self.phi = (self.p-1)*(self.q-1)
        gcd = 0
        while gcd != 1:
            self.publicKey = MyCryptoLib.random.randint(3, self.phi)
            gcd = MyCryptoLib.gcd(self.phi, self.publicKey)
        self.privateKey = MyCryptoLib.inverse(self.publicKey, self.phi)
        return self.n, self.publicKey

    def RSA_decrypt(self, cipher):
        """
        decrypt cipher message and return decrypted message
        """
        a = MyCryptoLib.Exponent(cipher, self.privateKey % (self.p-1), self.p)
        b = MyCryptoLib.Exponent(cipher, self.privateKey % (self.q-1), self.q)
        return MyCryptoLib.solve_system(a, self.p, b, self.q)


def RSA_encrypt(n, Kpub, message):
    """
    encrypt the message and return cipher
    """
    return MyCryptoLib.Exponent(message, Kpub, n)


def main():
    google = RSA_member()
    n, googlePublic = google.generate_keyPare()
    print(f'(n, e):\t({n}, {googlePublic})')

    print(f'Enter your message: (0-{n-1})')
    message = int(input())
    # message = MyCryptoLib.random.randint(0, n-1)
    print('message:\t', message)

    cipher = RSA_encrypt(n, googlePublic, message)
    print('cipher:\t\t', cipher)

    decipher = google.RSA_decrypt(cipher)
    print('decipher:\t', decipher)

    print('\nExample: p=5 q=11 e=3 x=9')
    exRSA = RSA_member()
    exRSA.p = 37
    exRSA.q = 31
    exRSA.n = exRSA.p*exRSA.q
    exRSA.phi = (exRSA.p-1)*(exRSA.q-1)
    exRSA.publicKey = 17
    exRSA.privateKey = MyCryptoLib.inverse(exRSA.publicKey, exRSA.phi)
    print('d =', exRSA.privateKey)
    x = 9
    cipher = RSA_encrypt(exRSA.n, exRSA.publicKey, x)
    cipher = 2
    print(f'y = RSA_encrypt(n={exRSA.n}, e={exRSA.publicKey}, x={x}) = {cipher}')
    decipher = exRSA.RSA_decrypt(cipher)
    print(f'x = RSA_decrypt(y={cipher}) = {decipher}')

if __name__ == "__main__":
    #main()
    print("hello")
    print(MyCryptoLib.Generate_long_prime(2048))
