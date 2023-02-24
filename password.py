from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
#import os.path
from os import path
import base64
import hashlib


password = b"buffalo"
h = hashlib.md5(password*5 + b'dummy test' + password*len(password))

if (h.hexdigest() != '7c20a917b42f45d27a5d7bc92d99a1ea'):
    print("Incorrect Password")
    quit()

#with open('salt.txt', 'rb') as s:
#	salt = s.read()

salt = hashlib.md5(password + password).hexdigest()
salt = bytes(salt, 'utf-8')

kdf = PBKDF2HMAC(
    	algorithm=hashes.SHA256(),
    	length=32,
    	salt=salt,
	backend=default_backend(),
    	iterations=480000)

key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

with open('filekey.key', 'wb') as filekey:
   	filekey.write(key)
