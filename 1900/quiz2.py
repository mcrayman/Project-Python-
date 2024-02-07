'''
I'm thinking of a random integer between 1 and 500.  Enter your guess: 300
Too low!  Attempts so far: 1
I'm thinking of a random integer between 1 and 500.  Enter your guess: 501
Invalid guess, but I won't count it against you...
I'm thinking of a random integer between 1 and 500.  Enter your guess: 400
Too high!  Attempts so far: 2
I'm thinking of a random integer between 1 and 500.  Enter your guess: 382
Yay, you got it!  Total attempts: 3
'''
import random 

n = random.randint(1, 500)

attempts = 1

print('I\'m thinking of a random integer between 1 and 500.')

guess = int(input('Enter your guess: '))

while n != guess:

	if 1 > guess or guess > 500:
		print('Invalid guess, but I won\'t count it against you...')
		guess = int(input('Enter your guess: '))

	elif n < guess:
		print('Too high!  Attempts so far: ', attempts)
		guess = int(input('Enter your guess: '))
		attempts += 1

	elif n > guess:
		print('Too low!  Attempts so far: ',attempts)
		guess = int(input('Enter your guess: '))
		attempts += 1

if n == guess:
	print('Yay, you got it!  Total attempts: ', attempts)