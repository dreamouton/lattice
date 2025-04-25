import gmpy2
from Crypto.Util.number import *
from sage.all import inverse_mod

FLAG = b'jason{??????????????????????????????????}'

def generate():
    p = getStrongPrime(2048)
    while True:
        f = getRandomNBitInteger(1024)
        g = getStrongPrime(768)
        h = gmpy2.invert(f, p) * g % p
        return (p, f, g, h)


def encrypt(plaintext, p, h):
    m = bytes_to_long(plaintext)
    r = getRandomNBitInteger(1024)
    c = (r * h + m) % p
    return c


def decrypt(p, h, f, g, c):
    a = (f*c) % p
    flag = (a*inverse_mod(f, g)) % g
    return flag


p, f, g, h = generate()
c = encrypt(FLAG, p, h)
print('Public Key:')
print('h =', h)
print('p =', p)
print('Encrypted Flag:')
print('c =', c)
