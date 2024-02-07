# demonstrates ceasar cipher 

def ceasar_encrypt(plain_text,shift):
	plain_text = plain_text.upper()
	#loop that visits each character of the plaintext
	ciphertext = ''
	for i in plain_text:
		if 'A' <= i <= 'Z': #if I is a capital letter......
			new_char = chr(ord(i) + shift) #ord changes value into byte number. chr changes new number into new letter(character)
			
			if new_char > 'Z':
				new_char = chr(ord(new_char) - 26)

			ciphertext = ciphertext + new_char
			print(f'{i} -> {new_char}')
		else:
			ciphertext = ciphertext + i

	return ciphertext


#funtion call
print(ceasar_encrypt('SLOTHS ARE NICE!!!!!', 2))
print(ceasar_encrypt('sloths are nice!!!!!', 2))
print(ceasar_encrypt('zebras are ok', 2))


