import random

alphabet_dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,
                 "K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,
                 "T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,}

in_text = "I love bagels" #ideally to be taken as input
key_no = 7 #ideally to be taken as input

enc_decrypt = "E" #ideally to be taken as input

#define exception for spacebar and if number is more than 26 
def encryption_sequence(message,key):
    encrypted_string = ''
    message = message.upper()
    for i in range (0, len(message)):
        alphabet = message[i]
        if alphabet == " ":
            encrypted_string = encrypted_string + " "
        else:
            alphabet_num = alphabet_dict[alphabet]
            new_alphabet_num = alphabet_num + key
            if new_alphabet_num > 26:
                new_alphabet_num -= 26
            new_alphabet = list(alphabet_dict.keys())[list(alphabet_dict.values()).index(new_alphabet_num)]
            encrypted_string = encrypted_string + new_alphabet

    return encrypted_string


if enc_decrypt == "E":
    print(encryption_sequence(in_text,key_no))