#This function take input are permutation table and key 64 bit and return key 56 bit
def applyPc1(pc1,key64bits):
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
def applyPc2(pc2,key56bits):
	key48bits = ""
	for i in pc2:
		key48bits += key56bits[i-1]
	return key48bits
#This function will return 16 keys
def generateKeys(key64bits,rk,pc1,pc2):
	roundKeys = []
	pc1Out = applyPc1(pc1,key64bits)
	L0,R0 = cutHaftKey56bits(pc1Out)
	for i in range(16):
		newL = leftShift(L0,rk[i])
		newR = leftShift(R0,rk[i])
		roundKey = applyPc2(pc2,newL+newR)
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
def applyExpansion(e,bits32):
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
def boxLookup(box,boxCount,firstLast,middle):
	dFirstLast = binToDec(firstLast)
	dMiddle = binToDec(middle)

	value = box[boxCount][dFirstLast][dMiddle]
	return decToBin(value)
#This function will return string 32 bits
def applyP(p,s32bits):
	result = ""
	for i in p:
		result += s32bits[i-1]
	return result
#This is tha F function
def functionF(p,box,e,pre32bits,key48bits):
	result = ""
	expanded_left_half = applyExpansion(e,pre32bits)
	xor_value = XOR(expanded_left_half,key48bits)
	bits6list = cutTo6bits(xor_value)
	for sboxcount, bits6 in enumerate(bits6list):
		first_last = getFirstLastBit(bits6)
		middle4 = getMiddleBit(bits6)
		sboxvalue = boxLookup(box,sboxcount,first_last,middle4)
		result += sboxvalue
	final32bits = applyP(p,result)	
	return final32bits
def textToHex(text):
	return (text.encode("UTF-8")).hex()
def hexToText(hexText):
	return (bytes.fromhex(hexText)).decode("UTF-8")
#This function will convert hex to bin
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
def applyIp(ip,plaintext):
	permutated = ""
	for i in ip:
		permutated += plaintext[int(i)-1]
	return permutated
def spliHalf(binarybits):
	return binarybits[:32],binarybits[32:]
def applyIp1(ip1, text):
	cipher = ""
	for index in ip1:
		cipher += text[int(index)-1]
	return cipher
#encrypt by des
def encryptDes(message,key,ip,ip1,p,e,rk,pc1,pc2,box):
	cipher = ""
	# Convert hex digits to binary
	plaintext_bits = hexToBin(message)
	key_bits = hexToBin(key)
	# Generate rounds key
	roundkeys = generateKeys(key_bits,rk,pc1,pc2)
	
	## initial permutation
	p_plaintext = applyIp(ip,plaintext_bits)
	## split in tow half
	L,R = spliHalf(p_plaintext)
	## start rounds
	for round in range(16):
		newR = XOR(L,functionF(p,box,e,R, roundkeys[round]))
		newL = R
		R = newR
		L = newL
	cipher = applyIp1(ip1, R+L)
	cipher = binToHex(cipher)
	return cipher
def decryptDes(message,key,ip,ip1,p,e,rk,pc1,pc2,box):
	text = ""
	# Convert hex digits to binary
	cipher_bits = hexToBin(message)
	key_bits = hexToBin(key)
	# Generate rounds key
	roundkeys = generateKeys(key_bits,rk,pc1,pc2)
	
	## initial permutation
	p_plaintext = applyIp(ip,cipher_bits)
	## split in tow half
	L,R = spliHalf(p_plaintext)
	## start rounds
	for round in range(16):
		newR = XOR(L,functionF(p,box,e,R, roundkeys[15-round]))
		newL = R
		R = newR
		L = newL
	text = applyIp1(ip1, R+L)
	text = binToHex(text)
	return text