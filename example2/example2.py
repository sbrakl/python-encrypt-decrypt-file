from shabcrypto import shabscrypto

password = "1234567890123456"
filename = "../secret.txt"
encryptfilename = "../secret.txt.aes"
s = shabscrypto(password)

def encrpytfile():
    with open(filename, 'rb') as f:
        content = f.read()
    encrpycontent = s.encrypt(content)
    with open(encryptfilename, 'wb') as f:
        f.write(encrpycontent)

def decrpytfile():
    with open(encryptfilename, 'rb') as f:
        content = f.read()
    decryptcontent = s.decrypt(content)
    with open(filename, 'wb') as f:
        f.write(decryptcontent)

def main():
    encrpytfile()
    decrpytfile()


if __name__ == '__main__':
    main()