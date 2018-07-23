# Public Parameter
p = 87
q = 43
g = 2  # modulus of p and q (assumption)

# Collect Input Data
print("""Enter Alice's Secret Key:""")
x1 = int(input("[+]Enter Alice's Secret Key: "))
y1 = (g^x1) % p
print("Alice's Public Key: ",y1)
x1 = bytes(x1)
y1 = bytes(y1)

print("""Enter Alice's Secret Key:""")
x2 = int(input("[+]Enter Bob's Secret Key: "))
y2 = (g^x2) % p
print("Bob's Public Key: ",y2)

x2 = bytes(x2)
y2 = bytes(y1)

# Gerenate k (128 bit) by Hash funtion
from hashlib import blake2b
h = blake2b(y2, digest_size=16)
h.update(x1)

k = h.hexdigest()
print("""K Value:""", k)
