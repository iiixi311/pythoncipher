# Public Parameter
# Define generating prime number function
import random
from random import randint
def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generate_big_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2**(n-1), 2**n)
        if is_prime(p, 1000):
            return p

# Define finding primitive root function
def find_primitive_root(numberToFactor, arr=list()):
    i = 2
    maximum = numberToFactor / 2 + 1
    while i < maximum:
        if numberToFactor % i == 0:
            return find_primitive_root(numberToFactor/i,arr + [i])
        i += 1
    return list(set(arr + [numberToFactor]))
# Set seed 
n = 10
# p is the prime
p = generate_big_prime(n)
print("[+] Generate prime number: {0}".format(p))
# q is the primitve root of p-1
q = find_primitive_root(p-1)
q = q[-1]
print("[+] Primitive root of p-1: {0}".format(q))
# g is an integer order q modulus p
g = random.randint(1, p-1)
g = pow(g, q, p)
print("[+] Generate g number: {0}".format(g))

# Collect Input Data
print("""Enter Alice's Secret Key:""")
x1 = int(input("[+]Enter Alice's Secret Key: "))
y1 = pow(g, x1, p)
print("Alice's Public Key: ",y1)
x1 = bytes(x1)
y1 = bytes(y1)

print("""Enter Alice's Secret Key:""")
x2 = int(input("[+]Enter Bob's Secret Key: "))
y2 = pow(g, x2, p)
print("Bob's Public Key: ",y2)
x2 = bytes(x2)
y2 = bytes(y1)

# Alice choose a random value x # x1
x = int(input("[+]Enter Alice's Secret Key: "))
# Gerenate k (128 bit) by Hash funtion
from hashlib import blake2b
h = blake2b(y2, digest_size=16)
h.update(x)
k = h.hexdigest()
print("""K Value:""", k)

# Generate k1, k2
splitat = len(k) / 2
k1 = k[:splitat]
k2 = k[splitat:]
print("""K1 Value:""",k1)
print("""K2 Value:""",k2)

import nacl.utils
from nacl.public import PrivateKey, Box
print("""Enter Alice's Secret Message:""")
m = bytes(input("[+]Enter Alice's Secret Message: "))

# Alice Use k1 to Encrypt her Secret Message
c = k1.encrypt(m)

# Alice Use k2 to Hash her Secret Message
from pyblake2 import blake2b
h = blake2b(k2, digest_size=16)
h.update(m)
r = h.hexdigest()

# Alice Use R and C to compute S
s = x / ((r + x1) % q )
