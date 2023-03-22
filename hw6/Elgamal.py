import MyCryptoLib
import random

class User:
    def generate_keyPare(self, p, alpha):
        """ 
        Generates a new private key.
        And returns the public key
        """
        self.privateKey = random.randint(1, p-1)
        self.publicKey = MyCryptoLib.Exponent(alpha, self.privateKey, p)
        return self.publicKey

    def DH_encrypt(self, p, alpha, Kpub, message):
        """
        encrypt the message and return (ephemeral_key, cipher)
        """
        i = random.randint(1, p-1)
        encryptKey = MyCryptoLib.Exponent(Kpub, i, p)
        ephemeralKey = MyCryptoLib.Exponent(alpha, i, p)
        return ephemeralKey, (message * encryptKey) % p
    
    def DH_decrypt(self, p, alpha, Keph, cipher):
        """
        decrypt cipher message and return decrypted message
        """
        decryptKey = MyCryptoLib.Exponent(Keph, p - 1 - self.privateKey, p)
        return (cipher * decryptKey) % p


def main():
    Bob = User()
    Alice = User()
    p = MyCryptoLib.Generate_long_prime(64)
    alpha = random.randint(2, p-2)
    Alice_pub = Alice.generate_keyPare(p, alpha)
    Bob_pub = Bob.generate_keyPare(p, alpha)
    message = 69420
    Keph, cipher = Alice.DH_encrypt(p, alpha, Bob_pub, message)

    print("Bob:\n\tKpr = {}\n\tKpub = {}\n".format(Bob.privateKey, Bob.publicKey))
    print("Alice:\n\tKpr = {}\n\tKpub = {}\n".format(Alice.privateKey, Alice.publicKey))
    
    print("Keph: ", Keph)
    print("Message: ", message)
    print("Cipher: ", cipher)


    print("Decrypt: ", Bob.DH_decrypt(p, alpha, Keph, cipher))

if __name__ == "__main__":
    main()