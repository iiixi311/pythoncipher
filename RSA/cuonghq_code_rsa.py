#!/usr/bin/env python3
#
# virtualenv -p python3.7 name_env
# pip install -r requirement.txt
import random

def is_prime(number):
	return all([number % i for i in range(2, int(n**0.5) + 1)]) and number > 1

# Greatest common divisor
def GCD(p, q):
	while q != 0:
		p, q = q, p % q
	return p


# Use Euclidean extended algorithm to compiting d
def egcd(p, q):
	if p == 0:
		return (q, 0, 1)
	else:
		g, x, y = egcd(q % p, p)
		return (g, y - (q // p) * x, x)

# Multiplicative inverse
def mulinv(e, fi):
    g, x, y = egcd(e, fi)
    return x % fi


def generate_keypair(p, q):
	n = p * q
	fi = (p - 1) * (q - 1)
	e = random.randrange(1, fi)
	gcd = GCD(e, fi)
	while gcd != 1:
		e = random.randrange(1, fi)
		gcd = GCD(e, fi)
	print(e)
	d = mulinv(e, fi)
	return ((e, n), (d, n))


def encrypt(pk, ciphertext):
	key, n = pk
	cipher = [(ord(char) ^ key) % n for char in ciphertext]
	return cipher


if __name__ == '__main__':
	p = 5
	q = 7
	public, private = generate_keypair(p, q)
	print(encrypt(private, "Hello World"))
