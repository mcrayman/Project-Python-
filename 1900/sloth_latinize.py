

def sloth_latinize(word):
	if 'SLOTH' in word or len(word) >= 8:
		return word
	elif word[0] in 'LMNP':
		return 'S' + word
	elif word[0] in 'AEIOU':
		return 'SL' + word
	else:
		return word[1:] + word[0] + 'LY'
	

def sloth_latinize_list(word_list):
	for i in range(len(word_list)):
		word_list[i] = sloth_latinize(word_list[i])


def sloth_latinize_new_list(word_list):
	return [sloth_latinize(i) for i in word_list]

stuff = ['MOON', 'ELEVEN', 'DINOSAUR']
print(sloth_latinize_new_list(stuff))
print(stuff)