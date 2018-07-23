"""Encrypt the plaintext and return the ciphertext"""
def encrypt(key,change,plaintext):
	result = ""
	for c in plaintext:
		try:
			position = (key.index(c)+change) % len(key)
			result += key[position]
		except Exception:
			result += c
	return result

"""Decrypt the plaintext and return the plaintext"""
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
check = True
while check:
	print("""Enter your chose:\n\t1. Encode\n\t2. Decode\n\t3. Exit""")
	chose = input("Your chose is: ")
	if chose == '1':
		key = input("[+]Enter a custom alphabet: ")
		text = input("[+]The text you want encode: ")
		change = int(input("[+]Enter the shift< a number >:"))
		ciphertext = encrypt(key,change,text)
		print("*The text after encode: ",ciphertext+"\n"+"*"*35)
	elif chose == '2':
		key = input("[+]Enter a custom alphabet: ")
		text = input("[+]The text you want decode: ")
		change = int(input("[+]Enter the shift< a number >:"))
		plaintext = decrypt(key,change,text)
		print("*The text after decode: ",plaintext+"\n"+"*"*35)
	elif chose == '3':
		check = False
	else:
		print("ERROR! You must chose 1,2 or 3.\n"+"*"*35)