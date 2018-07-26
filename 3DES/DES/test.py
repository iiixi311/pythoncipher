from destable import *
from huanlv_code_3DES import *
message = '0123456789ABCDEF'
key ='12345678ABCEDFF9'
ciphertext = encryptDes(message,key,ip,ip1,p,e,rk,pc1,pc2,box)
print(ciphertext)
text = decryptDes(ciphertext,key,ip,ip1,p,e,rk,pc1,pc2,box)
print(text)