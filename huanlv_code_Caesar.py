"""Encrypt the plaintext and return the ciphertext
------key: The characters to encode
------change: The number of shift
------plaintext: The text to encode
*=>encrypt return a string after encoding
"""
def encrypt(key,change,plaintext):
	result = ""
	for c in plaintext:
		try:
			position = (key.index(c)+change) % len(key)
			result += key[position]
		except Exception:
			result += c
	return result

"""Decrypt the plaintext and return the plaintext
------key: The characters to decode
------change: The number of shift
------plaintext: The text to encode
*=>decrypt return a string after decoding
"""
def decrypt(key,change,ciphertext):
	result = ""
	for c in ciphertext:
		try:
			position = (key.index(c)-change) % len(key)
			result += key[position]
		except Exception:
			result += c
	return result

"""The example of caesar algorithm"""
# key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# text = "TOIYEUVIETNAM"
# change = 3
# ciphertext = encrypt(key,change,text)
# plaintext = decrypt(key,change,ciphertext)
# print("Text: ",text)
# print("Ciphertext: ",ciphertext)
# print("Plaintext: ",plaintext)