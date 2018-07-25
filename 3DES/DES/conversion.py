def textToHex(text):
	return (text.encode("UTF-8")).hex()
def hexToText(hexText):
	return (bytes.fromhex(hexText)).decode("UTF-8")
def binToHex(text):
	lookup = {"0000" : "0", "0001" : "1", "0010" : "2", "0011" : "3", "0100" : "4", "0101" : "5", "0110" : "6", "0111" : "7", "1000" : "8", "1001" : "9", "1010" : "a", "1011" : "b", "1100" : "c", "1101":"d" , "1110":"e" ,  "1111":"f"}
	result = ""
	for i in range(0,len(text),4):
		result += lookup[text[i]+text[i+1]+text[i+2]+text[i+3]]
	return result
def hexToBin(text):
	lookup = {"0" : "0000", "1" : "0001", "2" : "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", "8" : "1000", "9" : "1001", "a" : "1010", "b" : "1011", "c" : "1100", "d" : "1101", "e" : "1110", "f" : "1111"}
	result = ""
	for byte in text:
		result =  result + lookup[byte]
	return result
def dec16ToBin(dec):
	result = bin(dec)[2:]
	if len(result) < 4 :
		result = "0"*(4-len(result))+result
	return result
def toPermute(text,pc):
	result = ""
	for i in range(len(pc)):
		j = pc[i] - 1
		result += text[j]
	return result
def cat2(text):
	result = []
	result.append(text[:int(len(text)/2)])
	result.append(text[int(len(text)/2):])
	return result
def cat8(text):
	result = []
	l = int(len(text)/8)
	for i in range(8):
		result.append(text[i*l:(i+1)*l])
	return result
def xor(binA,binB):
	result = ''.join('0' if i == j else '1' for i, j in zip(binA,binB))
	return result
def toLeft(text,bit):
	s1 = text[:bit]
	s2 = text[bit:]
	return s2 + s1
def toRight(text,bit):
	s1 = text[:len(text)-bit]
	s2 = text[len(text)-bit:]
	return s2 +s1
def toArray2D(text):
	l = int(len(text)/4)
	result = []
	temp =[]
	k = 0
	for i in range(4):
		for j in range(l):
			temp.append(text[k])
			k +=1
		result.append(temp)
		temp = []
	return result
def binTo2Dec(text):
	bae = text[0]+text[len(text)-1]
	betw = text[1:len(text)-1]
	baeDec = int(bae,2)
	betwDec = int(betw,2)
	result = []
	result.append(baeDec)
	result.append(betwDec)
	return result
def convertKeyToHex(key):
	hexKey = textToHex(key)
	l = len(hexKey)
	if l >16 :
		hexKey = hexKey[:16]
	elif l<16:
		temp = "0"*(16-l)
		hexKey = hexKey+temp
	return hexKey
def createKeys(keyString,pc1,pc2):
	C=[]
	D=[]
	CD=[]
	K=[]
	kHex=[]
	keyHex = convertKeyToHex(keyString)
	keyBin = hexToBin(keyHex)
	keyPc1 = toPermute(keyBin,pc1) 
	catKey = cat2(keyPc1)
	C.append(catKey[0])
	D.append(catKey[1])

	for i in range(1,17):
		bit = 2
		if i in [1,2,9,16]:
			bit = 1
		C.append(toLeft(C[i-1],bit))
		D.append(toRight(D[i-2],bit))
		CD.append(C[i]+D[i])
		K.append(toPermute(CD[i-1],pc2))
		kHex.append(binToHex(K[i-1]))

	return kHex