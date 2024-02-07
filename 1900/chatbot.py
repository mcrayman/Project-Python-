# Best chatbot ever

import random

#Get user input for what they want to say

user_input = ''

# check whethrer user input ends in '?'

while user_input != 'goodbye':
	user_input = input('Say or ask something (goodbye to exit): ')

	if user_input[len(user_input) - 1] == '?':
		print('Stop asking me questions!')

	elif len(user_input) > 20:
		print('I\'m a chatbot not a therapist!')

	# check for keyword 'sloth'
	elif user_input.count('sloth') > 0 or user_input.count('Sloth') > 0:
		print('A fellow sloth enthusiast I see, Im glad.')

	elif 'hello' in user_input:
		print('Hi')

	#figure out how to respond to input

	else:
		r = random.randint(1, 4)
		if r == 1:
			print('That is interesting.')
		elif r == 2:
			print('Try again later.')
		elif r == 3:
			print('k')
		else:
			print('I bet.')
