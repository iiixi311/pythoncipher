#####################################################################
# VIGENERE CIPHER
# Function of this program:
    # Senders input their message and the key
    # Program will encrypt their messages into Vigenere code and send to the receiver
    # Senders provide the key to the receiver to decrypt the text has been sent by senders
    

import math
import numpy as np
x_value = {
    "Z": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
    "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
    "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
    "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W":23, "X": 24, "Y": 25
}

y_value = {
    "A": 26, "B": 25, "C": 24, "D": 23, "E": 22,
    "F": 21, "G": 20, "H": 19, "I": 18, "J": 17, "K": 16,
    "L": 15, "M": 14, "N": 13, "O": 12, "P": 11, "Q": 10,
    "R": 9, "S": 8, "T": 7, "U": 6, "V": 5, "W":4, "X": 3, "Y": 2, "Z": 1, " ": 100
}


reverse_x_value = {
    0: "Z", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E",
    6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
    12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q",
    18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 100: " "
}

#this part of senders
def message_sender():
    # senders send their message 
    message = input("Please input your message: ")
    message = message.upper()
    # message belongs to y_value
    message_y_value = []
    if len(message) <= 0:
        print("Invalid message value, please enter your message again")
        message = input("Please input your message: ")
        message = message.upper()
        for i in message:
            message_y_value.append(i)        
    else:
        for i in message:
            message_y_value.append(i)
    return message_y_value
message_y_value = message_sender()


def key_encrypt():
    #senders enter their keys
    key = input("Please enter your key:")
    key = key.upper()
    # key belongs to x_value
    key_x_value = []
    if len(key) <= 0:
        print("Invalid key value, please enter your key again")
        key = input("Please enter your key:")
        key = key.upper()
        for i in key:
            key_x_value.append(i)
    else:
        for i in key:
            key_x_value.append(i)
    return key_x_value
key_x_value = key_encrypt()
    
def convert_message_to_value():
    #convert message to value
    message_sender_value = []
    for i in message_y_value:
        message_sender_value.append(y_value[i])
    return message_sender_value
message_sender_value = convert_message_to_value()
def convert_to_key_value():
    #convert key to value
    key_value = []
    for k in key_x_value:
        key_value.append(x_value[k])
    return key_value
key_value = convert_to_key_value()

def change_length_of_key_value():
    #change the length of key_value equal of length of message_sender_value
    key_value_update = []
    if len(key_value) > len(message_sender_value):
        key_value_update = key_value[:len(message_sender_value)]
    else:
        n = len(message_sender_value)/len(key_value)
        n = math.ceil(n)
        for i in range(n):
            key_value_update += key_value
            i += 1
        key_value_update = key_value_update[: len(message_sender_value)]
        return key_value_update

    return key_value_update
key_value_update = change_length_of_key_value()

encrypted_message_alphabet = []
def encrypt_message_alphabet():
    #export encrypted message alphabet
    for i in range(len(key_value_update)):
        if message_sender_value[i] != 100:
            value = key_value_update[i] - message_sender_value[i]
            if value >= 0:
                encrypted_message_alphabet.append(reverse_x_value[value])
            else:
                value = 26 + value
                encrypted_message_alphabet.append(reverse_x_value[value])
        else:
            encrypted_message_alphabet.append(100)
            
    return encrypted_message_alphabet
             

def export_message_alphabet():
    user_message_encrypted =""
    for i in encrypted_message_alphabet:
        if i == 100:
            i = " "
            user_message_encrypted += i
        else:
            user_message_encrypted += i
    return user_message_encrypted


def sender_message():
    #this function for sender message
    message_sender_value = convert_message_to_value()
    key_value = convert_to_key_value()
    key_value_update = change_length_of_key_value()
    encrypted_message_alphabet = encrypt_message_alphabet()
    user_message_encrypted = export_message_alphabet()
    print("Your encrypted message: \n",user_message_encrypted)
sender_message()



# this part of receivers
vigenere_value = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
    "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10,
    "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16,
    "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W":22, "X": 23, "Y": 24, "Z": 25, " ": 100
}
reverse_vigenere_value = {
    0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F",
    6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L",
    12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R",
    18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z", 100: " "    
}

def receiver_text():
    text = input("Please input your message: ")
    text = text.upper()
    # text belongs to vigenere_value
    text_receiver = []
    if len(text) <= 0:
        print("Invalid message value, please enter your message again")
    else:
        for i in text:
            text_receiver.append(i)
    return text_receiver
text_receiver = receiver_text()

def receiver_key():
    #receiver enter key
    key = input("Please enter your key:")
    key = key.upper()
    # key belongs to vigenere_value
    key_receiver = []
    if len(key) <= 0:
        print("Invalid key value, please enter your key again")
        key = input("Please enter your key:")
        key = key.upper()
        for i in key:
            key_receiver.append(i)
    else:
        for i in key:
            key_receiver.append(i)
    return key_receiver
key_receiver = receiver_key()
    
def receiver_text_value():
    convert_receiver_text_value = []
    for i in text_receiver:
        convert_receiver_text_value.append(vigenere_value[i])
    return convert_receiver_text_value
convert_receiver_text_value = receiver_text_value()

def receiver_key_value():
    convert_receiver_key_value = []
    for i in key_receiver:
        convert_receiver_key_value.append(vigenere_value[i])
    return convert_receiver_key_value
convert_receiver_key_value = receiver_key_value()

def change_length_receiver_key_value():
    #change the length of receiver_key_value equal of length of receiver_text_value
    receiver_key_value_update = []
    if len(convert_receiver_key_value) > len(convert_receiver_text_value):
        receiver_key_value_update = convert_receiver_key_value[:len(convert_receiver_text_value)]
    else:
        n = len(convert_receiver_text_value)/len(convert_receiver_key_value)
        n = math.ceil(n)
        for i in range(n):
            receiver_key_value_update += convert_receiver_key_value
            i += 1
        receiver_key_value_update = receiver_key_value_update[: len(convert_receiver_text_value)]
        return receiver_key_value_update

    return receiver_key_value_update
receiver_key_value_update = change_length_receiver_key_value()

decrypted_receiver_message_alphabet = []
def decrypt_message_alphabet():
    #export encrypted message alphabet
    for i in range(len(receiver_key_value_update)):
        if convert_receiver_text_value[i] != 100:
            value = convert_receiver_text_value[i] - receiver_key_value_update[i]
            if value >= 0:
                decrypted_receiver_message_alphabet.append(reverse_vigenere_value[value])
            else:
                value = 26 + value
                decrypted_receiver_message_alphabet.append(reverse_vigenere_value[value])
        else:
            decrypted_receiver_message_alphabet.append(" ")
            
    return decrypted_receiver_message_alphabet
    
def export_receiver_message_alphabet():
    receiver_message_decrypted =""
    for i in decrypted_receiver_message_alphabet:
        receiver_message_decrypted += i      
    return receiver_message_decrypted

def receiver_message():
    #this function for receiver message
    convert_receiver_text_value = receiver_text_value()
    convert_receiver_key_value = receiver_key_value()
    receiver_key_value_update = change_length_receiver_key_value()
    decrypted_receiver_message_alphabet = decrypt_message_alphabet()
    receiver_message_decrypted = export_receiver_message_alphabet()
    print("Your message has been decrypted sucessful: \n",receiver_message_decrypted)
receiver_message()
    



