#show a menu of option for the user

print('Welcome to the best ATM ever!')
print('1. Check Balance')
print('2. Deposit funds')
print('3. Withdraw funds')

#get user input for their choice

choice = int(input('Enter the number of your choice: '))

balance = 785

#do something different depending on the user's choice

if choice == 1:
	print(f'Current balance: ${balance:.2f}')

elif choice == 2:
	amount = int(input('Enter deposit amount: $'))
	if amount % 10 != 0:
		print('Sorry, you can only deposit in increments of 10.')
	elif amount > 1000:
		print('Sorry, no money laundering today, only up to $1000')
	elif amount <= 0:
		print('Sorry, the amount must be positive.')
	else: 
		balance += amount
		print(f'Current balance: ${balance:.2f}')	#same as balance = balance + amount 

elif choice == 3:
	amount = int(input('Enter withdraw amount: $'))
	if amount % 20 != 0:
		print('Sorry, you can only withdraw in increments of 20.')
	elif amount > balance:
		print('Insufficient funds, get a better job!')
	elif amount > 500:
		print('Sorry, the max allowed is 500.')
	elif amount <= 0:
		print('Sorry, the amount must be positive.')
	else: 
		balance -= amount
		print(f'Current balance: ${balance:.2f}')

else: 
	print('Invalid choice, please learn to read and enter 1 - 3.')
