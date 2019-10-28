import hashlib
import string
text = input('Enter the hash value = ')  # "CD04302CBBD2E0EB259F53FAC7C57EE2"

for character in string.printable:
	cipher = hashlib.md5(character.encode('utf-8')).hexdigest().upper()  # According to hint, hash is uppercase
	for j in range(9):
		cipher = hashlib.md5(cipher.encode('utf-8')).hexdigest().upper()
	if cipher == text:
		print('Original Value = ' + character)

