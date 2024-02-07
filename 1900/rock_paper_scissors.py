import random

g = 1
i = 1
tie = 0
win = 0
loss = 0


while i > 0:
	print(f'*** Game {g} ***')
	choice = input('(R)ock, (P)aper, or (S)cissors? ')
	if choice == 'R':
		choice = 'rock'
	if choice == 'P':
		choice = 'paper'
	if choice == 'S':
		choice = 'scissors'
	comp = random.randint(1,3)
	if comp == 1:
		comp = 'rock'
	elif comp == 2:
		comp = 'paper'
	elif comp == 3:
		comp = 'scissors'

	if choice != 'rock' or 'paper' or 'scissors':
		print('I need R, P, or S, try again:')

	winp = float((win / g) * 100)
	lossp = float((loss / g) * 100)
	tiep = float((tie / g) * 100)

	if choice == comp:
		tie += 1
		print('You chose: ',choice)
		print('Computer chose: ', comp)
		print("Tie")
		print('Stats so far:')
		print('-------------')
		print(f'Player wins: ',win ,'(',round(winp,1),'%)')
		print('Computer wins: ',loss ,'(',round(lossp,1),'%)')
		print('Ties: ',tie ,'(',round(tiep,1),'%)')
		play = input('Play again? (Y)es or (N)o')

		g += 1

	elif choice == 'rock':
		if comp == 'scissors':
			win += 1
			print(f'You chose: ',choice)
			print('Computer chose: ', comp)
			print('You win!')
		else:
			loss += 1
			print('You chose: ',choice)
			print('Computer chose: ', comp)
			print('Computer wins!')
	

		g += 1
		
	elif choice == 'paper':
		if comp == 'rock':
			win += 1
			print('You chose: ',choice)
			print('Computer chose: ', comp)
			print('You win!')
		else:
			loss += 1
			print('You chose: ',choice)
			print('Computer chose: ', comp)
			print('Computer wins!')
	
		g += 1
	
	elif choice == 'scissors':
		if comp == 'paper':
			win += 1
			print('You chose: ',choice)
			print('Computer chose: ', comp)
			print('You win!')
		else:
			loss += 1
			print('You chose: ',choice)
			print('Computer chose: ', comp)
			print('Computer wins!')
	
		g += 1

	
	
	
	print('Stats so far:')
	print('-------------')
	print(f'Player wins: ',win ,'(',round(winp,1),'%)')
	print('Computer wins: ',loss ,'(',round(lossp,1),'%)')
	print('Ties: ',tie ,'(',round(tiep,1),'%)')
	print('')
	play = input('Play again? (Y)es or (N)o ')
	if play == 'Y':
		pass
	elif play != 'Y':
		print('Thanks for playing!')
		quit()


	
	





		
	
