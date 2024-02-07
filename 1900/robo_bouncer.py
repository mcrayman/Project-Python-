'''
 simulates a robotic bouncer in front of the best club ever 
'''

# Get user input 

age = int(input('How old are you?'))

# determine whether the user is old enough to gain entry
if age >= 21 and age < 40:
	print('Great come on in! The sloths are great')
elif age >= 40:
	print('Go home and play bingo with your family!')
elif age < 0:
	print('Age can\'t be negative!')
elif age == 20:
	print('No sloths for you! You are too young now but come back next year.')	
else:
	diff = 21 - age 
	print('No sloths for you! You are too young now but come back in', diff, 'years.')
	 
	

	

	 
