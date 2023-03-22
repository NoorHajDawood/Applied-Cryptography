def printBytes(string):
    string = str(string)
    string = bytes(string, 'utf-8')
    print(" ".join("{:02x}".format(c) for c in string))

class RC4:
    def RC4_init(self, key):
        self.stream = []
        i = 0
        j = 0
        counter = 0
        S = list(bytes(key, 'utf-8'))
        length = len(S)
        S = [s%length for s in S]
        while counter < 32:
            i = (i+1) % length
            j = (j+S[i]) % length
            S[i], S[j] = S[j], S[i]
            self.stream.append(S[(S[i] + S[j]) % length])
            counter += 1
        return self.stream

    def RC4_XOR(self, str):
        arr1 = [ord(s) for s in str]
        result = bytes(a^b for (a, b) in zip(arr1, self.stream))
        return result

    def RC4_encrypt(self, message):
        cipher = self.RC4_XOR(message)
        return cipher.decode('utf-8')

    def RC4_decrypt(self, cipher):
        message = self.RC4_XOR(cipher)
        return message.decode('utf-8')

def main():
    rc4 = RC4()
    key = 'cryptii'
    print('key:')
    printBytes(key)
    stream = rc4.RC4_init(key)
    message = 'hello world'
    cipher = rc4.RC4_encrypt(message)
    print('cipher:\t', cipher)
    printBytes(cipher)
    decipher = rc4.RC4_decrypt(cipher)
    print('decipher:\t', decipher)
    pass


if __name__ == "__main__":
    main()