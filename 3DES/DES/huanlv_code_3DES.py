#Some usage tables for DES algorithm
#Initial permut made on the key
pc1 = (
	57, 49, 41, 33, 25, 17, 9,
	1, 58, 50, 42, 34, 26, 18,
	10, 2, 59, 51, 43, 35, 27,
	19, 11, 3, 60, 52, 44, 36,
	63, 55, 47, 39, 31, 23, 15,
	7, 62, 54, 46, 38, 30, 22,
	14, 6, 61, 53, 45, 37, 29,
	21, 13, 5, 28, 20, 12, 4
	)
#Permut applied on shifted key to get Ki+1
pc2 = (
	14, 17, 11, 24, 1, 5, 3,
	28, 15, 6, 21, 10, 23, 19,
	12, 4, 26, 8, 16, 7, 27,
	20, 13, 2, 41, 52, 31, 37,
	47, 55, 30, 40, 51, 45, 33,
	48, 44, 49, 39, 56, 34, 53,
	46, 42, 50, 36, 29, 32
	)
#Initial permut matrix for the datas
ip = (
	58, 50, 42, 34, 26, 18, 10, 2,
	60, 52, 44, 36, 28, 20, 12, 4,
	62, 54, 46, 38, 30, 22, 14, 6,
	64, 56, 48, 40, 32, 24, 16, 8,
	57, 49, 41, 33, 25, 17, 9, 1,
	59, 51, 43, 35, 27, 19, 11, 3,
	61, 53, 45, 37, 29, 21, 13, 5,
	63, 55, 47, 39, 31, 23, 15, 7
	)
#Final permut for datas after the 16 rounds
ip1 = (
	40, 8, 48, 16, 56, 24, 64, 32,
	39, 7, 47, 15, 55, 23, 63, 31,
	38, 6, 46, 14, 54, 22, 62, 30,
	37, 5, 45, 13, 53, 21, 61, 29,
	36, 4, 44, 12, 52, 20, 60, 28,
	35, 3, 43, 11, 51, 19, 59, 27,
	34, 2, 42, 10, 50, 18, 58, 26,
	33, 1, 41, 9, 49, 17, 57, 25
	)
#Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
e =  (
	32, 1, 2, 3, 4, 5,
	4, 5, 6, 7, 8, 9,
	8, 9, 10, 11, 12, 13,
	12, 13, 14, 15, 16, 17,
	16, 17, 18, 19, 20, 21,
	20, 21, 22, 23, 24, 25,
	24, 25, 26, 27, 28, 29,
	28, 29, 30, 31, 32, 1
	)
box = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2

