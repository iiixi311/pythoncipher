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