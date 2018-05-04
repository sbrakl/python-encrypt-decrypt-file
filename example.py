from simplecrypto import encrypt, decrypt
from os

password = "sometext"
filename = "secret.txt"

def encrpytfile():
    with open(filename, 'rb') as f:
        content = f.read()
    encrpycontent = encrypt(password, content)
    encryptfilename = filename + ".aes"
    with open(encryptfilename, 'wb') as f:
        f.write(encrpycontent)

def main():
    encrpytfile()


if __name__ == '__main__':
    main()