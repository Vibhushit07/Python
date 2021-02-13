'''
    Write the encrypted text of each of the following words using a Caesar cipher with a distance value of 3:
    a. python
    b. hacker
    c. wow
    And then decrypt it also.
    Write different scripts for encryption & decryption.
'''

def encrypt(string):
    enc = ""

    for i in string:
        if ord(i) < 120:
            enc += chr(ord(i) + 3)
        else:
            enc += chr(97 + (ord(i) - 120))

    return enc

def decrypt(string):
    dec = ""

    for i in string:
        if ord(i) > 99:
            dec += chr(ord(i) - 3)
        else:
            dec += chr(120 + (ord(i) - 97))

    return dec

enc = encrypt(input("Enter a string to encrypt: "))

print("Encypted data is: ", enc)
print("decypted data is: ", decrypt(enc))