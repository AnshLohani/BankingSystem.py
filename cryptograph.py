__key = 3

def Encrypt(value):
    Encrypted_pass = ''
    for i in value:
        Encrypted_pass += f"{chr(ord(i) + __key)}"
    return Encrypted_pass

def Decrypt(value):
    Decrypted_pass = ''
    for i in value:
        Decrypted_pass += f"{chr(ord(i) - __key)}"
    return  Decrypted_pass





