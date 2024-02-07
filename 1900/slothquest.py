# this program is a game designed to take user input for coordinate directions and has a random location as either vitory or defeat

import random

print('Welcome to Sloth Quest!')
print('-----------------------')

x = 0
y = 0
position = (x, y)


print('You’re currently at position (0, 0) in the world.')
print('Available commands: ')
print('N - go north, S - go south, E - go east, W - go west, X - exit game')

command = input('Enter command: ')

while command != 'X':
	if 'E' in command:
		x += 1
		position = (x, y)
		print('Moving east to', position)
		command = input('Enter command: ')
		if position == (random.randint(-5,5),random.randint(-5,5)) and position != (0,0):
			print('You’ve discovered a cache of sloths! Congrats, you win :)') or ('Oh no, you’ve been captured by anti-sloth protestors! You lose :(')
		
	elif 'N' in command:
		y += 1
		position = (x, y)
		print('Moving north to', position) 
		command = input('Enter command: ')
		if position == (random.randint(-5,5),random.randint(-5,5)) and position != (0,0):
			print('You’ve discovered a cache of sloths! Congrats, you win :)') or ('Oh no, you’ve been captured by anti-sloth protestors! You lose :(')
		

	elif 'S' in command:
		y -= 1
		position = (x, y)
		print('Moving south to', position)
		command = input('Enter command: ')
		if position == (random.randint(-5,5),random.randint(-5,5)) and position != (0,0):
			print('You’ve discovered a cache of sloths! Congrats, you win :)') or ('Oh no, you’ve been captured by anti-sloth protestors! You lose :(')
		
		
	elif 'W' in command:
		x -= 1
		position = (x, y)
		print('Moving west to', position)
		command = input('Enter command: ')
		if position == (random.randint(-5,5),random.randint(-5,5)) and position != (0,0):
			print('You’ve discovered a cache of sloths! Congrats, you win :)') or ('Oh no, you’ve been captured by anti-sloth protestors! You lose :(')

	elif command != 'N' or 'S' or 'E' or 'W':
		print('I find your lack of reading comprehension skills disturbing.')
		command = input('Enter command: ')

#generate hazard code 
		

