'''
A simple demonstration of exception handling
'''

while True:
	try:
		# Line 9 below can raise a ValueError if the user enters input that's
		#  not convertible into an int
		number = int(input('Enter an integer: '))
		print(f'Here\'s what you entered: {number}')

		# The break statement is reached only when a ValueError is *not*
		#  raised in line 9.  So the loop exits only when we have int input.
		break

	# This exception handler runs whenever a ValueError is raised from the try
	#  block
	except ValueError:
		print('That is not an integer!')

	# You can have as many exception handlers as needed, one per specific type
	#  exception that might be raised

	# An optional finally block at the end specifies actions that should
	#  happen regardless of whether or not any exceptions were raised
