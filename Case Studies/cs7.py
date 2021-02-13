'''
    You are given a string that was encoded by a Caesar cipher with an unknown distance value. 
    The text can contain any of the printable ASCII characters.
    Suggest an algorithm for cracking this code.

    - Input Plain Text & its Cipher Text
    - Output distance value d.
'''

def findDistance(cipherText, plainText):
    if(ord(cipherText[0]) - ord(plainText[0]) > 0):
        return (ord(cipherText[0]) - ord(plainText[0]))
    else:
        return 127 - (ord(plainText[0]) - ord(cipherText[0]))

print("Distance is: ", findDistance(input("Enter encrypted data: "), input("Enter plain text: ")))