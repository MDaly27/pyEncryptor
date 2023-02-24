from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os.path
from os import path
import base64

divider = b"{}{}{[][][][][______________--_-4873)))}}}\\\faisdfs8df93495873450483dsfdscvfdvdf7898"

if (not path.exists('filekey.key')):
	print("no file key\n")
	quit()

elif path.exists('cart/scramble.key'):
	with open('filekey.key', 'rb') as filekey:
    		key = filekey.read()

	# using the generated key
	fernet = Fernet(key)


	with open('cart/scramble.key', 'rb') as enc_file:
    		encrypted = enc_file.read()
	os.remove('cart/scramble.key')
	images = encrypted.split(divider)
	length = len(images)
	for i in range(0, int(len(images)/2)): #potential issues
		# decrypting the file
		# names are not encrypted
		n = images[i*2]
		fi = images[i*2+1]
		decrypted = fernet.decrypt(fi)
		with open('cart/' + str(n, 'utf-8'), 'wb') as p:
			p.write(decrypted)

else:
	encrypted = []
	names = []
	scram = b""
	with open('filekey.key', 'rb') as filekey:
    		key = filekey.read()

	# using the generated key
	fernet = Fernet(key)

	for f in os.listdir("cart"):
		names.append(f)
		#if (f[-3:] == "jpg"):
		with open('cart/' + f, 'rb') as image:
    			encrypted.append(fernet.encrypt(image.read()))
	for s in range(len(encrypted)):
		scram += bytes(names[s], 'utf-8') + divider + encrypted[s] + divider
	with open('cart/scramble.key', 'wb') as encrypted_file:
     		encrypted_file.write(scram)
	for f in os.listdir("cart"):
		print(f)
		if (f[-3:] != "key"):
			os.remove('cart/'+f)