[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

# Box-3

[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

],

# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6

[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8

[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

]
#Permut made after each SBox substitution for each round
p = (
	16, 7, 20, 21, 29, 12, 28, 17,
	1, 15, 23, 26, 5, 18, 31, 10,
	2, 8, 24, 14, 32, 27, 3, 9,
	19, 13, 30, 6, 22, 11, 4, 25
	)
#Matrix that determine the shift for each round of keys
rk = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)

#This function take input are permutation table and key 64 bit and return key 56 bit
def applyPc1(key64bits):
	key56bits = ""
	for i in pc1:
		key56bits += key64bits[i-1]
	return key56bits
#This function will cut key 56 bits to 2 keys 28 bits
def cutHaftKey56bits(key56bits):
	leftKey = key56bits[:28]
	rightKey = key56bits[28:]
	return leftKey,rightKey
#This function will shift left bit by number of bits
def leftShift(bits,numBits):
	result = bits[numBits:]+bits[:numBits]
	return result
#This function tacke input are key 56 bits and compression table and return key 48 bits
def applyPc2(key56bits):
	key48bits = ""
	for i in pc2:
		key48bits += key56bits[i-1]
	return key48bits
#This function will return 16 keys
def generateKeys(key64bits):
	roundKeys = []
	pc1Out = applyPc1(key64bits)
	L0,R0 = cutHaftKey56bits(pc1Out)
	for i in range(16):
		newL = leftShift(L0,rk[i])
		newR = leftShift(R0,rk[i])
		roundKey = applyPc2(newL+newR)
		roundKeys.append(roundKey)
	return roundKeys
def XOR(bits1,bits2):
	xorResult = ""
	for i in range(len(bits1)):
		if bits1[i] == bits2[i]: 
			xorResult += '0'
		else:
			xorResult += '1'
	return xorResult
#This function take input string 32 bits and return string 48 bits
def applyExpansion(bits32):
	bits48 = ""
	for i in e:
		bits48 += bits32[i-1]
	return bits48
#This function cut strign 48 bits to 6 bits
import textwrap
def cutTo6bits(str48bits):
	result = textwrap.wrap(str48bits,6)
	return result
#Some functions to support
def binToDec(bina):
	decimal = int(bina,2)
	return decimal
def decToBin(deci):
	bin4bits = bin(deci)[2:].zfill(4)
	return bin4bits
def getFirstLastBit(bits6):
	return bits6[0]+bits6[-1]
def getMiddleBit(bits6):
	return bits6[1:5]
def boxLookup(boxCount,firstLast,middle):
	dFirstLast = binToDec(firstLast)
	dMiddle = binToDec(middle)

	value = box[boxCount][dFirstLast][dMiddle]
	return decToBin(value)
#This function will return string 32 bits
def applyP(s32bits):
	result = ""
	for i in p:
		result += s32bits[i-1]
	return result
#This is tha F function
def functionF(pre32bits,key48bits):
	result = ""
	expanded_left_half = applyExpansion(pre32bits)
	xor_value = XOR(expanded_left_half,key48bits)
	bits6list = cutTo6bits(xor_value)
	for sboxcount, bits6 in enumerate(bits6list):
		first_last = getFirstLastBit(bits6)
		middle4 = getMiddleBit(bits6)
		sboxvalue = boxLookup(sboxcount,first_last,middle4)
		result += sboxvalue
	final32bits = applyP(result)	
	return final32bits
#Some functions convert
def textToHex(text):
	return (text.encode("UTF-8")).hex()
def hexToText(hexText):
	return (bytes.fromhex(hexText)).decode("UTF-8")
def hexToBin(hexdigits):
	bindigits = ""
	for hexdigit in hexdigits:
		bindigits += bin(int(hexdigit,16))[2:].zfill(4)
	return bindigits
def binToHex(text):
	lookup = {"0000" : "0", "0001" : "1", "0010" : "2", "0011" : "3", "0100" : "4", "0101" : "5", "0110" : "6", "0111" : "7", "1000" : "8", "1001" : "9", "1010" : "a", "1011" : "b", "1100" : "c", "1101":"d" , "1110":"e" ,  "1111":"f"}
	result = ""
	for i in range(0,len(text),4):
		result += lookup[text[i]+text[i+1]+text[i+2]+text[i+3]]
	return result
#Use initial permutation table
def applyIp(plaintext):
	permutated = ""
	for i in ip:
		permutated += plaintext[int(i)-1]
	return permutated
def spliHalf(binarybits):
	return binarybits[:32],binarybits[32:]
def applyIp1(text):
	cipher = ""
	for index in ip1:
		cipher += text[int(index)-1]
	return cipher
#encrypt by des
def encryptDes(message,key):
	message = textToHex(message)
	key = textToHex(key)
	result=""
	list64bits = textwrap.wrap(message,16)
	for item in list64bits:
		cipher = ""
		# Convert hex digits to binary
		plaintext_bits = hexToBin(item)
		key_bits = hexToBin(key)
		# Generate rounds key
		roundkeys = generateKeys(key_bits)
		
		## initial permutation
		p_plaintext = applyIp(plaintext_bits)
		## split in tow half
		L,R = spliHalf(p_plaintext)
		## start rounds
		for round in range(16):
			newR = XOR(L,functionF(R, roundkeys[round]))
			newL = R
			R = newR
			L = newL
		cipher = applyIp1(R+L)
		cipher = binToHex(cipher)
		result += cipher
	return result
def decryptDes(message,key):
	result=""
	list64bits = textwrap.wrap(message,16)
	key = textToHex(key)
	for item in list64bits:
		text = ""
		# Convert hex digits to binary
		plaintext_bits = hexToBin(item)
		key_bits = hexToBin(key)
		# Generate rounds key
		roundkeys = generateKeys(key_bits)
		
		## initial permutation
		p_plaintext = applyIp(plaintext_bits)
		## split in tow half
		L,R = spliHalf(p_plaintext)
		## start rounds
		for round in range(16):
			newR = XOR(L,functionF(R, roundkeys[15-round]))
			newL = R
			R = newR
			L = newL
		text = applyIp1(R+L)
		text = binToHex(text)
		result += hexToText(text)
	return result


"""TEST"""
message = 'xin chao cac ban'
key ='hello may cung'
ciphertext = encryptDes(message,key)
print(ciphertext)
text = decryptDes(ciphertext,key)
print(text)