


#this funciton captitalises all letters
def cleanup_text(original):
	original = original.upper()
	#loop that visits each character of the plaintext
	ciphertext = ''
	for i in original:
		if 'A' <= i <= 'Z': #if I is a capital letter......
			new_char = chr(ord(i)) #ord changes value into byte number. chr changes new number into new letter(character)
			
			if new_char > 'Z':
				new_char = chr(ord(new_char) - 26)

			ciphertext = ciphertext + new_char
			
		else:
			ciphertext = ciphertext 

	return ciphertext


print(cleanup_text('s t i l l e a s y '))
print(cleanup_text('**..slOtHs A...Re nI11cE!!!11!!!!'))
print(cleanup_text('1234567890'))

#this function swaps i and j in the string
def swap(x, i, j):
	#this assigns characters 
	if i >= len(x) and i <= -1:
		i += len(x)

	if j >= len(x) and j <= -1:
		j += len(x)
	#this swaps the characters i and j 
	if (i >= 0 and i < len(x)) and (j >= 0 and j < len(x)):
		letter = ''
		for val in range(len(x)):
			if val == j:
			   letter += x[i]
			elif val == i:
			    letter += x[j]
			else:
			    letter += x[val]
		return letter
	return None

print(swap('sloth',0,1))
print(swap('sloth',1,0))
print(swap('sloth',1,4))
print(swap('sloth',4,1))
print(swap('sloth',4,4))
print(swap('sloth',4,5))


def fancy_caesar(input_text, keyword, do_encrypt):
    input_text = cleanup_text(input_text)
    keyword = cleanup_text(keyword)
    if (do_encrypt):
        cipher = ''
   
        for i in range(len(input_text)):
            num = (((ord(input_text[i]) - 65) + (ord(keyword[i%len(keyword)]) - 65)) % 26) + 65
    
            cipher += chr(num)
  
        return cipher

    else:
        plain = ''
        for i in range(len(input_text)):
            num = (((ord(input_text[i]) - 65) - (ord(keyword[i%len(keyword)]) - 65)) % 26) + 65
            plain += chr(num)

        return plain
 
print(fancy_caesar('sloth', 'a', True))
print(fancy_caesar('sloth', 'a', False))
print(fancy_caesar('a', 'weird', True))
print(fancy_caesar('W', 'weird', False))
print(fancy_caesar('sloth', 'ABCDE', True))
print(fancy_caesar('smqwl', 'abcde', False))
print(fancy_caesar('‘zebras are mediocre!', 'lemon', True))
print(fancy_caesar('KiN..FnDEDS,.ZPh!!9234UCpCI', 'lEmoN', False))


def swap_encrypt(plaintext, keyword):
	plaintext = cleanup_text(plaintext)
	keyword = cleanup_text(keyword)

	for key in keyword:
		index = (ord(key) - 65) % len(plaintext)
		ciphertext = swap(plaintext,index, (index + 1) % len(plaintext))
	print(ciphertext)

def swap_decrypt(ciphertext,keyword):
	rev = ''
	ciphertext = cleanup_text(ciphertext)
	keyword = cleanup_text(keyword)

	for key in keyword:
		rev = key + rev

	for key in rev:
		index = (ord(key) - 65) % len(ciphertext)
		plaintext = swap(ciphertext,index,(index + 1) % len(ciphertext))
		print(plaintext)
  
print('swap_encrypt')
swap_encrypt('sloth','a')
swap_encrypt('sloth','aa')
swap_encrypt('SLOTH POWER','TOP')
print('swap_decrypt')

swap_decrypt('LSOTH','a')
swap_decrypt('SLOTH','aa')
swap_decrypt('RLOTPOHWES','TOP')


