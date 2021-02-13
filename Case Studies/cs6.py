'''
    Modify the encryption and decryption scripts to work with strings containing all of the printable characters.
    33-126 ascii value characters
    distance value will be dynamic & entered by the user
'''

def encrypt(string, distance):
    enc = ""

    for i in string:
        if ord(i) <= (126 - distance):
            enc += chr(ord(i) + distance)
        else:
            enc += chr(33 + (ord(i) - (126 - distance + 1)))

    return enc

def decrypt(string, distance):
    dec = ""

    for i in string:
        if ord(i) >= (33 + distance):
            dec += chr(ord(i) - distance)
        else:
            dec += chr((126 - distance + 1) + (ord(i) - 33))

    return dec

distance = int(input("Enter distance for data encryption: "))
string = input("Enter data to be encrypted: ")

enc = encrypt(string, distance)

print("Encrypted data:", enc)
print("Data after decrypting the encrypted data:", decrypt(enc, distance))