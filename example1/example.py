from simplecrypto import encrypt, decrypt

password = "sometext"
filename = "../secret.txt"
encryptfilename = "../secret.txt.aes"

def encrpytfile():
    with open(filename, 'rb') as f:
        content = f.read()
    encrpycontent = encrypt(password, content)
    with open(encryptfilename, 'wb') as f:
        f.write(encrpycontent)

def decrpytfile():
    with open(encryptfilename, 'rb') as f:
        content = f.read()
    decryptcontent = decrypt(password, content)
    with open(filename, 'wb') as f:
        f.write(decryptcontent)

def main():
    encrpytfile()
    decrpytfile()


if __name__ == '__main__':
    main()