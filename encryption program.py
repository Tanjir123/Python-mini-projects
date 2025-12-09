import string
import random
chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#Encrypt
message=input("Enter a message to encrypt:")
cipher_text=""
for letter in message:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"encrypted message:{cipher_text}")
#Decrypt
plain_text=""
message=input("Enter a message to decrypt:")
for letter in message:
    index=key.index(letter)
    plain_text+=chars[index]
print(f"Decrypted message:{plain_text}")