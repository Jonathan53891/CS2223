'''
PSEUDOCODE:

import binascii library

create p
create q
compute n

calculate gcd
calculate lcm

create e

calculate egcd
calculate modular multiplicative inverse

create message
print message

create hex data
print hex data

create plain text
print plain text

if plain text is larger than n
    raise Exception

calculate encrypted text
print encrypted text

convert encrypted text to int
convert modular multiplicative inverse to int
convert n to int

calculate decrypted text
print decrypted text

print decrypted message


'''
import binascii

p = pow(2, 141) - 1
q = pow(2, 140) - 1
n = p * q

a = p-1
b = q-1
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b / gcd(a, b)
lambda_n = lcm(a,b)

e = 65537

def egcd(c, d):
    if c == 0:
        return (d, 0, 1)
    else:
        g, y, x = egcd(d % c, c)
        return (g, x - (d // c) * y, y)
def modinv(c, m):
    g, x, y = egcd(c, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
d = modinv(e, lambda_n)

message = 'Cryptography is fun when it works!'
print('message: ', message)
 
hex_data = binascii.hexlify(message.encode())
print('hex data: ', hex_data)
 
plain_text = int(hex_data, 16)
print('plain text integer: ', plain_text)
 
if plain_text > n:
  raise Exception('plain text too large for key')
 
encrypted_text = pow(plain_text, e, n)
print('encrypted text integer: ', encrypted_text)

encrypted_text = int(encrypted_text)
d = int(d)
n = int(n)
decrypted_text = pow(encrypted_text, d, n)
print('decrypted text integer: ', decrypted_text)
print(hex(decrypted_text)[2:])
print('message: ', binascii.unhexlify(hex(decrypted_text)[2:]).decode())     # [2:] slicing, to strip the 0x part 
