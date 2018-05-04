from Crypto.Cipher import AES
from Crypto import Random
import base64

class shabscrypto():
    def __init__(self, password):
        self.password = password.rjust(16,'#')        

    def encrypt(self, data):        
        iv = Random.new().read(AES.block_size)        
        cipher = AES.new(self.password, AES.MODE_CFB, iv)
        encryptdata = iv + cipher.encrypt(data)    
        encoded = base64.urlsafe_b64encode(encryptdata)
        return encoded

    def decrypt(self, data):
        decodedata = base64.urlsafe_b64decode(data)        
        iv = decodedata[0:16]
        payload = decodedata[16:]        
        cipher = AES.new(self.password, AES.MODE_CFB, iv)
        decoded = cipher.decrypt(payload)        
        return decoded  
