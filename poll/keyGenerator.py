from Crypto.PublicKey import RSA
from hashlib import sha512

def keyGen():
    keyPair = RSA.generate(bits=1024)
    print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
    print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

    return keyPair.d,keyPair.n,keyPair.e
